# Exercise number 3°
# I added a tip to plus with the total costs

name = str(input("Whats is your name? "))
lastName = str(input("Whats is your last name? "))
menOrWoman = int(input("Type the number: '1' for Male | '2' for Female: "))
if menOrWoman == 1:
    genero = "HIM"
    prince = "prince"
    pron = "he"
elif menOrWoman == 2:
    genero = "HER"
    prince = "princess"
    pron = "she"
else:
    print("Type again")

print("\n")
print("One day you wake up and realize you are inside a castle. You get up and decide to investigate the place, as you've never been to one before.")
print("""
  You will always need to choose an option between two!
  1: You go to the door and try to open it to understand where you are!
  2: You look for information about where you are in your own room.
""")
choose = input("Choose between option '1' or '2':\n\n ")

# First choose
if choose == "1":
    print("""
  The door is closed and you hear voices coming towards the room. The person sad:
  -WE NEED TO CONVINCE {} TO MARRY \n""".format(genero))
    print("""
  1: You run back to bed and pretend to be asleep!
  2: Hide in the closet.\n
""")
    varOne = int(input("Choose between option '1' or '2':\n\n"))
    # Second choose
    if varOne == 1:
        print("A couple in elegant clothes from the 1500s wakes you up saying: {} {} Wake up! we need to talk about the wedding. \n".format(name, lastName))
        print("""
        1: You say you don't understand what's going on and run!
        2: Pretend everything is fine and play the part!\n
        """)
        varTwo = int(input("Choose between option '1' or '2':\n\n"))
        if varTwo == 1:
            print("When you try to run and escape through the door on your right there are guards and on your left the corridor is free. You manage to escape down the hall and hide in a room full of books.\n")
        elif varTwo == 2:
            print("You realize they're apparently your parents, you don't understand how, but you keep pretending to be who they think you are.\n")
        else:
            ("Type again!")

    elif varOne == 2:
        print("""
        You notice a very elegant couple entering the room and when they realize you're not there they mumble:
        -Where is {}? I thought he would be ready for the wedding meeting by now.\n
        """.format(pron))
        print("""
        1: Wait for them to leave to try to escape and find answers!
        2: Open the closet and demand that they explain what's going on!\n
        """)
        varTree = int(input("Choose between option '1' or '2':\n\n"))
        if varTree == 1:
            print("When they leave, they lock the door, your only way out is the window, but the question is how are you going to get out of a castle that is almost 50 meters high.\n")
        elif varTree == 2:
            print("They believe you are making excuses for not making the commitment of the political marriage and they lock you in your room to think about the misbehavior.\n")

    else:
        print("Type again!")

# First choose
elif choose == "2":
    print("You find on the headboard a letter referring to you as a {}. Soon after, you hear someone moving the knob to open the door.\n".format(prince))
    # Second choose
    print("""
  1: You run back to bed and pretend to be asleep!
  2: Hide in the closet.\n
    """)
    varOne = int(input("Choose between option '1' or '2':\n\n "))
    # Second choose
    if varOne == 1:
        print("A couple in elegant clothes from the 1500s wakes you up saying: {} {} Wake up! we need to talk about the wedding. \n".format(name, lastName))
        print("""
        1: You say you don't understand what's going on and run!
        2: Pretend everything is fine and play the part!\n
        """)
        varTwo = int(input("Choose between option '1' or '2':\n\n "))
        if varTwo == 1:
            print("When you try to run and escape through the door on your right there are guards and on your left the corridor is free. You manage to escape down the hall and hide in a room full of books.\n")
        elif varTwo == 2:
            print("You realize they're apparently your parents, you don't understand how, but you keep pretending to be who they think you are.\n")
        else:
            ("Type again!")

    elif varOne == 2:
        print("""
        You notice a very elegant couple entering the room and when they realize you're not there they mumble:
        -Where is {}? I thought he would be ready for the wedding meeting by now.\n
        """.format(pron))
        print("""
        1: Wait for them to leave to try to escape and find answers!
        2: Open the closet and demand that they explain what's going on!\n
        """)
        varTree = int(input("Choose between option '1' or '2':\n\n "))
        if varTree == 1:
            print("They believe you are making excuses for not making the commitment of the political marriage and they lock you in your room to think about the misbehavior.\n")
        elif varTree == 2:
            print("When they leave, they lock the door, your only way out is the window, but the question is how are you going to get out of a castle that is almost 50 meters high.\n")


else:
    print("\n Choice not valid.\n Try again.")
