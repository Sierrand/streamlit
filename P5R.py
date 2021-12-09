#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd

st.header("Persona 5 Royal Negotiation Guide")

st.write("An interactive guide to shadow negotiations in Persona 5 Royal")

palaces = ["None", "Kamoshida's Palace", "..."]
KArr = (["Jack", "..."], ["Pixie","..."], ["Agathion","..."], ["Mandrake","..."], ["Bicorn","..."], ["Cait Sith","..."], ["Incubus","..."], ["Kelpie","..."], ["Silky","..."], ["Succubus","..."], ["Angel","..."], ["Berith","..."], ["Archangel","..."], ["Eligor","..."])

selected = st.selectbox("Would you like to display all of the options from a particular palace?", palaces)

if selected == "Kamoshida's Palace":
    st.sidebar.header("Shadows in Kamoshida's Palace")
    st.sidebar.table(KArr)

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
pixie7 = pd.DataFrame({G:OOG, I:GBN, T:NOG, U:OGO}, index=["You have nothing I want.", "Do you have time?", "Don't turn me down."])
pixie9 = pd.DataFrame({G:ONN, I:NBB, T:GOO, U:GBG}, index=["I noticed.", "I didn't feel an 'aura'.", "But we may never meet again."])
pixie11 = pd.DataFrame({G:NNG, I:NOO, T:GNN, U:BNG}, index=["Not talking down to people.", 
                                                            "Sharing household chores.", 
                                                            "Splitting all the costs."])
pixie12 = pd.DataFrame({G:NNN, I:GNO, T:NGN, U:GNO}, index=["A High School Outfit.", "A Kimono.", "Don't wear anything."])
pixie14 = pd.DataFrame({G:OBB, I:GOB, T:OGN, U:BOG}, index=["Fine, I will.", "I can't just leave you.", "Is that reverse psychology?"])
pixie16 = pd.DataFrame({G:GNN, I:NNO, T:NBO, U:OOG}, index=["I'm not special.", "That's right.", "I have ulterior motives."])
pixie17 = pd.DataFrame({G:BON, I:NNN, T:NBB, U:NNN}, index=["That's right.", "I choose my targets carefully.", "I'm serious about this."])

bicorn1 = pd.DataFrame({G:OGN, I:GNO, T:GNB, U:GOG}, index=["You're right.", "I don't care.", "I don't know any other way."])
bicorn2 = pd.DataFrame({G:BOO, I:GBB, T:GOG, U:NGN}, index=["Yeah, we sure are.", "No, I thought this up myself.", "Want to join in?"])
bicorn5 = pd.DataFrame({G:NNG, I:GNN, T:GNO, U:OGO}, index=["An average level of happiness.", "Live fast, die young.", "Nothing."])
bicorn6 = pd.DataFrame({G:NGN, I:GOO, T:NGN, U:OGG}, index=["It's after school.", 
                                                            "I don't feel like going.", 
                                                            "I actually finished school."])
bicorn7 = pd.DataFrame({G:BGO, I:OBB, T:NGN, U:GON}, index=["A luxury cruise.", "Don't want to go anywhere.", "A trip to hell."])
bicorn9 = pd.DataFrame({G:GON, I:GBB, T:NGO, U:OBG}, index=["I don't really train.", "I just have a knack for it.", "At a gym from hell."])
bicorn11 = pd.DataFrame({G:OOG, I:GGN, T:GOO, U:NNG}, index=["This is true.", "That's not very fun.", "You dirty old man."])
bicorn12 = pd.DataFrame({G:BNG, I:BGN, T:GNB, U:OBG}, index=["Someone did once.", "I don't care.", "I don't want to grow old."])
bicorn15 = pd.DataFrame({G:GGG, I:GON, T:OGO, U:OGO}, index=["You're going to die.", "Why do we fight?", "I don't really know..."])
bicorn17 = pd.DataFrame({G:NBN, I:GBB, T:NNN, U:NNN}, index=["You won't suffer long.", 
                                                             "A coupon for a massage by me.", 
                                                             "I'll quietly be at your side."])
bicorn19 = pd.DataFrame({G:NBG, I:GOO, T:NGO, U:NGG}, index=["Nope.", "I'll consider it.", "What kind of girl is she?"])

