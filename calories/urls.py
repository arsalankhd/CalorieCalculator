from django.urls import path
from .views import FoodItemListView, FoodItemCreateView, FoodItemDeleteView, FoodItemUpdateView, FoodConsumedCreateView, FoodConsumedDeleteView, CalorieGoalEditView, ProfileView

urlpatterns = [
    path('fooditem_list/', FoodItemListView, name='fooditem_list'),
    path('fooditem_new/', FoodItemCreateView.as_view(), name='fooditem_new'),
    path('fooditem_delete/<int:pk>', FoodItemDeleteView.as_view(), name='fooditem_delete'),
    path('fooditem_edit/<int:pk>', FoodItemUpdateView.as_view(), name='fooditem_edit'),
    path('foodconsumed_new/', FoodConsumedCreateView, name='foodconsumed_new'),
    path('foodconsumed_delete/<int:pk>', FoodConsumedDeleteView.as_view(), name='foodconsumed_delete'),
    path('caloriegoal_edit/', CalorieGoalEditView, name='caloriegoal_edit'),
    path('profile/', ProfileView, name='profile'),
]