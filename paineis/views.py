from operator import add
from django.shortcuts import render, redirect
from paineis.forms import CounterCreateForm
from typing import Counter
from .models import Counter
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from .forms import CounterCreateForm
from django.contrib.auth.decorators import login_required



# Create your views here.


@login_required
def home(response):   
    title ='Bem vindo a pagina'
    form = 'Welcome this is the Home Page'
    add_panel = 'Adicionar Paineis'
    total = 'Total de Paineis'
    values = 'Total a receber' 
    paineis = 'Paineis e dias'
    context = {
        'title': title,
        'form': form,     
        'add_panel': add_panel,
        'total': total, 
        'values': values,
        'paineis': paineis,
    }
    
    return render(response, 'home.html',context)



@login_required
def quantity(response):         
    title = 'Quantidade de Paineis'
    queryset = Counter.objects.all()     
    context = {
        'title': title,
        'queryset': queryset,                    
    }  

    return render(response,'quantity.html', context)  

@login_required
def add_panel(request):       
    form = CounterCreateForm(request.POST or None)       
    if form.is_valid():                         
        queryset = Counter.objects.all()     
        instance = form.save(commit=False)
        instance.values_to_receive = instance.quantities * float(6.5)
        instance.total = instance.quantities + sum([item.quantities for item in queryset])
        instance.total_to_receive = instance.values_to_receive + sum([item.values_to_receive for item in queryset])   
        form.save()                      
        return redirect('/quantity')        
    context = {
        'form': form,
        'title': 'Adicionar Paineis',                    
    }    
    return render(request,'add_panel.html', context) 


@login_required
def total_a_receber(request):  
    form = CounterCreateForm(request.POST or None)       
    if form.is_valid():      
        instance.value = instance.total_to_receive  
        instance = form.save(commit=False)        
    return render(request, 'total_a_receber.html')



    






        