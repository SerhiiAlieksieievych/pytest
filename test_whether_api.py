import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_key")

def get_whether_info(lat, lon):
    params={"lat":lat,"lon":lon,"appid":API_KEY,"lang":"ua"}
    return requests.get(f"https://api.openweathermap.org/data/2.5/weather?", params=params)

print(get_whether_info(44, 56))

def test_get_whether_info():
    assert get_whether_info(40, 30).status_code == 200