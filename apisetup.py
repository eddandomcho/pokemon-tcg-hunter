import requests as req
import json

API_KEY = "pk_test_91cc2b3ec9c75d68efac0da0c21d750d1db419801774bb4f"
BASE_URL = "https://api.pokewallet.io"

def search_query(query):
    headers = {
        "X-API-Key" : API_KEY
    }

    response = req.get(
        f'{BASE_URL}/search',
        params={'q': query},
        headers=headers
    )

    result = response.json()
    dump = json.dumps(result, indent = 2)

    print(dump)

search_query("161/131")
    
