import requests

BASE_URL = "https://www.apple.com/in/shop/pickup-message-recommendations"

STORE_ID = "R756"

PRODUCTS = {
    "Black": "MG6J4HN/A",
    "White": "MG6K4HN/A",
    "Mist Blue": "MG6L4HN/A",
    "Sage": "MG6M4HN/A",
    "Lavender": "MG6N4HN/A",
}


def check_pickup(color, product):
    params = {
        "fae": "true",
        "mts.0": "regular",
        "mts.1": "compact",
        "searchNearby": "true",
        "store": STORE_ID,
        "product": product,
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=20,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
    )

    return {
        "color": color,
        "status_code": response.status_code,
        "text": response.text,
    }


def check_all():
    results = []

    for color, product in PRODUCTS.items():
        results.append(check_pickup(color, product))

    return results
