import random
import socket

def ServerSetup():
    pass

def Setup():
    global players
    players = []

    for n in range(1,11):
        print(f"Enter Player {n}'s name: ", end= " ")
        players.append(input(""))


def TeamSort(gamers):
    global TeamOne
    global TeamTwo

    TeamOne = []
    TeamTwo = []

    TeamOne = random.sample(gamers, 5)

    # Removes the Players in TeamOne
    for i in range(len(TeamOne)):
        gamers.remove(TeamOne[i])

    TeamTwo = random.sample(gamers, 5)

    # Print the two teams out
    print("\n")
    for i in range(len(TeamOne)):
        print(f"Player {i + 1} on team one is: {TeamOne[i]}")

    print("\n")

    for i in range(len(TeamTwo)):
        print(f"Player {i + 1} on team Two is: {TeamTwo[i]}")


def MapSort():
    global PlayMaps
    PlayMaps = []

    Maps = ["Dust II", "Office", "Mirage", "Inferno", "Overpass", "Nuke", "Italy", "Militia"]

    PlayMaps = random.sample(Maps, 3)

    print(f"The maps are {PlayMaps[0]}, {PlayMaps[1]}, {PlayMaps[2]}")


Setup()
TeamSort(players)
MapSort()
