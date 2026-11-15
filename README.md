# Mini-tournament-scoreboard

A Flask API for managing tournament match information and scores.

## Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/matches/` | Retrieve all matches |
| GET | `/matches/<match_id>/standings/` | Retrieve one match's standings |
| PATCH | `/matches/<match_id>/reset/` | Reset a match |
| PATCH | `/matches/<match_id>/score/` | Update a match score and bracket progression |

The `/` route displays API information.

## Setup and run

```bash
python -m venv venv
```

Activate the virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
python main.py
```
The API runs locally at `http://127.0.0.1:5000`.

## Project Summary

The Mini Tournament Scoreboard API is a REST API designed to manage and track team scores in a mini tournament. It allows users to add teams, view all team scores, retrieve a specific team's score, and update team scores. The API uses Python Flask and stores scoreboard data using Python lists or dictionaries. 