
import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

win_count = 0
loose_count = 0

print("")
print("------------------------------------------------------------------------------------")
print(" ")
print("$$$      $$$     $$$$$$$      $$$$$$$$$$      $$$$$$$$$$           $$$$$$$$$$")
print("$$$      $$$    $$$$$$$$$$    $$$$$$$$$$      $$$$$$$$$$$         $$$$$$$$$$$$")
print("$$$      $$$   $$$      $$$   $$$     $$              $$$         $$$      $$$")
print("$$$  $$  $$$   $$$      $$$   $$$    $$$        $$$$$$$$$         $$$      $$$")
print("$$$ $$$$ $$$   $$$$$$$$$$$$   $$$$$$$$$       $$$$$$$$$           $$$      $$$")
print("$$$$$$$$$$$$   $$$      $$$   $$$    $$$     $$$                  $$$      $$$")
print(" $$$$  $$$$    $$$      $$$   $$$    $$$      $$$$$$$$$$$   $$$    $$$$$$$$$$")
print("  $$    $$     $$$      $$$   $$     $$$        $$$$$$$$$   $$$     $$$$$$$$")
print(" ")
print("                                War, But Faster")
print(" ")
print("------------------------------------------------------------------------------------")
print(" ")
print("This is a card game called War.")
print(" ")
print("The goal is to pull a card that is worth more than your opponent.")
print(" ")
print("Your opponent is your computer.")
print(" ")
print("Who ever wins the most rounds wins")
print(" ")
print("GLHF")
print(" ")
print("------------------------------------------------------------------------------------")
print(" ")
num_of_rounds = int(input("How many rounds do you want to play: "))
print(" ")
start = input("Type 'start' to begin the game: ")
print(" ")
print("------------------------------------------------------------------------------------")
for i in range(num_of_rounds):
    if start == "start":
        print(" ")
        print("Your card:")
        your_card = random.choice(cards)
        print(your_card)
        print(" ")
        print("Opponents card:")
        opponent_card = random.choice(cards)
        print(opponent_card)
    elif start == "no":
        print(" ")
        print("Why don't you want to play. Are you scared?")
    else:
        print(" ")
        print("Invalid input. Restart program")

    if your_card > opponent_card:
        print(" ")
        print("Congrats you win this round!!")
        win_count += 1
        print("SCORE: ", win_count, "-", loose_count)
        print(" ")
    elif your_card < opponent_card:
        print(" ")
        print("Oh oh. You loose this round")
        loose_count += 1
        print("SCORE: ", win_count, "-", loose_count)
        print(" ")
    elif your_card == opponent_card:
        print(" ")
        print("------------------------------------------------------------------------------------")
        print("WAR WAR WAR WAR WAR WAR WAR WAR WAR WAR WAR WAR WAR WAR WAR WAR WAR WAR WAR WAR WAR ")
        print("------------------------------------------------------------------------------------")
        print(" ")
        print("Your card:")
        your_card2 = random.choice(cards)
        print(your_card2)
        print(" ")
        print("Opponents card:")
        opponent_card2 = random.choice(cards)
        print(opponent_card2)
        if your_card2 >= opponent_card2:
            print(" ")
            print("Congrats you win this war. You win the round!!")
            win_count += 1
            print("SCORE: ", win_count, "-", loose_count)
            print(" ")
        elif your_card2 < opponent_card2:
            print(" ")
            print("Oh oh. You loose this war. The opponent wins the round!!")
            loose_count += 1
            print("SCORE: ", win_count, "-", loose_count)
            print(" ")
    else:
        print("error")

    if win_count >= num_of_rounds:
        break
    elif loose_count >= num_of_rounds:
        break

if win_count > loose_count:
    print("YOU WIN!!!")
    print("YOU WIN!!!")
    print("YOU WIN!!!")
    print("YOU WIN!!!")
    print("YOU WIN!!!")
elif loose_count > win_count:
    print("YOU LOOSE")
    print("YOU LOOSE")
    print("YOU LOOSE")
    print("YOU LOOSE")
    print("YOU LOOSE")
elif win_count == loose_count:
    print("TIE")
    print("TIE")
    print("TIE")
    print("TIE")
    print("TIE")

input()
