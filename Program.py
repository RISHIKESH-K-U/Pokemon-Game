# IMPORT NEEDED MODULES
import random
import sys

# CLASS TO DEFINE MOVE


class Move:
    def __init__(self, movename, movetype, movepower, pokemontype):
        self.name = movename
        self.type = movetype
        self.power = float(movepower)
        if movetype == pokemontype:
            self.power = float(movepower) + (float(movepower)*0.5)

# CLASS TO DEFINE POKEMON


class Pokemon:
    def __init__(self, n, t, m1, m2, m3, m4):
        self.name = n
        self.type = t
        self.health = 20
        Move_Data = open("./Moves.txt", "r")
        mc = 0
        while mc < 35:
            data = Move_Data.readline()
            movelist = data.split()
            if movelist[0] == m1:
                self.move1 = Move(m1, movelist[2], movelist[1], t)
            if movelist[0] == m2:
                self.move2 = Move(m2, movelist[2], movelist[1], t)
            if movelist[0] == m3:
                self.move3 = Move(m3, movelist[2], movelist[1], t)
            if movelist[0] == m4:
                self.move4 = Move(m4, movelist[2], movelist[1], t)
            mc += 1

# DISPLAY FUNCTION TO DISPLAY USER POKEMON(AND HEALTH) AND COMPUTER POKEMON(AND HEALTH)


def Display():
    print(UserPokemon.name)
    u = 0
    while u < UserPokemon.health:
        print("|", end="")
        u += 1
    print("\n")
    print(CompPokemon.name)
    v = 0
    while v < CompPokemon.health:
        print("|", end="")
        v += 1
    print("\n")

# FUNCTION FOR USER TO SELECT MOVE


def UserPlay():
    print("CHOOSE YOUR MOVE : \n")
    print("1)", UserPokemon.move1.name, "-", UserPokemon.move1.power, "\n")
    print("2)", UserPokemon.move2.name, "-", UserPokemon.move2.power, "\n")
    print("3)", UserPokemon.move3.name, "-", UserPokemon.move3.power, "\n")
    print("4)", UserPokemon.move4.name, "-", UserPokemon.move4.power, "\n")
    choice = int(input())
    print("\n")
    if choice == 1:
        cmove = UserPokemon.move1.power
    if choice == 2:
        cmove = UserPokemon.move2.power
    if choice == 3:
        cmove = UserPokemon.move3.power
    if choice == 4:
        cmove = UserPokemon.move4.power
    CompPokemon.health = CompPokemon.health - cmove

# FUNCTION TO CHECK IF A POKEMON HAS FAINTED


def Result():
    if UserPokemon.health < 1:
        print(UserPokemon.name, " HAS FAINTED.", CompPokemon.name, " WINS\n")
        print("\nCOMPUTER HAS WON\n")
        sys.exit()
    elif CompPokemon.health < 1:
        print(CompPokemon.name, " HAS FAINTED.", UserPokemon.name, " WINS\n")
        print("\nUSER HAS WON\n")
        sys.exit()
    else:
        pass

# FUNCTION FOR COMPUTER TO PLAY.MOVE HAVING HIGHEST POWER HAS A GREATER CHANCE TO OCCUR


def CompPlay():
    if ((CompPokemon.move1.power >= CompPokemon.move2.power) and (CompPokemon.move1.power >= CompPokemon.move3.power) and (CompPokemon.move1.power >= CompPokemon.move4.power)):
        maxmove = CompPokemon.move1.power
        k = CompPokemon.move1
    if ((CompPokemon.move2.power >= CompPokemon.move1.power) and (CompPokemon.move2.power >= CompPokemon.move3.power) and (CompPokemon.move2.power >= CompPokemon.move4.power)):
        maxmove = CompPokemon.move2.power
        k = CompPokemon.move2
    if ((CompPokemon.move3.power >= CompPokemon.move1.power) and (CompPokemon.move3.power >= CompPokemon.move2.power) and (CompPokemon.move3.power >= CompPokemon.move4.power)):
        maxmove = CompPokemon.move3.power
        k = CompPokemon.move3
    if ((CompPokemon.move4.power >= CompPokemon.move1.power) and (CompPokemon.move4.power >= CompPokemon.move2.power) and (CompPokemon.move4.power >= CompPokemon.move3.power)):
        maxmove = CompPokemon.move4.power
        k = CompPokemon.move4
    decider = random.randint(1, 10)
    if decider >= 2 and decider <= 7:
        print("COMPUTER HAS USED THE MOVE\n ", k.name)
        UserPokemon.health = UserPokemon.health - maxmove
    elif decider == 1:
        print("COMPUTER HAS USED THE MOVE \n", CompPokemon.move1.name)
        UserPokemon.health = UserPokemon.health - CompPokemon.move1.power
    elif decider == 8:
        print("COMPUTER HAS USED THE MOVE\n ", CompPokemon.move2.name)
        UserPokemon.health = UserPokemon.health - CompPokemon.move2.power
    elif decider == 9:
        print("COMPUTER HAS USED THE MOVE\n ", CompPokemon.move3.name)
        UserPokemon.health = UserPokemon.health - CompPokemon.move3.power
    else:
        print("COMPUTER HAS USED THE MOVE\n ", CompPokemon.move4.name)
        UserPokemon.health = UserPokemon.health - CompPokemon.move4.power


# MAIN PROGRAM BEGINS
print("ENTER USER POKEMON : ")
print("1)Blastoise \n2)Charizard\n3)Venasaur\n4)Pidgeot\n5)Pikachu\n6)Sceptile\n7)Greninja\n8)Onix\n9)Gengar\n10)Alakazam\n")
User_Pokemon_Name = input()

o = random.randint(1, 10)
count = 0

CompPokemon = Pokemon(
    "Alakazam", "Psychic", "Confusion", "Psychic", "Focus-Blast", "Dazzlimg-Gleam")

Pokemon_Data = open("./Pokemon.txt", "r")

while count < 10:
    S = Pokemon_Data.readline()
    L = S.split()
    if (o == count):
        CompPokemon = Pokemon(L[0], L[5], L[1], L[2], L[3], L[4])
    if User_Pokemon_Name == L[0]:
        UserPokemon = Pokemon(L[0], L[5], L[1], L[2], L[3], L[4])
    count += 1

print("YOU HAVE SELECTED ", UserPokemon.name,
      " AND THE COMPUTER HAS SELECTED ", CompPokemon.name)

while CompPokemon.health >= 1 and UserPokemon.health >= 1:
    Display()
    UserPlay()
    Result()
    Display()
    CompPlay()
    Result()
