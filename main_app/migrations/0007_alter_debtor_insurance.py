# Generated by Django 4.1.1 on 2022-10-26 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_insurance_alter_payment_options_debtor_insurance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debtor',
            name='insurance',
            field=models.ManyToManyField(blank=True, to='main_app.insurance'),
        ),
    ]
