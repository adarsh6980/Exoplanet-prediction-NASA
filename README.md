# AstroMind: AI-Powered Exoplanet Discovery 🌌

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org)
[![NASA Challenge](https://img.shields.io/badge/NASA-Space%20Apps%20Challenge%202025-red.svg)](https://www.spaceappschallenge.org/)

An AI/ML platform that automates exoplanet discovery using NASA's datasets. Built for the **2025 NASA Space Apps Challenge**, it classifies celestial objects as exoplanets, candidates, or false positives with **81.6% accuracy** and **90.1% ROC-AUC**.

## 🎯 Challenge: "A World Away: Hunting for Exoplanets with AI"

Our solution creates an AI model trained on NASA's Kepler Object of Interest (KOI) dataset to automatically analyze astronomical data and identify potential exoplanets.

## ✨ Key Features

- **High Accuracy**: 81.6% accuracy with Random Forest classifier
- **Dual Input**: Single exoplanet analysis or batch CSV processing  
- **Real-time Predictions**: Instant classification with confidence scores
- **Interactive Visualizations**: Scatter plots, histograms, and data insights
- **NASA Data Integration**: Direct download from NASA KOI dataset

## 🚀 Quick Start

### Installation
```
git clone https://github.com/yourusername/astromind-exoplanet-discovery.git
cd astromind-exoplanet-discovery
pip install pandas numpy scikit-learn matplotlib joblib gdown imblearn
```

### Train Model
```
python exoplanet_classifier.py
```

### Make Predictions
```
# Single prediction
pred, prob = predict_single_row(365.25, 6.5, 84.0, 1.0, 1.0, 288)
print(f"Prediction: {'Exoplanet' if pred == 1 else 'False Positive'} ({prob*100:.1f}%)")

# Batch prediction from CSV
predict_from_csv('your_data.csv', rf, scaler)
```

## 🛠 Technical Overview

**Algorithm**: Random Forest Classifier (200 estimators)  
**Features**: 6 key astronomical parameters
- Orbital period, transit duration, transit depth
- Planet radius, stellar radius, equilibrium temperature

**Data Processing**:
- SMOTE balancing for class imbalance
- StandardScaler normalization
- Missing value handling

**Performance**:
- Accuracy: 81.6% | ROC-AUC: 90.1%
- Precision: 84% (FP), 80% (Confirmed)
- Recall: 78% (FP), 85% (Confirmed)

## 📊 Dataset

**Source**: NASA Kepler Objects of Interest  
**Size**: 9,564 objects (after preprocessing)  
**Classes**: Confirmed (1), Candidate (1), False Positive (0)  
**Split**: 80/20 train/test with stratification

## 👥 Team: Indovate AI

**Sai Tej** • **Kompally** • **Adarsh** • **Ramakrishna** • **Akanksha** • **Jagannath**

## 🏆 NASA Space Apps Challenge 2025

**Category**: Astrophysics Division | **Difficulty**: Advanced  
**Subjects**: AI/ML, Data Analysis, Space Exploration

## 🔗 Resources

- [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/)
- [Project Demo](your-demo-link)
- [Challenge Details](https://www.spaceappschallenge.org/)

---

*"Automating exoplanet discovery through intelligent data analysis"* 🚀
```
