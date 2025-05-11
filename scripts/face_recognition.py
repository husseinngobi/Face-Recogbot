from deepface import DeepFace

# Compare me.hus.jpg with itself (just for testing)

result = DeepFace.verify(
    img1_path=r"C:\Users\HP\OneDrive\Documents\FaceRecogBot\me.hus.jpg",
    img2_path=r"C:\Users\HP\OneDrive\Documents\FaceRecogBot\CEO-image.jpg",
    model_name="ArcFace",
    enforce_detection=False
)
print("Match Result:", result["verified"])