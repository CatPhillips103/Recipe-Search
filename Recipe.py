import requests
import hiddenkeys

id = hiddenkeys.app_id
key = hiddenkeys.app_key


def recipe_database(ingredient):
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={id}&app_key={key}'

    response = requests.get(url)
    found_recipes = response.json()
    return found_recipes["hits"]


def recipe_search():
    ingredient_criteria = input('What ingredient would you like to include in the recipe? ')

    answer = recipe_database(ingredient_criteria)

    print(answer)


recipe_search()
