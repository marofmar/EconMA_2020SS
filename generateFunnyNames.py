
import sys, random 

print("Welcome to the Psych 'Sidekick Name Picker.'\n")

first = ("Baby Anaconda", "Pythonian", "Big Farts", "Humongous Foot", "Grumpy Olive")

last = ("Fewhairs", "Jenkins", "Butterbaugh", "Kingfish", "Whipkey", "Neeky", "Pealike") 

while True:
    firstName = random.choice(first) 
    lastName = random.choice(last) 
    print("\n\n")
    print("{} {}".format(firstName, lastName), file = sys.stderr)
    print("\n\n") 

    try_again = input("\n\nWould you like to try again? Enter any key except 'n' (To quit, press 'n')\n")
    if try_again.lower() == "n":
        print("Good bye!")
        break
input("\nPress Enter to exit.") 

"""
Book title: Impractical Python Projects: Playful Programming Activities to Make You Smarter
Author: Lee Vaughan

"""