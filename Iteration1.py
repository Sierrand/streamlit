#!/usr/bin/env python
# coding: utf-8

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

GGG = ["G", "G", "G"]
GGN = ["G", "G", "-"]
GGO = ["G", "G", "O"]
GGB = ["G", "G", "B"]
GOG = ["G", "O", "G"]
GOO = ["G", "O", "O"]
GON = ["G", "O", "-"]
GOB = ["G", "O", "B"]
GNG = ["G", "-", "G"]
GNO = ["G", "-", "O"]
GNN = ["G", "-", "-"]
GNB = ["G", "-", "B"]
GBG = ["G", "B", "G"]
GBO = ["G", "B", "O"]
GBN = ["G", "B", "-"]
GBB = ["G", "B", "B"]

OGG = ["O", "G", "G"]
OGO = ["O", "G", "O"]
OGN = ["O", "G", "-"]
OGB = ["O", "G", "B"]
OOG = ["O", "O", "G"]
OOO = ["O", "O", "O"]
OON = ["O", "O", "-"]
OOB = ["O", "O", "B"]
ONG = ["O", "-", "G"]
ONO = ["O", "-", "O"]
ONN = ["O", "-", "-"]
ONB = ["O", "-", "B"]
OBG = ["O", "B", "G"]
OBO = ["O", "B", "O"]
OBN = ["O", "B", "-"]
OBB = ["O", "B", "B"]

NGG = ["-", "G", "G"]
NGO = ["-", "G", "O"]
NGN = ["-", "G", "-"]
NGB = ["-", "G", "B"]
NOG = ["-", "O", "G"]
NOO = ["-", "O", "O"]
NON = ["-", "O", "-"]
NOB = ["-", "O", "B"]
NNG = ["-", "-", "G"]
NNO = ["-", "-", "O"]
NNN = ["-", "-", "-"]
NNB = ["-", "-", "B"]
NBG = ["-", "B", "G"]
NBO = ["-", "B", "O"]
NBN = ["-", "B", "-"]
NBB = ["-", "B", "B"]

BGG = ["B", "G", "G"]
BGO = ["B", "G", "O"]
BGN = ["B", "G", "-"]
BGB = ["B", "B", "B"]
BOG = ["B", "O", "G"]
BOO = ["B", "O", "O"]
BON = ["B", "O", "-"]
BOB = ["B", "O", "B"]
BNG = ["B", "-", "G"]
BNO = ["B", "-", "O"]
BNN = ["B", "-", "-"]
BNB = ["B", "-", "B"]
BBG = ["B", "B", "G"]
BBO = ["B", "B", "O"]
BBN = ["B", "B", "-"]
BBB = ["B", "B", "B"]


jack_o_lantern1 = pd.DataFrame({G:NNG, I:NNN,T:GNN,U:GNO}, index=["You do sound busy.", "Your popularity won't last.", "Who cares?"])
jack_o_lantern2 = pd.DataFrame({G:NGN, I:NNN, T:OGN, U:GGB}, index=["Wow, you got me.", "What's all this now?", "This is real."])

pixie1 = pd.DataFrame({G:NGG, I:GNN, T:GOO, U:NNG}, index=["I'm sorry.", "Age doesn't matter.", "This isn't extreme."])
pixie2 = pd.DataFrame({G:NNG, I:GNN, T:NGN, U:NNN}, index=["Impressions.", "Making funny faces.", "Nothing."])
pixie3 = pd.DataFrame({G:GGG, I:GON, T:GNN, U:OOG}, index=["It's not meaningless.", "There are other ways to live.", "You had a good run."])
pixie4 = pd.DataFrame({G:GGN, I:BOG, T:GBN, U:GNO}, index=["That would take a while.", "There's no need to explain.", "Just shut up..."])
pixie5 = pd.DataFrame({G:OBG, I:GBO, T:GNO, U:OOG}, index=["This is a misunderstanding.", "I apologize.", "You've got the wrong idea."])
pixie6 = pd.DataFrame({G:OGN, I:GNG, T:GOO, U:GGG}, index=["If it pleases you.", "No strings attached?", "I've got enough on my plate..."])
pixie7 = pd.DataFrame({G:OOG, I:GBN, T:NOG, U:OGO}, index=["You have nothing I want.", "Do you have time?", "Don't turn me down."])
pixie8 = pd.DataFrame({G:GOG, I:NOO, T:GON, U:GGN}, index=["Fair enough.", "That is incorrect.", "What are you talking about?"])
pixie9 = pd.DataFrame({G:ONN, I:NBB, T:GOO, U:GBG}, index=["I noticed.", "I didn't feel an 'aura'.", "But we may never meet again."])
pixie10 = pd.DataFrame({G:GGG, I:NNG, T:GBG, U:GGG}, index=["Sorry...", "Just get plastic surgery.", "I'll take responsibility."])
pixie11 = pd.DataFrame({G:NNG, I:NOO, T:GNN, U:BNG}, index=["Not talking down to people.", 
                                                            "Sharing household chores.", 
                                                            "Splitting all the costs."])
pixie12 = pd.DataFrame({G:NNN, I:GNO, T:NGN, U:GNO}, index=["A High School Outfit.", "A Kimono.", "Don't wear anything."])
pixie13 = pd.DataFrame({G:NGG, I:GNN, T:OGG, U:OGG}, index=["I could.", "How could you tell?", "What do you want me to do?"])
pixie14 = pd.DataFrame({G:OBB, I:GOB, T:OGN, U:BOG}, index=["Fine, I will.", "I can't just leave you.", "Is that reverse psychology?"])
pixie15 = pd.DataFrame({G:BGG, I:GNG, T:OGG, U:GGG}, index=["That's right.", "It won't?", "It's for self-improvement."])
pixie16 = pd.DataFrame({G:GNN, I:NNO, T:NBO, U:OOG}, index=["I'm not special.", "That's right.", "I have ulterior motives."])
pixie17 = pd.DataFrame({G:BON, I:NNN, T:NBB, U:NNN}, index=["That's right.", "I choose my targets carefully.", "I'm serious about this."])

agathion1 = pd.DataFrame({G:NNG, I:NOG, T:GNG, U:GOG}, index=["Right after this, kid.", 
                                                              "Such a rude little boy...", 
                                                              "Dating's not important."])
agathion2 = pd.DataFrame({G:GNG, I:NGB, T:GNG, U:GNG}, index=["That's 'domestic violence.'", 
                                                              "What? No, you're wrong...", 
                                                              "Um, are things okay at home?"])
agathion3 = pd.DataFrame({G:OGN, I:NGN, T:GNG, U:GGG}, index=["A love letter.", "A threat letter.", "A coupon."])
agathion4 = pd.DataFrame({G:BGN, I:GNN, T:GGB, U:GGO}, index=["I'm smart.", "I'm good at PE.", "Shut up."])

if personaname == "Jack":
    st.write("I'm busy, ho. It's tough being so popular.")
    st.write(jack_o_lantern1)
    st.write("This is all some kind of TV thing, hee-ho! Where's the camera?")
    st.write(jack_o_lantern2)
elif personaname == ("Pixie") or ("pixie"):
    st.write("Ah, so I suppose you commit such extreme acts because you know you won't be punished harshly...")
    st.write(pixie1)
    st.write("But before you do, do something funny. What can you do?")
    st.write(pixie2)
    st.write("But this way of life in this world is all I've ever known.")
    st.write(pixie3)
    st.write("Care to explain yourself? I certainly hope you have a good reason for this boorish treatment.")
    st.write(pixie4)
    st.write("I insist you surrender yourself to the authorities.")
    st.write(pixie5)
    st.write("I'll go out with you just for today if there are no strings attached.")
    st.write(pixie6)
    st.write("I'm inclined to turn you down, but if you still wish to speak, I will perhaps consider it.")
    st.write(pixie7)
    st.write("Is it not possible for this series of events involving you and me to be attributed to that?")
    st.write(pixie8)
    st.write("I've been projecting a 'don't speak to me' aura towards you.")
    st.write(pixie9)
    st.write("Ooh, what if this leaves a scar and it's permanent?")
    st.write(pixie10)
    st.write("Tell me, what does 'equal footing' mean to you?")
    st.write(pixie11)
    st.write("What should I wear?")
    st.write(pixie12)
    st.write("When it came right down to it, you couldn't do anything to me!")
    st.write(pixie13)
    st.write("Won't you just leave me be?")
    st.write(pixie14)
    st.write("You carry a gun because you think it'll make you more popular with the girls?")
    st.write(pixie15)
    st.write("You, however are talking to me right here. Are you the exception to this rule?")
    st.write(pixie16)
    st.write("You're lucky it was just me. You can't do anything like this in the real world, right?")
    st.write(pixie17)
elif personaname == ("Agathion") or ("agathion"):
    st.write("Ain't people your age suppose'ta be out on dates and stuff instead?")
    st.write(agathion1)
    st.write("This is that 'domestic violins' thing, right?")
    st.write(agathion2)
    st.write("What was that, anyway?")
    st.write(agathion3)
    st.write("You're s'posed to go easy on kids! Are you stupid? Do you go to school and get stupid grades?")
    st.write(agathion4)