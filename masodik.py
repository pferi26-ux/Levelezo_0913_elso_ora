#masodik alkalom
import random

import modul

#szam= int(input("Kérek egy számot"))
'''szam= input("Kérek egy számot: ")
if szam.isdigit():
    szam=int(szam)
    if szam > 0:
        print("Pozitív")
    elif szam < 0:
        print("Negativ")
    else:
        print("Nulla")
else:
    print("Nem számjegy!")


jegy = int(input("Kérek egy érdemjegyet: "))
while jegy == 1 or jegy > 5 or jegy < 1:
    jegy = int(input("Kérek egy érdemjegyet: "))
    if jegy == 10:
        print("5*")
        break
else:
    print("Jól teljesített!")
print("Gratulálok!")


kocka = random.randint(1,6)
while True:
    tipp = int(input("Adja meg a tippet: "))
    if tipp == kocka:
        break
print("Sikerült eltalálni a számot!")


uzenet = "Jó reggelt!"
for betu in uzenet:
    print(betu)
    if betu == " ":
        break


lista = (1,4,7,78)
for elem in lista:
    print(elem)

for _ in range(1,4):
    print("Nem leszek többet rossz!")
for elem in range(1, 4):
    print(elem,"Nem leszek többet rossz!")

def fv():
    pass

for elem in range(1,6):
    if elem == 3:
        continue
    print(elem, "Nem leszek többet rossz!")


try:
    print(10/0)
except ZeroDivisionError:
    print("Hiba! nullával osztás")
except NameError:
    print("HIBA! névhiba")
print ("ok")


while True:
    try:
        szam = int(input("Adjon meg egy egész számot:"))
    except:
        print("Nem egész számot adott meg!")
    else:
        break
'''
