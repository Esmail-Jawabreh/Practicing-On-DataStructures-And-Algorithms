# Q-01
# What will be the output of the following code block?
init_tuple = ()
print(init_tuple.__len__())
print("---\n")
# A. None
# B.  1
# C. 0
# D. Exception


# Q-02
# What will be the output of the following code block?
init_tuple_a = "a", "b"
init_tuple_b = ("a", "b")

print(init_tuple_a == init_tuple_b)
print("---\n")
# A. 0
# B.  1
# C. False
# D. True


# Q-03
# What will be the output of the following code block?
init_tuple_a = "1", "2"
init_tuple_b = ("3", "4")

print(init_tuple_a + init_tuple_b)
print("---\n")
# A. (1, 2, 3, 4)
# B.  (‘1’, ‘2’, ‘3’, ‘4’)
# C. [‘1’, ‘2’, ‘3’, ‘4’]
# D. None


# Q-04
# What will be the output of the following code block?
init_tuple_a = 1, 2
init_tuple_b = (3, 4)

[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]
print("---\n")
# A. Nothing gets printed.
# B.  4
# C. 10
# D. TypeError: unsupported operand type


# Q-05
# What will be the output of the following code block?
init_tuple = [(0, 1), (1, 2), (2, 3)]
result = sum(n for _, n in init_tuple)

print(result)
print("---\n")
# A. 3
# B. 6
# C. 9
# D. Nothing gets printed.


# Q-06
# Which of the following statements given below is/are true?
# D
# A. Tuples have structure, lists have an order.
# B. Tuples are homogeneous, lists are heterogeneous.
# C. Tuples are immutable, lists are mutable.
# D. All of them.


# Q-07
# What will be the output of the following code block?
l = [1, 2, 3]
init_tuple = ("Python",) * (l.__len__() - l[::-1][0])

print(init_tuple)
print("---\n")
# A. ()
# B. (‘Python’)
# C. (‘Python’, ‘Python’)
# D. Runtime Exception.


# Q-08
# What will be the output of the following code block?
init_tuple = ("Python") * 3

print(type(init_tuple))
print("---\n")
# A. <class ‘tuple’>
# B. <class ‘str’>
# C. <class ‘list’>
# D. <class ‘function’>


# Q-09
# What will be the output of the following code block?
init_tuple = (1,) * 3
init_tuple[0] = 2

print(init_tuple)
print("---\n")
# A. (1, 1, 1)
# B. (2, 2, 2)
# C. (2, 1, 1)
# D. TypeError: ‘tuple’ object does not support item assignment


# Q-10
# What will be the output of the following code block?
init_tuple = ((1, 2),) * 7

print(len(init_tuple[3:8]))
print("---\n")
# A. Exception
# B. 5
# C. 4
# D. None
