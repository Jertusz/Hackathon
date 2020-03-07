import json
with open('recipe.json') as json_file:
    data = json.load(json_file)
    recipe = {}
    recka = data['recipe']
    recipe['name'] = recka['label']
    recipe['image'] = recka['image']
    recipe['source'] = recka['source']
    recipe['source_url'] = recka['url']
    recipe['tags'] = recka['healthLabels']
    recipe['ingredients_list'] = recka['ingredientLines']
    nutrients = {}
    for something in recka['totalNutrients']:
        nutrients[something] = recka['totalNutrients'][something]
    recipe['nutrients'] = nutrients

    print(recipe)




