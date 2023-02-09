from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.accounts.forms import DoctorForm, RecepcionistForm
from apps.accounts.models import Doctor, Recepcionist, User
from apps.recepcionista.forms import IncomeForm
from apps.recepcionista.models import Income

from .forms import CategoryForm, ExpensesForm
from .models import Category, Expenses


# Create your views here.
class Index(View):
    login_url = "/admin_login"

    def get(self, request):
        medicos = User.objects.filter(is_doctor=True, is_active=True).count()
        recepcionistas = User.objects.filter(
            is_recepcionist=True, is_active=True
        ).count()
        receitas = Income.objects.all()
        despesas = Expenses.objects.all()
        total_receita = 0
        total_despesa = 0
        saldo = 0

        for despesa in despesas:
            total_despesa += despesa.value
        for receita in receitas:
            total_receita += receita.value

        saldo = total_receita - total_despesa

        context = {
            "medicos": medicos,
            "recepcionistas": recepcionistas,
            "total_receita": total_receita,
            "total_despesa": total_despesa,
            "saldo": saldo,
        }
        return render(request, "index.html", context)


class ListDoctorView(LoginRequiredMixin, ListView):
    login_url = "/admin_login"

    def get(self, request):
        medico = Doctor.objects.all()
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


class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/admin_login"
    model = User
    form_class = DoctorForm
    template_name = "create_form.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/medico/list_doctor")


class ListRecepcionistView(LoginRequiredMixin, ListView):
    login_url = "/admin_login"

    def get(self, request):
        recepcionista = Recepcionist.objects.all()
        # recepcionista = User.objects.filter(is_recepcionist=True)
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
    # success_url = "/recepcionista/list_recepcionist"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/recepcionista/list_recepcionist")


# Fluxo de caixa - saída
class ListExpenseView(LoginRequiredMixin, ListView):
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


class CreateExpenseView(LoginRequiredMixin, CreateView):
    login_url = "/admin_login"
    model = Expenses
    form_class = ExpensesForm
    template_name = "despesas/despesa_form.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect("/financeiro/list_despesas")


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/admin_login"
    model = Expenses
    form_class = ExpensesForm
    template_name = "despesas/despesa_form.html"
    success_url = "/financeiro/list_despesas"


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/admin_login"
    model = Expenses
    success_url = "/financeiro/list_despesas"

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


# Categorias
class ListCategoryView(LoginRequiredMixin, View):
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


class CreateCategoryView(LoginRequiredMixin, CreateView):
    login_url = "/admin_login"
    model = Category
    form_class = CategoryForm
    template_name = "despesas/categoria_form.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect("/financeiro/categorias/list_categoria")


class UpdateCategoryView(LoginRequiredMixin, UpdateView):
    login_url = "/admin_login"
    model = Category
    form_class = CategoryForm
    template_name = "despesas/categoria_form.html"
    success_url = "/financeiro/categorias/list_categoria"


class DeleteCategoryView(LoginRequiredMixin, DeleteView):
    login_url = "/admin_login"
    model = Category
    success_url = "/financeiro/categorias/list_categoria"

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


# Fluxo de caixa - Entrada
class ListAdminIncomeView(LoginRequiredMixin, View):
    login_url = "/admin_login"

    def get(self, request):
        rendas = Income.objects.all()
        paginator = Paginator(rendas, 5)
        pagina_num = request.GET.get("page")
        obj_pagina = Paginator.get_page(paginator, pagina_num)
        context = {
            "rendas": rendas,
            "obj_pagina": obj_pagina,
        }
        return render(request, "caixa/list_caixa.html", context)


class AdminIncomeDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/admin_login"
    model = Income
    success_url = "/caixa/list_caixa"

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


def desative_recepcionist(request, pk):
    if request.method == "GET":
        user = User.objects.get(id=pk)
        if "check" in request.GET:
            user.is_active = True
        else:
            user.is_active = False
        user.save()
        return redirect("/recepcionista/list_recepcionist")
    return redirect("/")


def desative_doctor(request, pk):
    if request.method == "GET":
        user = User.objects.get(id=pk)
        if "check" in request.GET:
            user.is_active = True
        else:
            user.is_active = False
        user.save()
        return redirect("/medico/list_doctor")
    return redirect("/")
