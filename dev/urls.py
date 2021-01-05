from dev.api.apiviews import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include


rooter = DefaultRouter()
rooter.register('profile', ProfileViewSet, basename='profile')
rooter.register('projet', ProjetViewSet, basename='projet')
rooter.register('social-link', SocialViewSet, basename='social')
rooter.register('service', ServiceViewSet, basename='service')
rooter.register('competence', CompetenceViewSet, basename='competence')
rooter.register('categorie', CategorieViewSet, basename='categorie')
rooter.register('experience', ExperienceViewSet, basename='experience')
rooter.register('categorie-experience', ExperienceCategorieViewSet, basename='categorie-experience')

api_urlpatterns = [
    path('api/', include(rooter.urls)),
]