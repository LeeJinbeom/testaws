from rest_framework import serializers
from rest_framework.validators import UniqueValidator, ValidationError
from .models import Favourite, FavouriteGroup, Todo, TodoGroup

class FavouriteGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteGroup
        fields = '__all__'

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'

class TodoGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoGroup
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

# class TodoSerializer(serializers.Serializer):

