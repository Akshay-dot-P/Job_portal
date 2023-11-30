# myapp/serializers.py
from rest_framework import serializers

class JobSerializer(serializers.Serializer):
    title = serializers.CharField()
    degree_batch = serializers.CharField()
    location = serializers.CharField()
    date_text = serializers.CharField()
    link = serializers.URLField()
