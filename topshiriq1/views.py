from django.shortcuts import render
from rest_framework import viewsets

from config.search import CustomSearchFilter
from topshiriq1.models import Account, Vacancy
from topshiriq1.serializers import (AccountSerializer, LoginSerializer,
                                    VacancySerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class LoginViewSet(viewsets.ViewSet):
    queryset = Account.objects.all()
    serializer_class = LoginSerializer
    filter_backends = (CustomSearchFilter,)


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    def get_queryset(self):
        salary = self.request.query_params.get('salary', None)
        salary_from=self.request.query_params.get('salary_from', None)
        salary_to=self.request.query_params.get('salary_to', None)

        if salary:
            return Vacancy.objects.filter(salary=salary)
        if salary_from and salary_to:
            return Vacancy.objects.filter(salary__gte=salary_from, salary__lte=salary_to)

