from rest_framework import viewsets
from .serializer import ProfileSerializer, ProjetSerializer, SocialSerializer, ServiceSerializer, CompetenceSerializer, CategorieSerializer, ExperienceCateSerializer, ExperienceSerializer
from dev import models



class ProfileViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.objects.filter(status=True)
    serializer_class = ProfileSerializer
    
class ProjetViewSet(viewsets.ModelViewSet):
    queryset = models.Projet.objects.filter(status=True)
    serializer_class = ProjetSerializer

class SocialViewSet(viewsets.ModelViewSet):
    queryset = models.Social.objects.filter(status=True)
    serializer_class = SocialSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = models.Service.objects.filter(status=True)
    serializer_class = ServiceSerializer

class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = models.Competence.objects.filter(status=True)
    serializer_class = CompetenceSerializer
    
class CategorieViewSet(viewsets.ModelViewSet):
    queryset = models.Categorie.objects.filter(status=True)
    serializer_class = CategorieSerializer
    
class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = models.Experience.objects.filter(status=True)
    serializer_class = ExperienceSerializer

class ExperienceCategorieViewSet(viewsets.ModelViewSet):
    queryset = models.ExperienceCategorie.objects.filter(status=True)
    serializer_class = ExperienceCateSerializer