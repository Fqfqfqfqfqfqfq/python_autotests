import requests
import pytest

def test_get_trainers():
    response = requests.get("https://pokemonbattle.me:9104/trainers")
    assert response.status_code == 200
def test_get_trainers_name():
    response = requests.get("https://pokemonbattle.me:9104/trainers",params={'trainer_id':3336})
    assert response.json()['trainer_name'] == 'Des'