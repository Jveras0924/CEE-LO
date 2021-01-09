# |=======================================================Imports=======================================================|
import random

# |================================================Goobal Variables=====================================================|
# <----------------------------------------------Roll dice-------------------------------------------------------------->
# Used to intiate player turns
roll_dice = ""
# <-------------------------------------Dice rolls for Player 1 and Player 2-------------------------------------------->
# Stores player rolls
dice_roll_list1 = []
dice_roll_list2 = []
# <-------------------------------------------- Player Numbers -------------------------------------------------------->
# These numbers are tested to determine winner in normal circumstances
player2_test_num = 0
player1_test_num = 0
# <--------------------------------------------- Headcrack Win -------------------------------------------------------->
# Checks the 456 Headcrack win condition
head_crack_P2 = False
head_crack_P1 = False
head_crack = False
# <---------------------------------------------- Auto Loss ----------------------------------------------------------->
# Checks the 123 lose condition. The first person to roll a 123 automaticly loses.
loss_123_P2 = False
loss_123_P1 = False
loss_123 = False
# <---------------------------------------------- Tie ----------------------------------------------------------------->
# Checks if the players tie and gives them the rematch option.
tie = False
# <--------------------------------------------- Triples -------------------------------------------------------------->
# Checks for Triples, Triples beat everything excpet for a bigger triple.
player1_triple_num = 0
player2_triple_num = 0
triples = False


# |=====================================================Functions========================================================|
# <-------------------------------------------------Game Play Function-------------------------------------------------->
# This is the logic of the Game
def play_game():
    global head_crack
    global roll_dice
    global loss_123
    print("Player 1 please hit enter to continue")
    roll_dice = input("Roll the dice: ")

    handle_turns_p1()
    head_crack_win()
    check_123_loss()

    if head_crack == False and loss_123 == False:
        print("Player 2 please hit enter to continue")
        roll_dice = input("Roll the dice: ")

        handle_turns_p2()
        head_crack_win()
        check_123_loss()

    check_num_win()
    if triples == False:
        check_tie()

    print("If you would like to play again type Y, if not type quit: ")
    rematch = input()
    if rematch == "Y" or rematch == "y":
        play_game()


# <--------------------------------------------- Check Headcrack Win -------------------------------------------------->
# The first player to roll a 456 wins the game.
def head_crack_win():
    global head_crack_P1
    global head_crack_P2

    if head_crack_P1 == True:
        print("HeadCrack! Player 1 wins.")
        head_crack = True
    elif head_crack_P2 == True:
        print("HeadCrack! Player 2 wins.")
        head_crack = True
    # <----------------------------------------------- Check Number Win --------------------------------------------------->


# Compares the players numbers, the bigger number wins.
def check_num_win():
    global player1_test_num
    global player2_test_num
    global player1_triple_num
    global player2_triple_num

    if head_crack_P1 == False and head_crack_P2 == False and loss_123_P1 == False and loss_123_P2 == False:

        if triples == True and player1_triple_num > player2_triple_num:
            print("Player 1 got triple " + str(player1_triple_num) + "'s. That beats Player 2, Player 1 wins!")
        elif player1_test_num > player2_test_num:
            print("Player 1 got a " + str(player1_test_num) + " that is bigger than a " + str(
                player2_test_num) + ". Player 1 wins!")

        elif triples == True and player2_triple_num > player1_triple_num:
            print("Player 2 got triple " + str(player2_triple_num) + "'s. That beats Player 1, Player 2 wins!")
        elif player2_test_num > player1_test_num:
            print("Player 2 got a " + str(player2_test_num) + " that is bigger than a " + str(
                player1_test_num) + ". Player 2 wins!")


# <------------------------------------------------ Check Tie --------------------------------------------------------->
def check_tie():
    global tie
    global rematch
    if player1_test_num == player2_test_num:
        tie = True
        print("It's a Tie!")


# <-------------------------------------------- Check Auto Loss-------------------------------------------------------->
def check_123_loss():
    global loss_123_P1
    global loss_123_P2

    if loss_123_P1 == True:
        print("You rolled a 123 😫. Player 2 Won!.")
        loss_123 = True
    elif loss_123_P2 == True:
        print("You rolled a 123 😫. Player 1 Won!.")
        loss_123 = True


# <------------------------------------------ Handle Turns for Both Players ------------------------------------------->
def handle_turns_p1():
    global dice_roll_list1
    global player1_test_num
    global player1_triple_num
    global triples
    global head_crack_P1
    global loss_123_P1
    temp_list = []
    # this rolls 3 dice and prints the result
    dice1 = 1
    dice3 = 2
    dice2 = 3

    while dice1 != dice3:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)
        dice_roll_list1 = [dice1, dice2, dice3]
        print(dice_roll_list1)
        # check 456

        temp_list = dice_roll_list1
        temp_list.sort()
        if temp_list == [4, 5, 6]:
            head_crack_P1 = True
            break
        if temp_list == [1, 2, 3]:
            loss_123_P1 = True
            break

        # check good roll
        if dice1 == dice2 or dice2 == dice3:
            # check/assign triple
            if dice1 == dice2 == dice3:
                triples = True
                player1_triple_num = dice3
            # activate player number
            if dice1 == dice2:
                player1_test_num = dice3
            elif dice2 == dice3:
                player1_test_num = dice1
            elif dice1 == dice3:
                player1_test_num = dice2
            break
        if dice1 == dice3:
            player1_test_num = dice2


def handle_turns_p2():
    global dice_roll_list2
    global player2_test_num
    global player2_triple_num
    global triples
    global head_crack_P2
    global loss_123_P2
    temp_list = []

    # this rolls 3 dice and prints the result
    dice1 = 1
    dice3 = 2
    dice2 = 3

    while dice1 != dice3:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)
        dice_roll_list2 = [dice1, dice2, dice3]
        print(dice_roll_list2)
        # check 456
        temp_list = dice_roll_list2
        temp_list.sort()
        if temp_list == [4, 5, 6]:
            head_crack_P2 = True
            break
        if temp_list == [1, 2, 3]:
            loss_123_P2 = True
            break

        # check good roll
        if dice1 == dice2 or dice2 == dice3:
            # check/assign triple
            if dice1 == dice2 == dice3:
                triples = True
                player2_triple_num = dice3
            # activate player number
            if dice1 == dice2:
                player2_test_num = dice3
            elif dice2 == dice3:
                player2_test_num = dice1
            elif dice1 == dice3:
                player2_test_num = dice2
            break
        if dice1 == dice3:
            player2_test_num = dice2


# ----------------------------------------------------Start the Game-----------------------------------------------------

play_game()