caitsith1 = pd.DataFrame({G:ONG, I:GNB, T:NGN, U:NNB}, index=["Yes.", "No.", "It has nothing to do with this."])

incubus1 = pd.DataFrame({G:OOG, I:GGO, T:ONG, U:OGO}, index=["No it isn't.", "It's part of my face.", "My apologies."])
incubus2 = pd.DataFrame({G:GNN, I:NNN, T:NON, U:NGB}, index=["Pissy guys.", "Guys with no sense of humor.", "I never get mad."])
incubus3 = pd.DataFrame({G:GON, I:OGB, T:GGO, U:GBG}, index=["I don't want to die.", 
                                                             "There's something I must do.", 
                                                             "I want girls to like me."])

kelpie1 = pd.DataFrame({G:BNB, I:OBG, T:NNN, U:OGN}, index=["It does.", "Don't expect it.", "The elderly have bad manners."])
kelpie2 = pd.DataFrame({G:OOG, I:NGB, T:NGN, U:GGG}, index=["I'll make you into soup.", "I don't want to eat you.", "I'll mince you."])
kelpie3 = pd.DataFrame({G:NNG, I:NGO, T:GGO, U:GGG}, index=["Times have changed.", "Humans are powerful.", "This is a difficult topic..."])
kelpie4 = pd.DataFrame({G:OGO, I:OGO, T:GNN, U:GNG}, index=["I want you.", "Not really.", "Let me touch your paw."])
kelpie5 = pd.DataFrame({G:BOG, I:BBG, T:GOB, U:GGO}, index=["I'm sorry.", "Should I take off my shoes?", "Shut up."])

silky1 = pd.DataFrame({G:NGN, I:GOO, T:GBO, U:GBB}, index=["I never thought of that.", "I understand.", "What do you mean?"])

angel1 = pd.DataFrame({G:OBN, I:NNG, T:NNN, U:GNB}, index=["Not a bad idea.", "I don't want a kiss.", "Have some self-respect."])
angel2 = pd.DataFrame({G:NON, I:OBG, T:OGN, U:GNN}, index=["Older people trying to look young.", "No one bothers me.", "I hate everyone."])
angel3 = pd.DataFrame({G:NNN, I:OGN, T:OGN, U:NNG}, index=["Looks like it came true.", 
                                                           "It's just a horoscope.", 
                                                           "How is your luck in romance?"])
angel4 = pd.DataFrame({G:ONG, I:GNN, T:GNN, U:ONG}, index=["I feel bad.", "I don't agree with this.", "Everyone wins."])

archangel1 = pd.DataFrame({G:NNN, I:NGO, T:NNN, U:NNN}, index=["I can certainly try.", "No can do.", "What's veneration?"])
archangel2 = pd.DataFrame({G:NNN, I:BOG, T:NGN, U:GNN}, index=["Sin...?", "Please tell me.", "I've done nothing wrong."])
archangel3 = pd.DataFrame({G:NNN, I:GOB, T:NNN, U:GNG}, index=["You're a beloved neighbor.", 
                                                               "You're a loathsome foe.", 
                                                               "You sound preachy."])
archangel4 = pd.DataFrame({G:NNN, I:NGN, T:NGG, U:GNO}, index=["In your situation?", "You're tough.", "Don't push yourself."])
archangel5 = pd.DataFrame({G:NNN, I:NOG, T:NNN, U:NGN}, index=["I don't understand.", "I feel his gaze.", "I prefer a harsher stare."])
archangel6 = pd.DataFrame({G:NNN, I:GGN, T:NNN, U:NNN}, index=["I noticed.", "I can survive alone.", "Find it for me."])
archangel7 = pd.DataFrame({G:NNN, I:GBG, T:NNN, U:NGN}, index=["Sorry.", "'Words of repentance.'", "Not sorry."])
archangel8 = pd.DataFrame({G:NNN, I:NGN, T:NNN, U:NNB}, index=["Make it crowded where I shop.", 
                                                               "Give me violence.", 
                                                               "No calamities, please."])
archangel9 = pd.DataFrame({G:NNN, I:GNN, T:NNN, U:NNN}, index=["You're right.", "...", "..."])
archangel10 = pd.DataFrame({G:ONG, I:NGN, T:NNN, U:NNN}, index=["Leave the future to me.", "I need your guidance.", "I don't get it."])
archangel11 = pd.DataFrame({G:NNN, I:GON, T:NNN, U:NBG}, index=["Why can't we end war?", 
                                                                "No complaints here.", 
                                                                "I can't get a girlfriend."])
