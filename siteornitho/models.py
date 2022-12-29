from django.db import models

from geographie.models import Municipalite
from habitat.models import SousHabitat

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status=SiteOrnitho.Status.PUBLISHED)
class SiteOrnitho(models.Model):
    class Mois(models.IntegerChoices):
        ALL = 0, 'Toute l\'année'
        JAN=1, 'Janvier'
        FEB=2, 'Février'
        MAR=3, 'Mars'
        APR=4, 'Avril'
        MAY=5, 'Mai'
        JUN=6, 'Juin'
        JUL=7, 'Juillet'
        AUG=8, 'Août'
        SEP=9, 'Septembre'
        OCT=10, 'Octobre'
        NOV=11, 'Novembre'
        DEC=12, 'Décembre'

    class Status(models.IntegerChoices):
        DRAFT=0,'Ébauche'
        PUBLISHED=1,'Publié'

    # Nom du site..
    nom_du_site = models.CharField(max_length=125, verbose_name='Nom du site')
    # adresse
    # locid (hotspot)..
    locid = models.CharField(
        max_length=8, verbose_name='Id de localisation', null=True, blank=True)
    # longitude..
    longitude = models.DecimalField(
        verbose_name='Longitude', max_digits=9, decimal_places=6)
    # latitude..
    latitude = models.DecimalField(
        verbose_name='Latitude', max_digits=9, decimal_places=6)
    # website..
    url = models.URLField(verbose_name="Site Web",
                          max_length=200, null=True, blank=True)
    # Auteur..
    auteur = models.CharField(max_length=125, verbose_name="Auteur")
    # photo ..
    # photo_auteur ..
    # photo_date ..
    # miseajour
    miseajour = models.DateField("Mise à jour", auto_now=True)
    # municipalite..
    municipalite = models.ForeignKey(Municipalite, on_delete=models.RESTRICT)
    # stakeholder..
    stakeholder = models.CharField(
        verbose_name='Partenaire/propriétaire', max_length=255, null=True, blank=True)
    # periode_interet..
    periode_interet_debut = models.IntegerField( choices=Mois.choices)
    periode_interet_fin = models.IntegerField(
        choices=Mois.choices, null=True, blank=True)

    # habitat_dominant..
    # sous-habitat..
    sous_habitat = models.ManyToManyField(
        SousHabitat, related_name='sous_habitats' ,verbose_name=("Sous habitat"))
    # description_generale..
    description_generale = models.TextField(
        verbose_name="Description générale", max_length=1024)
    # transport..
    transport = models.BooleanField(
        verbose_name='Transport en commun', default=False)
    # acces_gratuit..
    acces_gratuit = models.BooleanField(
        verbose_name='Accès gratuit', default=False)
    # Bon_a_savoir..
    bon_a_savoir = models.TextField(
        verbose_name="Bon à savoir", max_length=1024)
    # toilettes..
    toilette = models.BooleanField(verbose_name='Toilettes', default=False)
    # picnique..
    picnique = models.BooleanField(
        verbose_name='Table à picnique', default=False)
    # banc..
    banc = models.BooleanField(verbose_name='Banc disponible', default=False)
    # enjeux..
    enjeux = models.TextField(
        verbose_name="Enjeux de conservation", max_length=1024)
    status=models.IntegerField(choices=Status.choices, default=1)

    def __str__(self):
        return f"{self.nom_du_site} - {self.municipalite}"

    objects = models.Manager() # The default manager. 
    published = PublishedManager() # Our custom manager.

class SiteOrnithoImage(models.Model):
    siteornitho = models.ForeignKey(
        SiteOrnitho,
        on_delete=models.CASCADE,
        related_name='images')
    title = models.CharField(verbose_name="Titre", max_length=125)
    photo_author = models.CharField(verbose_name="Auteur", max_length=125)
    photo_date = models.DateField(verbose_name="Date photo")
    image = models.ImageField(upload_to='siteornitho/images')

    def __str__(self) -> str:
        return f"{self.title} - {self.photo_author}"
