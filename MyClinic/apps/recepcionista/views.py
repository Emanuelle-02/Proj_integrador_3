from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from apps.recepcionista.forms import AppointmentForm, ExamForm, IncomeForm

from .models import Appointment, Exam, Income

# Create your views here.


class Recepcionist_Index(LoginRequiredMixin, View):
    login_url = "/recepcionista_login"

    def get(self, request):
        consultas = Appointment.objects.filter(status=False).count()
        exames = Exam.objects.filter(status=False).count()
        
        context = {
            "consultas": consultas,
            "exames": exames,
        }
        return render(request, "recepcionist_index.html", context)


class ListIncomeView(LoginRequiredMixin, View):
    login_url = "/recepcionista_login"

    def get(self, request):
        rendas = Income.objects.all()
        paginator = Paginator(rendas, 5)
        pagina_num = request.GET.get("page")
        obj_pagina = Paginator.get_page(paginator, pagina_num)
        context = {
            "rendas": rendas,
            "obj_pagina": obj_pagina,
        }
        return render(request, "receita/list_receita.html", context)


class IncomeCreateView(LoginRequiredMixin, CreateView):
    login_url = "/recepcionista_login"
    model = Income
    form_class = IncomeForm
    template_name = "receita/receita_form.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect("list_receita")


class IncomeEditView(LoginRequiredMixin, UpdateView):
    login_url = "/recepcionista_login"
    model = Income
    form_class = IncomeForm
    template_name = "receita/receita_form.html"
    success_url = "/list_receita"


class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/recepcionista_login"
    model = Income
    success_url = "/list_receita"

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class ListAppointmentView(LoginRequiredMixin, View):
    login_url = "/recepcionista_login"

    def get(self, request):
        consulta = Appointment.objects.filter(status=False)
        paginator = Paginator(consulta, 5)
        pagina_num = request.GET.get("page")
        obj_pagina = Paginator.get_page(paginator, pagina_num)
        context = {
            "consulta": consulta,
            "obj_pagina": obj_pagina,
        }
        return render(request, "consultas/appointment_list.html", context)


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    login_url = "/recepcionista_login"
    model = Appointment
    form_class = AppointmentForm
    template_name = "consultas/appointment_form.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect("list_appointments")


class AppointmentEditView(LoginRequiredMixin, UpdateView):
    login_url = "/recepcionista_login"
    model = Appointment
    form_class = AppointmentForm
    template_name = "consultas/appointment_form.html"
    success_url = "/list_appointments"


class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/recepcionista_login"
    model = Appointment
    success_url = "/list_appointments"

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class ListExamView(LoginRequiredMixin, View):
    login_url = "/recepcionista_login"

    def get(self, request):
        exame = Exam.objects.filter(status=False)
        paginator = Paginator(exame, 5)
        pagina_num = request.GET.get("page")
        obj_pagina = Paginator.get_page(paginator, pagina_num)
        context = {
            "exame": exame,
            "obj_pagina": obj_pagina,
        }
        return render(request, "exames/list_exams.html", context)
    

class ExamCreateView(LoginRequiredMixin, CreateView):
    login_url = "/recepcionista_login"
    model = Exam
    form_class = ExamForm
    template_name = "exames/exam_form.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect("list_exams")


class ExamEditView(LoginRequiredMixin, UpdateView):
    login_url = "/recepcionista_login"
    model = Exam
    form_class = ExamForm
    template_name = "exames/exam_form.html"
    success_url = "/list_exams"


class ExamDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/recepcionista_login"
    model = Exam
    success_url = "/list_exams"

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class ListDoneAppointmentView(LoginRequiredMixin, View):
    login_url = "/recepcionista_login"

    def get(self, request):
        consulta = Appointment.objects.filter(status=True)
        paginator = Paginator(consulta, 5)
        pagina_num = request.GET.get("page")
        obj_pagina = Paginator.get_page(paginator, pagina_num)
        context = {
            "consulta": consulta,
            "obj_pagina": obj_pagina,
        }
        return render(request, "consultas/done_appointment_list.html", context)
    

class ListDoneExamView(LoginRequiredMixin, View):
    login_url = "/recepcionista_login"

    def get(self, request):
        exame = Exam.objects.filter(status=True)
        paginator = Paginator(exame, 5)
        pagina_num = request.GET.get("page")
        obj_pagina = Paginator.get_page(paginator, pagina_num)
        context = {
            "exame": exame,
            "obj_pagina": obj_pagina,
        }
        return render(request, "exames/list_done_exams.html", context)