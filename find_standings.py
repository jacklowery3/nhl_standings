import os
import sys
import datetime
import requests
import json

# Usage: python find_standings.py [year]
# `year` is the year a season ENDS (2022 = the 2021-22 season). Defaults to the
# current season, which rolls over in September.
# Each run is one API request; the Basic plan has a small daily quota.
today = datetime.date.today()
current_season = today.year + 1 if today.month >= 9 else today.year
year = sys.argv[1] if len(sys.argv) > 1 else str(current_season)

url = "https://nhl-api5.p.rapidapi.com/nhlstandings"

querystring = {"year": year}

headers = {
	"X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
	"X-RapidAPI-Host": "nhl-api5.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Don't overwrite data.json with an error payload (403 not subscribed, 429 rate limited, ...)
if not response.ok:
	sys.exit(f"API error {response.status_code}: {response.text[:200]}")

data = response.json()

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Saved {year} standings to data.json")
