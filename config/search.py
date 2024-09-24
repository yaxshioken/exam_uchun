from rest_framework import filters


class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        search_fields = []
        if request.query_params.get("salary_from"):
            search_fields.append("salary")
        if request.query_params.get("salary_to"):
            search_fields.append("salary    ")
        if request.query_params.get("email_only"):
            search_fields.append("email")
        if search_fields:
            return search_fields

        return super().get_search_fields(view, request)
