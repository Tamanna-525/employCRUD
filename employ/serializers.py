from rest_framework import serializers
from .models import employ

class employSerializer(serializers.ModelSerializer):
    class Meta:
        model = employ
        fields = '__all__'