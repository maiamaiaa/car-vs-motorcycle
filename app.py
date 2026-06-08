import streamlit as st
import numpy as np
from PIL import Image
import os
import pickle
import io

# TensorFlow is lazy-loaded only when needed to avoid version conflicts
# tensorflow commented out - will be imported dynamically when model is loaded

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
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        padding: 1rem;
        border-radius: 0.5rem;
        color: #155724;
    }
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        padding: 1rem;
        border-radius: 0.5rem;
        color: #721c24;
    }
    .info-box {
        background-color: #e2e3e5;
        border: 1px solid #d6d8db;
        padding: 1rem;
        border-radius: 0.5rem;
        color: #383d41;
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
    """Load all trained models (Downloads from Google Drive if missing)"""
    models = {}
    model_paths = {
        'CNN Baseline': 'cnn_baseline_best_model.h5'
    }
    
    # KODE ID GOOGLE DRIVE MILIK EUGENIA
    DRIVE_FILE_IDS = {
        'CNN Baseline': '1ShkbPyQnoaSiAVs7eW3DkJNHw_x-iPto'
    }
    
    available_models = []
    missing_models = []
    
    # Import gdown untuk mengunduh dari Google Drive secara otomatis
    try:
        import gdown
    except ImportError:
        os.system("pip install gdown")
        import gdown

    for model_name, model_path in model_paths.items():
        # Jika file .h5 belum ada di server Streamlit, unduh otomatis menggunakan gdown
        if not os.path.exists(model_path) and model_name in DRIVE_FILE_IDS:
            with st.spinner(f"Sedang mengunduh model {model_name} dari Google Drive... (Harap tunggu sebentar karena ukuran file cukup besar)"):
                file_id = DRIVE_FILE_IDS[model_name]
                url = f'https://drive.google.com/uc?id={file_id}'
                gdown.download(url, model_path, quiet=False)

        # Setelah proses unduh selesai, muat arsitekturnya ke memori
        if os.path.exists(model_path):
            try:
                import tensorflow as tf
                # Muat model dengan compile=False agar terhindar dari ValueError
                models[model_name] = tf.keras.models.load_model(model_path, compile=False)
                available_models.append(model_name)
            except Exception as e:
                missing_models.append((model_name, str(e)))
        else:
            missing_models.append((model_name, f"Gagal mengunduh berkas dari Google Drive"))
    
    return models, available_models, missing_models
# ============= MAIN APPLICATION =============
def main():
    st.title("🚗🏍️ Car vs Motorcycle Classifier")
    st.markdown("**Automatic image classification using Deep Learning**")
    st.markdown("---")
    
    # Load models
    models, available_models, missing_models = load_models()
    
    # Show setup status
    if missing_models:
        st.markdown("""
        <div class="error-box">
        <h3>⚠️ Setup Required / Missing Models</h3>
        <p>Beberapa berkas model .h5 tidak ditemukan di direktori lokal atau gagal dimuat.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if available_models:
            st.success(f"✅ Model yang berhasil dimuat: {', '.join(available_models)}")
        
        st.info("""
        **Untuk menjalankan aplikasi ini secara lokal atau cloud:**
        
        1. Pastikan nama file model di folder proyek Anda cocok dengan definisi berikut:
           - `cnn_baseline_best_model.h5`
           - `mobilenetv2_best_model.h5`
           - `resnet50_best_model.h5`
        
        2. Jika Anda memindahkan model dari output Kaggle, lakukan pengubahan nama file (*rename*) terlebih dahulu agar sesuai dengan daftar di atas.
        
        3. Struktur file direktori yang diharapkan:
           ```
           deploy-folder/
           ├── app.py
           ├── cnn_baseline_best_model.h5
           ├── mobilenetv2_best_model.h5
           └── resnet50_best_model.h5
           ```
        """)
        
        # Jika setidaknya ada satu model yang berhasil dimuat, kita izinkan aplikasi tetap berjalan
        if not available_models:
            return
    
    # Show success header if all models are present
    if not missing_models:
        st.markdown("""
        <div class="success-box">
        <h3>✅ All Models Loaded Successfully!</h3>
        </div>
        """, unsafe_allow_html=True)
    
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
                # Lazy-load TensorFlow utilities when needed
                from tensorflow.keras.preprocessing.image import img_to_array
                
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
                
                # Determine class based on 0.5 threshold
                # (Kaggle class_indices: 0 untuk 'mobil', 1 untuk 'motor')
                class_label = "🏍️ Motorcycle" if confidence > 0.5 else "🚗 Car"
                confidence_pct = (confidence * 100) if confidence > 0.5 else ((1 - confidence) * 100)
                
                # Display results with styling
                st.markdown(f"<h2 style='text-align: center; color: #2E86AB;'>{class_label}</h2>", unsafe_allow_html=True)
                
                # Progress bar for confidence
                st.markdown(f"**Confidence Score:** {confidence_pct:.2f}%")
                st.progress(confidence_pct / 100)
                
                # Additional metrics
                st.metric("Raw Model Output (Sigmoid Prob)", f"{confidence:.4f}")
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
        <p>📚 Project: Car vs Motorcycle Image Classification | 🎓 Deep Learning UTS Proyek</p>
        <p>Nama: Eugenia Grasela Maia | NPM: 2355061008 | Universitas Lampung</p>
        <p>Sandbox: CNN Baseline | MobileNetV2 | ResNet50</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
