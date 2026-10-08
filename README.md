# 🛒 SmartShelf AI

A Deep Learning based computer-vision project for analyzing retail or restaurant shelves.

## Problem
Manual shelf inspection is slow and can miss empty product positions.

## Solution
SmartShelf AI analyzes a shelf image and estimates shelf availability. The project is designed to support YOLO object detection for identifying products and empty shelf positions.

## Features
- Shelf image upload
- Availability estimation
- Product/empty-slot analysis
- Restocking alert
- Streamlit web interface
- YOLO training and inference pipeline
- GitHub-ready structure

## Installation

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd SmartShelf_AI
python -m venv venv
```

Activate the environment:

Windows:
```bash
venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the demo

```bash
streamlit run app.py
```

## Train the Deep Learning model

Prepare a YOLO dataset using the included `dataset/data.yaml`, then:

```bash
python train.py
```

The trained model can be placed at:

```text
models/smartshelf.pt
```

## Dataset classes

- `product`
- `empty_slot`

## Project workflow

Image → Preprocessing → YOLO Detection → Product/Empty Slot Detection → Shelf Availability → Restocking Alert

## Future Improvements

- Barcode/product-name recognition
- Real-time camera support
- Automatic inventory database
- Email/WhatsApp restocking alerts
- Multi-shelf tracking
- Cloud deployment
- Mobile application

## Academic use

Suitable for a BTech AIML mini/final-year project demonstration.

## License

MIT

## Author
Mayank

B.tech Ai/Ml