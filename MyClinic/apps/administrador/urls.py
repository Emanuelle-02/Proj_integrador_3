from django.urls import include, path

from apps.administrador.views import *

from .views import *

urlpatterns = [
    path("index/", Index.as_view(), name="index"),
    path("medico/list_doctor", ListarDoctorView.as_view(), name="list_doctor"),
    path("cadastrar_medico", DoctorCreateView.as_view(), name="doctor_create"),
    path("delete_medico/<int:pk>", DoctorDeleteView.as_view(), name="doctor_delete"),
    path(
        "cadastrar_recepcionista",
        RecepcionistCreateView.as_view(),
        name="recepcionist_create",
    ),
    path(
        "recepcionista/list_recepcionist", ListarRecepcionistView.as_view(), name="list_recepcionist"
    ),
    path(
        "update_recepcionista/<int:pk>",
        RecepcionistUpdateView.as_view(),
        name="recepcionist_create",
    ),
    path("delete_recepcionista/<int:pk>", RecepcionistDeleteView.as_view(), name="recepcionist_delete"),
    # Fluxo de caixa - Entradas
    path("caixa/list_caixa", ListCaixaView.as_view(), name="list_caixa"),
    path("delete_caixa/<int:pk>", CaixaDeleteView.as_view(), name="delete_caixa"),
    # Fluxo de caixa - Saídas
    path(
        "financeiro/list_despesas", ListarDespesasView.as_view(), name="list_despesas"
    ),
    path("financeiro/lancar_despesa", CreateDespesaView.as_view(), name="despesa_form"),
    path(
        "financeiro/update-despesa/<int:pk>",
        DespesaUpdateView.as_view(),
        name="despesa_form",
    ),
    path(
        "financeiro/delete_despesa/<int:pk>",
        DespesaDeleteView.as_view(),
        name="delete_despesa",
    ),
    # Fluxo de Caixa - Categorias
    path(
        "financeiro/categorias/list_categoria",
        ListarCategoriasView.as_view(),
        name="list_categoria",
    ),
    path(
        "financeiro/categorias/criar_categoria",
        CreateCategoriaView.as_view(),
        name="categoria_form",
    ),
    path(
        "financeiro/categorias/update-categoria/<int:pk>",
        UpdateCategoriaView.as_view(),
        name="categoria_form",
    ),
    path(
        "financeiro/categorias/delete_categoria/<int:pk>",
        DeleteCategoriaView.as_view(),
        name="delete_categoria",
    ),
]
