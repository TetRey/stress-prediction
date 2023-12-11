import pickle
import streamlit as st

stress_model = pickle.load(open('data_stress.sav', 'rb'))

st.title('Stress Prediction For Student')

st.markdown("""
  <style>
  div.stButton {text-align:center;}
 
  </style>""", unsafe_allow_html=True)

import streamlit as st



JumlahKepanitiaan = st.text_input('How many committees have you served on?')
JumlahJamTidur = st.text_input('How many hours do you sleep on average each day?')
LamaPerjalanan = st.text_input('How long does it take from your house to campus? (On Minute)')
Olahraga = st.text_input('How long do you take excersise in a week (On Minute)')
Curhat = st.text_input('How many do you gossip in a week?')

stress_diagnosis =''

if st.button('Check!!!'):
    stress_diagnosis = stress_model.predict([[JumlahKepanitiaan,JumlahJamTidur,LamaPerjalanan,Olahraga,Curhat]])
    if(stress_diagnosis[0] == 1):
        stress_diagnosis = "You are stress right now, Take a deep breath and rest!!!"
        st.error(stress_diagnosis)
        
    else:
        stress_diagnosis = "You aren't stress, keep it woorks!!!"
        st.success(stress_diagnosis)

    

    