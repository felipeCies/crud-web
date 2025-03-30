from django.urls import path
from .views import EstoqueCreateView, EstoqueDetailView, EstoqueListView, EstoqueUpdateView, EstoqueDeleteView, home
from app import views

urlpatterns = [
    path('', home, name='home'),
    path('login/', views.login_view, name = "login"),
    path('form_estoque/', EstoqueCreateView.as_view(), name="form_estoque"),  
    path('lista_estoque/', EstoqueListView.as_view(), name="lista_estoque"),  
    path('form_estoque/<int:pk>/', EstoqueUpdateView.as_view(), name="editar_produto"),  
    path('lista_produto/<int:pk>/', EstoqueDetailView.as_view(), name="listar_produto"),  
    path('remover_produto/<int:pk>/', EstoqueDeleteView.as_view(), name="remover_produto"),
]

