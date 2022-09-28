from django.shortcuts import render
from django.http import HttpResponse

class Debtor:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, debts, age):
    self.name = name
    self.debts = debts
    self.age = age

debtors = [
  Debtor('Lolo', 5000000, 53),
  Debtor('Sachi', 250456, 20),
  Debtor('Candy', 8446511555, 18)
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Add new view
def debtors_index(request):
  return render(request, 'debtors/index.html', { 'debtors': debtors })