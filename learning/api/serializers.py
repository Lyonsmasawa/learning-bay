from dataclasses import field
from rest_framework.serializers import ModelSerializer
from learning.models import Group

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'