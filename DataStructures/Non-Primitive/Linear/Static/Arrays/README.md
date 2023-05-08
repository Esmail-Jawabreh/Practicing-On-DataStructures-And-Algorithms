## Arrays

### What is an array ?

#### an array is a data structure consisting of a collection of elements,
#### each identified by at least one array index or key.

#### an array is stored such that the position of each element can computed from its index by mathematical formula. 

#### <strong>Or</strong>

#### An array is a data structure that stores a fixed-size sequence of elements of the same type. It is one of the most fundamental data structures in computer programming. The elements in an array are stored in contiguous memory locations, which allows for efficient access and manipulation of the data.

<br>
<br>

### Arrays advantages:

- Random access: 
##### Elements in an array can be accessed directly using their index, which allows for efficient retrieval of data.
- Compact storage: 
##### Arrays store elements in contiguous memory locations, resulting in efficient memory usage.
- Efficiency: 
##### Arrays facilitate efficient manipulation and processing of large sets of data due to their predictable memory layout.

<br>
<br>

### Why do we need an array ?

- Storing and organizing data: 
##### Arrays provide a way to store and organize collections of data in a structured manner. Whether it's a list of numbers, names, or any other type of information, arrays allow you to keep related data together and access it efficiently.

- Random access: 
##### Arrays enable efficient random access to individual elements based on their index. By knowing the index of an element, you can directly access it without having to search through the entire collection. This random access allows for quick retrieval, modification, or processing of data.

- Iteration and traversal: 
##### Arrays make it easy to iterate over the elements in a collection using loops. By sequentially accessing each element in the array, you can perform operations on them, such as printing, summing, sorting, or applying algorithms.

- Efficiency in memory usage: 
##### Arrays store elements in contiguous memory locations. This property makes arrays memory-efficient because they use a fixed amount of memory, regardless of the number of elements. This efficiency is especially important when dealing with large amounts of data.

- Multi-dimensional data: 
##### Arrays can have multiple dimensions, such as two-dimensional matrices or grids. They allow you to represent and manipulate complex data structures, such as tables, images, or graphs, in a straightforward manner.

- Algorithms and data manipulation: 
##### Arrays are a fundamental building block for many algorithms and data manipulation operations. Sorting, searching, filtering, and many other operations often rely on arrays for efficient implementation and execution.

- Interfacing with lower-level operations: 
##### Arrays provide a convenient way to interface with lower-level operations and systems, such as interacting with memory, file I/O, or network protocols. They allow you to represent and manipulate data in a format that is compatible with these operations.

<br>
<br>

### Types of array

- One-dimensional array: 
##### Also known as a linear array, it is the simplest form of an array that stores elements in a single row. Each element is accessed using a single index. For example, an array of integers [1, 2, 3, 4, 5] is a one-dimensional array.

- Two-dimensional array: 
##### A two-dimensional array, also called a matrix, consists of elements arranged in rows and columns, forming a grid-like structure. It is accessed using two indices, one for the row and another for the column. For example, a 3x3 matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]] is a two-dimensional array.

- Multi-dimensional array: 
##### A multi-dimensional array has more than two dimensions. It can have three or more indices for accessing elements. Multi-dimensional arrays are useful for representing complex data structures like cubes, tensors, or higher-dimensional spaces.

- Jagged array: 
##### A jagged array, also known as an array of arrays, is an array whose elements are themselves arrays. Unlike a multidimensional array, jagged arrays allow for different lengths of sub-arrays. Each sub-array can have a different number of elements. For example, [[1, 2], [3, 4, 5], [6, 7, 8, 9]] is a jagged array.

- Dynamic array: 
##### A dynamic array is a resizable array that can change its size dynamically during runtime. It automatically grows or shrinks as elements are added or removed. Dynamic arrays provide flexibility when the number of elements is not known in advance, and they are commonly used in languages that support them, like Python's lists or Java's ArrayList.

- Sparse array: 
##### A sparse array is an array where most of the elements have a default or null value. It is designed to optimize memory usage by only storing non-default or non-null values. Sparse arrays are useful when dealing with large collections with mostly empty or default values, as they reduce memory consumption.

<br>
<br>

### Arrays is python

#### The array module in Python provides a fixed-size array data type that is more memory-efficient compared to lists when storing large collections of homogeneous data. This module is particularly useful when dealing with numeric data.

<br>

- insert()
##### The insert() method is a built-in function in Python that allows you to insert an element at a specified position.
```
name.insert(index, element)
```
<br>

- remove()
##### The remove() method is a built-in function in Python that allows you to remove the first occurrence of a specified element
```
name.remove(element)
```
<br>

- append()
##### The append() method is a built-in function in Python that allows you to add an element to the end.
```
name.append(element)
```
<br>

- extend()
##### The extend() method is a built-in function in Python that allows you to append elements from another iterable (such as a list, tuple, or string) to the end. 
```
name.extend(iterable)
```
<br>

- pop()
##### The pop() method is a built-in function in Python that allows you to remove and retrieve an element from a specific position.
```
name.pop(element)
```
<br>

- index()
##### The index() method is a built-in function in Python that allows you to find the index of the first occurrence of a specified element.
```
name.index(element)
```
<br>

- reverse()
##### The reverse() method is a built-in function in Python that allows you to reverse the order of elements.
```
name.reverse()
```
<br>

- buffer_info()
##### The buffer_info() method is a method specific to the array module in Python. It returns a tuple containing information about the underlying buffer of an array object. 
##### This method provides details such as the address and size of the buffer, which can be useful for low-level operations.
```
name.buffer_info()
```
<br>

- count()
##### The count() method is a built-in function in Python that allows you to count the number of occurrences of a specified element.
```
name.count(element)
```
<br>

- tostring()
##### In Python, the tostring() method is not available for lists. However, if you are referring to the tostring() method in the array module, it is used to convert an array to a string of bytes.
```
name.tostring()
```
<br>

- "slice"
##### A slice is a way to extract a portion of a sequence, such as a string, list, or tuple, in Python. It allows you to specify a range of indices to retrieve a subset of the elements from the original sequence.
```
sequence[start:end:step]
```

<br>
<br>

### Time and Space complexity of One Dimensional Array:
![One-Dimensional-Array](../../../../../Assets/One-Dimensional-Array.png)

<br>
<br>
