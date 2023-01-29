from django.urls import include, path

from apps.administrador.views import *

from .views import *

urlpatterns = [
    path("index/", Index.as_view(), name="index"),
    path("list_doctor", ListarDoctorView.as_view(), name="list_doctor"),
    path('cadastrar_medico', DoctorCreateView.as_view(), name='doctor_create'),
    path('cadastrar_recepcionista', RecepcionistCreateView.as_view(), name='recepcionist_create'),
    path("list_recepcionist", ListarRecepcionistView.as_view(), name="list_recepcionist"),
    # Financeiro - Despesas
    path("financeiro/list_despesas", ListarDespesasView.as_view(), name="list_despesas"),
    path("financeiro/lancar_despesa", CreateDespesaView.as_view(), name="despesa_form"),
    path("financeiro/update-despesa/<int:pk>", DespesaUpdateView.as_view(), name="despesa_form"),
    path("financeiro/delete_despesa/<int:pk>", DespesaDeleteView.as_view(), name="delete_despesa"),
    # Financeiro - Categorias
    path("financeiro/categorias/list_categoria", ListarCategoriasView.as_view(), name="list_categoria"),
    path("financeiro/categorias/criar_categoria", CreateCategoriaView.as_view(), name="categoria_form"),
    path("financeiro/categorias/update-categoria/<int:pk>", UpdateCategoriaView.as_view(), name="categoria_form"),
    path("financeiro/categorias/delete_categoria/<int:pk>", DeleteCategoriaView.as_view(), name="delete_categoria"),
] 