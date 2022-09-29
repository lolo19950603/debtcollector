from django.shortcuts import render
from django.http import HttpResponse
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

def debtors_detail(request, debtor_id):
  debtor = Debtor.objects.get(id=debtor_id)
  return render(request, 'debtors/detail.html', { 'debtor': debtor })