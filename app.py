import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the saved model and scaler
@st.cache_resource
def load_model():
    model = joblib.load('exoplanet_classifier.pkl')
    scaler = joblib.load('feature_scaler.pkl')
    return model, scaler

model, scaler = load_model()

# Streamlit app
st.title("🌟 Exoplanet Detection System")
st.write("Predict whether a Kepler Object of Interest (KOI) is an exoplanet")

# Sidebar for input method
st.sidebar.header("Choose Input Method")
input_method = st.sidebar.radio("", ["Manual Entry", "Upload CSV File"])

if input_method == "Manual Entry":
    st.header("Enter Planet Parameters")
    
    # Input fields for the 6 features you used
    koi_period = st.number_input("Orbital Period (days)", min_value=0.0, value=365.25)
    koi_duration = st.number_input("Transit Duration (hours)", min_value=0.0, value=6.5)
    koi_depth = st.number_input("Transit Depth (ppm)", min_value=0.0, value=500.0)
    koi_prad = st.number_input("Planetary Radius (Earth radii)", min_value=0.0, value=1.0)
    koi_srad = st.number_input("Stellar Radius (Solar radii)", min_value=0.0, value=1.0)
    koi_teq = st.number_input("Equilibrium Temperature (K)", min_value=0.0, value=288.0)
    
    if st.button("🔍 Predict Exoplanet"):
        # Prepare the input data
        features = np.array([[koi_period, koi_duration, koi_depth, koi_prad, koi_srad, koi_teq]])
        
        # Scale the features
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0]
        
        # Display results
        if prediction == 1:
            st.success("🪐 This is likely an EXOPLANET!")
            confidence = probability[1]
        else:
            st.error("❌ This is likely NOT an exoplanet")
            confidence = probability[0]
        
        st.write(f"**Confidence:** {confidence:.2%}")
        
        # Show probability breakdown
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Exoplanet Probability", f"{probability[1]:.2%}")
        with col2:
            st.metric("Not Exoplanet Probability", f"{probability[0]:.2%}")

elif input_method == "Upload CSV File":
    st.header("Upload Your Data File")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            # Read the uploaded file
            df = pd.read_csv(uploaded_file)
            st.write("**Uploaded Data Preview:**")
            st.dataframe(df.head())
            
            # Expected features (same as your model)
            expected_features = ['koi_period', 'koi_duration', 'koi_depth', 'koi_prad', 'koi_srad', 'koi_teq']
            
            # Check if all required columns exist
            if all(col in df.columns for col in expected_features):
                if st.button("🚀 Predict All"):
                    # Extract features
                    X = df[expected_features].values
                    
                    # Scale features
                    X_scaled = scaler.transform(X)
                    
                    # Make predictions
                    predictions = model.predict(X_scaled)
                    probabilities = model.predict_proba(X_scaled)
                    
                    # Add results to dataframe
                    df['Prediction'] = ['Exoplanet' if pred == 1 else 'Not Exoplanet' for pred in predictions]
                    df['Confidence'] = [prob.max() for prob in probabilities]
                    df['Exoplanet_Probability'] = [prob[1] for prob in probabilities]
                    
                    # Display results
                    st.write("**Prediction Results:**")
                    st.dataframe(df)
                    
                    # Summary statistics
                    exoplanet_count = sum(predictions)
                    total_count = len(predictions)
                    st.write(f"**Summary:** {exoplanet_count} potential exoplanets out of {total_count} objects ({exoplanet_count/total_count:.1%})")
                    
                    # Download results
                    csv = df.to_csv(index=False)
                    st.download_button("📥 Download Results", csv, "exoplanet_predictions.csv", "text/csv")
            else:
                st.error(f"Missing required columns. Expected: {expected_features}")
                
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")

# Add footer
st.markdown("---")
st.write("Built for NASA Space Apps Challenge 2025 🚀")

