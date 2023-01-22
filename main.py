import random

cards = [("asso","oro"), ("asso","bastoni"),("asso","spade"),("asso","coppe"),("due","oro"),("due","bastoni"),("due","spade"),("due","coppe"), ("tre","oro"), ("tre","bastoni"), ("tre","spade"), ("tre","coppe"), ("quattro","oro"), ("quattro","bastoni"), ("quattro","spade"), ("quattro","coppe"), ("cinque","oro"), ("cinque","bastoni"), ("cinque","spade"), ("cinque","coppe"), ("sei","oro"), ("sei","bastoni"), ("sei","spade"), ("sei","coppe"), ("sette","oro"), ("sette","bastoni"), ("sette","spade"), ("sette","coppe"), ("donna","oro"), ("donna","bastoni"), ("donna","spade"), ("donna","coppe"), ("cavallo","oro"), ("cavallo","bastoni"), ("cavallo","spade"), ("cavallo","coppe"), ("re","oro"), ("re","bastoni"), ("re","spade"), ("re","coppe")]
deck = cards
deck.remove(("cavallo","oro"))
deck.remove(("cavallo","bastoni"))
deck.remove(("cavallo","spade"))
deck.remove(("cavallo","coppe"))
points = {"oro":0,"bastoni":0,"spade":0,"coppe":0}
players = {} 

bids = points.copy()
bet_suit = ""

def pesca_carta():
    i = random.randint(0,len(deck)-1)
    carta_pescata = deck.pop(i)
    suit = carta_pescata[1]
    numero = carta_pescata[0]
    print("\npescato: ",numero," di ",suit)
    points.update({suit: points.get(suit)+1})
    print(points)
    return carta_pescata

def place_bids():
    print("Choose horse where to bet:")
    print("1. Oro")
    print("2. Bastoni")
    print("3. Spade")
    print("4. Coppe")
    choice = int(input("> "))
    if (choice == 1): bet_suit = "oro"
    elif (choice == 2): bet_suit = "bastoni"
    elif (choice == 3): bet_suit = "spade"
    elif (choice == 4): bet_suit = "coppe"
    else:
        print("you bloody bastard")
        place_bids()
    print("Choose how much to bet")
    choice = int(input("> "))
    bids.update({bet_suit: bids.get(bet_suit)+choice})
    print(bids)

def menu():
    print("1. Add player")
    print("2. Remove player")
    print("3. Start race")
    print("4. End current game")
    print("0. Exit")
    choice = int(input("> "))
    if (choice == 0): return 0
    if(choice == 1): add_player()
    elif(choice == 2): remove_player()
    elif(choice == 3): start_race()
    elif(choice == 4): end_race()
    else: 
        print("you dumb bitch")
        menu()

def add_player():
    name = input("new player name: ")
    players.update({name: 0})
    
def remove_player():
    for player in players:
        print(player,end=", ")
    choice = input("player to remove: ")
    try:
        del players[choice]
    except: 
        print(choice, " is not a player")
        remove_player()

def start_race():
    place_bids()
    won = False
    for i in range(0,36):
        if not won:
            carta = pesca_carta()
            if (points.get(carta[1]) >= 9):
                won = True
                print("\nWon: ",carta[1]," bet: ",bids.get(carta[1]))
                break
    
def end_race():
    print("Results:")
    print(players)

def main():
    x = menu()
    while (x != 0):
        x = menu()
    
main()
