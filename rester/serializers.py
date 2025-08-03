
from rest_framework import serializers
from .models import ChangeLog


class AdderSerializer(serializers.Serializer):
class ChangeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeLog
        fields = "__all__"
    n1 = serializers.IntegerField(label="Number 1")
    n2 = serializers.IntegerField(label="Number 2")
    res = serializers.IntegerField(label="Result", read_only=True)

    def create(self, validated_data):
        n1 = validated_data.pop("n1")
        n2 = validated_data.pop("n2")
        res = n1 + n2
        return {
            "res": res,
            "n1": n1,
            "n2": n2,
        }
