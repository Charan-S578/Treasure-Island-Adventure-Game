# if else Statement

#print("Welcome to rollercoaster!")
#height = int(input("What is your height in cm? "))
#if height >= 120:
#    print("You can ride the rollcoaster")
#   age = int(input("What is your age? "))
#    if age <= 12:
#        print("You have to pay $5")
#    if age >= 15:
#        print("You have to pay $7")
#    if age >= 18:
#        print("You have to pay $15")

#else:
#    print("Sorry you have to grow before you can ride rollcoaster")  

# Comparison Operators

#age = int(input("What is your age? "))
#if age > 18:
#    print("Your Eligible to vote")
#else:
#    print("Your not Eligible to vote")  

#    print("Your Eligible to vote")
#else:
#    print("Your not Eligible to vote") 

#if age >= 18:
#    print("Your Eligible to vote")
#else:
#    print("Your not Eligible to vote") 

#if age <= 18:
#    print("Your Eligible to vote")
#else:
#    print("Your not Eligible to vote")  
  
#number = int(input("Enter your number: "))  
#if number is 5:
#    print("Even") 
#else:
#    print("Odd")

#number_to_check = int(input("Enter your number to check it's Even or Odd? ")) 
#if number_to_check % 2 == 0:
#    print("Even")
#else:
#    print("Odd")    
# Day 3 Project Adventure Game

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? ' \
         'Type "left" or "right".').lower()
if choice1 == "left":
  choice2 = input('You\'re come to a lake. '
          'There is a island in the middle of the lake. '
          'Type "wait" to wait for a boat. '
          'Type "swim" to swim across.').lower()
  if choice2 == "wait":
    choice3 = input('You arrive at the island unharmed. '
                    'There is house with 3 doors. '
                    'one red, one yellow and one blue. '
                    'Which colour do you choose?').lower()
    if choice3 == "red":
       print("it's room full of fire. Game Over")
    elif choice3 == "yellow":
       print("You found the treasure. You Win")
    elif choice3 == "blue":   
       print("You entered room of beasts. Game Over")   
    else:
       print("You choose a door that doesn't exists. Game over")
  else:
     print("You got attacked by an angry thout. Game Over")
else:
    print("You fell in to hole. Game Over.")
