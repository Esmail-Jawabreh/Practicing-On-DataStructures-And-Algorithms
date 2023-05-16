# Accessing
shoppingList = ["Milk", "Cheese", "Butter"]

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "+"
    print(shoppingList[i])
print("---\n")


# Traversing
empty = []

for i in empty:
    print("I am empty")
print("---\n")


# Update/Insert \\ O(n)
List1 = [1, 2, 3, 4, 5, 6, 7]
List2 = [11, 12, 13, 14]
print(List1)
print(List2)

List1.insert(4, 15)
List1.append(55)
List1.extend(List2)

print(List1)
print("---\n")


# Slice | Delete \\ O(n)
newList = ["a", "b", "c", "d", "e", "f"]

newList.pop(2)

del newList[2:4]
newList.remove("e")

print(newList)
print("---\n")


#  Searching for an element in the List \\ O(n)
myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]


def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return "The value does not exist in the list"


print(searchinList(myList, 100))
print("---\n")


#   List operations / functions
total = 0
count = 0

while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    total = total + value
    count = count + 1
    average = total / count

print("Average:", average)
print("\n")


numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)

print("Average:", average)
print("---\n")


# strings 
a = 'spam-spam1-spam2'
delimiter = 'a'
b = a.split(delimiter)
print(b)
print(delimiter.join(b))
print("---\n")
