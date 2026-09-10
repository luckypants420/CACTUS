def addPerson():
    name = input("what is your name?")
    age = input("how old r u?")

    person = {"name": name, "age": age}
    return person


people = []

command = input("would you like to add a perosn? ").lower()

if command == "yes":
    person = addPerson()
    people.append(person)
elif command == "no":
    print("you exited the program !")

print(people)