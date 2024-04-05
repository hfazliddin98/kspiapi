from django.test import TestCase
import requests

jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEyNDg4MDk2LCJpYXQiOjE3MTIyMjg4OTYsImp0aSI6ImMzYjE0NmUyYmNhYjQyOTFiY2UzNWU1NTJlMTliMzgxIiwidXNlcl9pZCI6Mn0.CI07Jh0O-f64x853DvnHrf46Cqs_Dsh2W7E7mIU0jKE"
headers = {
    "Authorization": f"Bearer {jwt_token}"
}

tur_url = 'http://127.0.0.1:8000/home/galareya/tur/'
galareya_tur = requests.get(tur_url)
turlar = galareya_tur.json()[0]

print(turlar['id'])
pk = turlar['id']

url = 'http://127.0.0.1:8000/home/galareya/tur/create/'
galareya_url = 'http://127.0.0.1:8000/home/galareya/create/'


# data =  {
#     "tur_uz": "Institut",
#     "tur_ru": "Institut",
#     "tur_en": "Institut"
# }

# galareya = requests.post(url, data=data, headers=headers)
# print(galareya)
data1 = requests.get(f'http://127.0.0.1:8000/home/galareya/tur/{pk}/')
data =  {
    "rasm": "",
    "tur_id": data1.json(),
}

galareya = requests.post(galareya_url, data=data, headers=headers)
print(galareya)