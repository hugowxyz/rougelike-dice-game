import random, csv

def Create_Base():
    Board = []
    for Line in range(7, 0, -1):
        BoardLine = []
        for Row in range((Line * 7), (Line * 7 - 7), -1):
            BoardLine.append(str(Row))
        Board.append(BoardLine)
    return Board

def Format_Board(Board):
    for Line in range(7):
        for Row in range(7):
            if len(Board[Line][Row]) == 2:
                Board[Line][Row] += "|"
            elif len(Board[Line][Row]) == 1:
                Board[Line][Row] += " |"
    return Board

def Get_Player_Position(Current_Position):
    print("\n"+"-"*40,"\nIt's Player One's Turn!\nPress ANY key to roll:")
    PlayerInput = input("Say: ")
    Player_Roll = random.randint(1, 6)
    Player_Roll2 = random.randint(1, 6)
    if Player_Roll == Player_Roll2:
        write("Double")
        Player_Position = int(Current_Position) - (Player_Roll + Player_Roll2)
        print("\nOh no! You rolled a double. The God of Lust has Come For You... You will move",Player_Roll + Player_Roll2,"spaces back")
    else:
        print("\nYou will move:",Player_Roll+Player_Roll2,"spaces forward!")
        Player_Position = Player_Roll + Player_Roll2 + int(Current_Position)
    print("Your Current Position is:", Player_Position, "\n"+"-"*40)
    return str(Player_Position)

def Get_Player2_Position(Current_Position):
    print("\n"+"-"*40,"\nIt's Player Two's Turn!\nPress ANY key to roll:")
    PlayerInput = input("Say: ")
    Player_Roll = random.randint(1, 6)
    Player_Roll2 = random.randint(1, 6)
    if Player_Roll == Player_Roll2:
        write("Double")
        Player_Position = int(Current_Position) - (Player_Roll + Player_Roll2)
        print("\nOh no! You rolled a double. The God of Lust has Come For You... You will move",Player_Roll + Player_Roll2,"spaces back")
    else:
        print("\nYou will move:",Player_Roll+Player_Roll2,"spaces forward!")
        Player_Position = Player_Roll + Player_Roll2 + int(Current_Position)
    print("Your Current Position is:", Player_Position, "\n"+"-"*40)
    return str(Player_Position)

def Load_Obstacles():
    Obstacle = []
    Obstacle_New = []
    File = open("Obstacle.txt", "r")
    Reader = csv.reader(File)
    for Line in Reader:
        Obstacle.append(Line)
    for Line in Obstacle[0]:
        Obstacle_New.append(Line)
    return Obstacle_New

def Place_Obstacles():
    Obstacle_Pos = []
    Obstacle_Position = []
    File = open("Obstacle_Pos.txt", "r")
    Reader = csv.reader(File)
    for Line in Reader:
        Obstacle_Pos.append(Line)
    for Line in Obstacle_Pos[0]:
        Obstacle_Position.append(Line)
    Obstacle_Position = [Element.strip(" ") for Element in Obstacle_Position]
    return Obstacle_Position

def Get_Penalties():
    Penalties = []
    Format_Penalties = []
    File = open("Penalties.txt", "r")
    Reader = csv.reader(File)
    for Line in Reader:
        Penalties.append(Line)
    for Line in Penalties[0]:
        Format_Penalties.append(Line)
    Penalties = [Element.strip(" ") for Element in Format_Penalties]
    return Penalties
    
def Check_Collision(Player_Pos, Player2_Pos, Obstacle_Pos, Penalty):
    Player_Pos = int(Player_Pos)
    Player2_Pos = int(Player2_Pos)
    for Index in range(len(Obstacle_Pos)):
        #print("Player_Pos:", Player_Pos, "Obstacle_Pos:", Obstacle_Pos[Index])
        if Player_Pos == int(Obstacle_Pos[Index]):
            Player_Pos += int(Penalty[Index])
            write("NO")
            print("You have encoutered an obstacle.\nYour new position is:", Player_Pos,"\n"+  "="*40)
        if Player2_Pos == int(Obstacle_Pos[Index]):
            Player2_Pos += int(Penalty[Index])
            write("NO")
            print("You have encoutered an obstacle!\nYour new Position:", Player2_Pos, "\n="*40)
    return str(Player_Pos), str(Player2_Pos)

def Update_Board(Player_Pos, Player2_Pos, Obstacle, Obstacle_Pos):
    New_Board = Create_Base()
    
    for Line in range(7):
        for Row in range(7):
            #print("Board:", New_Board[Line][Row], "P_Pos:", Player_Pos, "P2_Pos:", Player2_Pos)
            if New_Board[Line][Row] == str(Player_Pos):
                New_Board[Line][Row] = "X"
            if New_Board[Line][Row] == str(Player2_Pos):
                New_Board[Line][Row] = "Y"
            for Index in range(len(Obstacle_Pos)):
                #print("Ob_Pos:", Obstacle_Pos[Index], "Board Pos:", New_Board[Line][Row])
                if New_Board[Line][Row] == Obstacle_Pos[Index]:
                    New_Board[Line][Row] = Obstacle[Index]

    New_Board = Format_Board(New_Board)
    
    for Line in New_Board:
        print(*Line)

    return New_Board

def Check_Win_Condition(Player_Pos, Player2_Pos):
    Won = False
    if int(Player_Pos) >= 49:
        write("Win")
        print("="* 40,"\nPlayer One is VICTORIOUS!","\n"+"="*40)
        Won = True
    elif int(Player2_Pos) >= 49:
        write("Win")
        print("="* 40,"\nPlayer Two is VICTORIOUS!","\n"+"="*40)
        Won = True
    if Won:
        return Won
    
def Main_Menu():
    print("Welcome to Dices and Dragons!\nChoose Option:\n1. Play\n2. Quit")
    userChoice = input("Say: ")
    if userChoice == "1":
        print("="*40,"\n"+ " "*10,"GAME COMMENCING","\n"+"="*40)
    elif userChoice == "2":
        quit()
    else:
        print("Try Again!")
        Main_Menu()

def write(file):
    with open("{}.txt".format(file), "r") as f:
        reader = csv.reader(f)
        for line in reader:
            print(line)

#----------------------------Main-----------------------------#

write("Intro")
Main_Menu()

Obstacle = Load_Obstacles()
Obstacle_Pos = Place_Obstacles()
Penalties = Get_Penalties()

Player_Pos = 1
Player2_Pos = 1
Won = False

while not Won:
    New_Board = Update_Board(Player_Pos, Player2_Pos, Obstacle, Obstacle_Pos)

    Player_Pos = Get_Player_Position(Player_Pos)
    Player2_Pos = Get_Player2_Position(Player2_Pos)
    Player_Pos, Player2_Pos = Check_Collision(Player_Pos, Player2_Pos, Obstacle_Pos, Penalties)

    Won = Check_Win_Condition(Player_Pos, Player2_Pos)
