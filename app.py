from flask import Flask, request, jsonify

app = Flask(__name__)

# Memória temporária para armazenar informações (depois podemos melhorar isso)
memory = {"messages": []}

@app.route("/", methods=["GET"])
def home():
    return "Luiz 1.0 está online!", 200

@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "Mensagem inválida"}), 400

    message = data["message"]
    memory["messages"].append(message)

    return jsonify({"response": f"Recebi sua mensagem: {message}"}), 200

@app.route("/history", methods=["GET"])
def history():
    return jsonify(memory), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
