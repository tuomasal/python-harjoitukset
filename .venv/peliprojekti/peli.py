nimi = input("Syötä nimesi:")
ikä = int(input("Syötä ikäsi:"))

tarvikkeet = []

def aloita():
    print("Peli on aloitettu.")
    tarvike = input("Kerro jokin tarvike jonka haluaisit ottaa matkaasi: ")
    tarvikkeet.append(tarvike)
    print("Olet ottanut mukaasi tarvikkeen", tarvike + ".")
def info():
    print("Pelin on tehnyt Tuomas vuonna 2026.")
    print("Hallussa olevat tarvikkeet:")
    for tarvike in tarvikkeet: 
        print("-", tarvike)
def lopeta():
    print("Peli lopetetaan.")

if ikä < 12:
    print("Valitettavasti peli on K-12, etkä täten voi pelata peliä.")

else: 
    print("Pelaajan nimi:", nimi, "ja", "Pelaajan ikä:", ikä)
    komento = ""
    while komento != "lopeta":
        print()
        print("Valikko")
        print("aloita - aloittaaksesi pelin")
        print("lopeta - lopettaaksesi pelin")
        print("info - katsoaksesi tietoja pelistä")         
        komento = input("Syötä komento:")
        if komento == "aloita":
            aloita()
        elif komento == "info":
            info()
        elif komento == "lopeta":
            lopeta()
        else: print("Virheellinen komento.")
   

