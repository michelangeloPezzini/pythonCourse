
userAnswer = input(
    "Hello user, we are gonna play a game. You should answer a serie of question. Are you ok with that? yes or no? ")

if userAnswer == "yes":
    print("You will create a story with aleatory worlds.")
    print("There are examples, but you can write whatever you want. Remember to follow the script, write what you are asking to.")
    print("That`s the funny part.")
    adjective = str(
        input("Type the first *ADJECTIVE* that comes to your mind! EX: Ugly or Cute "))
    animal = str(
        input("Type the first wild *ANIMAL* that comes to your mind! EX: Lion or Bear "))
    verb = str(
        input("Type the first *VERB* that comes to your mind! EX: Running or Jumping "))
    food = str(
        input("Type the first *food* that comes to your mind! EX: Deear or pizza "))
    word = food.lower()
    first = word[0]
    if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
        first = (f"an {word}")
        newFood = first
    else:
        first = (f"a {word}")
        newFood = first
    # end

    exclamation = str(
        input("Type the first *EXCLAMATION* that comes to your mind! EX: Wow! or Gosh! ")).capitalize()
    otherVerb = str(
        input("Type another *VERB* that comes to your mind! EX: Screeaming or Crying "))
    otherVerbTwo = str(
        input("Type another *VERB* that comes to your mind! EX: Jump or fight "))

  # Check if the first letter of a string is a vowel
    item = str(
        input("type an *OBJECT* to throw at the animal! EX: shoes or apple "))
    word = item.lower()
    first = word[0]
    if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
        first = (f"an {word}")
        newItem = first

    else:
        first = (f"a {word}")
        newItem = first
    # end
    place = str(input(
        "Type a public or privated *place* that comes to your mind! EX: Burguer King or cave "))
    days = int(
        input("Type how many *DAYS* passed. EX: 2 or 5 "))
    hero = str(
        input("Type a super *HERO* that comes to your mind! EX: Spider man or Batman "))

    print(f'''The other day, I was really in trouble. It all started when I saw a very
    {adjective} {animal} {verb} down the hallway. The animals was horrible and he was eating {newFood}. {exclamation}! I yelled. But all
    I could think to do was to {otherVerb} over and over. Miraculously,
    that caused it to stop, but not before it tried to {otherVerbTwo}
    right in front of my family. We threw {newItem} at him and after we ran because we were scared. We arrived at the {place} and tried to hide. We waited for {days} days until the {hero} arrived to help us''')

elif userAnswer == "no":
    print("We canot play the game if you dont type 'yes'")
else:
    print("Please enter yes or no.")
