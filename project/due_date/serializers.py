from rest_framework import serializers
from django.utils import timezone
import datetime


class DueDateSerializerMixin(serializers.Serializer):
    due_date = serializers.DateField(allow_null=True)
    due_description = serializers.CharField(allow_blank=True)
    due_status = serializers.SerializerMethodField()

    THRESHOLD = 7

    def get_due_status(self,obj):
        status = 'set'
        if obj.due_date is None:
            status = 'not_set'
        elif timezone.now().date() > obj.due_date:
            status = 'past'
        elif (timezone.now().date() + datetime.timedelta(
                days=self.THRESHOLD)) >= obj.due_date:
            status = 'soon'
        return status
