from flask import Flask, request, jsonify , render_template
from model import generate_response
app = Flask(__name__)
import time

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/generate", methods=["POST"])
def generate():
    data=request.json
    user_message=data.get("message")
    if not user_message:
        return jsonify({"error": "Message is required"}), 400
    
    system_prompt = "You are an AI assistant helping with customer inquiries. Provide a helpful and concise response."
    startime = time.time()
    try:
        result = generate_response(system_prompt, user_message)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    # If result is a list of profiles, format them
    if isinstance(result, list):
        formatted_response = ""
        for item in result:
            if isinstance(item, dict):
                name = item.get('name', 'Unknown')
                location = item.get('location', 'Unknown')
                profession = item.get('profession', 'Unknown')
                formatted_response += f"Name: {name}, Location: {location}, Profession: {profession}\n"
        result = {"response": formatted_response.strip(), "duration": time.time() - startime}
    else:
        result['duration'] = time.time() - startime
    
    return jsonify(result)
if __name__ == "__main__":
    app.run(debug=True)