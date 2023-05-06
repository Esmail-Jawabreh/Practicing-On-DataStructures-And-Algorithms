# Q-01 \ Product and Sum
# what is the runtime of below code ?
def foo(array):
    sum = 0
    product = 1

    for i in array:
        sum += i

    for i in array:
        product *= i

    print("Sum = " + str(sum) + ", Produt = " + str(product))


# Answer:
# Time Complexity: O(n)
#######################


# Q-02 \ Print Pairs
# what is the runtime of below code ?
def printPairs(array):
    for i in array:
        for j in array:
            print(str(i) + "," + str(j))


# Answer:
# Time Complexity: O(n^2)
#########################


# Q-03 \ Print Unordered Pairs
# what is the runtime of below code ?
def printUnoorderPairs(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            print(array[i] + "," + array[j])


# Answer:
# Time Complexity: O(n^2)
#########################


# Q-04 \ Print Unordered Pairs 2 Arrays
# what is the runtime of below code ?
def printUnoorderPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))


# Answer:
# Time Complexity: O(ab)
#########################


# Q-05 \ Print Unordered Pairs 2 Arrays 100000 Units
# what is the runtime of below code ?
def printUnoorderPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0, 100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))


# Answer:
# Time Complexity: O(ab)
#########################


# Q-06 \ Reverse
# what is the runtime of below code ?
def reverse(array):
    for i in range(0, int(len(array / 2))):
        other = len(array) - i - 1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)


# Answer:
# Time Complexity: O(n)
#########################


# Q-07 \ O(N)  Equivalents
# Which of the following are equivalent O(N)? Why?
# 1. O(N+P), where P < N/2
# 2. O(2N)
# 3. O(N+logN)
# 4. O(N+NlogN)
# 5. O(N+M)


# Answer:
# 1 & 2 & 3
#########################


# Q-08 \ Factorial Complexity
# what is the runtime of below code ?
def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Answer:
# Time Complexity: O(n)
#########################


# Q-09 \ Fibonacci Complexity
# what is the runtime of below code ?
def allFib(n):
    for i in range(n):
        print(str(i) + ":, " + str(fib(i)))


def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# Answer:
# Time Complexity: O(2^n)
#########################


# Q-10 \Powers of 2
# what is the runtime of below code ?
def powerOf2(n):
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powerOf2(int(n / 2))
        curr = prev * 2
        print(curr)
        return curr


# Answer:
# Time Complexity: O(logN)
#########################
