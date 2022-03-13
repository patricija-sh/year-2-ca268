print("Enter a name and number, or a name and ? to query (!! to exit)")

phonebook = {}

n = input()
while n != "!!":
    name, x = n.split()
    if x == "?":
        if name in phonebook:
            print(f"{name} has number {phonebook[name]}")
        else:
            print(f"Sorry, there is no {name}")
    else:
        phonebook[name] = x
    n = input()

print("Bye")
