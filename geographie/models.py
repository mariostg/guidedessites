from django.db import models

# Create your models here.
class Mrc(models.Model):
    name=models.CharField(max_length=75, unique=True, verbose_name='Nom')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name="MRC"
        verbose_name_plural="MRC"
        ordering=('name',)

class Municipalite(models.Model):
    name=models.CharField(max_length=75, unique=True, verbose_name='Municipalité')
    mrc=models.ForeignKey(Mrc, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.name
    
    class Meta():
        pass