from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .models import User,Role


class UserSingInSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"))
    password = serializers.CharField(label=_("Password"),
                                     style={'input_type': 'password'},
                                     trim_whitespace=False)


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'].lower(),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id','name','project','permissions')

