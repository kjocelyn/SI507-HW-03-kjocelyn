# This is the magic_eight.py file
import random
user_input = input("What is your question? ")

answers=[" Yes - definitely.","It is certain", "It is decidedly so","Without a doubt."," Yes - definitely."
        "You may rely on it.","As I see it, yes."," Most likely.",
        "Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again."
        "Ask again later.","Better not tell you now.","Cannot predict now.",
        "Concentrate and ask again.","Don't count on it.","My reply is no.",
        "My sources say no.","Outlook not so good.","Very doubtful."]
 
#print (random.choice(answers))


while True:
    if user_input[-1] == "?":
        print(random.choice(answers)) 
        user_input = input("What is your question? ")
    elif user_input == "quit":
        break
    else:
        print("I'm sorry, I can only answer questions")
        user_input = input("What is your question? ")
       
