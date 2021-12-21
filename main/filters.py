import django_filters
from django.db import models
from main.models import Jewelry


class JewelryFilter(django_filters.FilterSet):
    class Meta:
        model = Jewelry
        fields = '__all__'

        # tags = django_filters.ModelMultipleChoiceFilter(
        #     name='sitetags__name',
        #     to_field_name='name',
        #     lookup_type='in',
        #     queryset=Jewelry.objects.all()
        # )

