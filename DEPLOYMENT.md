# 🚀 Streamlit Deployment Guide

## ⚠️ Important Note: Model File Sizes

The trained models are very large (200-300 MB each), which exceeds GitHub's 100MB file size limit. There are several ways to handle this:

- **For local deployment**: Models should be generated locally by running the notebook
- **For cloud deployment**: Use Git LFS, GitHub Releases, or download models at startup

---

## Local Deployment (RECOMMENDED)

### Step 1: Clone the Repository

```bash
git clone https://github.com/maiamaiaa/car-vs-motorcycle.git
cd car-vs-motorcycle
```

### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Generate Models

Run the Jupyter notebook to train and save models:

```bash
jupyter notebook car-vs-motorcycle.ipynb
```

Execute all cells. The models will be saved as:
- `cnn_baseline_best_model.h5`
- `resnet50_best_model.h5`
- `mobilenetv2_best_model.h5`

Or check available models:
```bash
python download_models.py
```

### Step 5: Run the App

```bash
streamlit run app.py
```

Open your browser to: **http://localhost:8501**

---

## Cloud Deployment to Streamlit Cloud

### Option A: With Available Models (Works Now)

1. **Check which models you have:**
   ```bash
   python download_models.py
   ```

2. **Push to GitHub:** (with available models only)
   ```bash
   git add app.py requirements.txt .gitignore download_models.py
   git commit -m "Update app with model file size handling"
   git push origin main
   ```

3. **Deploy to Streamlit Cloud:**
   - Go to https://streamlit.io/cloud
   - Click "New app"
   - Select your GitHub repository
   - Streamlit will run the app with available models

### Option B: Using Git LFS (Large File Storage)

For storing large `.h5` files in GitHub:

```bash
# Install Git LFS
brew install git-lfs  # macOS
# or sudo apt-get install git-lfs  # Ubuntu

# Initialize LFS
git lfs install

# Track model files
git lfs track "*.h5"
git add .gitattributes

# Add models to LFS
git add *.h5
git commit -m "Add trained models with Git LFS"
git push origin main
```

### Option C: Download Models at Runtime

Create `download_models.py` with cloud storage hooks to download models when app starts.

---

## 📦 Project Structure

```
car-vs-motorcycle/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── download_models.py              # Model availability checker
├── .streamlit/
│   └── config.toml                # Streamlit configuration
├── .gitignore                      # Git ignore file
├── car-vs-motorcycle.ipynb         # Training notebook
├── README.md                       # Project overview
├── DEPLOYMENT.md                   # This file
│
# Models (generate locally or provide separately):
├── cnn_baseline_best_model.h5
├── resnet50_best_model.h5
└── mobilenetv2_best_model.h5
```

---

## 🔧 Troubleshooting

### ❌ "Models not found" Error

**Cause**: Models haven't been trained or provided

**Solution**: 
- Run `python download_models.py` to check
- Or run the Jupyter notebook to generate models
- The app will still work with any available models

### ❌ "Module not found" Error

**Solution**: Install requirements
```bash
pip install -r requirements.txt
```

### ❌ Streamlit App Shows Setup Instructions

**Cause**: Models not deployed to Streamlit Cloud

**Solution**:
- Option 1: Use Git LFS to store models
- Option 2: Train locally and configure download
- Option 3: Deploy with available models

### ❌ Large File Size Rejected by GitHub

**Cause**: Individual `.h5` files exceed 100MB

**Solutions**:
- Use Git LFS (recommended)
- Split models into smaller pieces
- Store in cloud storage and download at runtime
- Compress with model quantization

---

## 📊 Model Specifications

| Model | Architecture | File Size | Training Time |
|-------|--------------|-----------|-----------------|
| CNN Baseline | Custom CNN (3 layers) | ~255 MB | ~5-10 min |
| ResNet50 | Transfer Learning | ~211 MB | ~15-30 min |
| MobileNetV2 | Transfer Learning (Mobile) | ~50-100 MB | ~10-20 min |

---

## 🚀 Quick Start Commands

**Local deployment:**
```bash
git clone https://github.com/maiamaiaa/car-vs-motorcycle.git
cd car-vs-motorcycle
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python download_models.py
streamlit run app.py
```

**Cloud deployment:**
```bash
# Assuming models already trained and committed
git add .
git commit -m "Deployment ready"
git push origin main
# Then configure via Streamlit Cloud dashboard
```


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
