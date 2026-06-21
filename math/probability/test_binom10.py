#!/usr/bin/env python3
Binomial = __import__('binomial').Binomial

b1 = Binomial([30, 28, 31, 29, 30, 28, 31, 29, 30, 28])
print('n:', b1.n, 'p:', b1.p)

b2 = Binomial(n=50, p=0.6)
print('n:', b2.n, 'p:', b2.p)
print('expected n: 50 p: 0.6')

try:
    Binomial(n=0, p=0.5)
except ValueError as e:
    print(e)

try:
    Binomial(n=1, p=1.5)
except ValueError as e:
    print(e)

try:
    Binomial(data="not a list")
except TypeError as e:
    print(e)

try:
    Binomial(data=[1])
except ValueError as e:
    print(e)
