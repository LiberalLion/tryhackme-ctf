import requests

TARGET_API = "HERE YOUR TARGET_IP"

for i in range(0, 100):
    if i %2 == 1:
        response = requests.get(f'http://{TARGET_API}' + f':8000/api/{str(i)}')
        print(f"{str(i)} : {response.status_code}")
        print(response.text)
