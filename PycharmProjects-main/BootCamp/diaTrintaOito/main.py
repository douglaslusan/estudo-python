import requests

GENDER = "masculine"
WEIGHT_KG = 82
HEIGHT_CM = 174
AGE = 42

APP_ID = "a3765448"
API_KEY = "d5a14c988774f69cb7962e5f3ecedbc7"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)