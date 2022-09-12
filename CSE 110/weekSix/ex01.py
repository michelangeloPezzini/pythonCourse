name = str(input("Whats is your name? ")).capitalize()
lastName = str(input("Whats is your last name? ")).capitalize()
menOrWoman = int(input("Type the number: '1' for Male | '2' for Female: "))
if menOrWoman == 1:
    genero = "HIM"
    prince = "Prince"
    pron = "he"
elif menOrWoman == 2:
    genero = "HER"
    prince = "Princess"
    pron = "she"
else:
    print("\n \033[31mChoice not valid.\n Try again.\033[m")


print("\n")
print("\033[33mOne day you wake up and realize you are inside a castle. You get up and decide to investigate the place, as you've never been to one before.\033[m\n")
print("""
  You will always need to choose an option between two!
  \033[32m1: You go to the door and try to open it to understand where you are!'\033[m
  \033[35m2: You look for information about where you are in your own room!\033[m\n
""")
choose = int(input("Choose between option \033[32m'1'\033[m or \033[35m'2'\033[m:\n\n "))


#Choose one
if choose == 1:
  print("""\033[33m
  The door is closed and you hear voices coming towards the room. The person sad:
  -WE NEED TO CONVINCE {} TO MARRY!\033[m \n""".format(genero))
  print("""
  \033[32m1: You run back to bed and pretend to be asleep!\033[m
  \033[35m2: Hide in the closet!\033[m\n
""")

  varOne = int(input("Choose between option \033[32m'1'\033[m or \033[35m'2'\033[m:\n\n"))
  if varOne == 1:
    print("\033[33mA couple in elegant clothes from the 1500s wakes you up saying: {} {}, wake up you need to prepare for your wedding.\033[m\n".format(name, lastName))
    print("""
  \033[32m1: You say that you don't understand anything that is happening and ask them to explain!\033[m
  \033[35m2: Pretend everything is fine and play the part!\033[m\n
""")
    varTwo = int(input("Choose between option \033[32m'1'\033[m or \033[35m'2'\033[m:\n\n"))
    if varTwo == 1:
      print("\033[33mThey believe you are making excuses for not committing to a political marriage. They then ask you to do that to strengthen the armies and have a greater influence in the country. They ask you to calm down as you will be meeting Ellie soon.\033[m\n")
    elif varTwo ==2:
      print("\033[33mYou realize they're apparently your parents, you don't understand how, but you keep pretending to be who they think you are. So after you're done, you go to the main hall and see a giant picture of you with the title 'Prince of Bermesiah: First and Last Name'\033[m\n")
    else:
      print("\n \033[31mChoice not valid.\n Try again.\033[m")

  elif varOne == 2:
    print("""\033[33m
You notice a very elegant couple entering the room and when they realize you're not there they mumble:
Where is {}? we'll need to leave in 2 hours for his wedding.
Guards!! Find {}.\033[m\n""".format(pron, genero))
    print("""
  \033[32m1: Wait for them to leave to try to escape through the window and find answers!\033[m
  \033[35m2: Try to listen more closely to what they are saying!\033[m\n
""")
    varTwo = int(input("Choose between option \033[32m'1'\033[m or \033[35m'2'\033[m:\n\n"))
    if varTwo == 1:
      print("\033[33mWhen you manage to escape through the window on your right, looking at the corridor, you notice that there are guards circulating around the place, you wait for the corridor to be free. Then he manages to escape down the hall and hide in a room full of books, which looks like a giant library.\033[m\n")
    elif varTwo == 2:
      print("\033[33mYou hear them calling you the Prince of Bermesiah, and that today is your wedding to Ellie Loverfild. They need you to marry in order to unite the two families and kingdoms.\033[m\n")
    else:
      print("\n \033[31mChoice not valid.\n Try again.\033[m")

  else:
    print("\n \033[31mChoice not valid.\n Try again.\033[m")



#Choose Two
elif choose ==2:
  print("\n\033[33mYou find on the headboard a letter referring to you as the {} {}. Soon after, you hear someone moving the knob to open the door.".format(prince, lastName))
  print("""The door is closed and you hear voices coming towards the room. The person sad:
-WE NEED TO CONVINCE {} TO MARRY \n\033[m""".format(genero))
  print("""
  \033[32m1: You hide under the bed!\033[m
  \033[35m2: Wait for people to come in to chat!\033[m\n
""")
  varOne = int(input("Choose between option \033[32m'1'\033[m or \033[35m'2'\033[m:\n\n"))
  if varOne == 1:
    print("""\033[33m
You notice a very elegant couple entering the room and when they realize you're not there they mumble:
Where is {}? we'll need to leave in 2 hours for his wedding.
Guards!! Find {}.\033[m\n""".format(pron, genero))
    print("""
  \033[32m1: Wait for them to leave to look around the room for more clues!\033[m
  \033[35m2: You decide to show up and ask them to explain more about this wedding to you.\033[m\n
""")
    varTwo = int(input("Choose between option \033[32m'1'\033[m or \033[35m'2'\033[m:\n\n"))

    if varTwo == 1:
      print("\033[33mAfter they leave the room you start to investigate, you don't find anything technological, it's all analog, it seems that when you came here, you didn't bring anything from your world. You find only letters addressed to you, but without any important information.\033[m\n")
    elif varTwo == 2:
      print("\033[33mYou are scared, as you discover that it is your own wedding, but you remain calm around them. They explain to you that even though you don't know the girl, she appears to be a very nice person.\033[m\n")
    else:
      print("\n \033[31mChoice not valid.\n Try again.\033[m")

  elif varOne == 2:
    print("\033[33mA couple in elegant clothes from the 1500s enters the room and they call you: {} {}, hurry up we have to go, your wedding will be at 18:00h\033[m".format(name, lastName))
    print("""
  \033[32m1: You pretend everything is fine and get on paper to see how far this story goes!\033[m
  \033[35m2: You say you need to get some air, and try to find clues around the castle!\033[m\n
""")
    varTwo = int(input("Choose between option \033[32m'1'\033[m or \033[35m'2'\033[m:\n\n"))
    if varTwo == 1:
      print("\033[33mWhen you find out that it's your wedding you're getting ready for, you get scared, you think about hiding, but there's nowhere to run, there are many guards watching over you. They then give you the fanciest and most uncomfortable clothes you've ever worn, but you look classy.\033[m\n")
    elif varTwo == 2:
      print("\033[33mWhen going to an outdoor area, you see that you are in a giant castle, and that there is a very beautiful view of the city. You understand that this is not part of the time you lived in, so you begin to suspect.\033[m\n") 
    else:
      print("\n \033[31mChoice not valid.\n Try again.\033[m")
  else:
    print("\n \033[31mChoice not valid.\n Try again.\033[m")

else:
    print("\n \033[31mChoice not valid.\n Try again.\033[m")