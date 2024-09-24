from rest_framework import status, viewsets
from rest_framework.response import Response

from config.search import CustomSearchFilter
from topshiriq1.models import Account, Vacancy
from topshiriq1.serializers import (AccountSerializer, LoginSerializer,
                                    VacancySerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.filter(is_deleted=False)
    serializer_class = AccountSerializer

    def destroy(self, request, *args, **kwargs):
        account = self.get_object()
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def restore_account(self, request, pk=None):
        account = Account.objects.get(pk=pk)
        account.restore()
        return Response(status=status.HTTP_200_OK)


class LoginViewSet(viewsets.ViewSet):
    queryset = Account.objects.all()
    serializer_class = LoginSerializer
    filter_backends = (CustomSearchFilter,)


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    def get_queryset(self):
        salary = self.request.query_params.get("salary", None)
        salary_from = self.request.query_params.get("salary_from", None)
        salary_to = self.request.query_params.get("salary_to", None)

        if salary:
            return Vacancy.objects.filter(salary=salary)
        if salary_from and salary_to:
            return Vacancy.objects.filter(
                salary__gte=salary_from, salary__lte=salary_to
            )
