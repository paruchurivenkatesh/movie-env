from flask import Flask, request, jsonify

app = Flask(__name__)

state = {"step": 0}

@app.route("/reset", methods=["POST"])
def reset():
    state["step"] = 0
    return jsonify({
        "observation": "reset done",
        "reward": 0.0,
        "done": False
    })

@app.route("/step", methods=["POST"])
def step():
    data = request.json
    action = data.get("action", "")

    state["step"] += 1

    return jsonify({
        "observation": f"action: {action}",
        "reward": 1.0,
        "done": state["step"] > 2
    })

# ✅ REQUIRED FUNCTION
def main():
    app.run(host="0.0.0.0", port=7860)

# ✅ REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()
