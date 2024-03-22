import requests
from datetime import datetime as dt

NUTRITIONIX_APP_ID = ""
NUTRITIONIX_API_KEY = ""
NUTRITIONIX_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API_ENDPOINT = "https://api.sheety.co"


exercise = input("Tell me what exercise you did today and how long?")

nutritionix_headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
  }

nutritionix_json= {
    "query": exercise
}

response = requests.post(url=NUTRITIONIX_END_POINT, json=nutritionix_json, headers=nutritionix_headers)
nutritionix_response = response.json()


current_date = dt.now().strftime("%d/%m/%Y")
current_time = dt.today().strftime("%X")

sheety_headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
  }

for exercise in nutritionix_response["exercises"]:
    sheety_json= {
        "workout": {
                    "date": current_date,
                    "time":	current_time,
                    "exercise":	exercise["name"].title(),
                    "duration":	exercise["duration_min"],
                    "calories": exercise["nf_calories"]
        }

    }
    response = requests.post(url=SHEETY_API_ENDPOINT, json=sheety_json)
    #print(response.text)