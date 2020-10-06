from rest_framework import serializers
from rest_framework.validators import UniqueValidator, ValidationError
from django.contrib.auth import get_user_model
from .models import Students

class StudentBasicSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    email = serializers.CharField()

    def create(self, validated_data):
        return Students.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    User = get_user_model()
    class Meta:
        model = get_user_model()
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length = 10, 
    #                             validators = [UniqueValidator(queryset=Students.objects.all())])
    class Meta:
        model = Students
        fields = ['id', 'name', 'address', 'email', 'reg_user']

    # def validate_name(self, value):
    #     if len(value) < 3:
    #         raise ValidationError('3글자 이상은 적어주세요~')
    #     return value

    def validate(self, data):
        if len(data['name']) < 3:
            raise ValidationError('3글자 이상은 적어주세요~')
        return data
