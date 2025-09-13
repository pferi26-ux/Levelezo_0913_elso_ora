#ez egy próba modul

def osszeg():
    egyik = int(input("Kérek egy számot:"))
    masik = int(input("Kérek egy másik számot:"))

    eredmeny = egyik + masik

    print("A eredmény értéke:".center(50))
    print(str(egyik).rjust(50,"_"))
    print(str(masik).rjust(50,"_"))
    print("+")
    print(str(eredmeny).rjust(50,"_"))

    return

def szorzas():
    egyik = int(input("Kérek egy számot:"))
    masik = int(input("Kérek egy másik számot:"))

    eredmeny = egyik * masik

    print("A eredmény értéke:".center(50))
    print(str(egyik).rjust(50,"_"))
    print(str(masik).rjust(50,"_"))
    print("*")
    print(str(eredmeny).rjust(50,"_"))

    return