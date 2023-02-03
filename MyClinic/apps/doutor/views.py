from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
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
        consulta = Appointment.objects.filter(doctor=request.user.doctor)
        paginator = Paginator(consulta, 5)
        pagina_num = request.GET.get("page")
        obj_pagina = Paginator.get_page(paginator, pagina_num)
        context = {
            "consulta": consulta,
            "obj_pagina": obj_pagina,
        }
        return render(request, "consulta/list_appointment.html", context)
