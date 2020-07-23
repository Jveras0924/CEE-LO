#|=======================================================Imports=======================================================|
import random
#test the wininh conditons 2 beat 3 not supposed to happen
#type error line 80 198 string/ int
#|================================================Goobal Variables=====================================================|

#<----------------------------------------------Roll dice-------------------------------------------------------------->
#Used to intiate player turns
roll_dice = ""

#<-------------------------------------Dice rolls for Player 1 and Player 2-------------------------------------------->
#Stores player rolls
dice_roll_list1 = []

dice_roll_list2 = []

# <-------------------------------------------- Player Numbers -------------------------------------------------------->
#These numbers are tested to determine winner in normal circumstances
player1_test_num = ""

player2_test_num = ""

# <--------------------------------------------- Headcrack Win -------------------------------------------------------->
# Checks the 456 Headcrack win condition
head_crack = False
# <---------------------------------------------- Auto Loss ----------------------------------------------------------->
# Checks the 123 lose condition. The first person to roll a 123 automaticly loses.
loss_123 = False

# <---------------------------------------------- Tie ----------------------------------------------------------------->
# Checks if the players tie and gives them the rematch option.

tie = False

rematch = ""

# <--------------------------------------------- Triples -------------------------------------------------------------->
# Checks for Triples, Triples beat everything excpet for a bigger triple.

player1_triple_num = ""

player2_triple_num = ""

triples = False

#|=====================================================Functions========================================================|

#<-------------------------------------------------Game Play Function-------------------------------------------------->
# This is the logic of the Game
def play_game():
    global head_crack
    global roll_dice
    global loss_123
    print("Player 1 please hit enter to continue")

    roll_dice = input("Roll the dice: ")

    handle_turns_p1()

    head_crack_win()
    if head_crack == True:
        return
    check_123_loss()
    if loss_123 == True:
        return

    print("Player 2 please hit enter to continue")

    roll_dice = input("Roll the dice: ")

    handle_turns_p2()

    head_crack_win()
    if head_crack == True:
        return
    check_123_loss()
    if loss_123 == True:
        return

    check_num_win()
    check_tie()

#  <____________________________________________ Check Win Conditon Functions _________________________________________>

# <--------------------------------------------- Check Headcrack Win -------------------------------------------------->
# The first player to roll a 456 wins the game.
def head_crack_win():
    global head_crack
    if dice_roll_list1 == [4,5,6]:
        head_crack = True
        print("HeadCrack! Player 1 wins.")
    elif dice_roll_list1 == [4,6,5]:
        head_crack = True
        print("HeadCrack! Player 1 wins.")
    elif dice_roll_list1 == [5, 4, 6]:
        head_crack = True
        print("HeadCrack! Player 1 wins.")
    elif dice_roll_list1 == [5, 6, 4]:
        head_crack = True
        print("HeadCrack! Player 1 wins.")
    elif dice_roll_list1 == [6, 5, 4]:
        head_crack = True
        print("HeadCrack! Player 1 wins.")
    elif dice_roll_list1 == [6, 4, 5]:
        head_crack = True
        print("HeadCrack! Player 1 wins.")
    elif dice_roll_list2 == [4,5,6]:
        head_crack = True
        print("HeadCrack! Player 2 wins.")
    elif dice_roll_list2 == [4,6,5]:
        head_crack = True
        print("HeadCrack! Player 2 wins.")
    elif dice_roll_list2 == [5, 4, 6]:
        head_crack = True
        print("HeadCrack! Player 2 wins.")
    elif dice_roll_list2 == [5, 6, 4]:
        head_crack = True
        print("HeadCrack! Player 2 wins.")
    elif dice_roll_list2 == [6, 5, 4]:
        head_crack = True
        print("HeadCrack! Player 2 wins.")
    elif dice_roll_list2 == [6, 4, 5]:
        head_crack = True
        print("HeadCrack! Player 2 wins.")

