from django.shortcuts import render
from .models import Meal
import requests

def get_meals(request):
    all_meals = {}
    if 'name' in request.GET:
        name = request.GET['name']
        url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=%s' % name
        response = requests.get(url)
        data = response.json()
        meals = data['meals']

        for i in meals:
            meal_data = Meal(
                name = i['strMeal'],
                category = i['strCategory'],
                instructions = i['strInstructions'],
                region = i['strArea'],
                slug = i['idMeal'],
                image_url = i['strMealThumb']
            )
            meal_data.save()
        all_meals = Meal.objects.all().order_by('-id')

    return render (request, 'meals/meal.html', { "all_meals": 
    all_meals} )

def meal_detail(request, id):
    meal = Meal.objects.get(id = id)
    print(meal)
    return render (
        request,
        'meals/meal_detail.html',
        {'meal': meal}
    )