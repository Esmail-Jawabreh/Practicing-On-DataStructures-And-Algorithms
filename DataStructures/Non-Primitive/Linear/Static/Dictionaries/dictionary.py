# Update/add element to the dictionary \\ O(1)
myDict = {"name": "Edy", "age": 26}
myDict["address"] = "London"

print(myDict)
print("---\n")


# Traverse through a dictionary \\ O(n)
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])


traverseDict(myDict)
print("---\n")


# Searching a dictionary \\ O(n)
def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "The value does not exist"


print(searchDict(myDict, 27))
print("---\n")


# Delete or remove a dictionary \\ O(n)
myDict.pop("name")
# myDict.popitem() --> delete randomly
# myDict.clear() --> delete all elements
# del myDict['age'] --. to delete item

print(myDict)
print("---\n")


# sorted method
myDict = {"eooooa": 1, "aas": 2, "udd": 3, "sseo": 4, "werwi": 5}

print(sorted(myDict, key=len))
print("---\n")
