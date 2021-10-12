import streamlit as st
import pandas as pd

st.header("Persona 5 Royal Negotiation Guide")

st.write("An interactive guide to shadow negotiations in Persona 5 Royal")

palaceoption = st.radio("Please specify the palace you are in", ("Kamoshida's Palace", "Madarame's Palace"))
st.write("The current palace is:", palaceoption)

personaname = st.text_input("Type name here!")
st.write("The current persona is:", personaname)

jack_o_lantern1 = pd.DataFrame({"Gloomy":["x", "x", "G"], 
                                "Irritable":["x", "x", "x"],
                                "Timid":["G", "x", "x"], 
                                "Upbeat":["G", "x", "O"]},
                               index=["You do sound busy.", "Your popularity won't last.", "Who cares?"])

if personaname == "Jack":
    st.write("I'm busy, ho. It's tough being so popular.")
    st.write(jack_o_lantern1)
