# Generated by Django 3.2.6 on 2024-04-28 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='id',
        ),
        migrations.AlterField(
            model_name='materia',
            name='codigoMateria',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]