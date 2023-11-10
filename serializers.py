# myapp/serializers.py
from rest_framework.serializers import ModelSerializer
from myapp.models import CustomUsers

class pUserSerializer(ModelSerializer):
      class Meta:
            model = CustomUsers
            fields ='__all__'