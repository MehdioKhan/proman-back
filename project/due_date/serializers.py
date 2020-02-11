from rest_framework import serializers
from django.utils import timezone
import datetime


class DueDateSerializerMixin(serializers.Serializer):
    due_date = serializers.DateField(allow_null=True)
    due_description = serializers.CharField(allow_blank=True)
    due_days = serializers.SerializerMethodField()

    THRESHOLD = 7

    def get_due_days(self,obj):
        if not obj.due_date:
            return 'not_set'
        days = (obj.due_date - timezone.now().date())/(3600*24)
        return days
