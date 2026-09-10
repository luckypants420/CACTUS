def add_person():
    name = input("what is your name? ")
    age = input("how old r u ? ")
    email = input("what is your email? ")
    person = {
        "name": name,
        "age": age,
        "email": email,
    }
    return person


people = []

while True:
    command = input(
        "would you like to add, delete, or search for a person?, (enter q to exit!)"
    ).lower()
    if command == "add":
        person = add_person()
        people.append(person)
        print("person added!")
    elif command == "delete":
        pass
    elif command == "search":
        pass
    elif command == "q":
        break
    else:
        print("invalid command")

print(people)
