from rest_framework import serializers
from project.Models.LeadForm import *

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"

    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Name must contain at least 3 characters."
            )
        return value

    def validate_phone(self, value):
        value = str(value)

        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only digits."
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must be 10 digits."
            )

        return value

    def validate_email(self, value):
        if Lead.objects.filter(email=value).exclude(
            pk=self.instance.pk if self.instance else None
        ).exists():
            raise serializers.ValidationError(
                "Email already exists."
            )
        return value