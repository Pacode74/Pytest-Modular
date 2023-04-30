# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation
# https://github.com/csknk/fast-modular-exponentiation
# https://www.youtube.com/watch?v=lJ3CD9M3nEQ&ab_channel=ZachStar

print()
print("(1) - mod % 2 returns set of {0, 1}", "\n")

mod_2 = [i % 2 for i in range(0, 11)]
print(mod_2, "\n")
# [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

mod_2 = dict((i, n % 2) for i, n in enumerate(range(0, 11)))
print(mod_2, "\n")
# {0: 0, 1: 1, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0, 7: 1, 8: 0, 9: 1, 10: 0}

print(0 % 2)  # 0
print(2 % 2)  # 0
print(4 % 2)  # 0
print(6 % 2)  # 0
print(8 % 2, "\n")  # 0

print(1 % 2)  # 1
print(3 % 2)  # 1
print(5 % 2)  # 1
print(7 % 2)  # 1
print(9 % 2)  # 1
print()


print("(2) - mod % 3 returns set of {0, 1, 2}", "\n")

mod_2 = [i % 3 for i in range(0, 11)]
print(mod_2, "\n")
# [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]

mod_2 = dict((i, n % 3) for i, n in enumerate(range(0, 11)))
print(mod_2, "\n")
# {0: 0, 1: 1, 2: 2, 3: 0, 4: 1, 5: 2, 6: 0, 7: 1, 8: 2, 9: 0, 10: 1}

print(0 % 3)  # 0
print(3 % 3)  # 0
print(6 % 3)  # 0
print(9 % 3)  # 0
print(12 % 3, "\n")  # 0

print(1 % 3)  # 1
print(4 % 3)  # 1
print(7 % 3)  # 1
print(10 % 3)  # 1
print(13 % 3, "\n")  # 1

print(2 % 3)  # 2
print(5 % 3)  # 2
print(8 % 3)  # 2
print(11 % 3)  # 2
print(14 % 3, "\n")  # 2

print("(3) - mod % 4 returns set of {0, 1, 2, 3}")
mod_2 = [i % 4 for i in range(0, 11)]
print(mod_2)
# [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2]
mod_2 = dict((i, n % 4) for i, n in enumerate(range(0, 11)))
print(mod_2)
# {0: 0, 1: 1, 2: 2, 3: 3, 4: 0, 5: 1, 6: 2, 7: 3, 8: 0, 9: 1, 10: 2}
print()

print("(3.1) - negative mod % 4 returns set of {0, 1, 2, 3}")
mod_2 = [-i % 4 for i in range(0, 11)]
print(mod_2)
# [0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2]
mod_2 = dict((i, -n % 4) for i, n in enumerate(range(0, 11)))
print(mod_2)
# {0: 0, 1: 3, 2: 2, 3: 1, 4: 0, 5: 3, 6: 2, 7: 1, 8: 0, 9: 3, 10: 2}
print()

print("(4) - mod % 12 returns set of {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}")
mod_2 = [i % 12 for i in range(0, 11)]
print(mod_2)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mod_2 = dict((i, n % 12) for i, n in enumerate(range(0, 25)))
print(mod_2)
# {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 0,
# 13: 1, 14: 2, 15: 3, 16: 4, 17: 5, 18: 6, 19: 7, 20: 8, 21: 9, 22: 10, 23: 11, 24: 0}
print()


print("(5) - Testing if there is an inverse if gcd equals to 1")
from math import floor, gcd

print(gcd(1, 19), "\n")


print("(6) - Remainder function:")


def remainder(A: int = "dividend", B: int = "modulus"):
    from math import floor

    quantient = floor(A / B)
    return A - (B * quantient)


print(remainder(2**40, 13))
print(2**40 % 13, "\n")

print(remainder(5**117, 19))  # wrong result, I don't know why???
print(5**117 % 19, "\n")  # 1


print("(7) - Example Code: Exponent is a Power of 2:")


def exponent_power_of_2(a, e_power2, mod):
    for i in range(0, e_power2):
        a = (a * a) % mod
        print(f"a = {a}")
    return a


print(exponent_power_of_2(7, 4, 13), "\n")

print("(8) - Fast Modular exponentiation:")


def remainder_large(A: int = "dividend", B: int = "modulus", E: int = "exponenet"):
    from math import prod

    li = list(reversed([int(i) for i in bin(E)[2:]]))  # [1, 0, 1, 0, 1, 1, 1]
    l = [2**n for n in range(8)]  # [1, 2, 4, 8, 16, 32, 64, 128]
    t = [m for n, m in zip(li, l) if n]  # [1, 4, 16, 32, 64]
    return prod([(A**i) % B for i in t]) % B


print(remainder_large(5, 19, 117), "\n")

## Explanation:
# E = 117
# print(bin(E))
# li = list(reversed([int(i) for i in bin(E)[2:]]))
# print(li)

# l = [2**n for n in range(8)]
# print(l)

# t =  [m for n, m in zip(li, l) if n]
# print(t)

# n = 5
# modulus = 19
# from math import prod
# r = []
# for i in t:
#     print(i)
#     r.append(n**i % modulus)
# d = prod(r) % modulus
# print(d)


print("(9) - fast exponent:")


def fast_exp(b, e, m):
    r = 1  # if e is even number r = 1

    # Checking if e is odd or even.
    # Even number ends on 0 and odd ends on 1 in bits.
    # Return 0 if e is even number or returns 1 if e is odd number
    if 1 & e:  # if e is odd number then r = b:
        r = b
    while e:  # while e > 0:
        e >>= 1  # Floor e // 2
        b = (b * b) % m
        if e & 1:
            r = (r * b) % m
    return r


def fast_exp(b, e, m):
    r = 1  # if e is even number r = 1

    # Checking if e is odd or even.
    # Even number ends on 0 and odd ends on 1 in bits.
    # Return 0 if e is even number or returns 1 if e is odd number
    if 1 & e:  # if e is odd number then r = b:
        r = b
        print(f"r = {r}")  # r = 5
    while e:  # while e > 0:
        print()
        e >>= 1  # Floor e // 2
        print(f"e = {e}")
        b = (b * b) % m
        print(f"b = {b}")
        if e & 1:
            r = (r * b) % m
        print(f"r = {r}")
    return r


print(fast_exp(5, 117, 19))
# print(fast_exp(7, 256, 13))


print()
print((6**2 - 1) / 5)
print((7**2 + 1) / 5)
print((8**2 - 1) / 7)
