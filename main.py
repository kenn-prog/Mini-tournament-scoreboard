from flask import Flask, jsonify

from get_matches import matches_bp
from get_standings import standings_bp
from reset_match import reset_bp
from update_score import score_bp

main = Flask(__name__)

main.register_blueprint(matches_bp)
main.register_blueprint(standings_bp)
main.register_blueprint(reset_bp)
main.register_blueprint(score_bp)

@main.route("/", methods=["GET"])
def home():
    """Show the API welcome message and endpoint paths."""
    response = [
        "Welcome to Mini Tournament Scoreboard API",
        {
            "Endpoints": {
                "Matches": "/matches/",
                "Standing": "/matches/<match_id>/standings",
            }
        },
    ]

    return jsonify(response)


if __name__ == "__main__":
    main.run(debug=True)
