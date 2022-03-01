import sys
import math

# Zad 1

a = 1
b = 2
print(a, b)
c = 4.4
d = 5.5
print(c, d)
e = "pycharm"
f = "fajny"
print(e+" "+f)
g = 5j
h = 6 + 3.8j
print(g, h)
del a, b, c, d, e, f, g, h

# Zad 2

a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))
print("1.Dodawanie 2.Odejmowanie 3.Mnożenie 4.Dzielenie 5.Potęgownie: ")
c = int(input())
if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
   print(a*b)
elif c == 4:
    print(a/b)
elif c == 5:
    print(pow(a, b))
else:
    print("nieprawidlowa wartosc")
del a, b, c

# Zad 3

a = 2
a += 2
print(a)
b = 10
b -= 8
print(b)
c = 5
c *= 4
print(c)
d = 100
d /=25
print(d)
e = 2
e **= 10
print(e)
f = 11
f %= 3
print(f)
del a, b, c, d, e, f

# Zad 4

print(math.e**10)

print(pow(math.log(5 + (math.sin(8)) ** 2, math.e), 1/6))

print(math.floor(3.55))

print(math.ceil(4.80))
