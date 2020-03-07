import requests
from django.shortcuts import render, redirect
from creds import api_key, app_id
import json


def sample(request):
    params = {
        "q": ["chicken", "cheese"],
        "app_id": app_id,
        "app_key": api_key
    }
    r = requests.get("https://api.edamam.com/search?",params=params)
    print(r)
    json_data = json.loads(r.text)
    print(json_data)
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
    p_recipe['source'] = recka['source']
    p_recipe['source_url'] = recka['url']
    p_recipe['tags'] = recka['healthLabels']
    p_recipe['ingredients_list'] = recka['ingredientLines']
    nutrients = {}
    for something in recka['totalNutrients']:
        quantity = recka['totalNutrients'][something]['quantity']
        unit = recka['totalNutrients'][something]['unit']
        name = recka['totalNutrients'][something]['label']
        tmp = {'quantity': quantity, 'unit': unit}
        nutrients[name] = tmp
    p_recipe['nutrients'] = nutrients
    return p_recipe
