from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, TemplateView

from .models import User


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, "home.html")


class Login_Type(View):
    def get(self, request):
        return render(request, "op_login.html")


class Login(View):
    def get(self, request):
        return render(request, "login/login.html")

    def post(self, request):
        #if request.method == "POST":
        context = {"data": request.POST}
        context2 = {"data": request.POST}
        username = request.POST["username"]
        password = request.POST["password"]

        # if username and password:
        user = authenticate(username=username, password=password)
        if user:
            if user.is_staff:
                login(request, user)  # pragma: no cover
                return redirect("index")  # pragma: no cover

            messages.add_message(
                request,
                messages.ERROR,
                "Conta inativa ou inexistente!",
            )
            return render(
                request, "login/login_recepcionist.html", context2, status=401
            )

        messages.add_message(
            request,
            messages.ERROR,
            "Nome de usuário ou senha incorreta, por favor tente novamente",
        )
        return render(request, "login/login.html", context, status=401)


class Login_Reception(View):
    def get(self, request):
        return render(request, "login/login_recepcionist.html")

    def post(self, request):
        #if request.method == "POST":
        context = {"data": request.POST}
        context2 = {"data": request.POST}
        username = request.POST["username"]
        password = request.POST["password"]

            # if username and password:
        user = authenticate(username=username, password=password)
        if user:
            if user.is_recepcionist:
                login(request, user)
                return redirect("recepcionist_index")

            messages.add_message(
                request,
                messages.ERROR,
                "Conta inativa ou inexistente!",
            )
            return render(
                request, "login/login_recepcionist.html", context2, status=401
            )

        messages.add_message(
            request,
            messages.ERROR,
            "Nome de usuário ou senha incorreta, por favor tente novamente",
        )
        return render(request, "login/login_recepcionist.html", context, status=401)


class Login_Doctor(View):
    def get(self, request):
        return render(request, "login/login_doctor.html")

    def post(self, request):
        #if request.method == "POST":
        context = {"data": request.POST}
        context2 = {"data": request.POST}
        username = request.POST["username"]
        password = request.POST["password"]

        # if username and password:
        user = authenticate(username=username, password=password)
        if user:
            if user.is_doctor:
                login(request, user)
                return redirect("doc_index")

            messages.add_message(
                request, messages.ERROR, "Conta inativa ou inexistente!"
            )
            return render(request, "login/login_doctor.html", context2, status=401)

        messages.add_message(
            request,
            messages.ERROR,
            "Nome de usuário ou senha incorreta, por favor tente novamente",
        )
        return render(request, "login/login_doctor.html", context, status=401)


class Logout(View):
    def post(self, request):
        logout(request)
        return redirect("/type_login")