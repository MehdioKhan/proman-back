from rest_framework.decorators import api_view,permission_classes
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_200_OK,HTTP_404_NOT_FOUND
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import generics,viewsets
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSingInSerializer,UserSerializer,\
    UserSignupSerializer,RoleSerializer
from .authentication import token_expire_handler,expires_in
from .models import User,Role


@api_view(['POST'])
@permission_classes([AllowAny,])
def login(request):

    signin_serializer = UserSingInSerializer(data=request.data)

    if not signin_serializer.is_valid():
        return Response(signin_serializer.errors,status=HTTP_400_BAD_REQUEST)

    user = authenticate(email=signin_serializer.validated_data['email'].lower(),
                        password=signin_serializer.validated_data['password'])

    if not user:
        return Response({'details':'Invalid credentials or inactive user'},
                        status=HTTP_404_NOT_FOUND)
    token,_ = Token.objects.get_or_create(user=user)

    is_expired,token = token_expire_handler(token)

    user_serializer = UserSerializer(user)

    return Response({
        'user':user_serializer.data,
        'token':token.key,
        'expires_in':expires_in(token),
    },status=HTTP_200_OK)


def delete_token(user):
    try:
        token = Token.objects.get(user=user)
        token.delete()
    except Token.DoesNotExist:
        pass

    return True


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    delete_token(request.user)
    return Response({'details':'Logged out'},status=HTTP_200_OK)


class UserSignUp(generics.CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny,]
    queryset = User.objects.all()


class UsersList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

    def list(self, request, *args, **kwargs):
        project = request.GET.get('project',None)
        if not project:
            return Response({'error':'project not provided'},404)
        else:
            roles = self.get_queryset().filter(project=project)
            serializer = self.get_serializer_class()(roles,many=True)
            return Response(serializer.data)

