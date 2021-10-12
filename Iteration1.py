#!/usr/bin/env python
# coding: utf-8

import streamlit as st

st.header("The First Iteration")

st.write("Persona 5 Royal Negotiation Guide?")

personaname = st.text_input("Insert a name")
st.write("The current persona is:", personaname)
