from flask import Flask, request, jsonify,render_template
from agents.classifier_agent import ClassifierAgent
from werkzeug.utils import secure_filename
import os 

app = Flask(__name__, template_folder= "templates")
classifier = ClassifierAgent()

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_input():
    if request.is_json:
        input_data = request.get_json()
        result = classifier.route_input(input_data)
        return jsonify(result)

    elif 'email_text' in request.form:
        email_text = request.form['email_text']
        result = classifier.route_input(email_text)
        return jsonify(result)

    elif 'pdf_file' in request.files:
        file = request.files['pdf_file']
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        result = classifier.route_input(filepath)
        return jsonify(result)

    return jsonify({"error": "Unsupported input format"}), 400

if __name__ == '__main__':
    app.run(debug=True)
