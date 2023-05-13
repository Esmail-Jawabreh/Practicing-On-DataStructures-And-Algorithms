# from array import *

arr = [1, 2, 3]

# insert 4 in index [3]
arr.insert(3, 4)
print(arr)
print("---\n")


# traverse array \\ O(n)
def traverseArray(array):
    for i in array:
        print(i)


traverseArray(arr)
print("---\n")


# access Element \\ O(1)
def accessElement(array, index):
    if index >= len(array):
        print("there is no element in this indix")
    else:
        print(array[index])


accessElement(arr, 1)
print("---\n")


# search in Array \\ O(n)
def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "the element does not exist in this array."


print(searchInArray(arr, 2))
print(searchInArray(arr, 5))
print("---\n")


# remove 2
arr.remove(2)
print(arr)
print("---\n")