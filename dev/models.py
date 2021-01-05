from django.db import models
from tinymce import HTMLField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Profile(models.Model):
    """Model definition for Profile."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    specialte = models.CharField(max_length=250)
    description = HTMLField('description')
    contact = models.CharField(max_length=255)
    situation_geographique = models.CharField(max_length=250)
    date_naissance = models.DateField()
    localisation = models.TextField(null=True, blank=True)
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return self.user.username

class Social(models.Model):
    """Model definition for Social."""
    lien = models.URLField(max_length=200)
    fontawesome = models.CharField(max_length=250)
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Social."""

        verbose_name = 'Social'
        verbose_name_plural = 'Socials'

    def __str__(self):
        """Unicode representation of Social."""
        return self.fontawesome

class Service(models.Model):
    """Model definition for Service."""
    titre = models.CharField(max_length=250)
    description = models.TextField()
    fontawesome = models.CharField(max_length=250)
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Service."""

        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        """Unicode representation of Service."""
        return self.titre

class Categorie(models.Model):
    """Model definition for Categorie."""
    titre = models.CharField(max_length=250)
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.titre

class Competence(models.Model):
    """Model definition for Competence."""
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='comp_categorie')
    titre = models.CharField(max_length=250)
    niveau = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Competence."""

        verbose_name = 'Competence'
        verbose_name_plural = 'Competences'

    def __str__(self):
        """Unicode representation of Competence."""
        return self.titre
    

class Projet(models.Model):
    """Model definition for Projet."""
    fichier = models.FileField(upload_to='projets')
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Projet."""

        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'

    def __str__(self):
        """Unicode representation of Projet."""
        return f'Ressource [{self.fichier}]'

class ExperienceCategorie(models.Model):
    """Model definition for Categorie."""
    titre = models.CharField(max_length=250)
    fontawesome = models.CharField(max_length=250)
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'ExperienceCategorie'
        verbose_name_plural = 'ExperienceCategories'

    def __str__(self):
        """Unicode representation of ExperienceCategorie."""
        return self.titre


class Experience(models.Model):
    """Model definition for Experience."""
    experience = models.ForeignKey(ExperienceCategorie, on_delete=models.CASCADE, related_name='experience_categorie')
    structure = models.CharField(max_length=250)
    poste = models.CharField(max_length=250)
    description = models.TextField()
    annee_debut = models.IntegerField()
    annee_fin = models.IntegerField()
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Experience."""

        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        """Unicode representation of Experience."""
        return self.experience


class Contact(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'{self.nom} {self.prenom}'
