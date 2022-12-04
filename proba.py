import pickle
import numpy as np
import pandas as pd
import streamlit as st

model = pickle.load(open('lasso.pkl','rb'))



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

    racepctblack = st.slider("Percentage of population that is african american",min_value=0,max_value=100,key=0,value=28)
    agePct12t21 = st.slider("Percentage of population that is 12-21 in age",min_value=0,max_value=100,key=1,  value= 13)
    agePct65up = st.slider("Percentage of population that is 65 and over in age",min_value=0,max_value=100,key=2,value = 11)
    MalePctDivorce = st.slider("Percentage of males who are divorced",min_value=0,max_value=100,key=3,value=9)
    PctKids2Par = st.slider("Percentage of kids in family housing with two parents",min_value=0,max_value=100,key=4,value= 52)
    PctSpeakEnglOnly = st.slider("Percentage of people who speak only English",min_value=0,max_value=100,key=5,value=59)
    NumKidsBornNeverMar =  st.number_input("Births outside of marriage",value = 527557)
    NumInShelters = st.number_input("Number of people in homeless shelters",value =  23383)
    NumStreet = st.number_input("Number of homeless people counted in the street",value=10447)
   

    #x = data[['racepctblack','agePct12t21','agePct65up','MalePctDivorce','PctKids2Par','NumKidsBornNeverMar','PctSpeakEnglOnly','NumInShelters','NumStreet']]
    params = [[racepctblack,agePct12t21,agePct65up,MalePctDivorce,PctKids2Par,NumKidsBornNeverMar,PctSpeakEnglOnly,NumInShelters,NumStreet]]
    robbs = predict_robbery(params)


    if st.button("Predict"):
        if robbs>0:
            st.success('Number of predicted robberies: {}'.format(robbs))
        else:
            st.success('There will be no robberies.')

    
if __name__=='__main__':
        main()


