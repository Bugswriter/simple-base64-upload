import time
import base64
from flask import Flask, render_template, jsonify, Response
import cv2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

def generate_frames():
    while True:
        frame = cv2.imread("test.jpg")
        _ , buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/input_image")
def input_image():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/output_response")
def output_response():
    path = "test.jpg"

    with open(path, 'rb') as image_file:
        b64_encoded_image = "data:image/jpeg;base64, " + base64.b64encode(image_file.read()).decode("utf-8")

    return jsonify({"image": b64_encoded_image})

if __name__=="__main__":
    app.run(debug=True)
