question = input("What is your question?")
print(question)

while question != "quit":
    print(question)
    if question[-1] != '?':
        print("I'm sorry, I can only answer questions")
