from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Student, StudentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

