from flask import Flask, request, jsonify
from gpt_docs import work_ai
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
version = "v1"

# Роут для обработки запроса
@app.route("/process", methods=["POST"])
def process_message():
    try:
        data = request.get_json()
        chat_id = data.get("chat_id")
        msg = data.get("msg")
        
        if chat_id is None or msg is None:
            return jsonify({"error": "Missing chat_id or msg"}), 400
        
        result = work_ai(chat_id, msg)
        return jsonify(result)
    except Exception as e:
        return jsonify({"chat_id": chat_id, "answer": f"Ошибка: {e}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=5010)# port=5010,
