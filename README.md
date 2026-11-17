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

## Notes

- `data.json` is generated output and is gitignored.
- The API key is read from the `RAPIDAPI_KEY` environment variable; never
  commit it.
