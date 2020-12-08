from django.contrib.auth.models import User, Group
from blog.models import BlogPage
from home.models import HomePage
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class HomePageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomePage
        fields = ['body']


class BlogPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogPage
        fields = [
            'id',
            'title',
            'date',
            'intro',
            'body',
            'slug',
        ]
