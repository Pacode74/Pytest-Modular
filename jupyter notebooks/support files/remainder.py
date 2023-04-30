# https://realpython.com/python-modulo-operator/

print("I. Modulo in Mathematics")

print("(1) - % 12 time mod 12, yield digits in range from 0 to 11")
# print(00%12)    # 0
# print(1%12)     # 1
# print(2%12)     # 2
# print(3%12)     # 3
# print(4%12)     # 4
# print(5%12)     # 5
# print(6%12)     # 6
# print(7%12)     # 7
# print(8%12)     # 8
# print(9%12)     # 9
# print(10%12)    # 10
# print(11%12)    # 11
# print(12%12)    # 0
# print(13%12)    # 1
# print(14%12)    # 2
# print(15%12)    # 3
# print(16%12)    # 4
# print(17%12)    # 5
# print(18%12)    # 6
# print(19%12)    # 7
# print(20%12)    # 8
# print(21%12)    # 9
# print(22%12)    # 10
# print(23%12)    # 11
# print(24%12)    # 0
# print(25%12)    # 1

time = []
for i in range(0, 13):
    time.append(i % 12)
print(f"{time=}")

times = [t % 12 for t in range(0, 13)]
print(f"{times=}")

n = 7
print(f"n = 7, {[ t % n for t in range(1,n+1)]}")
[1, 2, 3, 4, 5, 0]  # n = 6
[1, 2, 3, 4, 5, 6, 0]  # n = 7

import random

n = random.randint(1, 25)
print([t % n for t in range(1, n + 1)])
print(1 % 3)
print(2 % 3)
print(3 % 3)

r = []
for i in range(1, 10):
    m = random.randint(1, 1000000000000)
    result = r.append(m % 3)
print(f"{r=}")

# 8 o'clock + 9 = 17 o'clock
t = 8 + 9
print(t % 12)
print()

print("(2) - a and b are congruent modulo n")
# https://en.wikipedia.org/wiki/Modular_arithmetic
theory = """ 
:a ≡ b (mod n)
:17 ≡ 5 (mod 12)
:This equation reads “a and b are congruent modulo n.” 
:This means that a and b are equivalent in mod n as they have the same remainder 
 when divided by n.
:This reads “17 and 5 are congruent modulo 12.” 
:17 and 5 have the same remainder, 5, when divided by 12. 
:So in mod 12, the numbers 17 and 5 are equivalent.

:n: modulus, n > 1
:a - b = kn
:17 - 5 = 12

:a = kn + b
:17 = 12 + 5

:a = pn + r     17 = 12 + 5
:b = qn + r     5 = 0 + 5

:p =< r < n

:a - b = kn
:k = p - q

:a mod n    17 mod 12       17 % 12 = 5
:b mod n    5 mod 12        5 % 12 = 5
"""
print(theory)
print(f"17%12: {17%12}")  # 5
print(f"5%12: {5%12}")  # 5
print()

print("(3) - example of Euclidean division")
# https://en.wikipedia.org/wiki/Euclidean_division
"""Suppose that a pie has 9 slices and they are to be divided evenly among 4 people.
a = bq + r  (9 = 4 * 2 + 1)
:conditions: b != 0, 0 =< r < |b|
a: dividend (number of slices in a pie = 9)
b: divisor (number of people = 4)
q: quotient (number of slices to be received by each person = 2)
r: remainder (leftover = 1)
9 % 4 
"""
# print(a % b)  # r
print(9 % 4)  # 1
print()

print(
    "(4) - Negative Operand - remiander takes the sign of the divisor, 'b' is a divisor"
)
# print(a % (-b))  # -r
# print((-a) % b)  # r
print(f"9 % -4: {9 % -4}")  # -3
print(f"-9 % 4: {-9 % 4}")  # 3
#
# difference between JavaScript and Python
# r: remainder
# a: dividend
# b: divisor
a = 8
b = -3
# print(8 % -3)  # 2  in JavaScript.
# use trancate(ceil) division which will always round a negative number toward zero
from math import factorial, floor, ceil

rj = a - (b * ceil(a / b))  # 2
print(f"rj: {rj}")
# print(-8 % 3)  # -1 in Python
# use floor division which will round a negative number away from zero
rp = a - (b * floor(a / b))  # -1
print(f"rp: {rp}")
#
# While the modulo used with the int and float types will take the sign
# of the divisor, other types(fmod, decimal.Decimal) will not.
from math import fmod

