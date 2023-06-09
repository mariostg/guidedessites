# Generated by Django 4.2 on 2023-04-17 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("geographie", "0002_mrc_created_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mrc",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="Modifier",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
