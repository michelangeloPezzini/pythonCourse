def vowel(item):
    word = item.lower()
    first = word[0]
    if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
        first = (f"an {word}")
        print(first)
    else:
        first = (f"a {word}")
        print(first)


var = str(
    input("type an *OBJECT* to throw at the animal! EX: shoes or apple "))

print(f"New item is: {vowel(var)}")
