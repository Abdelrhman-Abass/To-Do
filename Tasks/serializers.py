from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
# 	def validate(self, attrs):
# 		print('in')
# 		user = authenticate(username=attrs['username'], password=attrs['password'])
# 		if user is not None:
# 			if user.is_active:
# 				data = super().validate(attrs)
# 				refresh = self.get_token(self.user)
# 				refresh['username'] = self.user.username
# 				try:
# 					obj = UserProfile.objects.get(user=self.user)
# 					data["refresh"] = str(refresh)
# 					data["access"] = str(refresh.access_token)
# 					data["user_id"] = self.user.id
# 					data['user_name']= self.user.username
# 					data["email"] = self.email
# 					data["birth"] = obj.birth
# 					data["name"] = obj.name
# 					data['first_name']= self.user.first_name
# 					data['last_name']= self.user.last_name
# 				except Exception as e:
# 					raise serializers.ValidationError('Something Wrong!')
# 				return data
# 			else:
# 				raise serializers.ValidationError('Account is Blocked')
# 		else:
# 			raise serializers.ValidationError('Incorrect userid/email and password combination!')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ['name']        
