import os
from flask import Flask, render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
import pdfplumber

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads'

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():

    folder = app.config['UPLOAD_FOLDER']

    for filename in os.listdir(folder):

        if filename == '.gitkeep':
            continue

        file_path = os.path.join(folder, filename)
        
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")

    return render_template("index.html")

@app.route("/extract", methods=['POST'])
def extract():

    if 'pdf' not in request.files:
        return "No file part"

    file = request.files['pdf']
    
    if file.filename == '':
        return "No selected file"
    
    if not allowed_file(file.filename):
        return "Invalid file type"

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    text = ""

    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    return render_template("result.html", filename=filename.split('.')[0], text=text)

@app.route("/again", methods=['POST'])
def again():
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)