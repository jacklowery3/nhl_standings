# nhl_standings

Small script that fetches NHL standings from the NHL API on RapidAPI
(`nhl-api5.p.rapidapi.com`, `GET /nhlstandings?year=<season end year>`). See README.md.

## API budget: read this before calling the API

- The user is on the **free Basic plan** (small daily quota). Treat every
  API call as expensive.
- Make at most one call per task unless the user says otherwise. Never loop,
  poll, or retry automatically. On `429` or `403`, stop and report back.
- Reuse the existing `data.json` for analysis instead of re-fetching.
- The key is `RAPIDAPI_KEY` in `.env` (gitignored). Load it with
  `set -a; . ./.env; set +a`. Never print, echo, or commit the key.
