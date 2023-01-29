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
        error = ""
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST["password"]
            user = authenticate(username= username, password=password)
            try:
                if user.is_staff:
                    login(request, user)
                    return redirect("index")
                else:
                    error = "yes"
            except:
                error = "yes"
        d = {'error':error}
        return render(request, "login/login.html", d)


class Login_Reception(View):
    def get(self, request):
        return render(request, "login/login_recepcionist.html")

    def post(self, request):
        error = ""
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST["password"]
            user = authenticate(username= username, password=password)
            try:
                if user.is_recepcionist:
                    login(request, user)
                    return redirect("recepcionist_index")
                
                else:
                    error = "yes"
            except:
                error = "yes"
        d = {'error':error}
        return render(request, "login/login_recepcionist.html", d)
        

class Login_Doctor(View):
    def get(self, request):
        return render(request, "login/login_doctor.html")

    def post(self, request):
        error = ""
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST["password"]
            user = authenticate(username= username, password=password)
            try:
                if user.is_doctor:
                    login(request, user)
                    return redirect("doc_index")
                
                else:
                    error = "yes"
            except:
                error = "yes"
        d = {'error':error}
        return render(request, "login/login_doctor.html", d)


class Logout(View):
    def post(self, request):
        logout(request)
        return redirect('op_login')
