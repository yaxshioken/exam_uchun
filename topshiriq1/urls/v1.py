from django.urls import include, path
from rest_framework.routers import DefaultRouter

from topshiriq1.views import UserViewSet, VacancyViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("vacancy", VacancyViewSet, basename="vacancies")
app_name = "account"
urlpatterns = router.urls
