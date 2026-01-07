import requests

url = "http://localhost:9696/predict"

patient_data = {
    "pregnancies": 3,
    "glucose": 130.0,
    "bloodpressure": 80.0,
    "skinthickness": 30.0,
    "insulin": 100.0,
    "bmi": 55.0,
    "diabetespedigreefunction": 0.5,
    "age": 40
}

response = requests.post(url, json=patient_data)
print(response.json())