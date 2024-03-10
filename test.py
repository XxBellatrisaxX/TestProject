'''
what = input("Что делаем? (+, -, *, /)")
a = float(input("Введи первое число:"))
b = float(input("Введи второе число:"))
if what == "+":
    c= a + b
elif what == "-":
    c= a - b
elif what == "*":
    c= a * b
elif what == "/":
    c= a / b
print("Результат:" + str(c))

'''
from colorama import init
from colorama import Fore, Back, Style
init()

print( Fore.BLACK )
print( Back.LIGHTRED_EX )
what = input("Что делаем? (+, -, *, /)")
print( Fore.BLACK )
print( Back.LIGHTCYAN_EX)
a = float(input("Введи первое число:"))
b = float(input("Введи второе число:"))

print( Fore.BLACK )
print( Back.YELLOW )

if what == "+":
    c= a + b
elif what == "-":
    c= a - b
elif what == "*":
    c= a * b
elif what == "/":
    c= a / b
print("Результат:" + str(c))
input()
