## Recursion
<br>

### What is Recursion ?

#### Recursion is a way of solving a problem by having a function calling itself. 
#### and it's a method of solving a computational problem where the solution depends on solutions to smaller instances of the same problem. 
#### In other words, the function is defined in terms of itself. 
#### Recursion is a powerful technique that can be used to solve many problems, especially those that have a recursive structure.

#### and it can be used to solve a wide range of problems, including traversing trees and graphs, sorting algorithms such as quicksort and merge sort, and many more.
<br>
<br>

### Why Recursion ?

#### Recursion is a powerful programming technique that can be used to solve a wide range of problems.
#### Here are some reasons why recursion is a useful tool for programmers:
- Solving complex problems: 
##### Recursion is especially useful for solving problems that have a recursive structure. By breaking a problem down into smaller sub-problems that are similar to the original problem, recursion can provide an elegant and efficient solution.
- Simplifying code: 
##### Recursion can often make code simpler and more readable by breaking complex problems down into smaller, more manageable sub-problems. Recursive code can be easier to understand than complex iterative code.
- Reusability: 
##### Once a recursive function is written, it can be reused in many different contexts. This can save time and effort when solving similar problems in different programs.
- Efficiency: 
##### In some cases, recursion can be more efficient than iteration, especially when dealing with problems that have a recursive structure. For example, recursive algorithms can be used to traverse trees and graphs more efficiently than iterative algorithms.
- Flexibility: 
##### Recursion can be used with many different data structures and algorithms, such as sorting algorithms, search algorithms, and tree and graph traversal algorithms. This makes it a versatile tool for solving a wide range of problems.
- Interviews
<br>
<br>

### When to use it ?
- when we can easily breakdown a problem into similar subproblem.
- when we are fine with extra overhead (both time and space) that comes with it.
- when we need a quick working solution instead of efficient one.
- when traverse a tree.
- when we use memoization recursion.

### When to avoid it ?
- if time and space complexity matters for us.
- Recursion uses more memory, if we use embedded memory.
- Recursion can be slow.

---
<br>

### Recursive & Recursion

#### "Recursive" and "Recursion" are related terms, but they have different meanings.

#### "Recursive" refers to a function or method that calls itself. In other words, it is a function that uses recursion to solve a problem.

#### "Recursion" refers to the technique of solving a problem by breaking it down into smaller sub-problems and solving them recursively. Recursion is a programming technique that involves using a function that calls itself to solve a problem.

#### So while "recursive" describes a specific function or method, "recursion" is a more general term that refers to the technique of solving problems by breaking them down into smaller sub-problems and solving them recursively.

---
<br>

### Recursion & Iterative 

#### "Recursion" and "iteration" are two different approaches to solving problems in programming.

#### Recursion is a technique that involves breaking a problem down into smaller sub-problems that are similar to the original problem, and solving them recursively. This involves calling a function from within itself until a base case is reached, where the recursion stops. Recursion can be used to solve many problems, such as traversing trees and graphs, sorting algorithms, and many more.

#### Iteration, on the other hand, involves using loops to repeatedly execute a block of code until a condition is met. In this approach, the solution is achieved by repeatedly executing a set of instructions, rather than by breaking the problem down into smaller sub-problems. Iteration is often used for problems that require repetitive operations, such as sorting, searching, and processing large data sets.

#### Both recursion and iteration have their own strengths and weaknesses, and the choice between them depends on the problem being solved and the specific requirements of the program. In general, recursion can be more elegant and easier to understand for problems that have a recursive structure, while iteration can be more efficient and faster for problems that involve repetitive operations.
##### note: infinite Recursion can lead to system crash, but infinite Iteration seems recycle.
<br>

![types of data structures](../../Assets/Recursion%26Iterative.png)

---
<br>