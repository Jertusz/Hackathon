import requests
from django.shortcuts import render, redirect
from creds import api_key, app_id
import json
from django.http import HttpResponse


def sample(request):

    if request.method == 'POST':
        products = request.POST.get('query').split(' ')
        products = ", ".join(products)

        diet = request.POST.get('diet')
        calories = request.POST.get('calories')
        max_products = request.POST.get('ingredients')

        if max_products is None:
            max_products = 30
        if diet == "0":
            diet == "low-sodium"
        elif diet == "1":
            diet = "balanced"
        elif diet == "2":
            diet = "high-protein"
        elif diet == "3":
            diet = "high-fiver"
        elif diet == "4":
            diet = "low-fat"
        elif diet == "5":
            diet = "low-carb"
        else:
            diet = ""

    params = {
        "q": products,
        "app_id": app_id,
        "app_key": api_key,
    }

    if calories:
        calories = "0-" + str(calories)
        params['calorie'] = calories

    if diet:
        params['diet'] = diet

    if max_products:
        params['ingr'] = max_products

    r = requests.get("https://api.edamam.com/search?", params=params)
    json_data = json.loads(r.text)
    parsed_recipes = []
    for recipe in json_data["hits"]:
        parsed_recipes.append(parse_recipe(recipe))
    context = {
        'recipes': parsed_recipes,
    }
    return render(request, "main.html", context)


def parse_recipe(unparsed_recipe):
    p_recipe = {}
    recka = unparsed_recipe['recipe']
    p_recipe['name'] = recka['label']
    p_recipe['image'] = recka['image']
    p_recipe['people'] = str(int(recka['yield']))
    p_recipe['source'] = recka['source']
    p_recipe['source_url'] = recka['url']
    p_recipe['tags'] = recka['healthLabels']
    p_recipe['ingredients_list'] = recka['ingredientLines']
    nutrients = []
    for something in recka['totalNutrients']:
        quantity = recka['totalNutrients'][something]['quantity']
        unit = recka['totalNutrients'][something]['unit']
        name = recka['totalNutrients'][something]['label']
        nutrients.append(
            {'name': name, 'quantity': "%.2f" % quantity, 'unit': unit})
    p_recipe['nutrients'] = nutrients

    return p_recipe


def index(request):

    return render(request, "index.html", {})


def js(request):
    filename = request.path.strip("/")
    data = open(filename, "rb").read()
    return HttpResponse(data, mimetype="application/x-javascript")
