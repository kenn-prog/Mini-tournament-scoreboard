from flask import Blueprint, jsonify, request
from data import find_match_by_id

score_bp = Blueprint("update_score", __name__)


@score_bp.route("/matches/<int:match_id>/score/", methods=["PATCH"])
def update_score(match_id):
    match = find_match_by_id(match_id)

    if match is None:
        return jsonify({"message": "Match not found"}), 404

    data = request.get_json()

    if not data or "score1" not in data or "score2" not in data:
        return jsonify({"message": "Both scores are required"}), 400

    score1 = data["score1"]
    score2 = data["score2"]

    if (
        type(score1) != int
        or type(score2) != int
        or score1 < 0
        or score2 < 0
    ):
        return jsonify({"message": "Invalid scores"}), 400

    winning_score = 4 if match_id in [7, 8] else 3

    if score1 > winning_score or score2 > winning_score:
        return jsonify({"message": "Score exceeds winning limit"}), 400

    if score1 == score2 == winning_score:
        return jsonify({"message": "A match cannot have two winners"}), 400

    match["score1"] = score1
    match["score2"] = score2

    if score1 == winning_score:
        match["winner"] = match["team1"]
        match["status"] = "Completed"
    elif score2 == winning_score:
        match["winner"] = match["team2"]
        match["status"] = "Completed"
    else:
        match["winner"] = None
        match["status"] = "Ongoing"

    if match["status"] == "Completed":
        winner = match["winner"]
        loser = match["team2"] if winner == match["team1"] else match["team1"]

        progression = {
            1: [(3, "team2", winner)],
            2: [(4, "team2", winner)],
            3: [(5, "team1", winner), (6, "team1", loser)],
            4: [(5, "team2", winner), (6, "team2", loser)],
            5: [(8, "team1", winner), (7, "team1", loser)],
            6: [(7, "team2", winner)],
            7: [(8, "team2", winner)],
        }

        for next_match_id, team_slot, advancing_team in progression.get(
            match_id, []
        ):
            next_match = find_match_by_id(next_match_id)

            if next_match:
                next_match[team_slot] = advancing_team

    return jsonify({
        "message": "Match score updated successfully",
        "match": match,
    }), 200
