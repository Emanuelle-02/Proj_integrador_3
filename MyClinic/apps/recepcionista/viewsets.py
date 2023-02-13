from rest_framework import viewsets
from rest_framework.response import Response

from apps.recepcionista import serializer
from apps.recepcionista.models import Appointment, Exam, Income

from .serializer import AppointmentSerializer, ExamSerializer, IncomeSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.filter(status=False)
    serializer_class = AppointmentSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.filter(status=False)
    serializer_class = ExamSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
