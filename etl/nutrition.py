import requests
import os
from openfoodfacts.api import APIConfig, ProductResource

def fetch_openfoodfacts(product_name, max_results=20):
    api_config = APIConfig(user_agent='your-app-name/1.0')  # Replace with your app name
    product_resource = ProductResource(api_config)
    results = product_resource.text_search(product_name, page=1, page_size=max_results)
    if results and 'products' in results and len(results['products']) > 0:
        return results['products']
    return []

def fetch_nutritionix(product_name):
    url = "https://trackapi.nutritionix.com/v2/search/instant"
    headers = {
        "x-app-id": os.getenv("NUTRITIONIX_APP_ID"),
        "x-app-key": os.getenv("NUTRITIONIX_APP_KEY")
    }
    params = {"query": product_name}
    r = requests.get(url, headers=headers, params=params)
    return r.json()

def fetch_fatsecret(product_name):
    # Implement OAuth2 and API call as per FatSecret docs
    # Return nutrition info (stub for now)
    return {}

def get_nutrition_data(product_name):
    data = {}
    data['openfoodfacts'] = fetch_openfoodfacts(product_name)
    data['nutritionix'] = fetch_nutritionix(product_name)
    data['fatsecret'] = fetch_fatsecret(product_name)
    return data
