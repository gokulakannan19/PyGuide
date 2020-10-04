import django_filters
from django_filters import CharFilter
from .models import LegalAspectsOfBusiness, CorporateAccounting, Answer


class LegalAspectsofBusinessFilter(django_filters.FilterSet):
    question = CharFilter(field_name="question", lookup_expr='icontains')

    class Meta:
        model = LegalAspectsOfBusiness
        fields = "__all__"


class CorporateAccountingFilter(django_filters.FilterSet):
    question = CharFilter(field_name="question", lookup_expr='icontains')

    class Meta:
        model = CorporateAccounting
        fields = "__all__"
