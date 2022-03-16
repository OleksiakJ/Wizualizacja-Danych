import math
# lista=[]

# for element in sekwencja
#     if warunek_na_elementach
#         lista.append(akcja_na_elementach)
#
# lista=[akcja_na_elementach for element in sekwencja if warunek_na_elementach]

#a={x^2: x=<0,9>}

# a = []
# for x in range(0,10):
#     a.append(x**2)
# print(x)
#
# a2 = [x**2 for x in  range(0,10)]
# print(a2)
#
# b = []
# for x in range(0,6):
#     a.append(3**x)
# print(b)
#
# b2 = [3**x for x in range(0,6)]
# print(b2)
#
# c=[]
# for z in a:
#     if z%2==1:
#         c.append(z)
#     print(c)
#
# c2 = [x for x in a if x%2==1]
# print(c2)


#
# lista=[]
# for a in [1,2,3]:
#     for b in [4,5,6]:
#         lista.append((a,b))
# print(lista)
# lista2=[(a,b) for a in [1,2,3] for b in [4,5,6]]
# print(lista2)


# slownik={'PZU':'Państwowy zakład ubezpieczeń',
#          'ZUS':'Zakład ubezpieczeń społecznych',
#          'PKO':'Państwowa kasa oszczędności'}
# slownik_odwrocony ={}
# print(slownik)
# for key, value in  slownik.items():
#     slownik_odwrocony[value]=key
#     print(slownik_odwrocony)
# slownik2={value: key for key, value in slownik.items()}
# print(slownik2)

#     FUKNCJE
# def nazwa_funkcji(argumenty): (argumenty: pozycyjne, domysle(maja przypisana wartosc) *argument, **argument)
#     instrukcja
#     return

# def row_kwadartowe(a,b,c):
#     delta = b**2-4*a*c
#     if delta<0:
#         print('Brak rozwiązań')
#         return -1
#     elif delta == 0:
#         print('Jedno rozwiazanie ')
#         x= (-b)/(2*a)
#         print(x)
#     else:
#         print('Dwa rozwiązania')
#         x1=((-b) - math.sqrt(delta))/(2*a)
#         x2=((-b) + math.sqrt(delta))/(2*a)
#         print(x1)
#         print(x2)
#
# print(row_kwadartowe(10,10,3))
#
# def parzystosc (a):
#     if a %2==0:
#         print('liczba jest parzysta')
#     else:
#         print('liczba nie jest parzysta')
#
# print(parzystosc(9))
#
# def dlugosc_odcinka(x1=1,y1=2,x2=3,y2=4):
#     return math.sqrt((x2-x1)**2 + (y2-y1)**2)
#
# print(dlugosc_odcinka())
# #argumenty pozycyjne
# print(dlugosc_odcinka(4,5,6,9))
# #dwa pierwsze argumenty pozycyjne, kolejne dwa wpisywane wartosci
# print(dlugosc_odcinka(1,1,y2=8,x2=7))
# #wartosci przypisane dod danego argumentu w losowej kolejnosci
# print(dlugosc_odcinka(y2=3,x1=5,y1=6,x2=0))
# #dwa pierwsze argumenty jako domyslne, kolejne dwa z nowa wartoscia
# print(dlugosc_odcinka(y2=1,x2=6))

# def ciag(*liczba):
#     if len(liczba) == 0:
#         return 0
#     else:
#         suma=0
#         for i in liczba:
#             suma+=i
#         return suma
#
#
# print(ciag())
# print(ciag(1,2,3,4,5,6,7,8))

# def co_lubie(**rzeczy):
#     for cos in rzeczy:
#         print('lubie')
#         print(cos)
#         print('co lubie')
#         print(rzeczy[cos])
#
# co_lubie(gry=['planszowe','komputerowe'])

# a2 = [x**2 for x in  range(0,10)]
# print(a2)
#zad1
a=[1-x for x in range(1,11)]
print(a)

b=[4**x for x in range(0,8)]
print(b)

c=[x for x in b if x%2==0]
print(c)

#zad 4
def trojkat_prostokatny(a,b,c):
    if (c**2)==(a**2)+(b**2):
        print("jest to trojkat prostokatny")
    else:
        print('nie jest to trojkat prostokatny')
        return 0
print(trojkat_prostokatny(3,4,5))
print(trojkat_prostokatny(4,4,4))

#zad 5
def pole_trapezu(a=3,b=5,h=6):
    pole=((a+b)*h)/2
    print(pole)

print(pole_trapezu())
print(pole_trapezu(3,2,6))

