/* Write a function to do the division operation without using the built-in division*/

function division(number, dividedBy) {
    // Write you logic here.
    if (dividedBy === 0) {
        return 0;
    } else if (number < dividedBy) {
        return 0;
    } else {
        return 1 + division(number - dividedBy, dividedBy);
    }
}



/* Write a function that implement Math.pow(x,n) but using recursion
Example:
pow(2,4) = 16
*/

function pow(x, n) {
    // Write you logic here.
    if (n === 0) {
        return 1;
    }

    if (n > 0) {
        return x * pow(x, n - 1);
    } else {
        return 1 / (x * pow(x, -n - 1));
    }
}



/* The Fibonacci Series is a numeric series starting with the integers 0 and 1. In this series,
the next integer is determined by summing the previous two. This gives us:

0, 1, 1, 2, 3, 5, 8, 13, ...

Write a function that take n as parameter and return the nth element in the Fibonacci Series

Example: n = 4 ==> 3, n= 0 ==> 0, n = 3 ==> 2 */

function fibonacci(n) {
    // Write you logic here.
    if (n < 0) {
        return 0;
    } else if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}



/* The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Example: 
Input: n = 3, k = 3
Output: "213"  */

function getPermutation(n, k) {
    let nums = [];
    for (let i = 1; i <= n; i++) {
        nums.push(i);
    }

    let result = [];
    let count = 0;

    function backtrack(temp) {
        if (temp.length === n) {
            count++;
            if (count === k) {
                result = temp.join("");
            }
            return;
        }

        for (let i = 0; i < nums.length; i++) {
            if (!temp.includes(nums[i])) {
                temp.push(nums[i]);
                backtrack(temp);
                temp.pop();
            }
        }
    }

    backtrack([]);

    return result;
}