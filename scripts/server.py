from flask import Flask, request, jsonify
import face_recognition

app = Flask(__name__)

@app.route('/recognize', methods=['POST'])
def recognize_face():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image = request.files['image']
    face_data = face_recognition.load_image_file(image)
    results = face_recognition.face_encodings(face_data)

    return jsonify({"faces_found": len(results)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)