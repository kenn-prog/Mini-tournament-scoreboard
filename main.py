from flask import Flask, jsonify

main = Flask(__name__)

# API information route (not counted among the four match endpoints).
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
