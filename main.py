# i = 0
# while i < 10:
#     print(i)
#
#     if i == 5:
#         break
#
#     i += 1


## LECTION 2
# ADDING DICT
# D = {'Moscow': 1212,
#      'Pieter': 2232,
#      'Jupp': 211}
# D['Krasnodar'] = 1
# print(D)
# # print(D)
#
# for MOB in D:
#     print(MOB, D[MOB])
#
# T = 1, 2, 3, 4, 5, 6
# a, b, *rest = T
# print(*T)
# print(*rest, sep=':', end='!!!\n')

# # corteg
# def hello_n(name: str,
#             n: int):
#     for i in range(n):
#         print(f'Hello', name)
#
#
# vasya = 'Vasyl', 3
# hello_n('Vasyl', 5)
# print('', end='\n')
# hello_n(*vasya)

# # Range
# A = range(1, 19, 2)
# print(*A)
#
# for x in A:
#     print(x)

# # list
# A = [1, 2, 3]
# print(type(A))

import turtle
A = [(50, 11), (30, 20), (30, 30)]
# for i in range(len(A)):
#     angle, length = A[i]
#     turtle.forward(length)

# for T in A:
#     angle, length = T
#     turtle.forward(length)

# for angle, length in A:
#     turtle.forward(length)

# A = [1, 2, 3, 4]
# for i, x in enumerate(A):
#     print(i, x)

# ## LECTION 3 Функции Локальность имен и PyGame Dont Repeat Yourself / We Enjoy Typing LEGB local enclosed global builtin
# def foo() -> None: #annotation
#     pass
#     return None
#
#
# x = foo()
# print(x)

# import random as rn
#
#
# def foo() -> int:
#     if rn.randint(1, 2) == 1:
#         return 'Hello'
#     else:
#         return 5
#
#
# print(foo())


# def foo(x) -> int:  #formal parameters
#     return x**2
#
#
# y = foo(2)        # fact parameters
# print(x) # NameError


# def foo(x, z):
#     x[0] = 7   #replace
#     x = [4, 5, 6]
#     x*z
#
#
# A = [1, 2, 3]
# y = foo(A, 3)
# print(A)
# print(x)

# Duck Typing
def foo(x: str, y: int) -> str:  # contract function
    result = x
    for i in range(y-1):
        result += x
    return result


z = foo(2, 5)
print(z)
z = foo('ma', 2)
print(z)