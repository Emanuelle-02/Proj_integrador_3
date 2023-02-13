from rest_framework import serializers

from apps.recepcionista.models import Appointment, Exam, Income


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            "id",
            "patient",
            "age",
            "gender",
            "description",
            "doctor",
            "date",
            "user",
            "status",
            "sintoms",
            "medication",
            "exam",
        ]


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = [
            "id",
            "patient",
            "age",
            "gender",
            "type",
            "doctor",
            "date",
            "user",
            "status",
        ]


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ["id", "description", "value", "date", "user", "type_income"]
