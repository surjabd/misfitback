from django.contrib.auth.models import User
from rest_framework import serializers
from .models import acce_data


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'email')
        write_only_fields = ('password',)
    def create(self, validated_data):
    	user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
    	return user


class acce_dataSerializer(serializers.ModelSerializer):
	class Meta:
		model = acce_data
		fields = ['device_id', 'data_x', 'data_y', 'data_z']

