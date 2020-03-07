import requests
from django.shortcuts import render, redirect
from creds import api_key, app_id
import json
from django.http import HttpResponse
from .forms import queryForm


def sample(request):

    if request.method == 'POST':
        form = queryForm(request.POST)
        products = form['q'].value().split(' ')
        products = ", ".join(products)


    params = {
        "q": products,
        "app_id": app_id,
        "app_key": api_key
    }
    r = requests.get("https://api.edamam.com/search?",params=params)
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
    p_recipe['people'] = recka['yield']
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


def index(request):


    return render(request, "index.html", {'form': queryForm})


def js(request):
    filename = request.path.strip("/")
    data = open(filename, "rb").read()
    return HttpResponse(data, mimetype="application/x-javascript")