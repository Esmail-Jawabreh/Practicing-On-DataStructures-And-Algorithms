# create a Tuple
newTuple = ("a", "b", "c", "d", "e")
newTuple1 = tuple("abcde")

print(newTuple1)
print("---\n")


# Access Tuple elements
print(newTuple[0])
print("---\n")


# Traverse through tuple \\ O(n)

for i in newTuple:
    print(i)


for index in range(len(newTuple)):
    print(newTuple[index])

print("---\n")


# search for an element in Tuple \\ O(n)

print("a" in newTuple)


def searchInTuple(pTuple, element):
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
    return "The element does not exist"


print(searchInTuple(newTuple, "a"))
print("---\n")


# Tuple Operations / Functions
myTuple = (1, 4, 3, 2, 5)
myTuple1 = (1, 2, 6, 9, 8, 7)

print(myTuple + myTuple1)
print(myTuple * 4)
print(2 in myTuple1)

myTuple1.count(2)
myTuple1.index(2)
