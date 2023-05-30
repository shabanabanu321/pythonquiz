name= input("type your name!")
print("welcome",name,"to this adventure!")
answer=input("you are on a dirt road,it has come to an end and you can go left or right.Which way would you like to go?").lower()
if answer=="left":
    answer=input("you came to a river,you can walk around it or swim across?type walk to walk around and swim if you want to swim across:")
    if answer=="swim":
       print("you swam across the river and were eaten by an alligator")
    elif answer=="walk":
         print("you walked miles and ran out of water and lost the game")
    else:
      print("not a valid option .you lose")
elif answer=="right":
    answer=input("you came aross abridge ,it loose woobly,do you want to cross it or head back (cross/back)?")
    if answer=="back":
        print("you go back and lose")
    elif answer=="cross":
        answer=input("you can cross the bridge and meet a stranger.Do you want to talk to him(yes/no)")
        if answer=="yes":
            print("you talk to stranger and they will gift you the treasure.you won!!")
        elif answer=="no":
            print("you ignored the stranger they got offended and you lost")
        else:
            print("invalid option you lose")
    else:
        print("invalid option you lose")
else:
    print("invalid option you lose")
print("Thank you for trying",name)
