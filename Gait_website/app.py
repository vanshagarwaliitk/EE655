from flask import Flask, request, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploaded_videos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')  # Put your HTML in templates/index.html

@app.route('/upload', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return "No file part", 400
    video = request.files['video']
    if video.filename == '':
        return "No selected file", 400

    save_path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(save_path)
    print(f"[INFO] Saved to: {save_path}")
    return "Success", 200

if __name__ == '__main__':
    app.run(debug=True)
