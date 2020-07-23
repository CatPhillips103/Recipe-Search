import requests
import hiddenkeys

id = hiddenkeys.app_id
key = hiddenkeys.app_key

def recipe_database(ingredient):
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={id}&app_key={key}'

recipe_database()


