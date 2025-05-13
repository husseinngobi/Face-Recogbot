import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap  # Import QPixmap for handling images
from deepface import DeepFace

# Initialize QApplication BEFORE creating any widgets
app = QApplication(sys.argv)

class FaceRecognitionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Face Recognition Bot")
        
        # Adjust the window size to a smaller default
        self.setGeometry(300, 200, 400, 500)  # Adjust width and height

        # Apply styles to the window and buttons
        self.setStyleSheet("background-color: #2E3440; color: white;")

        layout = QVBoxLayout()

        # Add a profile picture with scaled size
        self.profile_pic = QLabel(self)
        pixmap = QPixmap("bot_pic.jpg") # Replace with your chosen image
        
        # Fallback: If the image doesn't load, create a blank placeholder
        if pixmap.isNull():
            pixmap = QPixmap(100, 100)  # Creates a blank 100x100 placeholder



        scaled_pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.profile_pic.setPixmap(scaled_pixmap)
        self.profile_pic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.profile_pic)

        self.label = QLabel("Upload an image for face detection and analysis.")
        layout.addWidget(self.label)

        self.upload_button = QPushButton("Upload Image")
        self.upload_button.setStyleSheet("background-color: #8FBCBB; font-size: 14px; padding: 10px;")
        self.upload_button.clicked.connect(self.upload_image)
        layout.addWidget(self.upload_button)

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
                result = DeepFace.analyze(
                    img_path=self.image_path,
                    actions=["age", "gender"],
                    detector_backend="mtcnn",
                    enforce_detection=False
                )
                age = result[0]["age"]
                gender = result[0]["gender"]
                self.label.setText(f"Detected Age: {age}, Gender: {gender}")
            except Exception as e:
                self.label.setText(f"Error: {str(e)}")

# Ensure QApplication starts before creating the GUI
if __name__ == "__main__":
    window = FaceRecognitionApp()
    window.show()
    sys.exit(app.exec())