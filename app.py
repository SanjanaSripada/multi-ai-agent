# app.py

from flask import Flask, request, jsonify, render_template
from agents.classifier_agent import ClassifierAgent

app = Flask(__name__)
classifier = ClassifierAgent()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/process', methods=['POST'])
def process_input():
    input_data = request.get_json()
    if not input_data or 'data' not in input_data:
        return jsonify({'error': 'No input data provided.'}), 400

    result = classifier.route_input(input_data['data'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
