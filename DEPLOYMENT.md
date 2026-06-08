# 🚀 Streamlit Deployment Guide

## Step-by-Step Deployment Instructions

### Step 1: Export Models from Kaggle

Jalankan notebook di Kaggle dan unduh 3 file model yang telah dilatih:
- `cnn_baseline_best_model.h5`
- `mobilenetv2_best_model.h5`
- `resnet50_best_model.h5`

Tempatkan file-file ini di folder yang sama dengan `app.py`.

### Step 2: Prepare Your GitHub Repository

1. **Initialize git repository:**
   ```bash
   cd projectUAS
   git init
   git add .
   git commit -m "Initial commit: Car vs Motorcycle classifier"
   ```

2. **Create `.gitignore` file** (untuk tidak meng-upload file besar):
   ```
   *.h5
   *.pickle
   __pycache__/
   .ipynb_checkpoints/
   *.pyc
   .DS_Store
   venv/
   env/
   ```

3. **Push to GitHub:**
   ```bash
   git remote add origin https://github.com/yourusername/car-vs-motorcycle.git
   git branch -M main
   git push -u origin main
   ```

### Step 3: Deploy to Streamlit Cloud

#### Option A: Automatic Deployment (Recommended)

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click **"New app"**
3. Select your GitHub repository
4. Configure:
   - **Repository**: `yourusername/car-vs-motorcycle`
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Click **"Deploy"**

#### Option B: Manual Setup (if models too large)

If model files exceed GitHub size limits:

1. **Compress models locally:**
   ```bash
   zip models.zip *.h5
   ```

2. **Store in cloud:**
   - Upload to Google Drive or similar cloud storage
   - Create a script to download them on app startup

3. **Update app.py to download models automatically:**
   ```python
   import gdown
   
   # Add this to load_models() function
   file_id = 'your_google_drive_file_id'
   gdown.download(f'https://drive.google.com/uc?id={file_id}', 'models.zip')
   # Extract zip file
   ```

### Step 4: Configure Streamlit Cloud Secrets (Optional)

If you need to store sensitive information:

1. Go to app settings in Streamlit Cloud
2. Add **Secrets** in format:
   ```
   [general]
   your_key = "your_value"
   ```

### Step 5: Test Locally First

```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

Then open: http://localhost:8501

---

## 📦 Project Structure

```
projectUAS/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── config.toml                # Streamlit configuration
├── .gitignore                      # Git ignore file
├── car-vs-motorcycle.ipynb         # Original Jupyter notebook
├── README.md                       # Project overview
├── projectUAS.drawio               # Project diagram
│
# Models (download from Kaggle):
├── cnn_baseline_best_model.h5
├── mobilenetv2_best_model.h5
└── resnet50_best_model.h5
```

---

## 🔧 Troubleshooting

### ❌ "Models not found" Error

**Solution:** Make sure `.h5` files are in the same directory as `app.py`

### ❌ "Module not found" Error

**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### ❌ App is too slow on Streamlit Cloud

**Solution:** 
- Use a smaller model or compress it
- Implement caching for model loading (already done with `@st.cache_resource`)
- Optimize image preprocessing

### ❌ Model file size too large for GitHub

**Solution:**
- Use Git LFS (Large File Storage)
- Or store models in cloud storage and download on app startup

---

## 📊 Performance Tips

1. **Model Loading**: Uses `@st.cache_resource` to load models only once
2. **Image Caching**: Images are cached to avoid reprocessing
3. **Batch Predictions**: App processes one image at a time for speed

---

## 🌐 Accessing Your App

After deployment, your app will be available at:
```
https://share.streamlit.io/yourusername/car-vs-motorcycle/main/app.py
```

---

## 📝 Customization

### Change App Title:
Edit in `app.py`:
```python
st.set_page_config(page_title="Your Custom Title")
```

### Change Model Selection:
Modify model paths in `load_models()` function

### Add More Features:
- Batch upload multiple images
- Show model comparison
- Add confidence threshold slider
- Export predictions as CSV

---

## ✅ Next Steps

1. ✅ Export models from Kaggle
2. ✅ Push to GitHub
3. ✅ Deploy to Streamlit Cloud
4. ✅ Test with sample images
5. ✅ Share with others!

---

**Happy Deploying! 🎉**
