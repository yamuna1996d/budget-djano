# Generated by Django 2.2.5 on 2019-10-01 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Djan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
        ),
    ]