print(8.0 % -3)  # -1.0 : uses the sign of the divisor 'b' using floor division.
print(fmod(8.0, -3.0))  # 2.0 uses the sign og the dividend 'a' using ceil division.
print()

print("(5) - Congruence classes")
"""
a mod 12 = 
:{..., a - 2n, a - n, a, a + n, a + 2n, ...}
:{..., 17 - 2*12, 17 - 12, 17, 17 + 12, 17 + 2*12}
:{..., -7, 5, 17, 29, 41}
  """
print(-7 % 12)  # 5
print(5 % 12)  # 5
print(17 % 12)  # 5
print(29 % 12)  # 5
print(41 % 12)  # 5
print()


def a_mod_n(a, n):
    """Creates congruence list of a's.
    Returns list of the same remainders"""
    ar = [a - 2 * n, a - n, a, a + n, a + 2 * n]
    print(f"{ar=}")  # [-5, 2, 9, 16, 23]
    r = [t % n for t in ar]
    return r  # [2, 2, 2, 2, 2]


print(a_mod_n(9, 7))
print(a_mod_n(5, 12))

print("(6) - Least residue system modulo n")
"""
We usually represent each residue class by the smallest nonnegative 
integer which belongs to that class.

This set, consisting of all the integers congruent to a modulo n, 
is called the congruence class, residue class, or simply residue of 
the integer a modulo n. When the modulus n is known from the context, 
that residue may also be denoted [a].

This set, consisting of all the integers congruent to a modulo 12, 
is called the congruence class, residue class, or simply residue of 
the integer a modulo 12. When the modulus 12 is known from the context, 
that residue may also be denoted [a].

:{0, 1, 2, ..., n -1} - Least residue system modulo n
:{1, 2, 3, 4} (mod 4) - Least residue system modulo 4, has 4 in a set

:{13, 14, 15, 16} (mod 4) - just residual system, does have 4 in set
:{−2, −1, 0, 1} (mod 4)   - just residual system, does have 4 in set
:{−13, 4, 17, 18} (mod 4) - just residual system
:{−5, 0, 6, 21} (mod 4)   - just residual system
:{27, 32, 37, 42} (mod 4) - just residual system

:{−5, 0, 6, 22} (mod 4) - not complete residual system mod 4. 
Because 6 ≡ 22 (mod 4)
:{5, 15}  (mod 4)       - not complete residual system mod 4 
Becase must have 4 residuals.
"""

print(1 % 4)  # 1
print(2 % 4)  # 2
print(3 % 4)  # 3
print(4 % 4)  # 0
print()

""" Just residual system"""
print(13 % 4)  # 1
print(14 % 4)  # 2
print(15 % 4)  # 3
print(16 % 4)  # 0
print()
print(-2 % 4)  # 1
print(-1 % 4)  # 2
print(0 % 4)  # 3
print(1 % 4)  # 0
print()
print(-13 % 4)  # 3
print(4 % 4)  # 0
print(17 % 4)  # 1
print(18 % 4)  # 2
print()
print(-5 % 4)  # 3
print(0 % 4)  # 0
print(6 % 4)  # 2
print(21 % 4)  # 1
print()
print(27 % 4)  # 3
print(32 % 4)  # 0
print(37 % 4)  # 1
print(42 % 4)  # 2
print()
print(-5 % 4)  # 3
print(0 % 4)  # 0
print(6 % 4)  # 2
print(22 % 4)  # 2
print()


print("II. Python Modulo Operator Basics")
print()
print("(7) - Modulo Operator With float")
# The official Python docs suggest using math.fmod()
# over the Python modulo operator when working with float values.
#
# first way
import math

print(math.fmod(13.3, 1.1))
# second way
print(13.3 % 1.1)
print()

print("(8) - Modulo Operator and divmod()")
print(f"37//5: {37//5}")
print(f"37 % 5: {37 % 5}")
import operator

print(f"divmod(37, 5): {divmod(37, 5)}")
print()

print("(9) - Modulo Operator Precedence")
"""The modulo operator (%) shares the same level of precedence as 
the multiplication (*), division (/), and floor division (//) operators."""
print(4 * 10 % 12 - 9)  # -5
print(4 * 10 % (12 - 9))  # 1
print()

print("(10) - % 10 yield the right-most digit")
print(122 % 10)  # 2

print("(11) - % 100 yield the last two digit")
print(122 % 100)  # 22

print("(12) - n% m where m>n yield n")
print(3 % 4)  # 3
print(56 % 78)  # 56

print("(13) - % 2 yield even(==0), uneven(!=0) digits")
for number in range(1, 10):
    if number % 2 != 0:
        print(number)


