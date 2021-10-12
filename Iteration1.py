import streamlit as st

st.header("Persona 5 Royal Negotiation Guide")

st.write("An interactive guide to shadow negotiations in Persona 5 Royal")

palaceoption = st.radio("Please specify the palace you are in", ("Kamoshida's Palace", "Madarame's Palace"))
st.write("The current palace is:", palaceoption)

st.write("Please include all - and '")
personaname = st.text_input("Type name here!")
st.write("The current persona is:", personaname)
