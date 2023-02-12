from django.urls import include, path

from apps.administrador.views import *

from .views import *

# app_name = "administrador"
urlpatterns = [
    # MÉDICO
    path("index/", Index.as_view(), name="index"),
    path("medico/list_doctor", ListDoctorView.as_view(), name="list_doctor"),
    path("cadastrar_medico", DoctorCreateView.as_view(), name="doctor_create"),
    path(
        "update_medico/<int:pk>",
        DoctorUpdateView.as_view(),
        name="doctor_create",
    ),
    path(
        "remove_doctor/<int:pk>",
        desative_doctor,
        name="remove_doctor",
    ),
    # RECEPCIONISTA
    path(
        "cadastrar_recepcionista",
        RecepcionistCreateView.as_view(),
        name="recepcionist_create",
    ),
    path(
        "recepcionista/list_recepcionist",
        ListRecepcionistView.as_view(),
        name="list_recepcionist",
    ),
    path(
        "update_recepcionista/<int:pk>",
        RecepcionistUpdateView.as_view(),
        name="recepcionist_create",
    ),
    path(
        "remove_recepcionist/<int:pk>",
        desative_recepcionist,
        name="remove_recepcionist",
    ),
    # Fluxo de caixa - Entradas
    path("caixa/list_caixa", ListAdminIncomeView.as_view(), name="list_caixa"),
    path("delete_caixa/<int:pk>", AdminIncomeDeleteView.as_view(), name="delete_caixa"),
    # Fluxo de caixa - Saídas
    path("financeiro/list_despesas", ListExpenseView.as_view(), name="list_despesas"),
    path("financeiro/lancar_despesa", CreateExpenseView.as_view(), name="despesa_form"),
    path(
        "financeiro/update-despesa/<int:pk>",
        ExpenseUpdateView.as_view(),
        name="despesa_form",
    ),
    path(
        "financeiro/delete_despesa/<int:pk>",
        ExpenseDeleteView.as_view(),
        name="delete_despesa",
    ),
    # Fluxo de Caixa - Categorias
    path(
        "financeiro/categorias/list_categoria",
        ListCategoryView.as_view(),
        name="list_categoria",
    ),
    path(
        "financeiro/categorias/criar_categoria",
        CreateCategoryView.as_view(),
        name="categoria_form",
    ),
    path(
        "financeiro/categorias/update-categoria/<int:pk>",
        UpdateCategoryView.as_view(),
        name="categoria_form",
    ),
    path(
        "financeiro/categorias/delete_categoria/<int:pk>",
        DeleteCategoryView.as_view(),
        name="delete_categoria",
    ),
    path("export_excel", export_excel, name="export_excel"),
]
