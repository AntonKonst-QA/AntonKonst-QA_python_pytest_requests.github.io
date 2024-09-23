import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4171f33b814aadb86a982c23e422c24f'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Бульба",
    "photo_id": 100
}

body_change = {
    "pokemon_id": "70274",
    "name": "N Бульба",
    "photo_id": 142
}

body_catch = {
    "pokemon_id": "70274"
}

# Создать покемона
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

# Смена имени покемона
response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

# Поймать покемона в покебол
response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)