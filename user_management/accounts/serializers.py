from rest_framework import seralizers
from django.contrib.auth import get_user_model

class UserSerializer(serializer.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ('id', 'username', 'email', 'first_name', 'last_name')
