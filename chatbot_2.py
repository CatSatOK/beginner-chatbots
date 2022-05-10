import random

#get user name
print("BOT: What do you want me to call you?")
user_name = input()

#templates
bot_template = "BOT : {0}"
user_template = user_name + " : {0}"

#defining variables
name = "Bad bot" 
weather = "rainy" 
mood = "grumpy"

#creating responses
responses = {
    "what's your name?" : [
        "You may call me Mr {0}".format(name),
        "I usually go by {0}".format(name)],
    "what's today's weather?": [ 
        "Today its {0}".format(weather), 
        "It's {0} today".format(weather)],
    "how are you?" : [
        "I'm {0} as always".format(mood), 
        "{0}! How about you?".format(mood)],
    "how old are you?" : [
        "don't you know its rude to ask that?"],
    "default": [
        "Does not compute"]
}

#defining response method
def respond(message):
    if message in responses: 
        bot_message = random.choice(responses[message])
    else: 
        bot_message = random.choice(responses["default"])
    return bot_message

#function for related responses
def related(x_text): 
    if "name" in x_text: 
        y_text = "what's your name?"
    elif "weather" in x_text: 
        y_text = "what's today's weather?"
    elif "how are" in x_text: 
        y_text = "how are you?"
    else: 
        y_text = ""
    return y_text

#sending message function
def send_message(message): 
  print(user_template.format(message)) 
  response = respond(message) 
  print(bot_template.format(response))

#testing
while 1: 
    my_input = input() 
    my_input = my_input.lower() 
    related_text = related(my_input) 
    send_message(related_text)
    if my_input == "exit" or my_input == "stop": 
        break
