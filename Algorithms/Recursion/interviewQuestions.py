# Q-01 \ Sum of Digits
# How to find the sum of digits of a positive integer number using recursion ?


def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "The number has to be positive integer only."
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(int(n / 10))


# Q-02 \ Power
# How to calculate power of a number using recursion ?


def power(base, exp):
    assert exp >= 0 and int(exp) == exp, "The exponent must be positive integer only."
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp - 1)


# Q-03 \ Greatest Common Divisor
# How to find GCD (great common Divisor) of two numbers using recursion ?


def gcd(a, b):
    assert int(a) == a and int(b) == b, "the numbers must be integers only."
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Q-04 \ Decimal To Binary
# How to convert a number from Decimal to Binary using recursion ?


def decimalToBinary(n):
    assert int(n) == n, "the parameter must be an integers only."
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(int(n / 2))
