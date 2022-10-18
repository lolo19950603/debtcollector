from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Debtor
from .forms import PaymentForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def debtors_detail(request, debtor_id):
  debtor = Debtor.objects.get(id=debtor_id)
  payment_form = PaymentForm()
  return render(request, 'debtors/detail.html', {
    'debtor': debtor, 'payment_form': payment_form
  })

def add_payment(request, debtor_id):
  form = PaymentForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_payment = form.save(commit=False)
    new_payment.debtor_id = debtor_id
    new_payment.save()
    debtor = Debtor.objects.get(id=debtor_id)
    debtor.debt = debtor.debt - new_payment.payment
    debtor.save()
  return redirect('detail', debtor_id=debtor_id)

class DebtorList(ListView):
  model = Debtor

class DebtorDetail(DetailView):
  model = Debtor

class DebtorCreate(CreateView):
  model = Debtor
  fields = '__all__'

class DebtorUpdate(UpdateView):
  model = Debtor
  fields = ['debt', 'age']

class DebtorDelete(DeleteView):
  model = Debtor
  success_url = '/debtors/'