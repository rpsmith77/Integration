import Main
import random


class Character:

    def __init__(self, stats=None, name="John Doe", house="Gryffindor", level=1, actions=None):
        if stats is None:
            stats = {}
        if actions is None:
            actions = ["Nothing", "Punch"]
        self.stats = stats
        self.name = name
        self.house = house
        self.level = level
        self.actions = actions


def makeStats(quizResults):
    stats = {
        "Intelligence": 10,
        "Wisdom": 10,
        "Dexterity": 10,
        "Charisma": 10,
        "Constitution": 10,
        "Strength": 10
    }
    # Gryffindor Stat Changes
    if quizResults[0] == 100:
        stats["Intelligence"] += -2
        stats["Wisdom"] += -3
        stats["Dexterity"] += 4
        stats["Charisma"] += 6
        stats["Constitution"] += 8
        stats["Strength"] += 6
    elif quizResults[0] >= 75:
        stats["Intelligence"] += -1
        stats["Wisdom"] += -2
        stats["Dexterity"] += 3
        stats["Charisma"] += 3
        stats["Constitution"] += 5
        stats["Strength"] += 4
    elif quizResults[0] >= 50:
        stats["Intelligence"] += 0
        stats["Wisdom"] += -1
        stats["Dexterity"] += 1
        stats["Charisma"] += 2
        stats["Constitution"] += 4
        stats["Strength"] += 3
    elif quizResults[0] >= 25:
        stats["Intelligence"] += 0
        stats["Wisdom"] += 0
        stats["Dexterity"] += 0
        stats["Charisma"] += 1
        stats["Constitution"] += 3
        stats["Strength"] += 2
    elif quizResults[0] >= 10:
        stats["Intelligence"] += 0
        stats["Wisdom"] += 0
        stats["Dexterity"] += 0
        stats["Charisma"] += 0
        stats["Constitution"] += 2
        stats["Strength"] += 1

    # Slytherin Stat Change
    if quizResults[1] == 100:
        stats["Intelligence"] += 4
        stats["Wisdom"] += 6
        stats["Dexterity"] += 8
        stats["Charisma"] += 6
        stats["Constitution"] += -3
        stats["Strength"] += -2
    elif quizResults[1] >= 75:
        stats["Intelligence"] += 3
        stats["Wisdom"] += 3
        stats["Dexterity"] += 5
        stats["Charisma"] += 4
        stats["Constitution"] += -2
        stats["Strength"] += -1
    elif quizResults[1] >= 50:
        stats["Intelligence"] += 1
        stats["Wisdom"] += 2
        stats["Dexterity"] += 3
        stats["Charisma"] += 4
        stats["Constitution"] += -1
        stats["Strength"] += 0
    elif quizResults[1] >= 25:
        stats["Intelligence"] += 0
        stats["Wisdom"] += 1
        stats["Dexterity"] += 2
        stats["Charisma"] += 3
        stats["Constitution"] += 0
        stats["Strength"] += 0
    elif quizResults[1] >= 10:
        stats["Intelligence"] += 0
        stats["Wisdom"] += 0
        stats["Dexterity"] += 1
        stats["Charisma"] += 2
        stats["Constitution"] += 0
        stats["Strength"] += 0

    # Ravenclaw Stat Change
    if quizResults[2] == 100:
        stats["Intelligence"] += 0
        stats["Wisdom"] += 8
        stats["Dexterity"] += 6
        stats["Charisma"] += -4
        stats["Constitution"] += 6
        stats["Strength"] += 0
    elif quizResults[2] >= 75:
        stats["Intelligence"] += 0
        stats["Wisdom"] += 6
        stats["Dexterity"] += 5
        stats["Charisma"] += -3
        stats["Constitution"] += 5
        stats["Strength"] += 0
    elif quizResults[2] >= 50:
        stats["Intelligence"] += 0
        stats["Wisdom"] += 5
        stats["Dexterity"] += 3
        stats["Charisma"] += -2
        stats["Constitution"] += 3
        stats["Strength"] += 0
    elif quizResults[2] >= 25:
        stats["Intelligence"] += 0
        stats["Wisdom"] += 5
        stats["Dexterity"] += 3
        stats["Charisma"] += -2
        stats["Constitution"] += 3
        stats["Strength"] += 0
    elif quizResults[2] >= 10:
        stats["Intelligence"] += 2
        stats["Wisdom"] += 0
        stats["Dexterity"] += 1
        stats["Charisma"] += 0
        stats["Constitution"] += 0
        stats["Strength"] += 0

    # Hufflepuff Stat Change
    if quizResults[3] == 100:
        stats["Intelligence"] += -1
        stats["Wisdom"] += -3
        stats["Dexterity"] += 6
        stats["Charisma"] += 6
        stats["Constitution"] += 8
        stats["Strength"] += 6
    elif quizResults[3] >= 75:
        stats["Intelligence"] += 0
        stats["Wisdom"] += -2
        stats["Dexterity"] += 3
        stats["Charisma"] += 3
        stats["Constitution"] += 5
        stats["Strength"] += 4
    elif quizResults[3] >= 50:
        stats["Intelligence"] += 0
        stats["Wisdom"] += -1
        stats["Dexterity"] += 3
        stats["Charisma"] += 3
        stats["Constitution"] += 5
        stats["Strength"] += 3
    elif quizResults[3] >= 25:
        stats["Intelligence"] += 0
        stats["Wisdom"] += 0
        stats["Dexterity"] += 1
        stats["Charisma"] += 1
        stats["Constitution"] += 3
        stats["Strength"] += 2
    elif quizResults[3] >= 10:
        stats["Intelligence"] += 0
        stats["Wisdom"] += 0
        stats["Dexterity"] += 0
        stats["Charisma"] += 0
        stats["Constitution"] += 2
        stats["Strength"] += 1

    return stats


