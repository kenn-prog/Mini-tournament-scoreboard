from flask import Blueprint, jsonify

from data import matches

matches_bp = Blueprint("matches", __name__)


@matches_bp.route("/matches/", methods=["GET"])
def get_matches():
    """Return a summary of every tournament match."""
    response = {
        "message": "Matches of the Tournament",
        "total_matches": len(matches),
        "matches": [
            {
                "match_id": match["match_id"],
                "stage": match["stage"],
                "team1": match["team1"],
                "team2": match["team2"],
                "status": match["status"],
            }
            for match in matches
        ],
    }

    return jsonify(response)