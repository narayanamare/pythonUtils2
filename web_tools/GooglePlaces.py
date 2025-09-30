import requests

API_KEY = "YOUR_API_KEY"
keyword = "restaurants near me"

url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
params = {
    "query": keyword,
    "key": API_KEY
}

response = requests.get(url, params=params)
data = response.json()

for place in data["results"]:
    print(place["name"])
    print(place.get("formatted_address", ""))
    print(place.get("rating", ""))
    print(place.get("user_ratings_total", ""))
    print("---")
