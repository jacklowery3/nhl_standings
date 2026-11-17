# nhl_standings

Using an API to tell me what's going on in the world of professional hockey (NHL).

A small Python script that pulls NHL standings for a season from the
**NHL API** on RapidAPI (`nhl-api5.p.rapidapi.com`, which serves ESPN's
standings data) and saves the raw response to `data.json`.

## Setup

```bash
pip install requests
```

Create a `.env` file in this folder (it's gitignored) with your RapidAPI key:

```
RAPIDAPI_KEY=your_rapidapi_key
```

You need an active subscription to **NHL API** on RapidAPI (the API ID is
`6afbcf43d210bc25c2f2aa5f`). A key alone isn't enough: RapidAPI keys only
work for the APIs you're subscribed to.

## Usage

```bash
set -a; . ./.env; set +a          # load RAPIDAPI_KEY into the shell
python find_standings.py          # current season
python find_standings.py 2022     # a specific season
```

`year` is the year the season **ends**: `2022` is the 2021-22 season, and
`2027` is 2026-27. The default is the current season, which rolls over in
September.

The script calls `GET /nhlstandings?year=<year>` and writes the JSON to
`data.json` in the current folder. If the API returns an error, it prints the
error and leaves any existing `data.json` alone.

## What's in `data.json`

- `standings.entries`: one entry per team (32), each with
  - `team`: name, abbreviation, location, logos
  - `stats`: a list of `{name, displayName, value, displayValue}`, including
    `points`, `wins`, `losses`, `otLosses`, `gamesPlayed`, `playoffSeed`,
    `differential`, `powerPlayPct` and `penaltyKillPct`
- `season`: the season returned (`displayName` like `2021-22`)
- `seasons`: every season the API knows about, with start and end dates

## API limits (Basic plan)

This project runs on the **free Basic plan** of the NHL API on RapidAPI,
which has a small request quota (check the API's Pricing tab for the current
numbers). Every run of `find_standings.py` uses one request.

- Don't loop, poll, or retry the API in quick succession. If you get a
  `429 Too many requests`, stop and wait.
- Work from the saved `data.json` when exploring or building on the data,
  instead of re-fetching it.
- A `403 "You are not subscribed to this API."` comes from RapidAPI itself and
  means the key isn't tied to an active subscription for this API. Retrying
  won't fix it.

## Notes

- `data.json` is generated output and is gitignored.
- Never commit the API key. It lives only in `.env`.
- History: this project originally used API-Sports' **API-Hockey**
  (`api-hockey.p.rapidapi.com`) and switched to the NHL API in Nov 2026.
