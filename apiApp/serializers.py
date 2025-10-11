from rest_framework import serializers
from app.models import Example


class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Example
        fields = '__all__'