# AstroMind: AI-Powered Exoplanet Discovery 🌌

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)  
[![Angular](https://img.shields.io/badge/Angular-15+-red.svg)](https://angular.io)  
[![Firebase](https://img.shields.io/badge/Firebase-Firestore-orange.svg)](https://firebase.google.com)  
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-green.svg)](https://scikit-learn.org)  
[![NASA Challenge](https://img.shields.io/badge/NASA-Space%20Apps%20Challenge%202025-blue.svg)](https://www.spaceappschallenge.org/)

An AI/ML platform that automates exoplanet discovery using NASA's datasets. Built for the **2025 NASA Space Apps Challenge**, it classifies celestial objects as exoplanets, candidates, or false positives with **81.6% accuracy** and **90.1% ROC-AUC**.

## 🎯 Challenge: "A World Away: Hunting for Exoplanets with AI"

Our solution creates an intelligent AI model trained on NASA's Kepler Object of Interest (KOI) dataset to automatically analyze astronomical data and identify potential exoplanets. The platform combines machine learning with modern web technologies to provide an accessible interface for researchers and space enthusiasts.

## ✨ Key Features

- **🎯 High Accuracy**: 81.6% accuracy with Random Forest classifier and 90.1% ROC-AUC  
- **📊 Dual Input Options**: Single exoplanet analysis or batch CSV processing  
- **⚡ Real-time Predictions**: Instant classification with confidence scores  
- **📈 Interactive Visualizations**: Scatter plots, histograms, and data insights  
- **🌐 Web Interface**: User-friendly Angular frontend for seamless interaction  
- **☁️ Cloud Integration**: Firebase Firestore for data storage and management  
- **🚀 NASA Data Integration**: Direct integration with NASA KOI dataset  

## 🏗️ System Architecture

### High-Level Architecture
![WhatsApp Image 2025-10-05 at 6 18 09 p m](https://github.com/user-attachments/assets/19266166-da93-49e0-91b3-715920da2a11)

### Technology Stack

| Layer         | Technology           | Purpose                                      |
|---------------|----------------------|----------------------------------------------|
| **Frontend**  | Angular 15+          | Interactive web interface, data visualization |
| **Database**  | Firebase Firestore   | Real-time data storage, user sessions         |
| **Backend**   | Python/Flask         | ML model serving, data processing             |
| **ML Framework** | scikit-learn      | Random Forest classifier, data preprocessing  |
| **Data Processing** | Pandas, NumPy | Data manipulation, feature engineering        |
| **Visualization** | Matplotlib, Chart.js | Plots, charts, model insights             |

## 🔄 Workflow

<img width="291" height="600" alt="Screenshot 2025-10-04 at 11 05 59 a m" src="https://github.com/user-attachments/assets/2d23f0b3-249a-4e25-b04a-3fd8a19d5cea" />


### Detailed Process Flow
1. **Data Upload**: Users upload CSV files through Angular interface  
2. **Validation**: Frontend validates data format and required columns  
3. **Storage**: Firebase Firestore securely stores uploaded data  
4. **Processing**: ML backend retrieves data, applies preprocessing pipeline  
5. **Classification**: Random Forest model generates predictions with confidence scores  
6. **Storage**: Results saved back to Firestore with unique session IDs  
7. **Visualization**: Angular dashboard displays results with interactive charts  
8. **Export**: Users can download processed results and visualizations  

## 🚀 Quick Start

### Prerequisites
- Node.js 16+ and npm  
- Python 3.8+  
- Firebase project setup  
- Git  

### Installation

#### 1. Clone Repository

Navigate to backend directory
cd backend
Install Python dependencies
pip install pandas numpy scikit-learn matplotlib joblib gdown imblearn flask firebase-admin
Train the model
python exoplanet_classifier.py
Start Flask server
python app.py



## 📊 Dataset Details

**Source**: NASA Exoplanet Archive - Kepler Objects of Interest  
**Original Size**: 10,000+ astronomical objects  
**Processed Size**: 9,564 objects (after cleaning and preprocessing)  
**Classes**:  
- Confirmed Exoplanets (1): 4,234 objects  
- False Positives (0): 5,330 objects  
**Train/Test Split**: 80/20 with stratified sampling  

### Data Preprocessing Pipeline
1. **Missing Value Handling**: Imputation using median values  
2. **Outlier Detection**: IQR-based outlier removal  
3. **Feature Scaling**: StandardScaler normalization  
4. **Class Balancing**: SMOTE oversampling for minority class  
5. **Feature Selection**: Correlation analysis and importance ranking  

## 👥 Team: Indovate AI

| Name                    |
|-------------------------|
| **Adarsh Ramakrishna**  | 
| **Akanksha Jagannath**  | 
| **Martin**              | 
| **Harshitha**           | 
| **Sai Tej Kompally**    | 
| **Abhinav Thakur**      | 

## 🏆 NASA Space Apps Challenge 2025

**Challenge**: A World Away: Hunting for Exoplanets with AI  
**Category**: Astrophysics Division  
**Difficulty**: Advanced  
**Subjects**: AI/ML, Data Analysis, Space Exploration, Web Development  

### Project Goals
- Automate exoplanet discovery process  
- Make astronomical data analysis accessible  
- Provide real-time classification capabilities  
- Create educational platform for space exploration  

## 🔗 Resources & Links

- 📚 NASA Exoplanet Archive: https://exoplanetarchive.ipac.caltech.edu/  
- 🎥 Project Demo Video: your-demo-link  
- 📖 Challenge Details: https://www.spaceappschallenge.org/  
- 🔬 Research Paper: your-paper-link  
- 🌐 Live Application: your-app-link  

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository (`git checkout -b feature/AmazingFeature`)  
2. Commit your changes (`git commit -m 'Add some AmazingFeature'`)  
3. Push to the branch (`git push origin feature/AmazingFeature`)  
4. Open a Pull Request  


*"Automating exoplanet discovery through intelligent data analysis and modern web technologies"* 🚀

**Built with ❤️ for NASA Space Apps Challenge 2025**

