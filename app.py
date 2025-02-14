from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Luiz 1.0 está online!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()
    
    respostas = {
        "oi": "Olá! Como posso te ajudar?",
        "quem é você?": "Sou o Luiz 1.0, sua IA assistente!",
        "como você funciona?": "Eu respondo mensagens e aprendo com o tempo.",
        "adeus": "Até mais! Sempre que precisar, estou aqui."
    }
    
    resposta = respostas.get(user_message, "Desculpe, não entendi. Pode repetir?")
    
    return jsonify({"response": resposta})

if __name__ == '__main__':
    app.run(debug=True)
