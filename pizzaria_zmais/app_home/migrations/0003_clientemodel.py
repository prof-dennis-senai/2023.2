# Generated by Django 4.2.11 on 2025-04-16 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0002_vendamodel_vendapizzamodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('alterado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
