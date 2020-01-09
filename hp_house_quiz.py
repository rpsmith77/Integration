""" Harry Potter Sorting Hat Quiz by Ryan Smith.
    This project is for my class COP 1500 Intro to Computer Science.
    The purpose of this project is to have a demonstration of the knowledge
    I accumulated during this semester.

    Sources: Descriptions of each House Source:
                    https://harrypotter.fandom.com/wiki/Hogwarts_Houses

             Quiz questions: Taken from the official Harry Potter Sorting Hat
                             Quiz on Pottermore.com (Site now down)

    __author__ = Ryan Smith """


# Cite: http://www.newthinktank.com/2016/07/learn-program-9/
# # Taught me how to use classes


class House:
    """
    This class creates each house the user can be sorted into

    Attributes:
        name (str): house name
        score (int): user's score
        descript (lis): description of the house
        percent (float): user's percentage of answers corresponding with
                         this house
    """

    def __init__(self, name="", score=0, descript=None, percent=0.0):
        """
        The constructor for the class House

        :param name: house name
        :param score: user's score
        :param descript: description of the house
        :param percent: user's percentage of answers corresponding with
                        this house
        """

        if descript is None:
            descript = []
        self.name = name
        self.score = score
        self.descript = descript
        self.percent = percent

    # Cite: http://www.newthinktank.com/2016/07/learn-program-5/
    # This tutorial taught me how to use functions in python

    @staticmethod
    def run_quiz():

        """
        Asks the quiz questions and interpret user input

        :return: integer associated with a specific house
        """

        # Cite: http://www.newthinktank.com/2016/06/learn-program-3/ # This
        # tutorial taught me how to use a while loop to check for proper input

        while True:  # Loop checking for valid input
            try:
                user_input = input()

                if len(user_input) != 1:
                    print("Invalid Input. Try Again.")
                    continue
                elif ('a' <= user_input <= 'd') or ('A' <= user_input <= 'D'):
                    if user_input in ('A', 'a'):
                        return 1
                    elif user_input in ('B', 'b'):
                        return 2
                    elif user_input in ('C', 'c'):
                        return 3
                    else:
                        return 4

                user_input = int(user_input)

                if user_input > 4 or user_input < 1:
                    print("Invalid Input. Try Again.")
                    continue

                return user_input

            except ValueError:
                print("Invalid Input. Try Again.")

    @staticmethod
    def do_sorting(gryffindor_score, slytherin_score, ravenclaw_score,
                   hufflepuff_score):
        """
        Sort user into correct house

        :param gryffindor_score: # of time user answered gryffindor
        :param slytherin_score: # of time user answered slytherin
        :param ravenclaw_score: # of time user answered ravenclaw
        :param hufflepuff_score: # of time user answered hufflepuff
        :return: result of quiz
        """
        house = House()
        unsorted_results = [gryffindor_score, slytherin_score, ravenclaw_score,
                            hufflepuff_score]
        sorted_results = sorted(unsorted_results, reverse=True)

        while True:

            if sorted_results[0] != sorted_results[1]:

                if unsorted_results[0] == sorted_results[0]:
                    return 0
                elif unsorted_results[1] == sorted_results[0]:
                    return 1
                elif unsorted_results[2] == sorted_results[0]:
                    return 2
                else:
                    return 3

            else:
                print("You tied two for two or more houses. Choose Which "
                      "House you wish to belong to! "
                      "\n1. Gryffindor\n2. Slytherin\n3. Ravenclaw\n4. "
                      "Hufflepuff")
                print("Gryffindor: {:.2f}%".format
                      (find_percentage(gryffindor_score, slytherin_score,
                                       ravenclaw_score, hufflepuff_score)))
                print("Slytherin:  {:.2f}%".format
                      (find_percentage(slytherin_score, gryffindor_score,
                                       ravenclaw_score, hufflepuff_score)))
                print("Ravenclaw:  {:.2f}%".format
                      (find_percentage(ravenclaw_score, slytherin_score,
                                       gryffindor_score, hufflepuff_score)))
                print("Hufflepuff: {:.2f}%".format
                      (find_percentage(hufflepuff_score, slytherin_score,
                                       ravenclaw_score, gryffindor_score)))

                tiebreaker_input = house.run_quiz()

                if tiebreaker_input == 1:
                    return 5
                elif tiebreaker_input == 2:
                    return 6
                elif tiebreaker_input == 3:
                    return 7
                else:
                    return 8


