# nhl_standings

Using an API to tell me what's going on in the world of professional hockey (NHL).

A small Python script that pulls NHL standings for a season from the
[API-Hockey](https://rapidapi.com/api-sports/api/api-hockey) API on RapidAPI
and saves the raw response to `data.json`.

## Setup

```bash
pip install requests
export RAPIDAPI_KEY=your_rapidapi_key   # from your RapidAPI dashboard
```

## Usage

```bash
python find_standings.py
```

This requests `/standings/` for league `57` (NHL) and season `2023`, then
writes the JSON response to `data.json` in the current folder. Change
`querystring` in `find_standings.py` to fetch a different season.

## API limits (Basic plan)

This project runs on the **free Basic plan** of API-Hockey on RapidAPI, which
allows only about **100 requests per day** (check the API's Pricing tab for
the current numbers). Every run of `find_standings.py` uses one request.

- Don't loop, poll, or retry the API in quick succession. If you get a
  `429 Too many requests`, stop and wait.
- Work from the saved `data.json` when exploring or building on the data,
  instead of re-fetching it.
- A `403 "You are not subscribed to this API."` comes from RapidAPI itself and
  means the key isn't tied to an active API-Hockey subscription. Retrying
  won't fix it.

## Notes

- `data.json` is generated output and is gitignored.
- The API key is read from the `RAPIDAPI_KEY` environment variable; never
  commit it.