# <----------------------------------------------- Check Number Win --------------------------------------------------->
# Compares the players numbers, the bigger number wins.
def check_num_win():
    global  player1_test_num
    global player2_test_num
    global player1_triple_num
    global player2_triple_num

    if player1_test_num > player2_test_num:
        print("Player 1 got a " + str(player1_test_num) + " that is bigger than a " + str(player2_test_num) + " . Player 1 wins!")
        if triples == True:
            print("Player 1 got triple " + str(player1_triple_num) + "'s. That beats Player 2, Player 1 wins!")
    elif player2_test_num > player1_test_num:
        print("Player 2 got a " + str(player2_test_num) + " that is bigger than a " + str(player1_test_num) + " . Player 2 wins!")
        if triples == True:
            print("Player 2 got triple " + str(player2_triple_num) + "'s. That beats Player 1, Player 2 wins!")
# <------------------------------------------------ Check Tie --------------------------------------------------------->

def check_tie():
    global  tie
    global rematch
    if player1_test_num == player2_test_num:
        tie = True
        print("It's a Tie!")

# <-------------------------------------------- Check Auto Loss-------------------------------------------------------->

def check_123_loss():
    global loss_123
    if dice_roll_list1 == [1, 2, 3]:
        loss_123 = True
        print("You rolled a 123 😫. Player 2 Won!.")
    elif dice_roll_list1 == [1, 3, 2]:
        loss_123 = True
        print("You rolled a 123 😫. Player 2 Won!.")
    elif dice_roll_list1 == [2, 1, 3]:
        loss_123 = True
        print("You rolled a 123 😫. Player 2 Won!.")
    elif dice_roll_list1 == [2, 3, 1]:
        loss_123 = True
        print("You rolled a 123 😫. Player 2 Won!.")
    elif dice_roll_list1 == [3, 2, 1]:
        loss_123 = True
        print("You rolled a 123 😫. Player 2 Won!.")
    elif dice_roll_list1 == [3, 1, 2]:
        loss_123 = True
        print("You rolled a 123 😫. Player 1 Won!.")
    elif dice_roll_list2 == [1, 2, 3]:
        loss_123 = True
        print("You rolled a 123 😫. Player 1 Won!.")
    elif dice_roll_list2 == [1, 3, 2]:
        loss_123 = True
        print("You rolled a 123 😫. Player 1 Won!.")
    elif dice_roll_list2 == [2, 1, 3]:
        loss_123 = True
        print("You rolled a 123 😫. Player 1 Won!.")
    elif dice_roll_list2 == [2, 3, 1]:
        loss_123 = True
        print("You rolled a 123 😫. Player 1 Won!.")
    elif dice_roll_list2 == [3, 2, 1]:
        loss_123 = True
        print("You rolled a 123 😫. Player 1 Won!.")
    elif dice_roll_list2 == [3, 1, 2]:
        loss_123 = True
        print("You rolled a 123 😫. Player 1 Won!.")

# <----------------------------------------------- Triples ------------------------------------------------------------>
#not used
def triple_num_win():
    global player2_test_num
    global player1_test_num
    global player1_triple_num
    global player2_triple_num
    if int(player1_triple_num) > int(player2_triple_num):
        print("Player 1's triples are higher than Player 2's. Player 1 wins!")
    elif int(player2_triple_num) > int(player1_triple_num):
        print("Player 2's triples are higher than Player 1's. Player 2 wins!")
    elif int(player1_triple_num) > int(player2_test_num):
        print("Triples beats non triples. Player 1 wins!")
    elif int(player2_triple_num) > int(player1_test_num):
        print("Triples beats non triples. Player 2 wins!")

# <----------------------------------------------- Rematch ------------------------------------------------------------>
#not used
def play_again():
    global  rematch
    rematch = print("If you would like to play again hit enter, if not type quit: ")
    if rematch == "":
        play_game()
    elif rematch == "quit":
        return

# <------------------------------------------ Handle Turns for Both Players ------------------------------------------->
def handle_turns_p1():
    global dice_roll_list1
    global player1_test_num
    global player1_triple_num
    global triples
    #this rolls 3 dice and prints the result
    while dice_roll_list1 != [0,0,0]:
        dice1 = random.randint(1, 6)

        dice2 = random.randint(1, 6)

        dice3 = random.randint(1, 6)

        dice_roll_list1 = [dice1, dice2, dice3]

        print(dice_roll_list1)
