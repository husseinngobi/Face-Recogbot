import cv2

image = cv2.imread(r"C:\Users\HP\OneDrive\Documents\FaceRecogBot\me.hus.jpg")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

print("✅ Faces Detected:", len(faces))  # Check if faces were found