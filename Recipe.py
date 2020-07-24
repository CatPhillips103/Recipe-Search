import requests
import hiddenkeys

id = hiddenkeys.app_id
key = hiddenkeys.app_key


def recipe_database(ingredient, health_labels,diet_labels):
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={id}&app_key={key}&Health={health_labels}&Diet={diet_labels}'

    response = requests.get(url)
    found_recipes = response.json()
    return found_recipes["hits"]


def recipe_search():
    ingredient_criteria = input('What ingredient would you like to include in the recipe? ')
    health_criteria = input('Do you have any specific dietary and/or allergy-free requests? ')
    diet_criteria = input('Any nutrition requests? ')

    answers = recipe_database(ingredient_criteria, health_criteria, diet_criteria)

    with open('recipe-inventory.txt', 'w+') as text_file:
        for answer in answers:
           recipe = answer["recipe"]
           text_file.write(f'{recipe["label"]}')




recipe_search()
