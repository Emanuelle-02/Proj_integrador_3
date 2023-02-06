from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from apps.recepcionista.models import Appointment


# Create your views here.
class Doctor_Index(View):
    login_url = "/medico_login"

    def get(self, request):
        return render(request, "doc_index.html")


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


def conclude_appointment_view(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.status = True
    appointment.save()
    return redirect(reverse("list_appointment"))
