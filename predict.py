"""
Inference module for SmartShelf AI.

Replace the placeholder model path with a trained YOLO model.
Example with Ultralytics:
    from ultralytics import YOLO
    model = YOLO("models/smartshelf.pt")
    results = model("sample.jpg")
"""

MODEL_PATH = "models/smartshelf.pt"

def predict(image_path):
    try:
        from ultralytics import YOLO
    except ImportError:
        raise RuntimeError("Install dependencies using: pip install -r requirements.txt")

    model = YOLO(MODEL_PATH)
    return model(image_path)

if __name__ == "__main__":
    print("SmartShelf AI inference module.")
    print(f"Expected trained model: {MODEL_PATH}")
