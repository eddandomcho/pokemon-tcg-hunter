import requests as req
import json

API_KEY = "pk_test_91cc2b3ec9c75d68efac0da0c21d750d1db419801774bb4f"
BASE_URL = "https://api.pokewallet.io"

headers = {
        "X-API-Key" : API_KEY
    }

def fetch_card_info(query):
    params = {
        "q": query
    }

    response = req.get(
        f'{BASE_URL}/search',
        params=params,
        headers=headers
    )

    result = response.json()
    card_info = result["results"][0]["card_info"]
    return(card_info)

def extract_set_name(card_number):
    card_info = fetch_card_info(card_number)
    set_name = card_info["set_name"]
    print(set_name)
    return(set_name)

def extract_card_rarity(card_number):
    card_info = fetch_card_info(card_number)
    rarity = card_info["rarity"]
    print(rarity)
    return(rarity)

extract_card_rarity("161/131")