import sys
import math

# if warunek1:
# --instrukcja lub blok instrukcji
#elif warunek2:
#-- instrukcja  lub blok instrukcji warunku 2
#elif warunek n:
#--instrukcje
#else:
#--instrukcja gdy warunki niespelnione
#warunki np. x==y, x!=y, x>y,x=>y

a=5
b=3
if(a==b):
    print("a jest rowne b")
else:
    print("a jest rozne od b ")
del a, b

a=9
b=9
if a>b:
    print("a jest wieksze od b")
elif a<b:
    print("a jest mniejsze od b")
else:
    print("liczby sa rowne")
del a, b
#operatory logiczne & and,

# a=input("wpisz liczbę: ")
# print(a)
# print(type(a))
# a=int(a)
# print(type(a))
# del a
# a=input('wpisz pierwsza liczbe: ')
# b=input('wpisz druga liczbe: ')
# c=input('wpisz trzecia liczbe: ')
# d=input('wpisz czwarta liczbe: ')
# a= int(a)
# b= int(b)
# c= int(c)
# d= int(d)
# if(a>b)&(c>d):
#     print('liczba a jest wieksza od liczby b i liczba c jest wieksza od liczby d')
# else:
#     print('liczba a jest mniejsza od liczby b lub liczba c jest mniejsza od liczby d')
#
# for licznik in sekwencja
# --intrukcja lub blok instrukcji
# else:
#  --instrukcja po wykonaniu petli for
# range(start,stop,step) elementy: startowy koncowy i z jaka jest zmieniany licznik
#  for(int i=0;i<10;i++) tak jak w c++
# for i in range(0, 7, ):
#     print(i)
# lista= ['a', 5, 6, 5.6]
# for a in lista:
#     print(a)
# else:
#     print('wyswietlone zostaly wszystkie elementy z listy')
# while warunek:
# -- instrukcja lub blok instrukcji gdy warunek spelniony
# else:
# --instrukcja po petli

# i=0
# while i<11:
#     print(i)
#     i+=1

# lista=[4,6,9,5,7,2,3]
# liczba=input('podaj liczbe: ')
# licznik=0
# while licznik<len(lista): #len to dlugosc listy
#     if int(liczba)-lista[licznik]==0:
#         print('liczba ' + str(liczba) + ' - ' + str(lista[licznik]) + ' =0')
#         break
#     else:
#         licznik +=1
# else:
#     print('zadna z watosci nie dala odpowiedniego wyniku ')

# lista1=[4,6,8,2,3,9]
# lista2=[4,7,5,2]
# suma=[]
# for a in lista1:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#     print(suma)

#try:
# --instrukcja, ktore moga zawierac blad
# except nazwa bledu
# --instrukcja po wykryciu bledu
# except nazwa bledu2:
# --instrukcja po wykreyciu bledu2
# .
# .
# .
# else:
# --wynik gdy nie ma bledu

# a = input("wczytaj pierwszą liczbę: ")
# b = input("wczytaj drugą liczbę: ")
# try:
#     a=int(a)
#     b=int(b)
#     wynik = a/b
#     print(wynik)
# except ZeroDivisionError:
#     print("nie można dzielić przez 0")
# except ValueError:
#     print('Nie wczytano liczby całkowitej')

# lista=['a',5,5.5,[1,2,3]]
# słownik={klucz:wartość} <= jeden element słownika
# do listy: append, insert, extand, pop, remove, del, sort, reverse

slownik={'klucz':'wartosc'}
print(slownik['klucz'])