def find_percentage(house_1, house_2, house_3, house_4):
    """
    Calculates each house's percentage.
    :param house_1: The house whose percentage is being calculated
    :param house_2: used to calculate percentage
    :param house_3: used to calculate percentage
    :param house_4: used to calculate percentage
    :return: house_1's percentage
    """
    return (house_1 / (house_1 + house_2 + house_3 + house_4)) * 100


def main():
    """
    The main function that runs the program
    """
    # Takes questions from external .txt file and stores it in a list
    # Cite:https://qiita.com/visualskyrim/items/1922429a07ca5f974467
    # That url showed me how to import the .txt file without \n at the end
    # of each line
    quiz_questions = [line.rstrip('\n') for line in
                      open("HP_Sort_Questions.txt")]

    # The house descriptions were take from
    # https://harrypotter.fandom.com/wiki/Hogwarts_Houses
    house_descriptions = [line.rstrip('\n') for line in open("House_Desc.txt")]

    # Contains Intro and Instructions
    intro = [line.rstrip('\n') for line in open("Intro_Instructions.txt")]

    # Create each house
    gryffindor = House("Gryffindor", descript=house_descriptions[0:8])
    slytherin = House("Slytherin", descript=house_descriptions[9:17])
    ravenclaw = House("Ravenclaw", descript=house_descriptions[19:26])
    hufflepuff = House("Hufflepuff", descript=house_descriptions[28:38])

    house = House()

    sort_loop = True

    for i in intro:  # prints intro
        print(i)

    print()  # Formatting

    for i in range(0, len(quiz_questions)):  # Prints out the question and
        # answer options before
        print(quiz_questions[i])
        if i % 5 == 0 and i != 0:
            answer = house.run_quiz()

            if answer == 1:
                gryffindor.score += 1
            elif answer == 2:
                slytherin.score += 1
            elif answer == 3:
                ravenclaw.score += 1
            else:
                hufflepuff.score += 1

            print()

    while sort_loop:

        sort_results = house.do_sorting(gryffindor.score, slytherin.score,
                                        ravenclaw.score, hufflepuff.score)

        if sort_results > 4:  # If it was tied this adds to the house's score
            if sort_results == 5:
                gryffindor.score += 1
            elif sort_results == 6:
                slytherin.score += 1
            elif sort_results == 7:
                ravenclaw.score += 1
            else:
                hufflepuff.score += 1

        else:
            if sort_results == 0:
                print("You were sorted into {}!".format(gryffindor.name), "\n")
                print(*gryffindor.descript, sep="\n")  # * operator prints
                sort_loop = False
            elif sort_results == 1:
                print("You were sorted into {}!".format(slytherin.name), "\n")
                print(*slytherin.descript, sep="\n")
                sort_loop = False
            elif sort_results == 2:
                print("You were sorted into {}!".format(ravenclaw.name), "\n")
                print(*ravenclaw.descript, sep="\n")
                sort_loop = False
            else:
                print("You were sorted into {}!".format(hufflepuff.name), "\n")
                print(*hufflepuff.descript, sep="\n")
                sort_loop = False

    gryffindor.percent = find_percentage(gryffindor.score, slytherin.score,
                                         ravenclaw.score, hufflepuff.score)
    slytherin.percent = find_percentage(slytherin.score, gryffindor.score,
                                        ravenclaw.score, hufflepuff.score)
    ravenclaw.percent = find_percentage(ravenclaw.score, slytherin.score,
                                        gryffindor.score, hufflepuff.score)
    hufflepuff.percent = find_percentage(hufflepuff.score, slytherin.score,
                                         ravenclaw.score, gryffindor.score)

    print("\nFinal Results:")
    print(gryffindor.name, "{:.2f}%".format(gryffindor.percent))
    print(slytherin.name, "{:.2f}%".format(slytherin.percent))
    print(ravenclaw.name, "{:.2f}%".format(ravenclaw.percent))
    print(hufflepuff.name, "{:.2f}%".format(hufflepuff.percent))


main()
