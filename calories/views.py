from django.shortcuts import render, redirect
from .forms import *
from .models import *
from accounts.models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView 
)
from datetime import date, datetime, timedelta
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required(login_url='login')
def FoodItemListView(request):
    foodItemList = foodItem.objects.filter(person_of=request.user)
    if foodItemList.count() == 0:
        food = foodItem(name='یک عدد نیمرو', calorie='92', person_of=request.user)
        food.save()

        food = foodItem(name='یک عدد تخم مرغ آب پز', calorie='77', person_of=request.user)
        food.save()

        food = foodItem(name='یک برش پنیر سفید (۲۸ گرم)', calorie='75', person_of=request.user)
        food.save()

        food = foodItem(name='یک لیوان چای شیرین', calorie='40', person_of=request.user)
        food.save()

        food = foodItem(name='کره بادام زمینی (۱۰۰ گرم)', calorie='588', person_of=request.user)
        food.save()

        food = foodItem(name='یک عدد موز بزرگ', calorie='120', person_of=request.user)
        food.save()

        food = foodItem(name='یک عدد پرتقال متوسط', calorie='75', person_of=request.user)
        food.save()

        food = foodItem(name='یک عدد سیب متوسط', calorie='75', person_of=request.user)
        food.save()

        food = foodItem(name='یک کف دست نان تافتون', calorie='35', person_of=request.user)
        food.save()

        food = foodItem(name='یک کفگیر برنج سفید پخته', calorie='250', person_of=request.user)
        food.save()

        food = foodItem(name='بادام زمینی (۱۰۰ گرم)', calorie='586', person_of=request.user)
        food.save()

        food = foodItem(name='گوشت گوسفند چرخ کرده با چربی (۱۰۰ گرم)', calorie='282', person_of=request.user)
        food.save()

        food = foodItem(name='گوشت سینه مرغ (۱۰۰ گرم)', calorie='172', person_of=request.user)
        food.save()

    context = {
        'foodItemList' : foodItemList,
    }

    return render(request, 'food_item.html', context)


class FoodItemCreateView(LoginRequiredMixin, CreateView):
        model = foodItem
        fields = "__all__"
        template_name = 'food_item_new.html'
        success_url = reverse_lazy('fooditem_list')


class FoodItemDeleteView(LoginRequiredMixin, DeleteView):
        model = foodItem
        template_name = 'food_item_delete.html'
        success_url = reverse_lazy('fooditem_list')

class FoodItemUpdateView(LoginRequiredMixin, UpdateView):
    model = foodItem
    template_name = 'food_item_edit.html'
    fields = ['name', 'calorie']
    success_url = reverse_lazy('fooditem_list')

@login_required(login_url='login')
def FoodConsumedCreateView(request):
    person = CustomUser.objects.get(id=request.user.id)
    form = foodConsumedForm(request.user, instance=person)

    if request.method == "POST":
        form = foodConsumedForm(request.user, request.POST, instance=person)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            quantity = form.cleaned_data.get('quantity')
            option = form.cleaned_data.get('option')
            person_of = form.cleaned_data.get('person_of')
            consumedfood = foodConsumed.objects.create(
                name=name, quantity=quantity, option=option, person_of=person_of)
            consumedfood.save()
            return redirect('/calories/profile')
        else:
            form = foodConsumedForm(request.user)

    context = {'form': form}

    return render(request, 'food_consumed_new.html', context)


class FoodConsumedDeleteView(LoginRequiredMixin, DeleteView):
    model = foodConsumed
    template_name = 'food_consumed_delete.html'
    success_url = reverse_lazy('profile')

@login_required(login_url='login')
def CalorieGoalEditView(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)
        user.calorie_goal = request.POST.get('calorie_goal')
        user.save()
        return redirect('/calories/profile')

    return render(request, 'caloriegoal_edit.html')


@login_required(login_url='login')
def ProfileView(request):
    profile = CustomUser.objects.get(id=request.user.id)
    profile_goal = profile.calorie_goal

    ProfileFoodConsumedList = foodConsumed.objects.filter(person_of=request.user)
    TodayFoodConsumedList = ProfileFoodConsumedList.filter(date=date.today())
    YesterdayFoodConsumedList = ProfileFoodConsumedList.filter(date=(date.today()-timedelta(days=1)))

    ThisWeekFoodConsumedList = []
    for i in range(7):
        ThisWeekFoodConsumedList = ProfileFoodConsumedList.filter(date=(date.today()-timedelta(days=i)))

    # base = date.today()
    # lastweek_dates = [base - timedelta(days=x) for x in range(7)]
    
    some_day_last_week = timezone.now().date() - timedelta(days=6)
    records = foodConsumed.objects.filter(date__gte=some_day_last_week,date__lt=(timezone.now() + timezone.timedelta(1)).date(),person_of=request.user)

    calorie_thisweek = 0
    calorie_today = 0
    calorie_yesterday = 0
    for f in ProfileFoodConsumedList:
        calorie_thisweek += f.name.calorie*f.quantity
    for f in TodayFoodConsumedList:
        calorie_today += f.name.calorie*f.quantity
    for f in YesterdayFoodConsumedList:
        calorie_yesterday += f.name.calorie*f.quantity

    calorie_compare = int(calorie_today - calorie_yesterday)
    if calorie_compare > 0:
        calorie_compare_to_yesterday = "+%d" %calorie_compare
    else:
        calorie_compare_to_yesterday = calorie_compare
    
    goal_percent = int(calorie_today/profile_goal*100)
    context = {
        'FoodConsumedList': TodayFoodConsumedList,
        'profile_goal': int(profile_goal),
        'calorie_today': int(calorie_today),
        'goal_percent': goal_percent,
        'calorie_compare': calorie_compare_to_yesterday,
        'calorie_thisweek': int(calorie_thisweek),
        'records': records,
    }
    return render(request, 'profile.html', context)