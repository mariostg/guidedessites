# Generated by Django 4.1.4 on 2022-12-16 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mrc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, unique=True, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'MRC',
                'verbose_name_plural': 'MRC',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Municipalite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, unique=True, verbose_name='Municipalité')),
                ('mrc', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='geographie.mrc')),
            ],
        ),
    ]