archangel12 = pd.DataFrame({G:NNN, I:ONG, T:GNN, U:NGN}, index=["I'll think about it.", "No need to be so dramatic.", "I decline."])
archangel13 = pd.DataFrame({G:NBN, I:GNN, T:NNN, U:NNN}, index=["You got me.", "You're mistaken.", "Are you okay?"])
archangel14 = pd.DataFrame({G:NNN, I:BNO, T:NNN, U:GNG}, index=["Omnipotent?", "I'm not beleaguered.", "There's someone I want to save."])
    
convo1 = "I'll go out with you just for today if there are no strings attached."
answ1 = ["If it pleases you.", "No strings attached?", "I've got enough on my plate..."]

convo2 = "Ooh, what if this leaves a scar and it's permanent?"
answ2 = ["Sorry...", "Just get plastic surgery.", "I'll take responsibility."]

convo3 = "When it came right down to it, you couldn't do anything to me!"
answ3 = ["I could.", "How could you tell?", "What do you want me to do?"]

convo4 = "You carry a gun because you think it'll make you more popular with the girls?"
answ4 = ["That's right.", "It won't?", "It's for self-improvement."]

convo5 = "Ain't people your age suppose'ta be out on dates and stuff instead?"
answ5 = ["Right after this, kid.", "Such a rude little boy...", "Dating's not important."]

convo6 = "This is that 'domestic violins' thing, right?"
answ6 = ["That's 'domestic violence.'", "What? No, you're wrong...", "Um, are things okay at home?"]

convo7 = "What was that, anyway?"
answ7 = ["A love letter.", "A threat letter.", "A coupon."]

convo8 = "You're s'posed to go easy on kids! Are you stupid? Do you go to school and get stupid grades?"
answ8 = ["I'm smart.", "I'm good at PE.", "Shut up."]

convo9 = "But this way of life in this world is all I've ever known."
answ9 = ["It's not meaningless.", "There are other ways to live.", "You had a good run."]

convo10 = "Care to explain yourself? I certainly hope you have a good reason for this boorish treatment."
answ10 = ["That would take a while.", "There's no need to explain.", "Just shut up..."]

convo11 = "I insist you surrender yourself to the authorities."
answ11 = ["This is a misunderstanding.", "I apologize.", "You've got the wrong idea."]

convo12 = "Is it not possible for this series of events involving you and me to be attributed to that?"
answ12 = ["Fair enough.", "That is incorrect.", "What are you talking about?"]

convo13 = "...Maybe I'll call the police. Maybe I'll tell 'em that you were worse than you actually were!"
answ13 = ["Call them. I dare you.", "Please don't.", "It was self-defense."]

convo14 = "Hey, if ya got any medicine, lend me some. One of them painkillers..."
answ14 = ["Are you okay?", "I have some antacids.", "That won't change anything?"]

convo15 = "Humans talk over drinks, right? How 'bout it? Hell, let me buy ya a round, sonny."
answ15 = ["Quit messing around.", "You're really paying?", "I'm a minor."]

convo16 = "If yer gonna kill me, do me a solid and make it quick."
answ16 = ["Aren't you scared?", "I'll have some more fun first.", "I won't make you suffer."]

convo17 = "Somethin' bad happen in yer life or somethin', sonny?"
answ17 = ["It's not like that.", "I got bad luck.", "Shut up."]

convo18 = "What's wrong with the way I look, huh?"
answ18 = ["You tempt people.", "You're ugly.", "Nothing's wrong."]

convo19 = "Couldn't ya at least make me a cup of tea or somethin'? Hell, that'd be real polite."
answ19 = ["So sorry.", "Brew your own.", "I'm not known for being polite."]

convo20 = "What do ya usually eat?"
answ20 = ["Curry.", "All sorts of things.", "Protein."]

convo21 = "What kinda 'fate' do ya think there is in this meetin' between me and you?"
answ21 = ["Fate brought us together.", "There is no such thing.", "I want to end this fate."]

