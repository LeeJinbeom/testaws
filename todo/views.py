from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import TodoGroupSerializer, TodoSerializer, FavouriteGroupSerializer, FavouriteSerializer
from .models import Favourite, FavouriteGroup, Todo, TodoGroup
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def Test(request):

    if request.method == 'GET':
        qs = Todo.objects.all()
        serializer1 = TodoSerializer(qs, many=True)
        serializer2 = TodoSerializer(qs, many=True)
        serializer3 = TodoSerializer(qs, many=True)
        data = {
            "doto1":serializer1.data,
            "doto2":serializer2.data,
            "doto3":serializer3.data
        }

        return Response(data)
    


# Create your views here.
class TodoGroupViewSet(viewsets.ModelViewSet):
    queryset = TodoGroup.objects.all()
    serializer_class = TodoGroupSerializer

class TodoViewSet(viewsets.ModelViewSet):
    
    def get_queryset(self):
        qs = super().get_queryset()

        status = self.request.query_params.get('status')
        if status:
            qs = qs.filter(status=status)
        return qs

    def create(self, request):
        # do your thing here
        print("호호호호호")
        print(request.data)
        print(request.user)
        print(request.data['name'])
        #request.data['name'] = str(request.user)
        #request.data['name'] = request.user
        return super().create(request)

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

class FavouriteGroupViewSet(viewsets.ModelViewSet):
    queryset = FavouriteGroup.objects.all()
    serializer_class = FavouriteGroupSerializer

class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer