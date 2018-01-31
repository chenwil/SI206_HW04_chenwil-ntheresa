from random import randrange

lst_of_answers =  ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", " You may rely on it",
"As I see it, yes", "Most likely", "Outlook good", "Yes", " Signs point to yes", "Reply hazy try again",
"Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it",
"My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

def askQuestion():
    question = input("What is your question? ")
    return question

def checkQuestion(question):
    if question[-1] != '?':
        print("I'm sorry, I can only answer questions")
        return False
    else:
        return True

def answerQuestion():
        random_answer = randrange(0,len(lst_of_answers))
        print(lst_of_answers[random_answer])


i = askQuestion()
while i != 'quit':
    if checkQuestion(i) != False:
        answerQuestion()
    i = askQuestion()
