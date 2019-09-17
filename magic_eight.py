# This is the magic_eight.py file

user_input = input("What is your question? ")

for response in user_input[-1]:
    if user_input == "?":
        pass
    elif user_input == "quit":
        break
    else:
        print("I'm sorry, I can only answer questions")
