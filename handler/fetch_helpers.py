import requests
from typing import List, Optional, Dict, Any

def fetch_data(url: str) -> Optional[Dict[str, Any]]:
    """
    Fetch data from a given URL.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        Optional[Dict[str, Any]]: The JSON response as a dictionary, or None if an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None

def get_water_type_url() -> Optional[str]:
    type_url = 'https://pokeapi.co/api/v2/type/'
    data = fetch_data(type_url)

    if data:
        for poke_type in data['results']:
            if poke_type['name'].lower() == 'water':
                return poke_type['url']

    return None

def fetch_water_pokemons() -> List[str]:
    water_type_url = get_water_type_url()
    if not water_type_url:
        print("Water type URL not found.")
        return []

    data = fetch_data(water_type_url)
    if data:
        return [pokemon['pokemon']['name'] for pokemon in data['pokemon']]

    return []