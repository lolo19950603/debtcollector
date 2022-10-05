from django.db import models
from django.urls import reverse

# Create your models here.
class Debtor(models.Model):
    name = models.CharField(max_length=100)
    debts = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('debtors_detail', kwargs={'pk': self.id})