import django_filters
from django_filters import CharFilter
from .models import Question, Answer


class QuestionFilter(django_filters.FilterSet):
    question = CharFilter(field_name="question", lookup_expr='icontains')

    class Meta:
        model = Question
        fields = "__all__"
