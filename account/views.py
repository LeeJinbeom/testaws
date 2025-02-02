from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view, action, permission_classes
from .serializers import UserSerializer

# Create your views here.
@api_view(['POST'])
def join(request):

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)