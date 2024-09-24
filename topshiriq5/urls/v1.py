from django.urls import include, path
from rest_framework.routers import DefaultRouter

from topshiriq1.views import UserViewSet, VacancyViewSet
from topshiriq5.models import Product
from topshiriq5.views import PostViewSet, ProductViewSet

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register("product", ProductViewSet)
app_name = "posts"
urlpatterns = router.urls
