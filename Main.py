# Ryan Smith

# Harry Potter Sorting Hat Quiz

# declaring house type variables
gryffindor = 0
slytherin = 0
ravenclaw = 0
hufflepuff = 0


# This function takes the users input and converts adds to the corresponding house's score
def answerSelect(answer):
    global gryffindor
    global slytherin
    global ravenclaw
    global hufflepuff
    if answer == 1:
        gryffindor = gryffindor + 1
    elif answer == 2:
        slytherin = slytherin + 1
    elif answer == 3:
        ravenclaw = ravenclaw + 1
    elif answer == 4:
        hufflepuff = hufflepuff + 1

def questionInput(question):
    # While loop checks if valid input.
    while True:
        try:
            print(question)
            ans = int(input())
            answerSelect(ans)

            if ans > 4 or ans < 1:
                print("Invalid Input. Try Again.")
                continue

            break

        except ValueError:
            print("Invalid Input. Try Again.")

        except:
            print("Unforeseen Error Occurred. Try Again. ")
    # Cite: http://www.newthinktank.com/2016/06/learn-program-3/
    # # This tutorial taught me how to use a while loop to check for proper input

# cite: http://www.newthinktank.com/2016/07/learn-program-5/
# # This tutorial taught me how to use functions in python

# Intro/Instructions
print("Welcome Witches and Wizards!")
print("This Quiz will tell you which Hogwarts house you belong in.")
print("It will tell you your next closest matching house, and the percentage you are of each house.")
print()
print("-----INSTRUCTIONS-----")
print("* Answer each question with the corresponding number.")
print("* A, B, C, D, a, b, c, and d will not work")
print("* That is it... it's pretty simple.")

# Question 1
questionInput("Testing 123\nFudge")

# Testing
print("Gryffindor:", gryffindor)
print("Slytherin:", slytherin)
print("Ravenclaw:", ravenclaw)
print("Hufflepuff:", hufflepuff)

# calculate which house you are in
totalScore = gryffindor + slytherin + ravenclaw + hufflepuff

percentGryff = gryffindor / totalScore * 100
percentSlyth = slytherin / totalScore * 100
percentRaven = ravenclaw / totalScore * 100
percentHuffle = hufflepuff / totalScore * 100
