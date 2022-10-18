from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator

# Create your models here.
class Debtor(models.Model):
    name = models.CharField(max_length=100)
    debt = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'debtor_id': self.id})

    def paid_off(self):
        return self.debt == 0

class Payment(models.Model):
    date = models.DateField()
    payment = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1)
        ]
    )
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.payment} on {self.date}"
    
    class Meta:
        ordering = ['date']
  