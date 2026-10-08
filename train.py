"""
Training starter for SmartShelf AI.

Dataset format for YOLO:
dataset/
  images/train/
  images/val/
  labels/train/
  labels/val/
  data.yaml

After preparing and labeling your dataset, run:
    python train.py
"""

MODEL_NAME = "yolo11n.pt"

def train():
    from ultralytics import YOLO
    model = YOLO(MODEL_NAME)
    model.train(
        data="dataset/data.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        project="runs",
        name="smartshelf"
    )

if __name__ == "__main__":
    train()
