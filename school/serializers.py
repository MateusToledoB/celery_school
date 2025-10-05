from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

        def validate_cpf(self, value):
            if Student.objects.filter(cpf=value).exists():
                raise serializers.ValidationError("CPF must be unique.")
            return value
