# This is the magic_eight.py file

user_input = input("What is your question? ")

while True:
    if user_input[-1] == "?":
        print("answers") #change "answer" according to the right code when merging
        user_input = input("What is your question? ")
    if user_input == "quit":
        break
    else:
        print("I'm sorry, I can only answer questions")
        user_input = input("What is your question? ")
          

   
    

