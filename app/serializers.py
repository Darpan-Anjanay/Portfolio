from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Profile,
    SocialLink,
    TechCategory,
    Technology,
    WorkHistory,
    Project
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ['id', 'platform_name', 'link']


class TechCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TechCategory
        fields = ['id', 'name']


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'name', 'category', 'description']


class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = ['id', 'company_name', 'designation', 'description', 'start_date', 'end_date', 'present']


class ProjectSerializer(serializers.ModelSerializer):
    techs = TechnologySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'techs', 'github_link', 'description','sortorder']




class ProfileSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True, read_only=True)
    techcategory_set = TechCategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'full_name',
            'profile_image',
            'working_as',
            'email',
            'contact_number',
            'bio',
            'skills_Overview',
            'resume',
            'social_links',
            'techcategory_set'
        ]

        