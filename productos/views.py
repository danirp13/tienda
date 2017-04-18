# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from productos.models import Marca, Zapato
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class ZapatoUpdate(UpdateView):
	model=Zapato
	fields='__all__'

class ZapatoDelete(DeleteView):
	model=Zapato
	success_url=reverse_lazy('zapato-list')

def first_view(request):
		return HttpResponse('<H1>Esta es mi primera vista en django</H1>')

class ZapatoListView(ListView):
	model=Zapato

class ZapatoDetailView(DetailView):
	model=Zapato	

def marca(request):
	marca_list=Marca.objects.all()
	context = {'object_list': marca_list}
	return render(request, 'productos/marca.html', context)		

def marca_detail(request,marca_id):
	marca=Marca.objects.get(id=marca_id)
	context = {'object':marca}
	return render(request, 'productos/marca_detail.html', context)