from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import acce_dataSerializer
from .models import acce_data
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


@api_view(['POST'])
def login_user(request):
	username = request.data['username']
	password = request.data['password']
	try:
		user = User.objects.get(username=username)
		password_old = user.password
		pwd_valid = check_password(password,password_old)
		if pwd_valid:
			token = Token.objects.filter(user=user).delete()
			token = Token.objects.create(user=user)
			return Response({'token': token.key})
		else:
			return Response({}, status=status.HTTP_401_UNAUTHORIZED)
	except:
		return Response({}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def save_data(request):
	serializers = acce_dataSerializer(data=request.data, context={"request": request})
	if serializers.is_valid():
		serializers.save()
		return Response({})
	else:
		return Response(serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET'])
def get_data(request):
	data = acce_data.objects.all().order_by('-id')
	serializers = acce_dataSerializer(data, many=True, context={"request": request})
	return Response(serializers.data)

