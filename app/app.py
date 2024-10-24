from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

# Path to your certificates folder
CERTIFICATES_FOLDER = os.path.join(os.getcwd(), 'app/certificates')

@app.route('/')
def index():
    # Get the selected format from the request, default to "all"
    selected_format = request.args.get('format', 'all')

    # List all files in the certificates folder
    files = os.listdir(CERTIFICATES_FOLDER)

    # Filter files based on the selected format
    if selected_format == 'jpg':
        files = [f for f in files if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
    elif selected_format == 'pdf':
        files = [f for f in files if f.endswith('.pdf')]

    return render_template('index.html', files=files, selected_format=selected_format)

@app.route('/certificates/<filename>')
def serve_certificate(filename):
    return send_from_directory(CERTIFICATES_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
