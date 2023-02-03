from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView

from apps.accounts.forms import DoctorForm, RecepcionistForm
from apps.accounts.models import User

from .forms import CategoryForm, ExpensesForm
from .models import Category, Expenses


# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, "index.html")


class ListarDoctorView(LoginRequiredMixin, View):
    login_url = "/admin_login"

    def get(self, request):
        medico = User.objects.filter(is_doctor=True)
        paginator = Paginator(medico, 4)
        pagina_num = request.GET.get("page")
        obj_pagina = Paginator.get_page(paginator, pagina_num)
        context = {
            "medico": medico,
            "obj_pagina": obj_pagina,
        }

        return render(request, "medico/list_doctor.html", context)


class DoctorCreateView(LoginRequiredMixin, CreateView):
    login_url = "/admin_login"
    model = User
    form_class = DoctorForm
    template_name = "create_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "doctor"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/medico/list_doctor")
        

class DoctorDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/admin_login"
    model = User
    success_url = "/medico/list_doctor"
    
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class ListarRecepcionistView(LoginRequiredMixin, View):
    login_url = "/admin_login"

    def get(self, request):
        recepcionista = User.objects.filter(is_recepcionist=True)
        paginator = Paginator(recepcionista, 4)
        pagina_num = request.GET.get("page")
        obj_pagina = Paginator.get_page(paginator, pagina_num)
        context = {
            "recepcionista": recepcionista,
            "obj_pagina": obj_pagina,
        }

        return render(request, "recepcionista/list_recepcionist.html", context)


class RecepcionistCreateView(LoginRequiredMixin, CreateView):
    login_url = "/admin_login"
    model = User
    form_class = RecepcionistForm
    template_name = "create_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "recepcionist"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("recepcionista/list_recepcionist")


class RecepcionistUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/admin_login"
    model = User
    form_class = RecepcionistForm
    template_name = "create_form.html"
    success_url = "/recepcionista/list_recepcionist"

class RecepcionistDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/admin_login"
    model = User
    success_url = "/recepcionista/list_recepcionist"
    
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


# DESPESAS
class ListarDespesasView(LoginRequiredMixin, View):
    login_url = "/admin_login"

    def get(self, request):
        despesas = Expenses.objects.all()
        paginator = Paginator(despesas, 4)
        pagina_num = request.GET.get("page")
        obj_pagina = Paginator.get_page(paginator, pagina_num)
        context = {
            "despesas": despesas,
            "obj_pagina": obj_pagina,
        }
        return render(request, "despesas/list_despesas.html", context)


class CreateDespesaView(LoginRequiredMixin, CreateView):
    login_url = "/admin_login"
    model = Expenses
    form_class = ExpensesForm
    template_name = "despesas/despesa_form.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect("/financeiro/list_despesas")


class DespesaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/admin_login"
    model = Expenses
    form_class = ExpensesForm
    template_name = "despesas/despesa_form.html"
    success_url = "/financeiro/list_despesas"


class DespesaDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/admin_login"
    model = Expenses
    success_url = "/financeiro/list_despesas"

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


# Categorias
class ListarCategoriasView(LoginRequiredMixin, View):
    login_url = "/admin_login"

    def get(self, request):
        categoria = Category.objects.all()
        paginator = Paginator(categoria, 4)
        pagina_num = request.GET.get("page")
        obj_pagina = Paginator.get_page(paginator, pagina_num)
        context = {
            "categoria": categoria,
            "obj_pagina": obj_pagina,
        }
        return render(request, "despesas/list_categoria.html", context)


class CreateCategoriaView(LoginRequiredMixin, CreateView):
    login_url = "/admin_login"
    model = Category
    form_class = CategoryForm
    template_name = "despesas/categoria_form.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect("/financeiro/categorias/list_categoria")


class UpdateCategoriaView(LoginRequiredMixin, UpdateView):
    login_url = "/admin_login"
    model = Category
    form_class = CategoryForm
    template_name = "despesas/categoria_form.html"
    success_url = "/financeiro/categorias/list_categoria"


class DeleteCategoriaView(LoginRequiredMixin, DeleteView):
    login_url = "/admin_login"
    model = Category
    success_url = "/financeiro/categorias/list_categoria"

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
