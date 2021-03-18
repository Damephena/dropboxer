from rest_framework import serializers

from .models import DropBox

class DropBoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = DropBox
        fields = '__all__'