gen1 = pd.DataFrame({G:OGN, I:GNG, T:GOO, U:GGG}, index=answ1)
gen2 = pd.DataFrame({G:GGG, I:NNG, T:GBG, U:GGG}, index=answ2)
gen3 = pd.DataFrame({G:NGG, I:GNN, T:OGG, U:OGG}, index=answ3)
gen4 = pd.DataFrame({G:BGG, I:GNG, T:OGG, U:GGG}, index=answ4)
gen5 = pd.DataFrame({G:NNG, I:NOG, T:GNG, U:GOG}, index=answ5)
gen6 = pd.DataFrame({G:GNG, I:NGB, T:GNG, U:GNG}, index=answ6)
gen7 = pd.DataFrame({G:OGN, I:NGN, T:GNG, U:GGG}, index=answ7)
gen8 = pd.DataFrame({G:BGN, I:GNN, T:GGB, U:GGO}, index=answ8)
gen9 = pd.DataFrame({G:GGG, I:GON, T:GNN, U:OOG}, index=answ9)
gen10 = pd.DataFrame({G:GGN, I:BOG, T:GBN, U:GNO}, index=answ10)
gen11 = pd.DataFrame({G:OBG, I:GBO, T:GNO, U:OOG}, index=answ11)
gen12 = pd.DataFrame({G:GOG, I:NOO, T:GON, U:GGN}, index=answ12)
gen13 = pd.DataFrame({G:NGO, I:GNN, T:NNN, U:GGN}, index=answ13)
gen14 = pd.DataFrame({G:GBG, I:NNG, T:GNN, U:OGN}, index=answ14)
gen15 = pd.DataFrame({G:NNG, I:GNG, T:BNN, U:BGB}, index=answ15)
gen16 = pd.DataFrame({G:GBG, I:GGO, T:GNG, U:OGO}, index=answ16)
gen17 = pd.DataFrame({G:GOG, I:GBO, T:GOO, U:OGB}, index=answ17)
gen18 = pd.DataFrame({G:GNN, I:OGG, T:GNN, U:GOB}, index=answ18)
gen19 = pd.DataFrame({G:NNG, I:OGG, T:GNN, U:BGB}, index=answ19)
gen20 = pd.DataFrame({G:NGN, I:GGN, T:GON, U:OOG}, index=answ20)
gen21 = pd.DataFrame({G:NGB, I:GOO, T:NGN, U:OOG}, index=answ21)

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
    st.write(convo9)
    st.write(gen9)
    st.write(convo10)
    st.write(gen10)
    st.write(convo11)
    st.write(gen11)
    st.write(convo1)
    st.write(gen1)
    st.write("I'm inclined to turn you down, but if you still wish to speak, I will perhaps consider it.")
    st.write(pixie7)
    st.write(convo12)
    st.write(gen12)
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
    st.write(convo5)
    st.write(gen5)
    st.write(convo6)
    st.write(gen6)
    st.write(convo7)
    st.write(gen7)
    st.write(convo8)
    st.write(gen8)
elif personaname == "Mandrake":
    st.write(convo1)
    st.write(gen1)
    st.write(convo13)
    st.write(gen13)
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
    st.write(convo19)
    st.write(gen19)
    st.write(convo14)
    st.write(gen14)
    st.write("Hey. So whaddya feel when you think about the future?")
    st.write(bicorn5)
    st.write("Hey. Why aren't ya at school?")
    st.write(bicorn6)
    st.write("How 'bout you, sonny? What kinda trip do you wanna take?")
    st.write(bicorn7)
    st.write(convo15)
    st.write(gen15)
    st.write("...I gotta ask. How do you work out?")
    st.write(bicorn9)
    st.write(convo16)
    st.write(gen16)
    st.write("If you ask me, it's a lot more fun ta go chasin' after younger ladies, but...")
    st.write(bicorn11)
    st.write("Know how they say, 'Be kind ta yer elders'? Has no one ever taught ya that?")
    st.write(bicorn12)
    st.write(convo17)
    st.write(gen17)
    st.write(convo20)
    st.write(gen20)
    st.write("What in the hell are ya tryin' ta tell me, anyway?")
    st.write(bicorn15)
    st.write(convo21)
    st.write(gen21)
    st.write("What kinda 'hospitality' will you show me at the end of my life?")
    st.write(bicorn17)
    st.write(convo18)
    st.write(gen18)
    st.write("...Y'know what I'm gettin' at, right? Ya think ya could let me go see my girl?")
    st.write(bicorn19)
