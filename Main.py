# Ryan Smith

# Harry Potter Sorting Hat Quiz


# Takes questions from external .txt file and stores it in a list
# Cite: https://qiita.com/visualskyrim/items/1922429a07ca5f974467
# # That url showed me how to import the .txt file without \n at the end of each line
questionList = [line.rstrip('\n') for line in open("HP_Sort_Questions.txt")]

# The house descriptions were take from https://harrypotter.fandom.com/wiki/Hogwarts_Houses
houseDescList = [line.rstrip('\n') for line in open("House_Desc.txt")]

# Contains Intro and Instructions
intro = [line.rstrip('\n') for line in open("Intro_Instructions.txt")]

# declaring house variables
gryffindor = 0
slytherin = 0
ravenclaw = 0
hufflepuff = 0


# This function takes the users input and converts adds to the corresponding house's score
# cite: http://www.newthinktank.com/2016/07/learn-program-5/
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



# Cite: http://www.newthinktank.com/2016/06/learn-program-3/
# # This tutorial taught me how to use a while loop to check for proper input
def questionInput():
    # While loop checks if valid input.
    while True:
        try:
            ans = input()
            if len(ans) != 1:  # Checks if input is multiple characters. If so it is rejected
                print("Invalid Input. Try Again.")
                continue
            elif (65 <= ord(ans) <= 68) or (97 <= ord(ans) <= 100):  # checks if 'A' - 'D' or 'a' - 'd'
                if ans == "A" or ans == "a":
                    ans = 1
                elif ans == "B" or ans == "b":
                    ans = 2
                elif ans == "C" or ans == "c":
                    ans = 3
                else:
                    ans = 4

            ans = int(ans)

            if ans > 4 or ans < 1:  # Checks for proper input
                print("Invalid Input. Try Again.")
                continue

            answerSelect(ans)
            break

        except ValueError:
            print("Invalid Input. Try Again.")



# Intro/Instructions
for i in intro:
    print(i)

# Questions
for i in range(0, len(questionList)):
    print(questionList[i])
    if i % 5 == 0 and i != 0:  # this prints out the full question before asking for the input
        questionInput()
        print()

# # Testing
# print("Gryffindor:", gryffindor)
# print("Slytherin:", slytherin)
# print("Ravenclaw:", ravenclaw)
# print("Hufflepuff:", hufflepuff)

# Calculate the users percentage in each house
totalScore = gryffindor + slytherin + ravenclaw + hufflepuff
percentGryff = gryffindor / totalScore * 100
percentSlyth = slytherin / totalScore * 100
percentRaven = ravenclaw / totalScore * 100
percentHuffle = hufflepuff / totalScore * 100

# used in below while loop to see what percentage in each house is largest for the user
checkUnsort = [percentGryff, percentSlyth, percentRaven, percentHuffle]
checkSort = sorted(checkUnsort, reverse=True)

# This While Loop checks to see which house the user belongs in. It also checks to see if there is a tie.
# If there is a tie it will ask a tie breaker question until there is no longer a tie.
q = 1
while q != 0:
    if checkSort[0] != checkSort[1]:
        if checkUnsort[0] == checkSort[0]:
            print("You got Gryffindor!\n")
            print(houseDescList[0])
        elif checkUnsort[1] == checkSort[0]:
            print("You got Slytherin!\n")
            print(houseDescList[1])
        elif checkUnsort[2] == checkSort[0]:
            print("You got Ravenclaw!\n")
            print(houseDescList[2])
        else:
            print("You got Hufflepuff!\n")
            print(houseDescList[3])
        break
    elif checkSort[0] == checkSort[1]:
        resultsDict = {"Gryffindor: ": percentGryff,
                       "Slytherin:  ": percentSlyth,
                       "Ravenclaw:  ": percentRaven,
                       "Hufflepuff: ": percentHuffle}

        print("\nResults:")

        for x, y in resultsDict.items():
            print(x, "{:,.2f}%".format(y))

        print(
            "\nTie Breaker Question:\nWhich house do you want to be in?\n   1. Gryffindor\n   2. Slytherin\n   3. Ravenclaw\n   4. Hufflepuff")
        questionInput()

        totalScore = gryffindor + slytherin + ravenclaw + hufflepuff
        percentGryff = gryffindor / totalScore * 100
        percentSlyth = slytherin / totalScore * 100
        percentRaven = ravenclaw / totalScore * 100
        percentHuffle = hufflepuff / totalScore * 100

        checkUnsort = [percentGryff, percentSlyth, percentRaven, percentHuffle]
        checkSort = sorted(checkUnsort, reverse=True)
        continue
q = 0

# # Testing
# print("Gryffindor:", gryffindor)
# print("Slytherin:", slytherin)
# print("Ravenclaw:", ravenclaw)
# print("Hufflepuff:", hufflepuff)

resultsDict = {"Gryffindor: ": percentGryff,
               "Slytherin:  ": percentSlyth,
               "Ravenclaw:  ": percentRaven,
               "Hufflepuff: ": percentHuffle}
print("\nFinal Results:")
for x, y in resultsDict.items():
    print(x, "{:,.2f}%".format(y))
