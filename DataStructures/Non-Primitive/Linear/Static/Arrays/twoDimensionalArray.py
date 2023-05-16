import numpy as np

twoDArray = np.array(
    [[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]
)
print(twoDArray)
print("---\n")


# Insertion

newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1)
# axis = 0  => row
# axis = 1  => column

print(newTwoDArray)
print("---\n")


newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=0)
print(newTwoDArray)
print("---\n")


# Accessing an element of Two Dimensional Array \\ O(1)
def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][colIndex])


accessElements(newTwoDArray, 1, 2)
print("---\n")


# Traversal \\ O(n^2)
def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traverseTDArray(twoDArray)
print("---\n")


# Searching for an element in Two Dimensional Array \\ O(mn)
def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return "The value is located index " + str(i) + " " + str(j)
    return "The element no found"


print(searchTDArray(twoDArray, 10))
print("---\n")


# Deletion \\ O(mn)
newTDArray = np.delete(twoDArray, 1, axis=1)
print(newTDArray)
print("---\n")