elif personaname == "Cait Sith":
    st.write(convo5)
    st.write(gen5)
    st.write("Is it 'cause I wasn't a 'good kid'?")
    st.write(caitsith1)
    st.write(convo6)
    st.write(gen6)
    st.write(convo7)
    st.write(gen7)
    st.write(convo8)
    st.write(gen8)
elif personaname == "Incubus":
    st.write("It's pretty rude, man.")
    st.write(incubus1)
    st.write("What kinda guys piss you off?")
    st.write(incubus2)
    st.write("Why're you so desperate?")
    st.write(incubus3)
elif personaname == "Kelpie":
    st.write("Man, I'm about ta be a victim of that too. Hell, does this country even have a future?")
    st.write(kelpie1)
    st.write("Me am really in soup, now. Do what you want. Me am ready if you want grill me, so...")
    st.write(kelpie2)
    st.write("So why me in this situation right now? Why me at your mercy?")
    st.write(kelpie3)
    st.write("There something you want say to me, right?")
    st.write(kelpie4)
    st.write("Why you keep trampling here? What you humans thinking?")
    st.write(kelpie5)
elif personaname == "Silky":
    st.write(convo9)
    st.write(gen9)
    st.write(convo10)
    st.write(gen10)
    st.write(convo11)
    st.write(gen11)
    st.write(convo12)
    st.write(gen12)
    st.write("You do understand that we are here because of people like you, right?")
    st.write(silky1)
elif personaname == "Succubus":
    st.write(convo2)
    st.write(gen2)
    st.write(convo3)
    st.write(gen3)
    st.write(convo4)
    st.write(gen4)
elif personaname == "Angel":
    st.write("Hey, how about this? If you don't shoot me, then I'll kiss you. Not a bad deal, right?")
    st.write(angel1)
    st.write(convo1)
    st.write(gen1)
    st.write("I'm sure there're other people in the world who'd irritate you more. C'mon, tell me.")
    st.write(angel2)
    st.write(convo13)
    st.write(gen13)
    st.write("My horoscope said I was going to have 'relationship difficulties' today.")
    st.write(angel3)
    st.write(convo2)
    st.write(gen2)
    st.write("We'll just say you win. So can we stop this?")
    st.write(angel4)
    st.write(convo3)
    st.write(gen3)
    st.write(convo4)
    st.write(gen4)
elif personaname == "Berith":
    st.write(convo14)
    st.write(gen14)
    st.write(convo15)
    st.write(gen15)
    st.write(convo16)
    st.write(gen16)
    st.write(convo17)
    st.write(gen17)
    st.write(convo18)
    st.write(gen18)
elif personaname == "Archangel":
    st.write("Can you sacrifice yourself in order to demonstrate your veneration of our Father?")
    st.write(archangel1)
    st.write("Do you know what I speak of?")
    st.write(archangel2)
    st.write("Do you seek friendly competition with a beloved neighbor? Or have you come to destroy a hated foe?")
    st.write(archangel3)
    st.write("I fear neither death, nor you.")
    st.write(archangel4)
    st.write("It is to become aware of the gaze of our Father, who watches over you with loving grace.")
    st.write(archangel5)
    st.write("It seems the Son of Man have denounced the word of our father. Tell me, what worth have you found?")
    st.write(archangel6)
    st.write("Let me hear you utter words of repentance.")
    st.write(archangel7)
    st.write("Name a calamity that you can bear.")
    st.write(archangel8)
    st.write("Think carefully. I am not the one you should detest.")
    st.write(archangel9)
    st.write("To view me as an enemy is to incur our Father's wrath. Man's future rests in your hands.")
    st.write(archangel10)
    st.write("...Very well. In the place of our Father, I shall listen to your complaints.")
    st.write(archangel11)
    st.write("Vow that you will use that power in the name of our Father.")
    st.write(archangel12)
    st.write("You have appeared to test my adoration of our Father. Yes, you are... the Tempter")
    st.write(archangel13)
    st.write("You, who reside in that world of the almighty, what is it that has beleaguered you so?")
    st.write(archangel14)
elif personaname == "Eligor":
    st.write(convo19)
    st.write(gen19)
    st.write(convo20)
    st.write(gen20)
    st.write(convo21)
    st.write(gen21)
else:
    st.write("No name chosen.")
