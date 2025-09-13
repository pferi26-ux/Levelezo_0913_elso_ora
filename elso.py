import  random
import modul
#from modul import osszeg, szorzas
#from modul import *
#import modul as m
#from modul import osszeg as szum
#első próbálkozás

'''
    több soros


kor = 50
nev = "Elemér"
hazas = True

#inkrementálás
kor += 5

print("Felhasználó: ", nev, kor, hazas)

szoveg = "Rendszámtartó"

print(szoveg)
print(szoveg[0])
print(szoveg[0:4])
print(szoveg[4:8])
print(szoveg[-5:])

lista = ["Rend", "szám", "tartó"]

print(lista)
print(lista[1])
print(lista[0], lista[1], lista[2])
print(lista[0], lista[1], lista[2],sep="")

lista.append("tábla")
print(lista)

halmaz = {1,2,3,"négy",1}
print(halmaz)

szotar ={"név": "Józsi", "kor": 40, "házas": True}
print(szotar)


kor= int(input("Hány éves vagy: "))
kor += 5
print("A felhasználó kora:", kor, sep="\n\t")
'''

kor = 50

#print("A felhasználó kora:".rjust(50,"_"), kor)
#print("A felhasználó kora:".ljust(50,"_"), kor)

print("A felhasználó kora:".center(50,"_"))

print(f"A felhasználó kora: {kor}")

print("A felhasználó kora: {0}".format(kor))

print(random.randint(5,10))

modul.osszeg()
modul.szorzas()

#osszeg()
#m.osszeg()
#szum()