from django.urls import include, path

from .views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', Home.as_view(), name="home"),
    path('type_login/', Login_Type.as_view(), name="op_login"),
    path('admin_login/', Login.as_view(), name="login"),
    path('recepcionista_login/', Login_Reception.as_view(), name="login_recepcionist"),
    path('medico_login/', Login_Doctor.as_view(), name="login_doctor"),
    path("logout/", Logout.as_view(), name="logout"),
]