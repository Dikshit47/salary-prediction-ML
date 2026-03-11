
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Page Title

st.title("💼 Salary Prediction System")
st.write("Machine Learning Project using Regression")

# Load Dataset

data = pd.read_csv("Salary Data.csv")

st.subheader("Dataset Preview")
st.dataframe(data.head())

# Data Visualization

st.subheader("Data Visualization")

fig1, ax1 = plt.subplots()
sns.histplot(data['Salary'], kde=True, ax=ax1)
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
sns.scatterplot(x=data['Experience_Year'], y=data['Salary'], ax=ax2)
st.pyplot(fig2)

# User Input Section

st.subheader("Enter Employee Details")

age = st.number_input("Age", min_value=18, max_value=60, value=25)

experience = st.number_input("Years of Experience", min_value=0, max_value=40, value=2)

gender = st.selectbox("Gender", data['Gender'].unique())

degree = st.selectbox("Degree", data['Degree'].unique())

job_title = st.selectbox("Job Title", data['Job_Title'].unique())


# Encoding Inputs

gender_encode = data['Gender'].astype('category').cat.codes[data['Gender']==gender].iloc[0]

degree_encode = data['Degree'].astype('category').cat.codes[data['Degree']==degree].iloc[0]

job_encode = data['Job_Title'].astype('category').cat.codes[data['Job_Title']==job_title].iloc[0]


# Load Model

model = pickle.load(open("salary_model.pkl","rb"))


# Prediction

if st.button("Predict Salary"):

    input_data = np.array([[age, gender_encode, degree_encode, job_encode, experience]])

    prediction = model.predict(input_data)

    st.success(f"💰 Predicted Salary = {round(prediction[0],2)}")
