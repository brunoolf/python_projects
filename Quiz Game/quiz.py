# Game made for my college project. 

# A game made for you to guess which continent each country is from.

# brunoo_lf

def game_new():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print ("------")
        print(key)
        for i in options[question_num -1]:
            print(i)
        guess = input ("Select ( A , B , C )")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1


    display_score(correct_guesses, guesses)

def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print ("--------------")
    print ("RESULT")
    print ("--------------")

    print ("Correct answers: ", end="")
    for i in questions:
        print(questions.get(i), end ="")
    print()

    print("Your answers: " , end ="")
    for i in guesses:
        print( i , end ="")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your pontuation is: " +str(score)+" Points")


questions = {
    "From what continent is Canada? " : "A",
    "From what continent is Egypt? " : "C",
    "From what continent is Australia? " : "A",
    "From what continent is Colombia? " : "A",
    "From what continent is Spain? " : "B",
    "From what continent is Mexico? " : "C",
    "From what continent is Germany? " : "C",
    "From what continent is Ecuador? " : "A",
    "From what continent is Greece? " : "B",
    "From what continent is Peru? " : "B",
}

options = [
    ["A. North America ", "B. Africa ", "C. Asia"],
    ["A. Europe", "B. Asia", "C. Africa"],
    ["A. Oceania ", "B. Africa", "C. Antarctica"],
    ["A. South America", "B. Asia", "C. North America"],
    ["A. North America ", "B. Europe ", "C. Asia"],
    ["A. Europe", "B. Asia", "C. North America"],
    ["A. Oceania ", "B. North America", "C. Europe "],
    ["A. South America", "B. Asia ", "C. Antarctica "],
    ["A. South America", "B. Europe", "C. Asia"],
    ["A. Europe", "B. South America ", "C. Asia"],
]

game_new()

print("Good bye!")