#this returns 1 valid roll that gets a players numbers
        #All combonations of 1,2,3

        if dice_roll_list1 == [1,2,3]:
            return
        elif dice_roll_list1 == [3,2,1]:

            return
        elif dice_roll_list1 == [2,1,3]:

            return
        elif dice_roll_list1 == [1,3,2]:

            return
        elif dice_roll_list1 == [2,3,1]:

            return
        elif dice_roll_list1 == [3,1,2]:

            return
        #all combos of 4,5,6
        elif dice_roll_list1 == [4,5,6]:

            return
        elif dice_roll_list1 == [4,6,5]:

            return
        elif dice_roll_list1 == [5,6,4]:

            return
        elif dice_roll_list1 == [5,4,6]:

            return
        elif dice_roll_list1 == [6,5,4]:

            return
        elif dice_roll_list1 == [6,4,5]:
            return
        #all triples
        elif dice_roll_list1 == [1,1,1]:
            player1_test_num = 10
            player1_triple_num = 1
            triples = True
            return
        elif dice_roll_list1 == [2,2,2]:
            player1_test_num = 20
            player1_triple_num = 2
            triples =True
            return
        elif dice_roll_list1 == [3,3,3]:
            player1_test_num = 30
            player1_triple_num = 3
            triples = True
            return
        elif dice_roll_list1 == [4,4,4]:
            player1_test_num = 40
            player1_triple_num = 4
            triples = True
            return
        elif dice_roll_list1 == [5,5,5]:
            player1_test_num = 50
            player1_triple_num = 5
            triples = True
            return
        elif dice_roll_list1 == [6,6,6]:
            player1_test_num = 60
            player1_triple_num = 6
            triples = True
            return
        #all combo of 2 1s
        elif dice_roll_list1 == [1,1,2]:
            player1_test_num = 2
            return
        elif dice_roll_list1 == [1,1,3]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [1,1,4]:
            player1_test_num = 4
            return
        elif dice_roll_list1 == [1,1,5]:
            player1_test_num = 5
            return
        elif dice_roll_list1 == [1,1,6]:
            player1_test_num = 6
            return
        elif dice_roll_list1 == [2,1,1]:
            player1_test_num = 2
            return
        elif dice_roll_list1 == [3,1,1]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [4,1,1]:
            player1_test_num = 4
            return
        elif dice_roll_list1 == [5,1,1]:
            player1_test_num = 5
            return
        elif dice_roll_list1 == [6,1,1]:
            player1_test_num = 6
            return
        elif dice_roll_list1 == [1,2,1]:
            player1_test_num = 2
            return
        elif dice_roll_list1 == [1,3,1]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [1,4,1]:
            player1_test_num = 4
            return
        elif dice_roll_list1 == [1,5,1]:
            player1_test_num = 5
            return
        elif dice_roll_list1 == [1,6,1]:
            player1_test_num = 2
            return
        #all combo of 2 2's
        elif dice_roll_list1 == [2,2,1]:
            player1_test_num = 1
            return
        elif dice_roll_list1 == [2,2,3]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [2,2,4]:
            player1_test_num = 4
            return
        elif dice_roll_list1 == [2,2,5]:
            player1_test_num = 5
            return
        elif dice_roll_list1 == [2,2,6]:
            player1_test_num = 6
            return
        elif dice_roll_list1 == [1,2,2]:
            player1_test_num = 1
            return
        elif dice_roll_list1 == [3,2,2]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [4,2,2]:
            player1_test_num = 4
            return
        elif dice_roll_list1 == [5,2,2]:
            player1_test_num = 5
            return
        elif dice_roll_list1 == [6,2,2]:
            player1_test_num = 6
            return
        elif dice_roll_list1 == [2,1,2]:
            player1_test_num = 1
            return
        elif dice_roll_list1 == [2, 3, 2]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [2, 4, 2]:
            player1_test_num = 4
            return
        elif dice_roll_list1 == [2, 5, 2]:
            player1_test_num = 5
            return
        elif dice_roll_list1 == [2, 6, 2]:
            player1_test_num = 6
            return
        #all combos of 2 3's
        elif dice_roll_list1 == [3,3,1]:
            player1_test_num = 1
            return
        elif dice_roll_list1 == [3, 3, 2]:
            player1_test_num = 2
            return
        elif dice_roll_list1 == [3, 3, 4]:
            player1_test_num = 4
            return
        elif dice_roll_list1 == [3, 3, 5]:
            player1_test_num = 5
            return
        elif dice_roll_list1 == [3, 3, 6]:
            player1_test_num = 6
            return
        elif dice_roll_list1 == [1, 3, 3]:
            player1_test_num = 1
            return
        elif dice_roll_list1 == [2, 3, 3]:
            player1_test_num = 2
            return
        elif dice_roll_list1 == [4, 3, 3]:
            player1_test_num = 4
            return
        elif dice_roll_list1 == [5, 3, 3]:
            player1_test_num = 5
            return
        elif dice_roll_list1 == [6, 3, 3]:
            player1_test_num = 6
            return
        elif dice_roll_list1 == [3, 1, 3]:
            player1_test_num = 1
            return
        elif dice_roll_list1 == [3, 2, 3]:
            player1_test_num = 2
            return
        elif dice_roll_list1 == [3, 4, 3]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [3, 5, 3]:
            player1_test_num = 5
            return
        elif dice_roll_list1 == [3, 6, 3]:
            player1_test_num = 6
            return
        #all combos of 2 4's
        elif dice_roll_list1 == [4, 4, 1]:
            player1_test_num = 1
            return
        elif dice_roll_list1 == [4, 4, 2]:
            player1_test_num = 2
            return
        elif dice_roll_list1 == [4, 4, 3]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [4, 4, 5]:
            player1_test_num = 5
            return
        elif dice_roll_list1 == [4, 4, 6]:
            player1_test_num = 6
            return
        elif dice_roll_list1 == [1, 4, 4]:
            player1_test_num = 1
            return
        elif dice_roll_list1 == [2, 4, 4]:
            player1_test_num = 2
            return
        elif dice_roll_list1 == [3, 4, 4]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [5, 4, 4]:
            player1_test_num = 5
            return
        elif dice_roll_list1 == [6, 4, 4]:
            player1_test_num = 6
            return
        elif dice_roll_list1 == [4, 1, 4]:
            player1_test_num = 1
            return
        elif dice_roll_list1 == [4, 2, 4]:
            player1_test_num = 2
            return
        elif dice_roll_list1 == [4, 3, 4]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [4, 5, 4]:
            player1_test_num = 5
            return
        elif dice_roll_list1 == [4, 6, 4]:
            player1_test_num = 6
            return
        #all combos of 2 5's
        elif dice_roll_list1 == [5, 5, 1]:
            player1_test_num = 1
            return
        elif dice_roll_list1 == [5, 5, 2]:
            player1_test_num = 2
            return
        elif dice_roll_list1 == [5, 5, 3]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [5, 5, 4]:
            player1_test_num = 4
            return
        elif dice_roll_list1 == [5, 5, 6]:
            player1_test_num = 6
            return
        elif dice_roll_list1 == [1, 5, 5]:
            player1_test_num = 1
            return
        elif dice_roll_list1 == [2, 5, 5]:
            player1_test_num = 2
            return
        elif dice_roll_list1 == [3, 5, 5]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [4, 5, 5]:
            player1_test_num = 4
            return
        elif dice_roll_list1 == [6, 5, 5]:
            player1_test_num = 6
            return
        elif dice_roll_list1 == [5, 1, 5]:
            player1_test_num = 1
            return
        elif dice_roll_list1 == [5, 2, 5]:
            player1_test_num = 2
            return
        elif dice_roll_list1 == [5, 3, 5]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [5, 4, 5]:
            player1_test_num = 4
            return
        elif dice_roll_list1 == [5, 6, 5]:
            player1_test_num = 6
            return
        #all combos of 2 6's
        elif dice_roll_list1 == [6, 6, 1]:
            player1_test_num = 1
            return
        elif dice_roll_list1 == [6, 6, 2]:
            player1_test_num = 2
            return
        elif dice_roll_list1 == [6, 6, 3]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [6, 6, 4]:
            player1_test_num = 4
            return
        elif dice_roll_list1 == [6, 6, 5]:
            player1_test_num = 5
            return
        elif dice_roll_list1 == [1, 6, 6]:
            player1_test_num = 1
            return
        elif dice_roll_list1 == [2, 6, 6]:
            player1_test_num = 2
            return
        elif dice_roll_list1 == [3, 6, 6]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [4, 6, 6]:
            player1_test_num = 4
            return
        elif dice_roll_list1 == [5, 6, 6]:
            player1_test_num = 5
            return
        elif dice_roll_list1 == [6, 1, 6]:
            player1_test_num = 1
            return
        elif dice_roll_list1 == [6, 2, 6]:
            player1_test_num = 2
            return
        elif dice_roll_list1 == [6, 3, 6]:
            player1_test_num = 3
            return
        elif dice_roll_list1 == [6, 4, 6]:
            player1_test_num = 4
            return
        elif dice_roll_list1 == [6, 5, 6]:
            player1_test_num = 5
            return

