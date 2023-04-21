from django.db import models
from django.conf import settings

# https://www.atlas-oiseaux.qc.ca/donneesqc/codes.jsp?lang=fr&pg=habitat


class Habitat(models.Model):
    habitat = models.CharField(max_length=40, unique=True, verbose_name="Habitat")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="Habitat_Creator"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="Habitat_Modifier"
    )
    created_at = models.DateTimeField("Date création", auto_now_add=True)
    updated_at = models.DateTimeField("Date mise à jour", auto_now=True)

    def __str__(self) -> str:
        return self.habitat

    class Meta:
        verbose_name = "Habitat"
        ordering = ("habitat",)


class SousHabitat(models.Model):
    sous_habitat = models.CharField(max_length=55, verbose_name="Sous-habitat")
    habitat = models.ForeignKey(Habitat, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return f"{self.habitat} - {self.sous_habitat}"

    class Meta:
        verbose_name = "Sous-habitat"
