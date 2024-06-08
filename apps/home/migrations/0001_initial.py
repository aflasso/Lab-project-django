# Generated by Django 3.2.6 on 2024-06-08 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('codigoMateria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreMateria', models.CharField(max_length=100)),
                ('cantCreditos', models.IntegerField()),
                ('horario', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
                ('puntuacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=50)),
                ('facultad', models.CharField(max_length=50)),
                ('usuario', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Valoracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=100)),
                ('comentario', models.CharField(max_length=100)),
                ('puntuacion', models.CharField(max_length=100)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valoraciones', to='home.estudiante')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valoraciones', to='home.materia')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('numeroSemestre', models.IntegerField()),
                ('cantidadCreditos', models.IntegerField()),
                ('programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semestres', to='home.programa')),
            ],
        ),
        migrations.AddField(
            model_name='materia',
            name='profesorAsignado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materias', to='home.profesor'),
        ),
        migrations.AddField(
            model_name='materia',
            name='semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materias', to='home.semestre'),
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aprobado', models.BooleanField(default=False)),
                ('cursando', models.BooleanField()),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.estudiante')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.materia')),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='materias',
            field=models.ManyToManyField(related_name='estudiantes', through='home.Inscripcion', to='home.Materia'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='programa_academico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudiantes', to='home.programa'),
        ),
    ]
