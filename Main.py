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
            ans = input()

            if (65 <= ord(ans) <= 68) or (97 <= ord(ans) <= 100):
                if ans == "A" or ans == "a":
                    ans = 1
                elif ans == "B" or ans == "b":
                    ans = 2
                elif ans == "C" or ans == "c":
                    ans = 3
                elif ans == "D" or ans == "d":
                    ans = 4
                else:
                    print("Invalid Input. Try Again.")
                    continue

            ans = int(ans)

            if ans > 4 or ans < 1:
                print("Invalid Input. Try Again.")
                continue

            answerSelect(ans)
            break

        except ValueError:
            print("Invalid Input. Try Again.")
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
print("* Answer each question with the corresponding number.\n    *A, B, C, and D will also work")
print("* Answer as truthfully as possible.")
print("* Have fun!")

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

resultsDict = {"Gryffindor: ": (gryffindor / totalScore * 100),
               "Slytherin:  ": (slytherin / totalScore * 100),
               "Ravenclaw:  ": (ravenclaw / totalScore * 100),
               "Hufflepuff: ": (hufflepuff / totalScore * 100)}

for i in resultsDict:
    print(i, end="")
    print(resultsDict[i])