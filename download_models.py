"""
Download script for pre-trained models.

Due to GitHub's 100MB file size limit, models are not stored in the repository.
This script provides options to obtain the models for local deployment.
"""

import os
import sys
from pathlib import Path

def check_models_exist():
    """Check which models are already present"""
    models = {
        'CNN Baseline': 'cnn_baseline_best_model.h5',
        'MobileNetV2': 'mobilenetv2_best_model.h5',
        'ResNet50': 'resnet50_best_model.h5'
    }
    
    print("Checking for trained models...\n")
    missing = []
    found = []
    
    for name, path in models.items():
        if os.path.exists(path):
            size_mb = os.path.getsize(path) / (1024 * 1024)
            print(f"✅ {name}: FOUND ({size_mb:.1f} MB)")
            found.append(name)
        else:
            print(f"❌ {name}: MISSING")
            missing.append(name)
    
    return found, missing

def show_instructions():
    """Show setup instructions"""
    print("\n" + "="*60)
    print("HOW TO GET THE MODELS")
    print("="*60 + "\n")
    
    print("Option 1: Generate models locally (RECOMMENDED)")
    print("-" * 50)
    print("""
1. Ensure you have all dependencies installed:
   pip install -r requirements.txt

2. Run the Jupyter notebook:
   jupyter notebook car-vs-motorcycle.ipynb

3. Execute all cells to train and save models
   - CNN Baseline will be saved as: cnn_baseline_best_model.h5
   - ResNet50 will be saved as: resnet50_best_model.h5
   - MobileNetV2 will be saved as: mobilenetv2_best_model.h5

4. Models will be automatically saved in the project directory
""")
    
    print("\nOption 2: Download from cloud storage")
    print("-" * 50)
    print("""
Contact the project maintainer to obtain pre-trained models,
or upload your own trained models to a cloud storage service:
- Google Drive
- Hugging Face Model Hub
- AWS S3
- Azure Blob Storage
""")
    
    print("\nOption 3: Use Streamlit from cloud with restricted models")
    print("-" * 50)
    print("""
Deploy to Streamlit Cloud with the models that are available.
The app will automatically detect available models and display them.
""")

if __name__ == "__main__":
    print("\n🔍 MODEL AVAILABILITY CHECKER\n")
    
    found, missing = check_models_exist()
    
    if found and not missing:
        print(f"\n✅ SUCCESS: All {len(found)} models are ready!")
        print("\nYou can now run the app with:")
        print("   streamlit run app.py")
    elif found:
        print(f"\n⚠️  PARTIAL: {len(found)}/{len(found)+len(missing)} models available")
        print("The app will work with available models.")
        print("\nYou can run the app with:")
        print("   streamlit run app.py")
    else:
        print(f"\n❌ NO MODELS FOUND: All {len(missing)} models are missing")
    
    show_instructions()
    
    print("\n" + "="*60)
    print("For more information, see DEPLOYMENT.md")
    print("="*60 + "\n")
