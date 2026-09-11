# when dynamic arrays grow theres an overhead where they copy the
# old array and create more room, and geometric progression is
# what is happening for new insertions

monthly_expenses = [2200, 2350, 2600, 2130, 2190]

comparing_jan_feb_expenses = monthly_expenses[1] - monthly_expenses[0]
print("in feb i spent $",comparing_jan_feb_expenses, " more than jan ")

total_expense_1stQuart = monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2]
print("total expenses in first quarter is ", total_expense_1stQuart)

if 2000 in monthly_expenses:
    print("you spent exactly 2000 in a month")
else:
    print("there's not a single month where you spent exactly 2000")

monthly_expenses.append(1980)
print(monthly_expenses)

print("you get a refund of 200 in april")
monthly_expenses[3] = monthly_expenses[3] - 200
print(monthly_expenses)

heroes = ["spider-man", "thor", "hulk", "iron man", "captain america"]
length_of_list = len(heroes)
print(length_of_list)

heroes.append("black panther")
print(heroes)

heroes.remove("black panther")
print(heroes)
heroes.insert(3,"black panther")
print(heroes)

heroes[1:3] = ["doctor strange"]
print(heroes)
heroes.sort()
print(heroes)

oddNums = []

addNum = int(input("what is the max odd number you would like to add to the list "))
for i in range(1, addNum):
    if(i % 2 == 1):
        oddNums.append(i)
    
print(oddNums)