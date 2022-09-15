from rest_framework import serializers
from .models import Feedback

class ClientSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Feedback
        fields = '__all__'


class ClientDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'