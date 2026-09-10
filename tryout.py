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


def sqrNum(nums):
    sqrNums = []
    for i in nums:
        sqrNums.append(i * i)
    return sqrNums

numbers = [9,3,2,5]
print(sqrNum(numbers))
print(numbers)