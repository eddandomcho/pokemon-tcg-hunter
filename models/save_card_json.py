import requests
import json
import models.query_card_info as qci

API_KEY = "pk_test_91cc2b3ec9c75d68efac0da0c21d750d1db419801774bb4f"
BASE_URL = "https://api.pokewallet.io"

headers = {
        "X-API-Key" : API_KEY
    }

def fetch_card_json(query):
    params = {
        "q": query
    }

    response = requests.get(
        f"{BASE_URL}/search",
        params = params,
        headers = headers
    )

    result = response.json()
    return(result)

def print_card_json(query):
    params = {
        "q": query
    }

    response = requests.get(
        f"{BASE_URL}/search",
        params = params,
        headers = headers
    )

    result = response.json()
    dump = json.dumps(result, indent = 2)

    print(dump)

def write_card_json(query):
    result = fetch_card_json(query)
    eng_name = qci.fetch_card_info(query)["name"]
    eng_name = eng_name.replace("/", "-")

    file_path = f"files/ascended_heroes/{eng_name}.json"

    with open(file_path, mode = "w", encoding = "utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"Saved data to files/ascended_heroes/{eng_name}.json")

