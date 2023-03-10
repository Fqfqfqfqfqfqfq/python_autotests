import requests


token = 'bf4dc885edafacb2e27e9a6fd729fcb2'
response = requests.post('https://pokemonbattle.me:9104/pokemons', 
headers= {'Content-Type' : 'application/json','trainer_token' : token}, 
json={"name": "жульбазавр", "photo": "https://dolnikov.ru/pokemons/albums/010.png"
}
)
print(response.text)

change_name_response = requests.put('https://pokemonbattle.me:9104/pokemons', 
headers= {'Content-Type' : 'application/json','trainer_token' : token},json={
    "pokemon_id": 6053,
    "name": "Jojo",
    "photo": ""
})
print(change_name_response.text)

pokeball_response = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', 
headers= {'Content-Type' : 'application/json','trainer_token' : token},json={
    "pokemon_id": 6053
})
print(pokeball_response.text)