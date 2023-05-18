## Tuples

#### a tuple is an ordered, immutable collection of elements. 
#### It is similar to a list, but unlike lists, tuples cannot be modified once created.
#### Tuples are defined using parentheses () or the tuple() constructor. 
<br>

#### Tuples are commonly used in situations where you want to group related values together, such as returning multiple values from a function or representing coordinates in a 2D plane.
<br>
<br>

---
<br>

### Tuples vs Lists

#### Tuples and lists are both used to store collections of elements in Python, but they have some important differences in terms of their properties and use cases:
<br>

- Mutability: 
##### Lists are mutable, which means you can modify, add, or remove elements from a list after it is created. 
##### Tuples, on the other hand, are immutable, meaning their elements cannot be changed once the tuple is created.
<br>

- Syntax: 
##### Lists are defined using square brackets [], 
##### while tuples are defined using parentheses ().
<br>

- Performance: 
##### Tuples are generally more lightweight and faster to create and access than lists. 
##### Since tuples are immutable, they can be optimized for performance by the Python interpreter. 
##### Lists, being mutable, require additional memory allocation and operations when elements are added, removed, or modified.
<br>

- Use Cases: 
##### Tuples are commonly used when you want to store a collection of related values that should not be changed, such as coordinates, database records, or function arguments. 
##### Lists are more suitable when you need a dynamic collection of elements that can be modified, such as a list of items in a shopping cart or a collection of user inputs.
<br>

#### In summary, if you have a collection of elements that should not be changed, use a tuple. If you need a collection that can be modified or updated, use a list.
<br>
<br>

---
<br>

### Tuples Methods
<br>

- count(element): 
##### Returns the number of times a specified element appears in the tuple.
```
my_tuple = (1, 2, 2, 3, 2, 4)
print(my_tuple.count(2))  # Output: 3
```
<br>

- index(element): 
##### Returns the index of the first occurrence of a specified element in the tuple.
```
my_tuple = (1, 2, 2, 3, 2, 4)
print(my_tuple.index(2))  # Output: 1
```
<br>

- len(tuple): 
##### Returns the length (number of elements) of the tuple.
```
my_tuple = (1, 2, 3, 'a', 'b', 'c')
print(len(my_tuple))  # Output: 6
```
<br>

- sorted(tuple): 
##### Returns a new list containing the sorted elements of the tuple.
```
my_tuple = (3, 1, 4, 2)
sorted_tuple = sorted(my_tuple)
print(sorted_tuple)  # Output: [1, 2, 3, 4]
```
<br>

- tuple(iterable): 
##### Creates a new tuple from an iterable object, such as a list or another tuple.
```
my_list = [1, 2, 3]
new_tuple = tuple(my_list)
print(new_tuple)  # Output: (1, 2, 3)
```
<br>

