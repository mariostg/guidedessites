from django.db import models
from django.conf import settings
from datetime import date

# Create your models here.
class Mrc(models.Model):
    name = models.CharField("nom", max_length=75, unique=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="Mrc_Creator"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="Mrc_Modifier"
    )
    created_at = models.DateTimeField("Date création", auto_now_add=True)
    updated_at = models.DateTimeField("Date mise à jour", auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "MRC"
        verbose_name_plural = "MRC"
        ordering = ("name",)


class Municipalite(models.Model):
    name = models.CharField(max_length=75, unique=True, verbose_name="Municipalité")
    mrc = models.ForeignKey(Mrc, on_delete=models.RESTRICT)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="municipalite_creator"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="municipalite_modifier"
    )
    created_at = models.DateTimeField("Date création", auto_now_add=True)
    updated_at = models.DateTimeField("Date mise à jour", auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        pass
