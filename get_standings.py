from flask import Blueprint, jsonify
from data import find_match_by_id

standings_bp = Blueprint("standings", __name__)


@standings_bp.route("/matches/<int:match_id>/standings/", methods=["GET"])
def get_match_standings(match_id):
    
    match = find_match_by_id(match_id)

    if match is None:
        return jsonify({"message": "Match not found"}), 404

    response = {
        "match_id": match["match_id"],
        "stage": match["stage"],
        "team1": match["team1"],
        "team2": match["team2"],
        "score1": match["score1"],
        "score2": match["score2"],
        "winner": match.get("winner"),
        "status": match["status"],
    }

    return jsonify(response)