import sys
import requests
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

# Initialize QApplication BEFORE creating any widgets
app = QApplication(sys.argv)

class FaceRecognitionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Face Recognition Bot")
        
        # Adjust the window size
        self.setGeometry(300, 200, 400, 500)

        # Apply styles to the window
        self.setStyleSheet("background-color: #2E3440; color: white;")

        layout = QVBoxLayout()

        # Profile picture for bot
        self.profile_pic = QLabel(self)
        pixmap = QPixmap("bot_pic.jpg")
        if pixmap.isNull():
            pixmap = QPixmap(100, 100)  # Blank placeholder
        
        scaled_pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.profile_pic.setPixmap(scaled_pixmap)
        self.profile_pic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.profile_pic)

        self.label = QLabel("Upload an image for face detection.")
        layout.addWidget(self.label)

        # Upload Button
        self.upload_button = QPushButton("Upload Image")
        self.upload_button.setStyleSheet("background-color: #8FBCBB; font-size: 14px; padding: 10px;")
        self.upload_button.clicked.connect(self.upload_image)
        layout.addWidget(self.upload_button)

        # Analyze Face Button
        self.analyze_button = QPushButton("Analyze Face")
        self.analyze_button.setStyleSheet("background-color: #88C0D0; font-size: 14px; padding: 10px;")
        self.analyze_button.clicked.connect(self.analyze_face)
        layout.addWidget(self.analyze_button)

        self.setLayout(layout)
        self.image_path = ""

    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image")
        if file_name:
            self.image_path = file_name
            self.label.setText(f"Image Selected: {file_name}")

    def analyze_face(self):
        if self.image_path:
            try:
                files = {"image": open(self.image_path, "rb")}
                response = requests.post("http://51.20.70.169:5000/recognize", files=files)

                if response.status_code == 200:
                    data = response.json()
                    age = data.get("age", "N/A")
                    gender = data.get("gender", "N/A")
                    self.label.setText(f"Detected Age: {age}, Gender: {gender}")
                else:
                    self.label.setText("Error: Failed to connect to EC2")
            except Exception as e:
                self.label.setText(f"Error: {str(e)}")

# Start the application
if __name__ == "__main__":
    window = FaceRecognitionApp()
    window.show()
    sys.exit(app.exec())