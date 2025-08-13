from rest_framework import serializers
from .models import inscrito
class InscritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = inscrito
        fields = '__all__'