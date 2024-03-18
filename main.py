import requests
NUTRITIONIX_APP_ID = ""
NUTRITIONIX_API_KEY = ""
NUTRITIONIX_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


nutritionix_headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
  }

nutritionix_params = {
    "query": "run for 2 hours"
}

response = requests.post(url=NUTRITIONIX_END_POINT, json=nutritionix_params, headers=nutritionix_headers)
print(response.text)
print("Initial Commit")