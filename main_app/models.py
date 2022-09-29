from django.db import models

# Create your models here.
class Debtor(models.Model):
    name = models.CharField(max_length=100)
    debts = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return self.name