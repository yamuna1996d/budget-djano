# Generated by Django 2.2.5 on 2019-11-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Djan', '0006_income_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenditure',
            name='amount',
            field=models.IntegerField(default='300'),
        ),
    ]
