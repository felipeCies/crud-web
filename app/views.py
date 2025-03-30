from django.contrib import messages
from django.shortcuts import render

from django.views.generic import CreateView
from .models import Estoque
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ( CreateView, ListView, UpdateView, DetailView, DeleteView )
from django.urls import reverse_lazy

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  
            login(request, user)   
            return redirect('lista_estoque')  
        

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')


class EstoqueCreateView(CreateView):
    model= Estoque
    fields = "__all__"
    template_name = "form_estoque.html"
    success_url = reverse_lazy ("lista_estoque")   

class EstoqueListView(ListView):
    model = Estoque
    template_name = "lista_estoque.html"

class EstoqueUpdateView(UpdateView):
    model = Estoque
    fields = "__all__"
    template_name = "form_estoque.html"
    success_url = reverse_lazy("lista_estoque")
    
class EstoqueDetailView(DetailView):
    model = Estoque  
    template_name = "lista_produto.html" 
    context_object_name = "fun"
    
class EstoqueDeleteView(DeleteView):
    model = Estoque
    template_name = "remover_produto.html"
    success_url = reverse_lazy("lista_estoque")
    
