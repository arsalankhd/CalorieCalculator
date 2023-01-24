from django.contrib import admin
from .models import *

class foodItemAdmin(admin.ModelAdmin):
    list_display = ('person_of', 'name', 'calorie')

class foodConsumedAdmin(admin.ModelAdmin):
    list_display = ('person_of', 'name', 'quantity', 'option', 'date')


admin.site.register(foodItem, foodItemAdmin)
admin.site.register(foodConsumed, foodConsumedAdmin)