import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
from PIL import Image
import os
import pickle
import io

# ============= PAGE CONFIGURATION =============
st.set_page_config(
    page_title="Car vs Motorcycle Classifier",
    page_icon="🏍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============= CUSTOM STYLING =============
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF6B6B;
        color: white;
        border-radius: 10px;
        padding: 0.5rem;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FF5252;
    }
    </style>
    """, unsafe_allow_html=True)

# ============= SIDEBAR CONFIGURATION =============
st.sidebar.title("🚗 Car vs Motorcycle Classifier")
st.sidebar.markdown("---")
st.sidebar.info(
    """
    **Project Overview:**
    - Deep Learning Classification Model
    - Identifies whether an image contains a **car** or **motorcycle**
    - Trained using 3 different architectures
    
    **Models Available:**
    1. CNN Baseline
    2. MobileNetV2 (Transfer Learning)
    3. ResNet50 (Transfer Learning)
    """
)
st.sidebar.markdown("---")

# ============= MODEL LOADING & CACHING =============
@st.cache_resource
def load_models():
    """Load all trained models"""
    models = {}
    model_paths = {
        'CNN Baseline': 'cnn_baseline_best_model.h5',
        'MobileNetV2': 'mobilenetv2_best_model.h5',
        'ResNet50': 'resnet50_best_model.h5'
    }
    
    Available_models = []
    
    for model_name, model_path in model_paths.items():
        if os.path.exists(model_path):
            try:
                models[model_name] = tf.keras.models.load_model(model_path)
                Available_models.append(model_name)
            except Exception as e:
                st.warning(f"Could not load {model_name}: {str(e)}")
        else:
            st.warning(f"⚠️ Model file not found: {model_path}")
    
    if not Available_models:
        st.error(
            """
            ❌ No models found! 
            
            **Setup Instructions:**
            1. Download the trained models from Kaggle notebook
            2. Place `.h5` files in the same directory as this app:
               - `cnn_baseline_best_model.h5`
               - `mobilenetv2_best_model.h5`
               - `resnet50_best_model.h5`
            3. Restart the Streamlit app
            """
        )
    
    return models, Available_models

# ============= MAIN APPLICATION =============
def main():
    st.title("🚗🏍️ Car vs Motorcycle Classifier")
    st.markdown("**Automatic image classification using Deep Learning**")
    st.markdown("---")
    
    # Load models
    models, available_models = load_models()
    
    if not available_models:
        st.error("Please follow the setup instructions in the sidebar.")
        return
    
    # Two-column layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📤 Upload Image")
        
        # Model selection
        selected_model = st.selectbox(
            "Select Model to Use:",
            available_models,
            index=0
        )
        
        # Image upload
        uploaded_file = st.file_uploader(
            "Choose an image (JPG, PNG, WebP, HEIF):",
            type=["jpg", "jpeg", "png", "webp", "heic", "heif"]
        )
        
        if uploaded_file is not None:
            # Display uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            # Show image info
            st.caption(f"Image size: {image.size}")
    
    with col2:
        st.subheader("🔍 Prediction Results")
        
        if uploaded_file is not None:
            # Prepare image for model
            try:
                # Convert and resize image
                if image.mode != 'RGB':
                    image = image.convert('RGB')
                
                image_resized = image.resize((224, 224))
                image_array = img_to_array(image_resized)
                image_array = np.expand_dims(image_array, axis=0)
                image_array = image_array / 255.0  # Normalize
                
                # Make prediction with selected model
                model = models[selected_model]
                prediction = model.predict(image_array, verbose=0)
                confidence = float(prediction[0][0])
                
                # Determine class
                class_label = "🏍️ Motorcycle" if confidence > 0.5 else "🚗 Car"
                confidence_pct = (confidence * 100) if confidence > 0.5 else ((1 - confidence) * 100)
                
                # Display results with styling
                st.markdown(f"<h2 style='text-align: center; color: #2E86AB;'>{class_label}</h2>", unsafe_allow_html=True)
                
                # Progress bar for confidence
                st.markdown(f"**Confidence Score:** {confidence_pct:.2f}%")
                st.progress(confidence_pct / 100)
                
                # Additional metrics
                st.metric("Raw Model Output", f"{confidence:.4f}")
                st.metric("Threshold", "0.5000")
                
                # Detailed explanation
                with st.expander("📊 Detailed Analysis"):
                    col_a, col_b = st.columns(2)
                    
                    with col_a:
                        st.write("**Model Used:**", selected_model)
                        st.write("**Input Size:**", (224, 224))
                        st.write("**Output Type:**", "Binary Classification")
                    
                    with col_b:
                        motorcycle_conf = confidence * 100
                        car_conf = (1 - confidence) * 100
                        st.write(f"**Motorcycle Confidence:** {motorcycle_conf:.2f}%")
                        st.write(f"**Car Confidence:** {car_conf:.2f}%")
                
            except Exception as e:
                st.error(f"❌ Error processing image: {str(e)}")
        else:
            st.info("👆 Upload an image to see predictions")
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: gray; font-size: 0.8rem;'>
        <p>📚 Project: Car vs Motorcycle Image Classification | 🎓 Deep Learning UAS</p>
        <p>Models: CNN Baseline | MobileNetV2 | ResNet50</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
