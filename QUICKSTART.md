# 🚀 Quick Start Guide - Streamlit Deployment

## Langkah Cepat (5 Menit)

### 1️⃣ Persiapan di Kaggle
```
Jalankan notebook sampai tuntas → Download 3 file .h5:
- cnn_baseline_best_model.h5
- mobilenetv2_best_model.h5  
- resnet50_best_model.h5
```

### 2️⃣ Setup Folder Lokal
```bash
cd projectUAS

# Paste file .h5 ke folder ini
# Folder structure should be:
# projectUAS/
#  ├── app.py
#  ├── cnn_baseline_best_model.h5
#  ├── mobilenetv2_best_model.h5
#  ├── resnet50_best_model.h5
#  └── requirements.txt
```

### 3️⃣ Test Lokal
```bash
pip install -r requirements.txt
streamlit run app.py
```
**Buka:** http://localhost:8501

### 4️⃣ Push ke GitHub
```bash
git init
git add .
git commit -m "Initial: Car vs Motorcycle Classifier"
git remote add origin https://github.com/YOUR_USERNAME/car-vs-motorcycle.git
git push -u origin main
```

### 5️⃣ Deploy ke Streamlit Cloud
1. Go to https://streamlit.io/cloud
2. Click "New app"
3. Select your GitHub repository
4. Set main file as `app.py`
5. Click "Deploy"

✅ **Done!** Your app is live! 🎉

---

## 🎯 Model Comparison

| Model | Training Speed | Accuracy | Inference Speed |
|-------|--------------|----------|-----------------|
| CNN Baseline | ⚡⚡⚡ Fast | 🎯 Good | ⚡⚡⚡ Fastest |
| MobileNetV2 | ⚡⚡ Medium | 🎯🎯 Better | ⚡⚡ Fast |
| ResNet50 | ⚡ Slow | 🎯🎯🎯 Best | ⚡ Medium |

---

## 🔗 Useful Links

- **Streamlit Docs**: https://docs.streamlit.io/
- **Streamlit Cloud**: https://streamlit.io/cloud
- **GitHub**: https://github.com/

---

## 📞 Support

Jika ada error, baca `DEPLOYMENT.md` untuk troubleshooting lengkap.
