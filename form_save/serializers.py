from rest_framework import serializers
from .models import Form
import ipdb


class FormSerializer(serializers.ModelSerializer):
    class Meta:

        model = Form
        fields = [
            "id",
            "type",
            "date",
            "value",
            "cpf",
            "creditCard",
            "time",
            "storeOwner",
            "storeName",
        ]
        read_only_fields = ["id"]

    # ipdb.set_trace()

    def create(self, validated_data):

        return Form.objects.create(**validated_data)
