from django.shortcuts import render
from .models import Klass, Teacher, Student
from .serializers import KlassSerializer, TeacherSerializer, StudentSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class KlassViewSet(ModelViewSet):
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer