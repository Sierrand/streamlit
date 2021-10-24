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
pixie7 = pd.DataFrame({G:OOG, I:GBN, T:NOG, U:OGO}, index=["You have nothing I want.", "Do you have time?", "Don't turn me down."])
pixie8 = pd.DataFrame({G:GOG, I:NOO, T:GON, U:GGN}, index=["Fair enough.", "That is incorrect.", "What are you talking about?"])
pixie9 = pd.DataFrame({G:ONN, I:NBB, T:GOO, U:GBG}, index=["I noticed.", "I didn't feel an 'aura'.", "But we may never meet again."])
pixie11 = pd.DataFrame({G:NNG, I:NOO, T:GNN, U:BNG}, index=["Not talking down to people.", 
                                                            "Sharing household chores.", 
                                                            "Splitting all the costs."])
pixie12 = pd.DataFrame({G:NNN, I:GNO, T:NGN, U:GNO}, index=["A High School Outfit.", "A Kimono.", "Don't wear anything."])
pixie14 = pd.DataFrame({G:OBB, I:GOB, T:OGN, U:BOG}, index=["Fine, I will.", "I can't just leave you.", "Is that reverse psychology?"])
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

mandrake1 = pd.DataFrame({G:NGO, I:GNN, T:NNN, U:GGN}, index=["Call them. I dare you.", "Please don't.", "It was self-defense."])

bicorn1 = pd.DataFrame({G:OGN, I:GNO, T:GNB, U:GOG}, index=["You're right.", "I don't care.", "I don't know any other way."])
bicorn2 = pd.DataFrame({G:BOO, I:GBB, T:GOG, U:NGN}, index=["Yeah, we sure are.", "No, I thought this up myself.", "Want to join in?"])
bicorn3 = pd.DataFrame({G:NNG, I:OGG, T:GNN, U:BGB}, index=["So sorry.", "Brew your own.", "I'm not known for being polite."])
bicorn4 = pd.DataFrame({G:GBG, I:NNG, T:GNN, U:OGN}, index=["Are you okay?", "I have some antacids.", "That won't change anything?"])
bicorn5 = pd.DataFrame({G:NNG, I:GNN, T:GNO, U:OGO}, index=["An average level of happiness.", "Live fast, die young.", "Nothing."])
bicorn6 = pd.DataFrame({G:NGN, I:GOO, T:NGN, U:OGG}, index=["It's after school.", 
                                                            "I don't feel like going.", 
                                                            "I actually finished school."])
bicorn7 = pd.DataFrame({G:BGO, I:OBB, T:NGN, U:GON}, index=["A luxury cruise.", "Don't want to go anywhere.", "A trip to hell."])
bicorn8 = pd.DataFrame({G:NNG, I:GNG, T:BNN, U:BGB}, index=["Quit messing around.", "You're really paying?", "I'm a minor."])
bicorn9 = pd.DataFrame({G:GON, I:GBB, T:NGO, U:OBG}, index=["I don't really train.", "I just have a knack for it.", "At a gym from hell."])
bicorn10 = pd.DataFrame({G:GBG, I:GGO, T:GNG, U:OGO}, index=["Aren't you scared?", 
                                                             "I'll have some more fun first.", 
                                                             "I won't make you suffer."])
bicorn11 = pd.DataFrame({G:OOG, I:GGN, T:GOO, U:NNG}, index=["This is true.", "That's not very fun.", "You dirty old man."])
bicorn12 = pd.DataFrame({G:BNG, I:BGN, T:GNB, U:OBG}, index=["Someone did once.", "I don't care.", "I don't want to grow old."])
bicorn13 = pd.DataFrame({G:GOG, I:GBO, T:GOO, U:OGB}, index=["It's not like that.", "I got bad luck.", "Shut up."])
bicorn14 = pd.DataFrame({G:NGN, I:GGN, T:GON, U:OOG}, index=["Curry.", "All sorts of things.", "Protein."])
bicorn15 = pd.DataFrame({G:GGG, I:GON, T:OGO, U:OGO}, index=["You're going to die.", "Why do we fight?", "I don't really know..."])
bicorn16 = pd.DataFrame({G:NGB, I:GOO, T:NGN, U:OOG}, index=["Fate brought us together.", 
                                                             "There is no such thing.", 
                                                             "I want to end this fate."])
bicorn17 = pd.DataFrame({G:NBN, I:GBB, T:NNN, U:NNN}, index=["You won't suffer long.", 
                                                             "A coupon for a massage by me.", 
                                                             "I'll quietly be at your side."])
bicorn18 = pd.DataFrame({G:GNN, I:OGG, T:GNN, U:GOB}, index=["You tempt people.", "You're ugly.", "Nothing's wrong."])
bicorn19 = pd.DataFrame({G:NBG, I:GOO, T:NGO, U:NGG}, index=["Nope.", "I'll consider it.", "What kind of girl is she?"])

convo1 = "I'll go out with you just for today if there are no strings attached."
answ1 = ["If it pleases you.", "No strings attached?", "I've got enough on my plate..."]
convo2 = "Ooh, what if this leaves a scar and it's permanent?"
answ2 = ["Sorry...", "Just get plastic surgery.", "I'll take responsibility."]
convo3 = "When it came right down to it, you couldn't do anything to me!"
answ3 = ["I could.", "How could you tell?", "What do you want me to do?"]
convo4 = "You carry a gun because you think it'll make you more popular with the girls?"
answ4 = ["That's right.", "It won't?", "It's for self-improvement."]

gen1 = pd.DataFrame({G:OGN, I:GNG, T:GOO, U:GGG}, index=answ1)
gen2 = pd.DataFrame({G:GGG, I:NNG, T:GBG, U:GGG}, index=answ2)
gen3 = pd.DataFrame({G:NGG, I:GNN, T:OGG, U:OGG}, index=answ3)
gen4 = pd.DataFrame({G:BGG, I:GNG, T:OGG, U:GGG}, index=answ4)

if personaname == "":
    st.write("Please enter a name.")
elif personaname == "Jack":
    st.write("I'm busy, ho. It's tough being so popular.")
    st.write(jack_o_lantern1)
    st.write("This is all some kind of TV thing, hee-ho! Where's the camera?")
    st.write(jack_o_lantern2)
elif personaname == "Pixie":
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
    st.write(convo1)
    st.write(gen1)
    st.write("I'm inclined to turn you down, but if you still wish to speak, I will perhaps consider it.")
    st.write(pixie7)
    st.write("Is it not possible for this series of events involving you and me to be attributed to that?")
    st.write(pixie8)
    st.write("I've been projecting a 'don't speak to me' aura towards you.")
    st.write(pixie9)
    st.write(convo2)
    st.write(gen2)
    st.write("Tell me, what does 'equal footing' mean to you?")
    st.write(pixie11)
    st.write("What should I wear?")
    st.write(pixie12)
    st.write(convo3)
    st.write(gen3)
    st.write("Won't you just leave me be?")
    st.write(pixie14)
    st.write(convo4)
    st.write(gen4)
    st.write("You, however are talking to me right here. Are you the exception to this rule?")
    st.write(pixie16)
    st.write("You're lucky it was just me. You can't do anything like this in the real world, right?")
    st.write(pixie17)
elif personaname == "Agathion":
    st.write("Ain't people your age suppose'ta be out on dates and stuff instead?")
    st.write(agathion1)
    st.write("This is that 'domestic violins' thing, right?")
    st.write(agathion2)
    st.write("What was that, anyway?")
    st.write(agathion3)
    st.write("You're s'posed to go easy on kids! Are you stupid? Do you go to school and get stupid grades?")
    st.write(agathion4)
elif personaname == "Mandrake":
    st.write(convo1)
    st.write(gen1)
    st.write("...Maybe I'll call the police. Maybe I'll tell 'em that you were worse than you actually were!")
    st.write(mandrake1)
    st.write(convo2)
    st.write(gen2)
    st.write(convo3)
    st.write(gen3)
    st.write(convo4)
    st.write(gen4)
elif personaname == "Bicorn":
    st.write("A bad rep spreads like wildfire. If I were you, I'd quit all this nonsense. What's the point?")
    st.write(bicorn1)
    st.write("Are all the kids these days doin' stuff like this?")
    st.write(bicorn2)
    st.write("Couldn't ya at least make me a cup of tea or somethin'? Hell, that'd be real polite.")
    st.write(bicorn3)
    st.write("Hey, if ya got any medicine, lend me some. One of them painkillers...")
    st.write(bicorn4)
    st.write("Hey. So whaddya feel when you think about the future?")
    st.write(bicorn5)
    st.write("Hey. Why aren't ya at school?")
    st.write(bicorn6)
    st.write("How 'bout you, sonny? What kinda trip do you wanna take?")
    st.write(bicorn7)
    st.write("Humans talk over drinks, right? How 'bout it? Hell, let me buy ya a round, sonny.")
    st.write(bicorn8)
    st.write("...I gotta ask. How do you work out?")
    st.write(bicorn9)
    st.write("If yer gonna kill me, do me a solid and make it quick.")
    st.write(bicorn10)
    st.write("If you ask me, it's a lot more fun ta go chasin' after younger ladies, but...")
    st.write(bicorn11)
    st.write("Know how they say, 'Be kind ta yer elders'? Has no one ever taught ya that?")
    st.write(bicorn12)
    st.write("Somethin' bad happen in yer life or somethin', sonny?")
    st.write(bicorn13)
    st.write("What do ya usually eat?")
    st.write(bicorn14)
    st.write("What in the hell are ya tryin' ta tell me, anyway?")
    st.write(bicorn15)
    st.write("What kinda 'fate' do ya think there is in this meetin' between me and you?")
    st.write(bicorn16)
    st.write("What kinda 'hospitality' will you show me at the end of my life?")
    st.write(bicorn17)
    st.write("What's wrong with the way I look, huh?")
    st.write(bicorn18)
    st.write("...Y'know what I'm gettin' at, right? Ya think ya could let me go see my girl?")
    st.write(bicorn19)
else:
    st.write("No name chosen.")