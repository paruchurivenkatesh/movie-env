from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy state
state = {
    "step": 0
}

@app.route("/reset", methods=["POST"])
def reset():
    state["step"] = 0
    return jsonify({
        "observation": "Environment reset",
        "reward": 0.0,
        "done": False
    })

@app.route("/step", methods=["POST"])
def step():
    data = request.json
    action = data.get("action", "")

    state["step"] += 1

    return jsonify({
        "observation": f"Action received: {action}",
        "reward": 1.0,
        "done": state["step"] > 2
    })

@app.route("/")
def home():
    return "OpenEnv Movie Env is running"

app.run(host="0.0.0.0", port=7860)
