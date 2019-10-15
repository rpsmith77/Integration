# Ryan Smith

# Harry Potter Sorting Hat Quiz

# Cite: http://www.newthinktank.com/2016/07/learn-program-9/
# # Taught me how to use classes


class House:

    def __init__(self, name="", score=0, descript=None, percent=0.0):  # function that creates each house
        if descript is None:  
            descript = []
        self.name = name
        self.score = score
        self.descript = descript
        self.percent = percent

    # cite: http://www.newthinktank.com/2016/07/learn-program-5/
    # # This tutorial taught me how to use functions in python
    @staticmethod
    def runQuiz():
        # Cite: http://www.newthinktank.com/2016/06/learn-program-3/
        # # This tutorial taught me how to use a while loop to check for proper input

        while True:  # Makes sure input is valid
            try:
                ans = input()

                if len(ans) != 1:  # Checks if input is multiple characters. If so it is rejected
                    print("Invalid Input. Try Again.")
                    continue

                elif (65 <= ord(ans) <= 68) or (97 <= ord(ans) <= 100):  # checks if 'A' - 'D' or 'a' - 'd'
                    if ans == "A" or ans == "a":
                        return 1
                    elif ans == "B" or ans == "b":
                        return 2
                    elif ans == "C" or ans == "c":
                        return 3
                    else:
                        return 4

                ans = int(ans)

                if ans > 4 or ans < 1:  # Checks for proper input
                    print("Invalid Input. Try Again.")
                    continue

                return ans

            except ValueError:
                print("Invalid Input. Try Again.")

    @staticmethod
    def doSorting(house1, house2, house3, house4):  # Sorts you into your correct house
        house = House()
        checkUnsort = [house1, house2, house3, house4]
        checkSort = sorted(checkUnsort, reverse=True)

        while True:

            if checkSort[0] != checkSort[1]:  # Checks if there is a tie

                if checkUnsort[0] == checkSort[0]:  # comparing sorted to unsorted to tell which house to sort user in
                    return 0
                elif checkUnsort[1] == checkSort[0]:
                    return 1
                elif checkUnsort[2] == checkSort[0]:
                    return 2
                else:
                    return 3

            else:
                print("You tied two for two or more houses. Choose Which House you wish to belong to!"
                      "\n1. Gryffindor\n2. Slytherin\n3. Ravenclaw\n4. Hufflepuff")
                print("Gryffindor: {:.2f}%".format(findPercentage(house1, house2, house3, house4)))
                print("Slytherin:  {:.2f}%".format(findPercentage(house2, house1, house3, house4)))
                print("Ravenclaw:  {:.2f}%".format(findPercentage(house3, house2, house1, house4)))
                print("Hufflepuff: {:.2f}%".format(findPercentage(house4, house2, house3, house1)))

                answer = house.runQuiz()

                if answer == 1:
                    return 5
                elif answer == 2:
                    return 6
                elif answer == 3:
                    return 7
                else:
                    return 8


def findPercentage(h1, h2, h3, h4):
    return (h1 / (h1 + h2 + h3 + h4)) * 100


def main():
    # Takes questions from external .txt file and stores it in a list
    # Cite: https://qiita.com/visualskyrim/items/1922429a07ca5f974467
    # # That url showed me how to import the .txt file without \n at the end  of each line
    questionList = [line.rstrip('\n') for line in open("HP_Sort_Questions.txt")]

    # The house descriptions were take from https://harrypotter.fandom.com/wiki/Hogwarts_Houses
    houseDescList = [line.rstrip('\n') for line in open("House_Desc.txt")]

    # Contains Intro and Instructions
    intro = [line.rstrip('\n') for line in open("Intro_Instructions.txt")]

    # Creates each house
    gryffindor = House("Gryffindor", 0, houseDescList[0:8])
    slytherin = House("Slytherin", 0, houseDescList[9:17])
    ravenclaw = House("Ravenclaw", 0, houseDescList[19:26])
    hufflepuff = House("Hufflepuff", 0, houseDescList[28:38])

    house = House()

    for i in intro:  # prints intro
        print(i)

    print()  # Formatting

    for i in range(0, len(questionList)):  # Prints out the question and answer options before
        print(questionList[i])
        if i % 5 == 0 and i != 0:
            answer = house.runQuiz()

            if answer == 1:
                gryffindor.score += 1
            elif answer == 2:
                slytherin.score += 1
            elif answer == 3:
                ravenclaw.score += 1
            else:
                hufflepuff.score += 1

            print()

    while True:

        result = house.doSorting(gryffindor.score, slytherin.score, ravenclaw.score, hufflepuff.score)

        if result > 4:  # If it was tied this adds to the house's score
            if result == 5:
                gryffindor.score += 1
            elif result == 6:
                slytherin.score += 1
            elif result == 7:
                ravenclaw.score += 1
            else:
                hufflepuff.score += 1

        else:
            if result == 0:
                print("You were sorted into {}!".format(gryffindor.name), "\n")
                print(*gryffindor.descript, sep="\n")  # * operator prints every item in the list
                break
            elif result == 1:
                print("You were sorted into {}!".format(slytherin.name), "\n")
                print(*slytherin.descript, sep="\n")
                break
            elif result == 2:
                print("You were sorted into {}!".format(ravenclaw.name), "\n")
                print(*ravenclaw.descript, sep="\n")
                break
            else:
                print("You were sorted into {}!".format(hufflepuff.name), "\n")
                print(*hufflepuff.descript, sep="\n")
                break

    gryffindor.percent = findPercentage(gryffindor.score, slytherin.score, ravenclaw.score, hufflepuff.score)
    slytherin.percent = findPercentage(slytherin.score, gryffindor.score, ravenclaw.score, hufflepuff.score)
    ravenclaw.percent = findPercentage(ravenclaw.score, slytherin.score, gryffindor.score, hufflepuff.score)
    hufflepuff.percent = findPercentage(hufflepuff.score, slytherin.score, ravenclaw.score, gryffindor.score)

    print("\nFinal Results:")
    print(gryffindor.name, "{:.2f}%".format(gryffindor.percent))
    print(slytherin.name, "{:.2f}%".format(slytherin.percent))
    print(ravenclaw.name, "{:.2f}%".format(ravenclaw.percent))
    print(hufflepuff.name, "{:.2f}%".format(hufflepuff.percent))


main()
