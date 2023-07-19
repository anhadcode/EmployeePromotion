import streamlit as st
import pandas as pd
st.set_page_config(layout="wide",page_title="Employee Promotion")
#department	education	gender	no_of_trainings	age	previous_year_rating	length_of_service	awards_won?	avg_training_score	is_promoted

st.title("Employee Promotion Predicter")
df= pd.read_csv('train.csv')
cols= st.columns(3)
with cols[0]:
    dept= st.selectbox("Select a Department", df['department'].unique())
    training= st.number_input("Number of Trainings")
    service_length=  st.number_input("Years of service")

with cols[1]:
    education= st.selectbox("Select an Education", ["Master's & above","Bachelor's","Below Secondary"])
    age= st.number_input("Age")
    awards= st.number_input("Awards won")


with cols[2]:
    gender= st.selectbox("Gender", df['gender'].unique())
    training_score= st.number_input("Average score of Trainings")
    rating= st.slider("Rating of the employee", min_value=0.0, max_value=5.0, step=0.10)


import pickle
pipe= pickle.load(open('classifier.pkl','rb'))

data= pd.DataFrame({"department":[dept],"education":[education],"gender":[gender],"no_of_trainings":[training],
             "age":[age],"previous_year_rating":[rating],"length_of_service":[service_length],"awards_won?":[awards],"avg_training_score":[training_score]})


with cols[1]:
    if st.button("Predict", use_container_width=True):
        if pipe.predict(data)==1:
            st.subheader("This employeee should be Promoted")
        else:
            st.subheader("Not Promoted")


