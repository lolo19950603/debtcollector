from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Debtor, Insurance
from .forms import PaymentForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def debtors_detail(request, debtor_id):
  debtor = Debtor.objects.get(id=debtor_id)
  insurance_debtor_doesnt_have = Insurance.objects.exclude(id__in = debtor.insurance.all().values_list('id'))
  payment_form = PaymentForm()
  return render(request, 'debtors/detail.html', {
    'debtor': debtor, 'payment_form': payment_form,
    'insurance': insurance_debtor_doesnt_have
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

def assoc_insurance(request, debtor_id, insurance_id):
  Debtor.objects.get(id=debtor_id).insurance.add(insurance_id)
  return redirect('detail', debtor_id=debtor_id)

class DebtorList(ListView):
  model = Debtor

class DebtorDetail(DetailView):
  model = Debtor

class DebtorCreate(CreateView):
  model = Debtor
  fields = ['name', 'debt', 'age']

class DebtorUpdate(UpdateView):
  model = Debtor
  fields = ['debt', 'age']

class DebtorDelete(DeleteView):
  model = Debtor
  success_url = '/debtors/'

class InsuranceList(ListView):
  model = Insurance

class InsuranceCreate(CreateView):
  model = Insurance
  fields = '__all__'

class InsuranceDelete(DeleteView):
  model = Insurance
  success_url = '/Insurances/'