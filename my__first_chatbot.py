import re
import random
import string

goodbye = r"laters|quit|ciao|bye|see ya|goodbye|à \+"
msg_bye = ["okelydokely", "Do what you want", "Whatevs"]
msg_unknown = ["Does not compute",
              "You what now?",
              "lala i can't hear you"]
meteo = r"whats the weather like in .*?|Is it raining in.*?|What temperature is it in .*?"
greetings = r"hiya!|hi|hello"
msg_greeting = ["What you want?", "Sup"]
hru = r"how are you?|how's things?"
msg_hru = ["better if you stopped bothering me", "like you care"]
name = r"what's your name?|what are you called?"
msg_name = ["nosy aren't you", "Mr mind your own business"]
age = r"how old are you?|whats your age?"
msg_age = ["never you mind!", "don't you know its rude to ask that?"]
song = r"what's your favourite song?|do you have a favourite song?"
msg_song = ["I don't like music", "I like the sound of nails down a blackboard"]
home = r"where's home?|where do you live?"
msg_home = ["never never land", "where ever I want"]
job = r"what do you do?|what's your job?"
msg_job = ["I don't do much", "I'm unemployable"]
blank = r""
msg_blank = ["Are you there?", "Not got anything to say?"]

flag = True
print("""Welcome to beginner bot! \n What do you want to ask? : \n (Say bye when you want to quit)""")
while flag:
    text_user = input("> ")
    text_user = text_user.lower()
    #bye
    if (re.search(goodbye, text_user)):
        print(random.choice(msg_bye))
        flag = False
    #weather
    elif (re.search(meteo, text_user)):
        text_user = re.sub(f"[{string.punctuation}]", " ", text_user)
        print(f"Its raining in {text_user.split()[-1]}")
    #reponds to hello
    elif (re.search(greetings, text_user)):
        print(random.choice(msg_greeting))
    #responds to how are you
    elif (re.search(hru, text_user)):
        print(random.choice(msg_hru))
    #gives name
    elif (re.search(name, text_user)):
        print(random.choice(msg_name))
    #gives age
    elif (re.search(age, text_user)):
        print(random.choice(msg_age))
    #gives favourite song
    elif (re.search(song, text_user)):
        print(random.choice(msg_song))
    #says where he lives
    elif (re.search(home, text_user)):
        print(random.choice(msg_home))
    #says his job
    elif (re.search(job, text_user)):
        print(random.choice(msg_job))
    #if blank input
    elif (re.search(blank, text_user)):
        print(random.choice(msg_blank))
    #default
    else:
        print(random.choice(msg_unknown))
