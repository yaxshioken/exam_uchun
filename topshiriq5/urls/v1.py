from django.urls import include, path
from rest_framework.routers import DefaultRouter

from topshiriq1.views import UserViewSet, VacancyViewSet
from topshiriq5.views import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
app_name = "posts"
urlpatterns =router.urls
