from django.urls import path

from .views import *

urlpatterns = [
    path(
        "recepcionist_index/", Recepcionist_Index.as_view(), name="recepcionist_index"
    ),
    # CONSULTAS
    path("list_appointments", ListAppointmentView.as_view(), name="appointment_list"),
    path(
        "create_appointment", AppointmentCreateView.as_view(), name="appointment_form"
    ),
    path(
        "edit_appointment/<int:pk>",
        AppointmentEditView.as_view(),
        name="appointment_form",
    ),
    path(
        "delete_appointment/<int:pk>",
        AppointmentDeleteView.as_view(),
        name="delete_appointment",
    ),
    path(
        "list_done_appointments",
        ListDoneAppointmentView.as_view(),
        name="done_appointment_list",
    ),
    # EXAMES
    path("list_exams", ListExamView.as_view(), name="exams_list"),
    path("create_exam", ExamCreateView.as_view(), name="exam_form"),
    path(
        "edit_exam/<int:pk>",
        ExamEditView.as_view(),
        name="exam_form",
    ),
    path(
        "delete_exam/<int:pk>",
        ExamDeleteView.as_view(),
        name="delete_exam",
    ),
    path("list_done_exams", ListDoneExamView.as_view(), name="exams_done_list"),
    # RECEITA
    path("list_receita", ListIncomeView.as_view(), name="list_receita"),
    path("create_income", IncomeCreateView.as_view(), name="receita_form"),
    path("editar_receita/<int:pk>", IncomeEditView.as_view(), name="receita_form"),
    path("delete_receita/<int:pk>", IncomeDeleteView.as_view(), name="delete_receita"),
]
