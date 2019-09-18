#Ryan Smith

#Harry Potter Sorting Hat Quiz

#declaring house type variables
gryffindor = 0
slytherin = 0
ravenclaw = 0
hufflepuff = 0

print("Welcome")

#variables to show print platform 9 and 3/4 in a long way.
platform9 = str(3 ** 2)
platform3 = str(10 // 3)
platform4 = str(9 % 5)

print("The train will leave from Platform", platform9 , "and", platform3 + "/" + platform4)
print()

#Intro/Instructions
print("This Quiz will tell you which Hogwarts house you belong in.")
print("It will tell you your next closest matching house, and the percentage you are of each house.")
print()
print("-----INSTRUCTIONS-----")
print("* Answer each question with the corresponding number.")
print("* A, B, C, D, a, b, c, and d will not work")
print("* That is it... it's pretty simple.")

#cite: http://www.newthinktank.com/2016/07/learn-program-5/
# # This tutorial taught me how to use functions in python
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
    else:
        print("Invalid Input")

#Question 1
print("Question 1: \nTest")
answerSelect(int(input()))
print("Gryffindor:", gryffindor)
print("Slytherin:", slytherin)
print("Ravenclaw:", ravenclaw)
print("Hufflepuff:", hufflepuff)
