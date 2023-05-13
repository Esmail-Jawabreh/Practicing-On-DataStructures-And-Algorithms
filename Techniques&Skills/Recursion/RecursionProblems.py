# capitalize Words
def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])


words = ["i", "am", "learning", "recursion"]
print(capitalizeWords(words))  # ['I', 'AM', 'LEARNING', 'RECURSION']
print("---\n")


# capitalize First
def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])


print(capitalizeFirst(["car", "taco", "banana"]))  # ['Car','Taco','Banana']
print("---\n")


# collect Strings
def collectStrings(obj):
    resultArr = []
    for key in obj:
        if type(obj[key]) is str:
            resultArr.append(obj[key])
        if type(obj[key]) is dict:
            resultArr = resultArr + collectStrings(obj[key])
    return resultArr


obj = {
    "stuff": "foo",
    "data": {
        "val": {
            "thing": {"info": "bar", "moreInfo": {"evenMoreInfo": {"weMadeIt": "baz"}}}
        }
    },
}

print(collectStrings(obj))  # ['foo', 'bar', 'baz'])
print("---\n")


# Factorial
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)


print(factorial(1))  # 1
print(factorial(2))  # 2
print(factorial(4))  # 24
print(factorial(7))  # 5040
print("---\n")


# fib
def fib(num):
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)


print(fib(4))  # 3
print(fib(10))  # 55
print(fib(28))  # 317811
print(fib(35))  # 9227465
print("---\n")


# flatten
def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else:
            resultArr.append(custItem)
    return resultArr


print(flatten([1, 2, 3, [4, 5]]))  # [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]]))  # [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]]))  # [1, 2, 3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))  # [1, 2, 3]
print("---\n")


# is Palindrome ?
def isPalindrome(strng):
    if len(strng) == 0:
        return True
    if strng[0] != strng[len(strng) - 1]:
        return False
    return isPalindrome(strng[1:-1])


print(isPalindrome("awesome"))  # false
print(isPalindrome("foobar"))  # false
print(isPalindrome("tacocat"))  # true
print(isPalindrome("amanaplanacanalpanama"))  # true
print(isPalindrome("amanaplanacanalpandemonium"))  # false
print("---\n")


# nested Even Sum
def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key] % 2 == 0:
            sum += obj[key]
    return sum


obj1 = {
    "outer": 2,
    "obj": {
        "inner": 2,
        "otherObj": {"superInner": 2, "notANumber": True, "alsoNotANumber": "yup"},
    },
}

obj2 = {
    "a": 2,
    "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
    "c": {"c": {"c": 2}, "cc": "ball", "ccc": 5},
    "d": 1,
    "e": {"e": {"e": 2}, "ee": "car"},
}

print(nestedEvenSum(obj1))  # 6
print(nestedEvenSum(obj2))  # 10
print("---\n")


# Power
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


print(power(2, 0))  # 1
print(power(2, 2))  # 4
print(power(2, 4))  # 16
print("---\n")


# product Of Array
def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])


print(productOfArray([1, 2, 3]))  # 6
print(productOfArray([1, 2, 3, 10]))  # 60
print("---\n")


# recursive Range
def recursiveRange(num):
    if num <= 0:
        return 0
    return num + recursiveRange(num - 1)


print(recursiveRange(6))
print("---\n")


# reverse
def reverse(strng):
    if len(strng) <= 1:
        return strng
    return strng[len(strng) - 1] + reverse(strng[0 : len(strng) - 1])


print(reverse("python"))  # 'nohtyp'
print(reverse("appmillers"))  # 'srellimppa'
print("---\n")


# some Recursive
def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not (cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True


def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True


print(someRecursive([1, 2, 3, 4], isOdd))  # true
print(someRecursive([4, 6, 8, 9], isOdd))  # true
print(someRecursive([4, 6, 8], isOdd))  # false
print("---\n")


# stringify Numbers
def stringifyNumbers(obj):
    newObj = obj
    for key in newObj:
        if type(newObj[key]) is int:
            newObj[key] = str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key] = stringifyNumbers(newObj[key])
    return newObj


obj = {
    "num": 1,
    "test": [],
    "data": {"val": 4, "info": {"isRight": True, "random": 66}},
}


print(stringifyNumbers(obj))
# {'num': '1',
#  'test': [],
#  'data': {'val': '4',
#           'info': {'isRight': True, 'random': '66'}
#           }
# }
print("---\n")
