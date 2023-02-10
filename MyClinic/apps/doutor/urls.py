from django.urls import path

from .views import *

urlpatterns = [
    path("doc_index/", Doctor_Index.as_view(), name="doc_index"),
    path(
        "list_doc_appointments",
        ListDocAppointmentView.as_view(),
        name="list_appointment",
    ),
    path(
        "conclude_appointment/<int:pk>",
        conclude_appointment_view,
        name="conclude_appointment",
    ),
    path(
        "appointment_data/<int:pk>",
        AppointmentDataView.as_view(),
        name="appoint_form",
    ),
    path(
        "complete_appointments",
        ListDocAppointmentCompleteView.as_view(),
        name="list_complete_appointment",
    ),
    # EXAMES
    path(
        "list_doc_exam",
        ListDocExamView.as_view(),
        name="list_exam",
    ),
    path(
        "conclude_exam/<int:pk>",
        conclude_exam_view,
        name="conclude_exam",
    ),
    path(
        "complete_exam",
        ListDocExamCompleteView.as_view(),
        name="list_complete_exam",
    ),
    path("appointment_detail/<int:pk>",AppointmentDocDatailView.as_view(), name="appointment_detail"),
    path("prescription_detail/<int:pk>",PrecriptionDocDatailView.as_view(), name="prescription_detail"),
    path(
        "list_medical_leave", ListMedicalLeaveView.as_view(), name="list_medical_leave",
    ),
    path("create_medical_leave", CreateMedicalLeave.as_view(), name="leave_form"),
    path("leave_detail/<int:pk>",MedicalLeaveDatailView.as_view(), name="leave_detail"),
]
