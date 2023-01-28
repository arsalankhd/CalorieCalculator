import django_filters
from django_filters import CharFilter
from .models import *

class FoodItemFilter(django_filters.FilterSet):
	food_name = CharFilter(field_name = 'name' , lookup_expr = 'icontains',label='جستجوی غذا ها')
	class Meta:
		model = foodItem
		fields = ['food_name']