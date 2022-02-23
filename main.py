import sys
import math
#
# print(sys.version)
#
# a='inżynier\n systemów\n informatycznych\n'
# print(a)
#
# print(type(a))
#
# b = 5
#
# print(b)
# print(type(b))
#
# c=6.5
#
# print(c)
# print(type(c))
#
# d = 2+3j
# print(d)
# print(type(d))
#
# #nowa_podloga
#
# # dfgsdfger
# # ergdfgdfg ctrl+/
# # del a <<<<usuwanie zmiennej
# # print(a)<<<< juz sie nie pokaze bo jest usunieta
#
# f='isi '#spacja aby mozna bylo oddzielic wyrazy
# g='grupa 3'
# print(f+g)
# h=7
# i=2
# print(h//i)#dzielenie calkowite
# print(h**i)#potegowanie h-potega i- wykladnik potegi **-potegowanie
#
# print(math.pow(h, i))#potegowanie z biblioteki math typ float
#  #ulamki zapisywac w (nawiasach)
#
#  h += 1
#  print(h)

a = 5
b = 3
c = a - b
print('wynik działania %(z1)d - %(z2)d = %(z3)d'%{'z1':a , 'z2': b , 'z3': c})
print("wynik z działania {0:d} - {1:d} = {2:d}".format (a, b, c))