def handle_turns_p2():
    global dice_roll_list2
    global player2_test_num
    global player2_triple_num
    global triples
    while dice_roll_list1 != [0, 0, 0]:
        dice4 = random.randint(1, 6)

        dice5 = random.randint(1, 6)

        dice6 = random.randint(1, 6)

        dice_roll_list2 = [dice4, dice5, dice6]

        print(dice_roll_list2)
        # this returns 1 valid roll that gets a players numbers
        # All combonations of 1,2,3
        if dice_roll_list2 == [1, 2, 3]:

            return
        elif dice_roll_list2 == [3, 2, 1]:

            return
        elif dice_roll_list2 == [2, 1, 3]:

            return
        elif dice_roll_list2 == [1, 3, 2]:

            return
        elif dice_roll_list2 == [2, 3, 1]:

            return
        elif dice_roll_list2 == [3, 1, 2]:

            return
        # all combos of 4,5,6
        elif dice_roll_list2 == [4, 5, 6]:

            return
        elif dice_roll_list2 == [4, 6, 5]:

            return
        elif dice_roll_list2 == [5, 6, 4]:

            return
        elif dice_roll_list2 == [5, 4, 6]:

            return
        elif dice_roll_list2 == [6, 5, 4]:

            return
        elif dice_roll_list2 == [6, 4, 5]:

            return
        # all triples
        elif dice_roll_list2 == [1, 1, 1]:
            player2_test_num = 10
            player2_triple_num = 1
            triples = True
            return
        elif dice_roll_list2 == [2, 2, 2]:
            player2_test_num = 20
            player2_triple_num = 2
            triples = True
            return
        elif dice_roll_list2 == [3, 3, 3]:
            player2_test_num = 30
            player2_triple_num = 3
            triples = True
            return
        elif dice_roll_list2 == [4, 4, 4]:
            player2_test_num = 40
            player2_triple_num = 4
            triples = True
            return
        elif dice_roll_list2 == [5, 5, 5]:
            player2_test_num = 50
            player2_triple_num = 5
            triples = True
            return
        elif dice_roll_list2 == [6, 6, 6]:
            player2_test_num = 60
            player2_triple_num = 6
            triples = True
            return
        # all combo of 2 1s
        elif dice_roll_list2 == [1, 1, 2]:
            player2_test_num = 2
            return
        elif dice_roll_list2 == [1, 1, 3]:
            player2_test_num = 3
            return
        elif dice_roll_list2 == [1, 1, 4]:
            player2_test_num = 4
            return
        elif dice_roll_list2 == [1, 1, 5]:
            player2_test_num = 5
            return
        elif dice_roll_list2 == [1, 1, 6]:
            player2_test_num = 6
            return
        elif dice_roll_list2 == [2, 1, 1]:
            player2_test_num = 2
            return
        elif dice_roll_list2 == [3, 1, 1]:
            player2_test_num = 3
            return
        elif dice_roll_list2 == [4, 1, 1]:
            player2_test_num = 4
            return
        elif dice_roll_list2 == [5, 1, 1]:
            player2_test_num = 5
            return
        elif dice_roll_list2 == [6, 1, 1]:
            player2_test_num = 6
            return
        elif dice_roll_list2 == [1, 2, 1]:
            player2_test_num = 2
            return
        elif dice_roll_list2 == [1, 3, 1]:
            player2_test_num = 3
            return
        elif dice_roll_list2 == [1, 4, 1]:
            player2_test_num = 4
            return
        elif dice_roll_list2 == [1, 5, 1]:
            player2_test_num = 5
            return
        elif dice_roll_list2 == [1, 6, 1]:
            player2_test_num = 6
            return
        # all combo of 2 2's
        elif dice_roll_list2 == [2, 2, 1]:
            player2_test_num = 1
            return
        elif dice_roll_list2 == [2, 2, 3]:
            player2_test_num = 3
            return
        elif dice_roll_list2 == [2, 2, 4]:
            player2_test_num = 4
            return
        elif dice_roll_list2 == [2, 2, 5]:
            player2_test_num = 5
            return
        elif dice_roll_list2 == [2, 2, 6]:
            player2_test_num = 6
            return
        elif dice_roll_list2 == [1, 2, 2]:
            player2_test_num = 1
            return
        elif dice_roll_list2 == [3, 2, 2]:
            player2_test_num = 3
            return
        elif dice_roll_list2 == [4, 2, 2]:
            player2_test_num = 4
            return
        elif dice_roll_list2 == [5, 2, 2]:
            player2_test_num = 5
            return
        elif dice_roll_list2 == [6, 2, 2]:
            player2_test_num = 6
            return
        elif dice_roll_list2 == [2, 1, 2]:
            player2_test_num = 1
            return
        elif dice_roll_list2 == [2, 3, 2]:
            player2_test_num = 3
            return
        elif dice_roll_list2 == [2, 4, 2]:
            player2_test_num = 4
            return
        elif dice_roll_list2 == [2, 5, 2]:
            player2_test_num = 5
            return
        elif dice_roll_list2 == [2, 6, 2]:
            player2_test_num = 6
            return
        # all combos of 2 3's
        elif dice_roll_list2 == [3, 3, 1]:
            player2_test_num = 1
            return
        elif dice_roll_list2 == [3, 3, 2]:
            player2_test_num = 2
            return
        elif dice_roll_list2 == [3, 3, 4]:
            player2_test_num = 4
            return
        elif dice_roll_list2 == [3, 3, 5]:
            player2_test_num = 5
            return
        elif dice_roll_list2 == [3, 3, 6]:
            player2_test_num = 6
            return
        elif dice_roll_list2 == [1, 3, 3]:
            player2_test_num = 1
            return
        elif dice_roll_list2 == [2, 3, 3]:
            player2_test_num = 2
            return
        elif dice_roll_list2 == [4, 3, 3]:
            player2_test_num = 4
            return
        elif dice_roll_list2 == [5, 3, 3]:
            player2_test_num = 5
            return
        elif dice_roll_list2 == [6, 3, 3]:
            player2_test_num = 6
            return
        elif dice_roll_list2 == [3, 1, 3]:
            player2_test_num = 1
            return
        elif dice_roll_list2 == [3, 2, 3]:
            player2_test_num = 2
            return
        elif dice_roll_list2 == [3, 4, 3]:
            player2_test_num = 4
            return
        elif dice_roll_list2 == [3, 5, 3]:
            player2_test_num = 5
            return
        elif dice_roll_list2 == [3, 6, 3]:
            player2_test_num = 6
            return
        # all combos of 2 4's
        elif dice_roll_list2 == [4, 4, 1]:
            player2_test_num = 1
            return
        elif dice_roll_list2 == [4, 4, 2]:
            player2_test_num = 2
            return
        elif dice_roll_list2 == [4, 4, 3]:
            player2_test_num = 3
            return
        elif dice_roll_list2 == [4, 4, 5]:
            player2_test_num = 5
            return
        elif dice_roll_list2 == [4, 4, 6]:
            player2_test_num = 6
            return
        elif dice_roll_list2 == [1, 4, 4]:
            player2_test_num = 1
            return
        elif dice_roll_list2 == [2, 4, 4]:
            player2_test_num = 2
            return
        elif dice_roll_list2 == [3, 4, 4]:
            player2_test_num = 3
            return
        elif dice_roll_list2 == [5, 4, 4]:
            player2_test_num = 5
            return
        elif dice_roll_list2 == [6, 4, 4]:
            player2_test_num = 6
            return
        elif dice_roll_list2 == [4, 1, 4]:
            player2_test_num = 1
            return
        elif dice_roll_list2 == [4, 2, 4]:
            player2_test_num = 2
            return
        elif dice_roll_list2 == [4, 3, 4]:
            player2_test_num = 3
            return
        elif dice_roll_list2 == [4, 5, 4]:
            player2_test_num = 5
            return
        elif dice_roll_list2 == [4, 6, 4]:
            player2_test_num = 6
            return
        # all combos of 2 5's
        elif dice_roll_list2 == [5, 5, 1]:
            player2_test_num = 1
            return
        elif dice_roll_list2 == [5, 5, 2]:
            player2_test_num = 2
            return
        elif dice_roll_list2 == [5, 5, 3]:
            player2_test_num = 3
            return
        elif dice_roll_list2 == [5, 5, 4]:
            player2_test_num = 4
            return
        elif dice_roll_list2 == [5, 5, 6]:
            player2_test_num = 6
            return
        elif dice_roll_list2 == [1, 5, 5]:
            player2_test_num = 1
            return
        elif dice_roll_list2 == [2, 5, 5]:
            player2_test_num = 2
            return
        elif dice_roll_list2 == [3, 5, 5]:
            player2_test_num = 3
            return
        elif dice_roll_list2 == [4, 5, 5]:
            player2_test_num = 4
            return
        elif dice_roll_list2 == [6, 5, 5]:
            player2_test_num = 6
            return
        elif dice_roll_list2 == [5, 1, 5]:
            player2_test_num = 1
            return
        elif dice_roll_list2 == [5, 2, 5]:
            player2_test_num = 2
            return
        elif dice_roll_list2 == [5, 3, 5]:
            player2_test_num = 3
            return
        elif dice_roll_list2 == [5, 4, 5]:
            player2_test_num = 4
            return
        elif dice_roll_list2 == [5, 6, 5]:
            player2_test_num = 6
            return
        # all combos of 2 6's
        elif dice_roll_list2 == [6, 6, 1]:
            player2_test_num = 1
            return
        elif dice_roll_list2 == [6, 6, 2]:
            player2_test_num = 2
            return
        elif dice_roll_list2 == [6, 6, 3]:
            player2_test_num = 3
            return
        elif dice_roll_list2 == [6, 6, 4]:
            player2_test_num = 4
            return
        elif dice_roll_list2 == [6, 6, 5]:
            player2_test_num = 5
            return
        elif dice_roll_list2 == [1, 6, 6]:
            player2_test_num = 6
            return
        elif dice_roll_list2 == [2, 6, 6]:
            player2_test_num = 2
            return
        elif dice_roll_list2 == [3, 6, 6]:
            player2_test_num = 3
            return
        elif dice_roll_list2 == [4, 6, 6]:
            player2_test_num = 4
            return
        elif dice_roll_list2 == [5, 6, 6]:
            player2_test_num = 5
            return
        elif dice_roll_list2 == [6, 1, 6]:
            player2_test_num = 1
            return
        elif dice_roll_list2 == [6, 2, 6]:
            player2_test_num = 2
            return
        elif dice_roll_list2 == [6, 3, 6]:
            player2_test_num = 3
            return
        elif dice_roll_list2 == [6, 4, 6]:
            player2_test_num = 4
            return
        elif dice_roll_list2 == [6, 5, 6]:
            player2_test_num = 5
            return

#----------------------------------------------------Start the Game-----------------------------------------------------

play_game()