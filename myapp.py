from flask import Flask, render_template, request, jsonify
from pyzbar.pyzbar import decode
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    if 'image' not in request.files:
        return 'No file part', 400
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        # Convert string data to 1D numpy array
        nparr = np.fromstring(file.read(), np.uint8)

        # Decode numpy array into image
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Decode barcodes
        decoded_objects = decode(img)

        # Return barcode data
        return jsonify([obj.data.decode("utf-8") for obj in decoded_objects])

if __name__ == '__main__':
    app.run(debug=True)
