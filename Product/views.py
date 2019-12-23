from django.shortcuts import render

from rest_framework import generics, permissions
#from .serializers import PostSerializer
#from .permissions import IsAuthorOrReadOnly


def home(request):
    return render('home')
