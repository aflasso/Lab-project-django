# Generated by Django 3.2.6 on 2024-04-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20240427_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semestre',
            name='id',
        ),
        migrations.AddField(
            model_name='semestre',
            name='codigo',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='codigo',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='materia',
            name='codigoMateria',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='codigo',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
