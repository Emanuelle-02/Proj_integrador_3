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
        name="appointment_form",
    ),
    path(
        "complete_appointments",
        ListDocAppointmentCompleteView.as_view(),
        name="list_complete_appointment",
    ),
]
