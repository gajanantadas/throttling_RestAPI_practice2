from django.shortcuts import render
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle
# Create your views here.
class EmployeeList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope='viewemp'
class EmployeeCreate(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modify'

class EmployeeUpdate(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modify'

class EmployeeDestroy(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_classes = [ScopedRateThrottle]


