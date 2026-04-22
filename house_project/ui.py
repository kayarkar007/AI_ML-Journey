import streamlit as st
import requests

st.title("🏠 House Price Predictor")

qual = st.number_input("Overall Quality", min_value=1, max_value=10)
area = st.number_input("Living Area (sq ft)")
garage = st.number_input("Garage Cars")
basement = st.number_input("Basement Area")
year = st.number_input("Year Built")
bath = st.number_input("Full Bathrooms")

if st.button("Predict Price"):

    data = {
        "OverallQual": qual,
        "GrLivArea": area,
        "GarageCars": garage,
        "TotalBsmtSF": basement,
        "YearBuilt": year,
        "FullBath": bath
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        result = response.json()

        st.success(f"Predicted Price: ₹ {round(result['Predicted Price'], 2)}")

    except:
        st.error("API not running ❌")