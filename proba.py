import pickle
import numpy as np
import pandas as pd
import streamlit as st


f = open("lasso.pls", "rb")
model = pickle.load(f)



def predict_robbery(params):
  
    prediction = model.predict(params)
    return int(prediction)

def main():
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> US Robbery Prediction </h2>
    </div>
    """
   
    st.markdown(html_temp, unsafe_allow_html = True)

    #'population','numbUrban','medIncome','NumUnderPov','NumKidsBornNeverMar','NumImmig','NumInShelters','NumStreet'
    population = st.number_input("population",1)
    numbUrban = st.number_input("numbUrban",1)
    medIncome = st.number_input("medIncome",1)
    NumUnderPov = st.number_input("NumUnderPov",1)
    NumKidsBornNeverMar = st.number_input("NumKidsBornNeverMar",1)
    NumImmig = st.number_input("NumImmig",1)
    NumInShelters = st.number_input("NumInShelterst",1)
    NumStreet = st.number_input("NumStreet",1)

    params = [[population,numbUrban,medIncome,NumUnderPov,NumKidsBornNeverMar,NumImmig,NumInShelters,NumStreet]]
    robbs = predict_robbery(params)


    if st.button("Predict"):
        if robbs>0:
            st.success('Number of predicted robberis: {}'.format(predict_robbery(params)))
        else:
            st.success('There will be no robberies.')

    
if __name__=='__main__':
        main()


