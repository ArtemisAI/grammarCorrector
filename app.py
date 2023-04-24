from flask import Flask, render_template, request, jsonify
# Import the generate_response function from gpt.py
from gpt import generate_response

from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.form.get('prompt')
    response = generate_response(prompt)
    return jsonify(response)

@app.route('/clear', methods=['POST'])
def clear():
    return jsonify({"success": True})

if __name__ == '__main__':
    # Set the host to '0.0.0.0' to make the application accessible on the LAN
    app.run(host='0.0.0.0', port=5000, debug=True)
