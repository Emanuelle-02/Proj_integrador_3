from django.urls import path

from .views import *

urlpatterns = [
    path("doc_index/", Doctor_Index.as_view(), name="doc_index"),
    path("list_doc_appointments", ListDocAppointmentView.as_view(), name="list_appointment"),
]