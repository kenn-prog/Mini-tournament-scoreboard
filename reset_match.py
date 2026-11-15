from flask import Blueprint, jsonify
from data import find_match_by_id

reset_bp = Blueprint("reset_match", __name__)

@reset_bp.route("/matches/<int:match_id>/reset/", methods=["PATCH"])
def reset_match(match_id):
    
    match = find_match_by_id(match_id)

    if match is None:
        return jsonify({"message": "Match not found"}), 404

    match["score1"] = None
    match["score2"] = None
    match["winner"] = None
    match["status"] = "Upcoming"

    response = {
        "match_id": match["match_id"],
        "score1": match["score1"],
        "score2": match["score2"],
        "winner": match["winner"],
        "status": match["status"],
    }

    return jsonify({
        "message": "Match reset successfully",
        "match": response,
    }), 200
