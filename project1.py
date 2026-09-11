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


def delete_contact(people):
    print("contact list size: ", len(people))
    if not people:
        print("contact list is empty")
        return

    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

    while True:
        number = input("enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("invalid number, out of range!")
            else:
                break
        except ValueError:
            print("invalid number")
    people.pop(number - 1)
    print("person deleted")


# mutable property which means changes to the list will happen everywhere

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
        delete_contact(people)
    elif command == "search":
        pass
    elif command == "q":
        break
    else:
        print("invalid command")

print(people)
