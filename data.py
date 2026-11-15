matches = [
    {
        "match_id": 1,
        "stage": "Play-Ins",
        "date": "October 21, 2026",
        "team1": "TeamA",
        "team2": "TeamB",
        "score1": None,
        "score2": None,
        "status": "Upcoming",
    },
    {
        "match_id": 2,
        "stage": "Play-Ins",
        "date": "October 21, 2026",
        "team1": "TeamC",
        "team2": "TeamD",
        "score1": None,
        "score2": None,
        "status": "Upcoming",
    },

    # UPPER BRACKET SEMIFINALS (BO5)
    {
        "match_id": 3,
        "stage": "Upper Bracket Semifinals",
        "date": "October 22, 2026",
        "team1": "TeamE",
        "team2": "Winner of Match 1",
        "score1": None,
        "score2": None,
        "status": "Upcoming",
    },
    {
        "match_id": 4,
        "stage": "Upper Bracket Semifinals",
        "date": "October 22, 2026",
        "team1": "TeamF",
        "team2": "Winner of Match 2",
        "score1": None,
        "score2": None,
        "status": "Upcoming",
    },

    # UPPER BRACKET FINALS (BO5)
    {
        "match_id": 5,
        "stage": "Upper Bracket Finals",
        "date": "October 23, 2026",
        "team1": "Winner of Match 3",
        "team2": "Winner of Match 4",
        "score1": None,
        "score2": None,
        "status": "Upcoming",
    },

    # LOWER BRACKET SEMIFINALS (BO5)
    {
        "match_id": 6,
        "stage": "Lower Bracket Semifinals",
        "date": "October 23, 2026",
        "team1": "Loser of Match 3",
        "team2": "Loser of Match 4",
        "score1": None,
        "score2": None,
        "status": "Upcoming",
    },

    # LOWER BRACKET FINALS (BO7)
    {
        "match_id": 7,
        "stage": "Lower Bracket Finals",
        "date": "October 24, 2026",
        "team1": "Loser of Match 5",
        "team2": "Winner of Match 6",
        "score1": None,
        "score2": None,
        "status": "Upcoming",
    },

    # GRAND FINALS (BO7)
    {
        "match_id": 8,
        "stage": "Grand Finals",
        "date": "October 25, 2026",
        "team1": "Winner of Match 5",
        "team2": "Winner of Match 7",
        "score1": None,
        "score2": None,
        "status": "Upcoming",
    },
]


def find_match_by_id(match_id):
    """Return a match by ID, or None when it does not exist."""
    return next(
        (match for match in matches if match["match_id"] == match_id),
        None,
    )
