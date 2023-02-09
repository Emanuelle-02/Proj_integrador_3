from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from apps.doutor.forms import AppointmentPrescriptionForm
from apps.recepcionista.models import Appointment, Exam


# Create your views here.
class Doctor_Index(View):
    login_url = "/medico_login"

    def get(self, request):
        consultas = Appointment.objects.filter(
            doctor=request.user.doctor, status=False
        ).count()
        exames = Exam.objects.filter(doctor=request.user.doctor, status=False).count()

        context = {
            "consultas": consultas,
            "exames": exames,
        }
        return render(request, "doc_index.html", context)


class ListDocAppointmentView(LoginRequiredMixin, View):
    login_url = "/medico_login"

    def get(self, request):
        consulta = Appointment.objects.filter(doctor=request.user.doctor, status=False)
        paginator = Paginator(consulta, 5)
        pagina_num = request.GET.get("page")
        obj_pagina = Paginator.get_page(paginator, pagina_num)
        context = {
            "consulta": consulta,
            "obj_pagina": obj_pagina,
        }
        return render(request, "consulta/list_appointment.html", context)


class ListDocAppointmentCompleteView(LoginRequiredMixin, View):
    login_url = "/medico_login"

    def get(self, request):
        consulta = Appointment.objects.filter(doctor=request.user.doctor, status=True)
        paginator = Paginator(consulta, 5)
        pagina_num = request.GET.get("page")
        obj_pagina = Paginator.get_page(paginator, pagina_num)
        context = {
            "consulta": consulta,
            "obj_pagina": obj_pagina,
        }
        return render(request, "consulta/list_complete_appointment.html", context)


class AppointmentDataView(LoginRequiredMixin, UpdateView):
    login_url = "/recepcionista_login"
    model = Appointment
    form_class = AppointmentPrescriptionForm
    template_name = "consulta/appoint_form.html"
    success_url = "/list_doc_appointments"


class AppointmentDatailView(LoginRequiredMixin, DetailView):
    login_url = "/recepcionista_login"
    model = Appointment


def conclude_appointment_view(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.status = True
    appointment.save()
    return redirect(reverse("list_appointment"))


def conclude_exam_view(request, pk):
    exam = Exam.objects.get(id=pk)
    exam.status = True
    exam.save()
    return redirect(reverse("list_exam"))


class ListDocExamView(LoginRequiredMixin, View):
    login_url = "/medico_login"

    def get(self, request):
        exame = Exam.objects.filter(doctor=request.user.doctor, status=False)
        paginator = Paginator(exame, 5)
        pagina_num = request.GET.get("page")
        obj_pagina = Paginator.get_page(paginator, pagina_num)
        context = {
            "exame": exame,
            "obj_pagina": obj_pagina,
        }
        return render(request, "exame/list_exam.html", context)


class ListDocExamCompleteView(LoginRequiredMixin, View):
    login_url = "/medico_login"

    def get(self, request):
        exame = Exam.objects.filter(doctor=request.user.doctor, status=True)
        paginator = Paginator(exame, 5)
        pagina_num = request.GET.get("page")
        obj_pagina = Paginator.get_page(paginator, pagina_num)
        context = {
            "exame": exame,
            "obj_pagina": obj_pagina,
        }
        return render(request, "exame/list_complete_exam.html", context)
