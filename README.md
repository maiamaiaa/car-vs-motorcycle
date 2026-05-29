# Car vs Motorcycle Image Classification

Proyek deep learning untuk klasifikasi otomatis antara **mobil (car)** dan **motor (motorcycle)** menggunakan tiga arsitektur neural network yang berbeda.

## 📋 Daftar Isi

- [Deskripsi Project](#deskripsi-project)
- [Fitur Utama](#fitur-utama)
- [Requirements](#requirements)
- [Struktur Project](#struktur-project)
- [Cara Menggunakan](#cara-menggunakan)
- [Metodologi](#metodologi)
- [Model & Hasil](#model--hasil)
- [Tim Pengembang](#tim-pengembang)

## 📝 Deskripsi Project

Notebook ini mengimplementasikan pipeline lengkap untuk **image classification** dengan fokus pada:
- Download dataset dari Google Drive
- Preprocessing dan standardisasi format gambar (HEIC, HEIF, PNG, JPG, WebP)
- Data augmentation untuk menambah variabilitas dataset
- Stratified splitting (70% training, 15% validation, 15% testing)
- Pelatihan & evaluasi 3 model deep learning berbeda

**Tujuan**: Membangun classifier yang akurat untuk membedakan antara mobil dan motor dengan 3 pendekatan berbeda.

## ✨ Fitur Utama

### 1. **Data Preprocessing Komprehensif**
- ✅ Download otomatis dari Google Drive menggunakan `gdown`
- ✅ Ekstraksi file ZIP
- ✅ Konversi format gambar (HEIC → JPG)
- ✅ Resize & normalisasi
- ✅ Handling multiple image formats

### 2. **Data Augmentation**
- **Offline Augmentation**: Generate augmentasi fisik ke folder → meningkatkan dataset per kelas menjadi 600 gambar
  - Random rotation (0-25°)
  - Width/height shift (±15%)
  - Zoom (±20%)
  - Horizontal flip
  - Brightness adjustment (0.7-1.3x)

- **Online Augmentation**: Real-time augmentation selama training

### 3. **Stratified Data Splitting**
Pembagian data yang seimbang:
```
Total Dataset → 70% Training | 15% Validation | 15% Testing
Stratified berdasarkan class label untuk menjaga balance
```

### 4. **Tiga Arsitektur Model**

#### Model 1: **CNN Baseline**
- Dibangun dari nol (scratch)
- 3 Conv2D layers + MaxPooling
- 2 Dense layers dengan Dropout
- Cocok untuk pembelajaran dasar

```python
Conv2D(32) → Conv2D(64) → Conv2D(128) → Dense(256) → Dense(1)
```

#### Model 2: **MobileNetV2** (Transfer Learning)
- Feature extraction + Fine-tuning (2 tahap)
- Pre-trained on ImageNet
- Lightweight & efficient
- Cocok untuk deployment

#### Model 3: **ResNet50** (Transfer Learning)
- Feature extraction + Fine-tuning (2 tahap)
- Pre-trained on ImageNet
- Deep architecture untuk akurasi tinggi
- Layer-specific trainable strategy

### 5. **Training dengan Callbacks**
- **EarlyStopping**: Henti training jika val_loss tidak membaik selama 5 epoch
- **ModelCheckpoint**: Simpan model terbaik (berdasarkan val_loss)

### 6. **Visualisasi & Evaluasi**
- Kurva training history (accuracy & loss)
- Comparison sebelum vs sesudah augmentasi
- Sample batch dari dataset
- Evaluasi pada test set

## 📦 Requirements

```
python >= 3.8
tensorflow >= 2.10
keras >= 2.10
pillow >= 9.0
pillow-heif >= 0.0.1
gdown >= 4.0
split-folders >= 0.5.1
scikit-learn >= 1.0
numpy >= 1.21
matplotlib >= 3.5
```

### Instalasi Dependencies

```bash
pip install -q split-folders gdown pillow-heif tensorflow scikit-learn
```

## 📂 Struktur Project

```
projectUAS/
├── car-vs-motorcycle.ipynb      # Main notebook
├── README.md                     # This file
├── projectUAS.drawio            # Architecture diagram
├── mobil1.jpg, mobil2.jpg, ...  # Contoh gambar (jika tersimpan lokal)
└── motor1.jpg, motor2.jpg, ...  # Contoh gambar (jika tersimpan lokal)
```

### Data Structure (selama training)
```
/dataset_raw/                    # Raw dataset (hasil ekstraksi)
├── mobil/
└── motor/

/gabungan/                       # Combined + augmented
├── mobil1.jpg
├── mobil2.jpg
├── ... (hingga 600 per kelas)
├── motor1.jpg
└── ...

/dataset_split/                  # Stratified split
├── train/
│   ├── mobil/
│   └── motor/
├── val/
│   ├── mobil/
│   └── motor/
└── test/
    ├── mobil/
    └── motor/
```

## 🚀 Cara Menggunakan

### 1. **Persiapan**

Clone repository dan masuk ke folder project:
```bash
git clone https://github.com/yourusername/car-vs-motorcycle.git
cd car-vs-motorcycle
```

### 2. **Menjalankan Notebook**

**Option A: Jupyter Notebook (Local)**
```bash
jupyter notebook car-vs-motorcycle.ipynb
```

**Option B: Google Colab**
1. Buka [Google Colab](https://colab.research.google.com/)
2. Upload atau import notebook dari GitHub
3. Jalankan cell secara berurutan

**Option C: Kaggle**
1. Upload ke Kaggle
2. Jalankan dengan akses sumber daya GPU/TPU

### 3. **Eksekusi Step-by-Step**

Jalankan cell notebook dalam urutan:
1. **Cell 1**: Download & ekstrak dataset dari Google Drive
2. **Cell 2**: Standardisasi format gambar (HEIC → JPG)
3. **Cell 3**: Physical data augmentation (offline)
4. **Cell 4**: Stratified data splitting
5. **Cell 5-6**: Data loading & visualization
6. **Cell 7-9**: Model definition
7. **Cell 10**: Training CNN Baseline
8. **Cell 11**: Training MobileNetV2
9. **Cell 12**: Training ResNet50
10. **Cell 13+**: Visualization & evaluation

## 📊 Metodologi

### Data Collection & Preprocessing
1. **Source**: Images dari Google Drive (file_id: 1VHA-PIYJdG0wGfNRYIfTwQSpvaEhysrT)
2. **Format Standardization**: Semua gambar dikonversi ke JPG dengan resolution 224×224 px
3. **Class Balance**: Target 600 gambar per kelas setelah augmentasi

### Data Augmentation Strategy
- **Physical Augmentation (Offline)**: Generate variasi baru dan simpan ke disk
- **Online Augmentation**: Rescaling (1/255) selama training
- **Benefit**: Lek network mengatasi underfitting dan meningkatkan generalisasi

### Training Configuration

| AspectAspect | Value |
|---|---|
| Input Size | 224×224 px |
| Batch Size | 32 |
| Optimizer | Adam (LR: 0.001) |
| Loss Function | Binary Crossentropy |
| Epochs | 30 (Baseline), 30 (Transfer Learning) |
| Early Stopping | Yes (patience=5) |

### Evaluation Metrics
- **Accuracy**: Keakuratan prediksi klasifikasi
- **Loss**: Binary crossentropy loss
- **Validation Curves**: Monitoring overfitting

## 🎯 Model & Hasil

### Model Comparison

| Model | Type | Parameters | Training Time | Best Val Accuracy |
|---|---|---|---|---|
| CNN Baseline | From Scratch | ~1.3M | ~15 min | - |
| MobileNetV2 | Transfer Learning | ~2.3M | ~20 min | - |
| ResNet50 | Transfer Learning | ~23.6M | ~30 min | - |

**Note**: Hasil akurasi bergantung pada:
- Kualitas dataset
- Hardware (GPU/CPU)
- Hyperparameter tuning

### Saved Models
Setiap model terbaik disimpan sebagai `.h5` file:
```
cnn_baseline_best_model.h5
mobilenetv2_best_model.h5
resnet50_best_model.h5
```

## 📈 Expected Outputs

Notebook akan generate:
- ✅ Training history plots (accuracy & loss curves)
- ✅ Sample visualization (sebelum/sesudah augmentasi)
- ✅ Dataset statistics
- ✅ Model weights (.h5 files)
- ✅ Prediction results pada test set

## 🔧 Tips & Tricks

### Optimasi Performance

1. **GPU Acceleration**
   - Gunakan Google Colab / Kaggle untuk GPU support
   - Tensorflow otomatis mendeteksi & menggunakan GPU

2. **Memory Management**
   - Reduce batch size jika out of memory
   - Gunakan `tf.data` untuk optimasi pipeline

3. **Hyperparameter Tuning**
   - Adjust learning rate
   - Modify augmentation intensity
   - Change dropout rate

### Common Issues

| Issue | Solution |
|---|---|
| Dataset tidak download | Pastikan file_id masih valid & akses Google Drive aktif |
| Out of memory | Reduce batch_size atau gunakan GPU |
| Model not converging | Increase learning rate atau check data quality |
| Augmentation terlalu ekstrim | Adjust augmentation parameters |

## 📚 Referensi

- [TensorFlow Documentation](https://www.tensorflow.org/api_docs)
- [Keras Preprocessing](https://keras.io/api/preprocessing/image/)
- [Transfer Learning Guide](https://www.tensorflow.org/tutorials/images/transfer_learning)
- [MobileNetV2 Paper](https://arxiv.org/abs/1801.04381)
- [ResNet50 Paper](https://arxiv.org/abs/1512.03385)

## 👥 Tim Pengembang

- **Nama**: [Eugenia Grasela Maia]
- **Universitas**: [Semester 6, Deep Learning Course]
- **Kontak**: [eugenia@email.com]

## 📄 Lisensi

Proyek ini menggunakan lisensi **MIT License**.

## 🙏 Acknowledgments

- Dataset diperoleh dari sumber private (Google Drive)
- Pre-trained models dari ImageNet (TensorFlow/Keras)
- Inspirasi dari berbagai jupyter notebooks open-source

---

**Last Updated**: May 2026  
**Status**: ✅ Complete & Ready for Submission
