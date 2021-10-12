
import streamlit as st
import pandas as pd

st.header("Persona 5 Royal Negotiation Guide")

st.write("An interactive guide to shadow negotiations in Persona 5 Royal")

personaname = st.text_input("Type name here!")
st.write("The current persona is:", personaname)

G = "Gloomy"
I = "Irritable"
T = "Timid"
U = "Upbeat"

jack_o_lantern1 = pd.DataFrame({G:["-", "-", "G"], 
                                I:["-", "-", "-"],
                                T:["G", "-", "-"], 
                                U:["G", "-", "O"]},
                               index=["You do sound busy.", "Your popularity won't last.", "Who cares?"])

jack_o_lantern2 = pd.DataFrame({"Gloomy":["-", "G", "-"], 
                                "Irritable":["-", "-", "-"],
                                "Timid":["O", "G", "-"], 
                                "Upbeat":["G", "G", "B"]},
                               index=["Wow, you got me.", "What's all this now?", "This is real."])

if personaname == "Jack":
    st.write("I'm busy, ho. It's tough being so popular.")
    st.write(jack_o_lantern1)
    st.write("This is all some kind of TV thing, hee-ho! Where's the camera?")
    st.write(jack_o_lantern2)
