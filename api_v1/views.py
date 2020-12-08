from django.contrib.auth.models import User, Group
from home.models import HomePage
from blog.models import BlogPage
from rest_framework import viewsets
from rest_framework import permissions
from api_v1.serializers import UserSerializer, GroupSerializer, HomePageSerializer, BlogPageSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class HomePageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows home pages to be viewed or edited.
    """
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
    permission_classes = [permissions.IsAuthenticated]


class BlogPageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blog pages to be viewed or edited.
    """
    queryset = BlogPage.objects.all()
    serializer_class = BlogPageSerializer
    permission_classes = [permissions.IsAuthenticated]
