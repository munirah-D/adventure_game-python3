import time
import random
monesters = ["wicked fairie", "dragon", "pirate", ]
monester = random.choice(monesters)
weapon="degger"

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def adventure_game():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + monester + " is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty(but not very effective) dagger.\n")
    firts_choice()

def firts_choice():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice_house_cave = input("Please enter ( 1 or 2).")
    if choice_house_cave  == "1":
        house(monester)
    elif choice_house_cave  == "2":
        cave(weapon)
    else:
        print("Invaild input: Please enter 1 or 2")
        firts_choice()

def house(monester):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a " + monester + ".")
    print_pause("Eep! This is the " + monester + "'s house!")
    print_pause("The " + monester + "  attacks you!")
    print_pause("You feel a bit under-prepered for this, what with only having a tiny dagger.")
    print_pause("Would you like to (1) fight or (2) run away?")
    choice_fight_run = input("Please enter ( 1 or 2).")
    if choice_fight_run  == "1" :
            print_pause("You do your best...")
            print_pause("but your dagger is ni match fir the" + monester )
            print_pause("You have been defeated!")
            play_again()
    elif choice_fight_run  == "2" : 
        print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
        firts_choice()
    else:
        print("Invaild input: Please enter 1 or 2")
        house(monester)

def cave(weapon):
        weapon = "Sword"
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical " + weapon + "of Ogoroth!")
        print_pause("You discard you silly old dagger and take the " + weapon + " with you.")
        print_pause("You walk back out to the feild.")
        secound_choice()

def secound_choice():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice_house_cave = input("Please enter ( 1 or 2).")
    if choice_house_cave  == "1":
        secound_house(monester)
    elif choice_house_cave  == "2":
        secound_cave()
    else:
        print("Invaild input: Please enter 1 or 2")
        secound_choice()

def secound_house(monester):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a " + monester + ".")
    print_pause("Eep! This is the " + monester + "'s house!")
    print_pause("The " + monester + "  attacks you!")
    print_pause("Would you like to (1) fight or (2) run away?")
    choice_fight_run = input("Please enter ( 1 or 2).")
    if choice_fight_run  == "1" :
        print_pause("As the" + monester + " moves to attack, you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in you hand as you brace yourself for the attack.") 
        print_pause("But the "+ monester +" takes one look at your shiny new toy and runs away!")
        print_pause("You have rid the town of the" + monester + ". You are victorious!")
        play_again()
    elif choice_fight_run  == "2" : 
        print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
        secound_choice()
    else:
        print("Invaild input: Please enter 1 or 2")
        secound_house(monester)
 
def secound_cave():
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        print_pause("What would you like to do?")
        number3 = input("Please enter ( 1 or 2).")
        if number3 == "1" :
            secound_house(monester)
        elif number3 == "2" : 
            secound_cave()
        else:
            print("Invaild input: Please enter 1 or 2")
            secound_cave()

def play_again():
    play = input("Would you like to play again? (y/n)")
    if play == "y":
        print_pause("Excellent! Restarting the game ...")
        adventure_game()
    elif play == "n":
        exit()
    else:
        play_again()

adventure_game()