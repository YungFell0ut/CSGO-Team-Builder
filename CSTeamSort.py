import random
import socket

def Server():
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP
    ServerSocket.bind((socket.gethostname(), 1337))  # Connect on the most elite port
    ServerSocket.listen(10)  # Ten clients can connect

    while True:
        ClientSocket, address = ServerSocket.accept()
        print(f"{address} has connected!")
        ClientSocket.send(TeamOneMsg.encode("utf-8"))



def Setup():
    global players
    players = []

    for n in range(1,11):
        print(f"Enter Player {n}'s name: ", end= " ")
        players.append(input(""))


def TeamSort(gamers):
    global TeamOne
    global TeamTwo
    global TeamOneMsg
    global TeamTwoMsg

    TeamOne = []
    TeamTwo = []

    TeamOneMsg = ""
    TeamTwoMsg = ""

    TeamOne = random.sample(gamers, 5)

    # Removes the Players in TeamOne
    for i in range(len(TeamOne)):
        gamers.remove(TeamOne[i])

    TeamTwo = random.sample(gamers, 5)

    #  Puts the teams into a string format to send over the network.
    for i in range(len(TeamOne)):
        TeamOneMsg += f"Player {i + 1} on team one is: {TeamOne[i]}"
        TeamOneMsg += "\n"

    for i in range(len(TeamTwo)):
        TeamTwoMsg += f"Player {i + 1} on team two is: {TeamTwo[i]}"
        TeamTwoMsg += "\n"

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
Server()