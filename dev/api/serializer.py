from rest_framework import serializers
from dev import models

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'
        depth = 1

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Social
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'

class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Competence
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    comp_categorie = CompetenceSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = models.Categorie
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experience
        fields = '__all__'


class ExperienceCateSerializer(serializers.ModelSerializer):
    experience_categorie = ExperienceSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = models.ExperienceCategorie
        fields = '__all__'
        depth = 1
        
class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projet
        fields = '__all__'