def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return num % 2 != 0


print()

# # don't compare modulo to one as not all modulo operatons
# # will return the same remainder:
# def is_odd(num):
#     return num % 2 == 1
print(-3 % 2)  # 1
print(3 % -2)  # -1
print(-2 % 2)  # 0
print(2 % -2)  # 0
print()


print("(14) - How to Run Code at Specific Intervals in a Loop")


def split_names_into_rows(name_list, modulus=3):
    for index, name in enumerate(name_list, start=1):
        # -^ central aligning of space
        print(f"{name:-^15}", end=" ")
        # how many names per raw
        if index % modulus == 0:
            print()
    print()


names = ["Picard", "Riker", "Troi", "Crusher", "Worf", "Data", "La Forge"]
split_names_into_rows(names)
print()
split_names_into_rows(names, modulus=2)
print()
split_names_into_rows(names, modulus=1)
print()


print("(15) - How to Create Cyclic Iteration")
# Cyclic iteration describes a type of iteration that
# will reset once it gets to a certain point. Generally,
# this type of iteration is used to restrict the index of
# the iteration to a certain range.

import turtle
import random


def draw_with_cycle_itaration():
    colors = ["green", "cyan", "orange", "purple", "red", "yellow", "white"]

    turtle.bgcolor("gray8")  # Hex: #333333
    turtle.pendown
    turtle.pencolor(random.choice(colors))  # First color is random

    i = 0  # Initial index

    while True:
        i = (i + 1) % 6  # Update the index [1, 2, 3, 4, 5, 0]
        turtle.pensize(i)  # Set pensize to i
        turtle.forward(500)
        turtle.right(170)

        # Resetting mechanism - Pick a random color
        if i == 0:  # [1, 2, 3, 4, 5, 0]
            turtle.pencolor(random.choice(colors))


# draw_with_cycle_itaration()

n = 7
# print([ t % n for t in range(1,n+1)])
[1, 2, 3, 4, 5, 0]  # n = 6
[1, 2, 3, 4, 5, 6, 0]  # n = 7


print("(16) - Convert smaller unit to larger unit: Convert Inches to Feet")
# 1 foot  = 12 inches

# def convert_inches_to_feet(total_inches):
#     inches = total_inches % 12
#     feet = total_inches // 12

#     print(f"{total_inches} inches = {feet} feet and {inches} inches")

# convert_inches_to_feet(16)

import operator


def convert_inches_to_feet(total_inches):
    feet, inches = divmod(total_inches, 12)
    print(f"{total_inches} inches = {feet} feet and {inches} inches")


convert_inches_to_feet(16)
# 16 inches = 1 feet and 4 inches


print(
    "(17) - Convert smaller unit to larger unit: Convert minute to day, hours, munutes"
)

# print(f'Number of minutes in a day: {24*60}')  # 1440

# def convert_minutes_to_days(total_mins):
#     days = total_mins // 1440
#     extra_minutes = total_mins % 1440

#     hours = extra_minutes // 60
#     minutes = extra_minutes % 60

#     print(f"{total_mins} = {days} days, {hours} hours, and {minutes} minutes")


def convert_minutes_to_days(total_mins):
    import operator

    days, extra_minutes = divmod(total_mins, 24 * 60)
    hours, minutes = divmod(extra_minutes, 60)
    print(f"{total_mins} = {days} days, {hours} hours, and {minutes} minutes")


convert_minutes_to_days(1503)
# 1503 = 1 days, 1 hours, and 3 minutes
convert_minutes_to_days(3456)
# 3456 = 2 days, 9 hours, and 36 minutes
print()

print("(18) - is it a prime number?")


