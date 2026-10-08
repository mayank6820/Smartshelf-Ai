import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.set_page_config(page_title="SmartShelf AI", page_icon="🛒", layout="wide")

st.title("🛒 SmartShelf AI")
st.caption("Deep Learning based shelf availability analysis")

uploaded = st.file_uploader("Upload a shelf image", type=["jpg","jpeg","png"])

def analyze_image(img):
    arr = np.array(img)
    h, w = arr.shape[:2]

    # Demo visual analysis. Replace with a trained YOLO model in production.
    gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 60, 150)
    edge_density = float(np.mean(edges > 0))

    # Estimate occupancy from image texture; this is intentionally a lightweight demo.
    availability = int(np.clip(55 + edge_density * 180, 20, 98))
    empty = max(1, round((100 - availability) / 10))
    products = max(1, round(availability / 5))

    return availability, empty, products

if uploaded:
    image = Image.open(uploaded).convert("RGB")
    col1, col2 = st.columns([1.4, 1])

    with col1:
        st.image(image, caption="Uploaded shelf", use_container_width=True)

    availability, empty, products = analyze_image(image)

    with col2:
        st.subheader("Analysis")
        st.metric("Shelf availability", f"{availability}%")
        st.metric("Estimated products", products)
        st.metric("Empty positions", empty)

        if availability < 75:
            st.error("⚠️ Restocking recommended")
        else:
            st.success("✅ Shelf looks sufficiently stocked")

        st.info(
            "This starter demo contains the complete application pipeline. "
            "For real object-level detection, place a trained YOLO model in "
            "`models/` and connect it in `predict.py`."
        )
else:
    st.info("Upload a shelf image to begin.")
