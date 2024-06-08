from rest_framework.serializers import ModelSerializer
from .models import Klass, Teacher, Student


class KlassSerializer(ModelSerializer):
    class Meta:
        model = Klass
        fields = '__all__'


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'