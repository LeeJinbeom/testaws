from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import status
from .serializers import StudentSerializer, StudentBasicSerializer
from .models import Students
import json

@api_view(['GET','POST'])
def Test(request, pk):

    if request.method == 'GET':
        qs = Students.objects.all()
        serializer = StudentBasicSerializer(qs, many=True)

        print(JSONRenderer().render(serializer.data))
        print(JSONParser().parse(BytesIO(JSONRenderer().render(serializer.data))))
        return Response(serializer.data)
    
    elif request.method == 'POST':
        qs = get_object_or_404(Students, pk=pk)
        # serializer = StudentBasicSerializer(data=request.data)
        serializer = StudentBasicSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()




class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name=name)
        return qs

    @action(detail=False, methods=['GET'])
    def incheon(self, request):
        qs = self.get_queryset().filter(address__contains='인천')
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PUT'])
    def init(self, request, pk):
        instance = self.get_object()
        instance.address = ""
        instance.email = ""
        instance.save(update_fields=['address', 'email'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



# class StudentView(APIView):

#     def get(self, request):
#         qs = Students.objects.filter()
#         serializer = StudentSerializer(qs, many=True)
#         return Response(serializer.data)        

#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors)


# class StudentDetailView(APIView):

#     def get_object(self, pk):
#         return get_object_or_404(Students, pk=pk)

#     def get(self, request, pk):
#         qs = self.get_object(pk)
#         serializer = StudentSerializer(qs)
#         return Response(serializer.data)        

#     def put(self, request, pk):
#         qs = self.get_object(pk)
#         serializer = StudentSerializer(qs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         qs = self.get_object(pk)
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def StudentView(request):

#     if request.method == 'GET':
#         qs = Students.objects.filter()
#         serializer = StudentSerializer(qs, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'PUT', 'DELETE'])
# def StudentDetailView(request, pk):

#     qs = get_object_or_404(Students, pk=pk)

#     if request.method == 'GET':
#         serializer = StudentSerializer(qs)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = StudentSerializer(qs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         qs.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

