from rest_framework import serializers
from .models import Form
import ipdb


class FormSerializer(serializers.ModelSerializer):
    class Meta:

        model = Form
        fields = "__all__"

    def create(self, validated_data):

        return Form.objects.create(**validated_data)