def makeNPC_housePercentages(mainHouseName):
    randomHousePercentList = []
    total = 0
    for i in range(3):
        secondaryHousePercent = random.randint(100, 2499) / 100
        randomHousePercentList.append(secondaryHousePercent)
        total += secondaryHousePercent

    mainHousePercent = 100 - total

    housePercentList = []
    if mainHouseName == "Gryffindor":
        housePercentList.append(mainHousePercent)
        for percentage in randomHousePercentList:
            housePercentList.append(percentage)
    elif mainHouseName == "Slytherin":
        housePercentList.append(randomHousePercentList[0])
        housePercentList.append(mainHousePercent)
        housePercentList.append(randomHousePercentList[1])
        housePercentList.append(randomHousePercentList[2])
    elif mainHouseName == "Ravenclaw":
        housePercentList.append(randomHousePercentList[0])
        housePercentList.append(randomHousePercentList[1])
        housePercentList.append(mainHousePercent)
        housePercentList.append(randomHousePercentList[2])
    elif mainHouseName == "Ravenclaw":
        housePercentList.append(randomHousePercentList[0])
        housePercentList.append(randomHousePercentList[1])
        housePercentList.append(randomHousePercentList[2])
        housePercentList.append(mainHousePercent)

    return housePercentList


def makeNPC(npcHouse, level):
    NPC_name = makeNPC_name()
    NPC_housePercentage = makeNPC_housePercentages(npcHouse)

    return Character(makeStats(NPC_housePercentage), NPC_name, npcHouse, level)


def makeNPC_name():
    randomFirstName = random.randint(0,99)
    randomLastName = random.randint(0,99)

    firstName = [line.rstrip('\n') for line in open("NPC_First_Name.txt")]
    lastName = [line.rstrip('\n') for line in open("NPC_Last_Name.txt")]

    combinedName = str(firstName[randomFirstName] + lastName[randomLastName])

    return combinedName


def mainCharacter():
    gryffindorNPC = makeNPC("Gryffindor", 1)

    quizStats = Main.main()
    print(quizStats)

    statistics = makeStats(quizStats)

    name = input("What's your name? ")
    player = Character(statistics, name, "Hufflepuff", 1)
    for key, value in player.stats.items():
        print(key, value)
    print(player.name)
    print(player.house)
    print(player.level)
    print(player.actions)


    print(gryffindorNPC.name)
    for key, value in gryffindorNPC.stats.items():
        print(key, value)
    print(gryffindorNPC.house)
    print(gryffindorNPC.level)
    print(gryffindorNPC.actions)


mainCharacter()
