import streamlit as st
import pickle
import numpy as np



def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()
regressor = data['model']
le_country = data['le_country']
le_education = data['le_education']



def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    countries = (
        "United States",  
        "India",             
        "United Kingdom",     
        "Germany",           
        "Canada",            
        "Brazil",              
        "France",               
        "Spain",               
        "Australia",           
        "Netherlands",        
        "Poland",            
        "Italy",            
        "Russian Federation",
        "Sweden",
         )

    education = (
        "Less than a Bachelor degree",
        "Bachelor's degree", 
        "Master's degree", 
        "Post grad",
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)

    experience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    if ok:
        X_new = np.array([[country, education, experience]])
        X_new[:, 0] = le_country.transform(X_new[:, 0])
        X_new[:, 1] = le_education.transform(X_new[:, 1])
        X_new = X_new.astype(float)

        salary = regressor.predict(X_new)
        st.subheader(f"The estimated yearly salary is ${salary[0]:.2f}")

