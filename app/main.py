import os
import requests


def get_weather() -> tuple[float, str]:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("API_KEY environment variable is not set")

    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "Paris"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Request failed {response.status_code}")
    data = response.json()

    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    return temperature, condition


if __name__ == "__main__":
    temperature, condition = get_weather()
    print(f"Paris: {temperature} °C, {condition}")
