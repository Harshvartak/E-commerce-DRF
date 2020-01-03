from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer


@api_view(['POST', ])


def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			CustomUser = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['username']= CustomUser.username
			token = Token.objects.get(user=CustomUser).key
			data['token']=token
		else:
			data = serializer.errors
		return Response(data)
