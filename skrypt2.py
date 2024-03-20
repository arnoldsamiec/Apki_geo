import math
import random

wartosc = 100

dodawanie = wartosc+123.15
print(dodawanie)

potega = dodawanie**12
print(potega)

tekst = str(potega)
print(tekst)

wartosc_pi = math.pi
print(wartosc_pi)

lista = [4,5,6,7,8,3]
losowa = random.choice(lista)
print(losowa)


tekst = f"Wartosc: {tekst}"
print(tekst)

print(len(tekst))

print(tekst[1:4])

# dir oznacza co moge zrobic z tekstem
#print(dir(tekst))

print(tekst.upper())

listaa = list(tekst)
print(listaa)

print(tekst[0:8])
