from rest_framework import routers
from api_v1 import views
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'home-pages', views.HomePageViewSet)
router.register(r'blog-pages', views.BlogPageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
