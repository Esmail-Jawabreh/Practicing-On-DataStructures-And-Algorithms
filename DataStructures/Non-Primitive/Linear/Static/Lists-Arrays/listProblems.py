# extracting the middle elements from a list.
def middle(lst):
    new = lst[1:]
    del new[-1]
    return new


# calculating the sum of the elements along the diagonal of a square matrix. (2D Lists)
def sumDiagonal(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i][i]
    return sum


# finding the first and second largest elements in a given list. (Best Score)
def firstSecond(given_list):
    a = given_list  # make a copy
    a.sort(reverse=True)
    print(a)

    first = a[0]
    second = None

    for element in given_list:
        if element != first:
            second = element
            return first, second


# finding a missing number in a given list of consecutive numbers.
def missingNumber(myList, totalCount):
    expectedSum = totalCount * ((totalCount + 1) / 2)
    actualSum = 0
    for i in myList:
        actualSum += i
    return int(expectedSum - actualSum)


# removing duplicate elements from a given list.
def removeDuplicates(myList):
    new_list = []

    for i in myList:
        if i not in new_list:
            new_list.append(i)

    return new_list


# finding pairs of numbers in a given list that add up to a specified sum.
def pairSum(myList, sum):
    result = []
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] + myList[j] == sum:
                result.append(str(myList[i]) + "+" + str(myList[j]))
    return result