def check_prime_number(num):
    if num < 2:
        print(f"{num} must be greater than or equal to 2 to be prime.")
        return

    factors = [(1, num)]
    i = 2

    while i * i <= num:
        if num % i == 0:
            factors.append((i, num // i))
        i += 1

    if len(factors) > 1:
        print(f"{num} is not prime. It has the following factors: {factors}")
    else:
        print(f"{num} is a prime number")


check_prime_number(135)
# 135 is not prime. It has the following factors: [(1, 135), (3, 45), (5, 27), (9, 15)]


print("(19) - Caesar Cipher")
import string


def caesar_cipher(text, shift, decrypt=False):
    if not text.isascii() or not text.isalpha():
        raise ValueError("Text must be ASCII and contain no numbers.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    result = ""

    if decrypt:
        shift = shift * -1

    for char in text:
        if char.islower():
            index = lowercase.index(char)
            result += lowercase[(index + shift) % 26]
        else:
            index = uppercase.index(char)
            result += uppercase[(index + shift) % 26]

    return result


# print(caesar_cipher('pavlo',5))         # ufaqt
# print(caesar_cipher('ufaqt',5,True))    # pavlo


print("(20) - Vigenère cipher")
import string


def vigenere_cipher(text, key, decrypt=False):
    if not text.isascii() or not text.isalpha() or not text.isupper():
        raise ValueError("Text must be uppercase ASCII without numbers.")

    uppercase = string.ascii_uppercase  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    results = ""

    for i, char in enumerate(text):
        current_key = key[i % len(key)]
        char_index = uppercase.index(char)
        key_index = uppercase.index(current_key)

        if decrypt:
            index = char_index - key_index + 26
        else:
            index = char_index + key_index

        results += uppercase[index % 26]

    return results


# encrypted = vigenere_cipher("REALPYTHON", "MODULO")
# print(encrypted)  # DSDFAMFVRH
# decrypted = vigenere_cipher(encrypted, 'MODULO', True)
# print(decrypted)

print("(21) - decimal.Decimal")
# Decimal uses the sign of the dividend for the results.
# a % b
# a: dividend
# b: divisor

import decimal

print(decimal.Decimal(15) % decimal.Decimal(4))  # 3
print(15 % 4)  # 3

# use trancate(ceil) division which will always round a negative number toward zero
print(decimal.Decimal(-15) % decimal.Decimal(4))  # -3
# use floor division which will round a negative number away from zero
print(-15 % 4)  # 1

# use trancate(ceil) division which will always round a negative number toward zero
print(decimal.Decimal(15) % decimal.Decimal(-4))  # 3
# use floor division which will round a negative number away from zero
print(15 % -4)  # -1
print()

print(decimal.Decimal("12.5") % decimal.Decimal("5.5"))
print(12.5 % 5.5)
print()

print(-13.3 % 1.1)  # 1.0000000000000004
print(decimal.Decimal("-13.3") % decimal.Decimal("1.1"))  # -0.1


print("22 - add all numbers in the integer")
# # Write a program that will return the sum of the digits of an integer.

# # my solution
# n = 236
# num = [int(d) for d in str(n)]
# print(sum(num))


# teachers' solution
def digit_sum(number):
    sum = 0
    while number > 0:
        sum = sum + number % 10
        print(f"sum: {sum}")
        number = number // 10
        print(f"number:{number}")
    return sum


print(digit_sum(236))
print()

print("23 - seperate digits with commas")
# str_num = str(1000000)
# str_num = str_num[::-1]
# print(str_num)
# comma = ','
# new_str=''

# for i, num in enumerate(str_num):
#     if i !=0 and (i%3) == 0:
#         new_str = new_str + comma
#     new_str = new_str + num
# print(new_str[::-1])
print()

print("24 - calculate number of divisors of integer")
# https://www2.math.upenn.edu/~deturck/m170/wk2/numdivisors.html#:~:text=In%20general%2C%20if%20you%20have,exponents%20%2B%201%22s%20together.
# Write a function that will calculate the number of divisors of a positive integer and return those divisors.
num = 24
my_list = [
    i for i in range(1, num + 1) if num % i == 0
]  # [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 48, 72, 144] 15
print(my_list, len(my_list))

# https://www.youtube.com/watch?v=r-5pUvCzqYA&ab_channel=AnilKumar
num = 24
n1 = 2 * 2 * 2 * 3
n2 = (3 + 1) * (1 + 1)
print(n1)
print(n2)
print()

n = 24
l = []
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        l.append(i)
print(l)
print(len(l))

print()
n = 24
for i in range(1, n + 1):
    print(n % i)

print()
print("25 - numerator // denominator vs numerator % denominator")
print("155/4 = numerator/denominator")
numerator = 155
denominator = 4
from math import floor

print(f"155/4 : {155/4}")
print(f"155 // 4: {155//4}")
print(f"floor(155 / 4): {floor(155 / 4)}")
print(f"remainder 155 % 4: {155 % 4}")
print(f"155 = 4 * 38 + 3")
print(f"{4 * (155 // 4) + (155 %4)} = 4 * (155 // 4) + (155 %4)")
print(
    f"{numerator} = {denominator * (numerator//denominator) + (numerator % denominator)}"
)

# The equation works for positive and negative numbers
# numerator = denominator * (numerator//denominator) + numerator % denominator

print()
