from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Debtor


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Add new view
def debtors_index(request):
  debtors = Debtor.objects.all()
  return render(request, 'debtors/index.html', { 'debtors': debtors })

class DebtorList(ListView):
  model = Debtor

class DebtorDetail(DetailView):
  model = Debtor

class DebtorCreate(CreateView):
  model = Debtor
  fields = '__all__'

class DebtorUpdate(UpdateView):
  model = Debtor
  fields = ['debts', 'age']

class DebtorDelete(DeleteView):
  model = Debtor
  success_url = '/debtors/'