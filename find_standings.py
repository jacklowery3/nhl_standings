import os
import requests
import json

# league info
# id = 57 (NHL)
# usa = 1d (countr
# season:2023
# current:false
# start:"2023-09-23"
# end:"2023-10-07"

url = "https://api-hockey.p.rapidapi.com/standings/"

querystring = {"league":"57","season":"2023"}

headers = {
	"X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
	"X-RapidAPI-Host": "api-hockey.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)