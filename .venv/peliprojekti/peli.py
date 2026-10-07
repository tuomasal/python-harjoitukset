from pelaaja import Pelaaja 
from paikka import Paikka

def readfile(filename):
    with open(filename, "r", encoding="utf-8") as tiedosto:
        text = tiedosto.read()
    return text

rantap = Paikka("Ranta")
torip = Paikka("Tori")
kirkkop = Paikka("Kirkko")

def tallenna_peli():
    with open("save.txt", "w", encoding="utf-8") as tiedosto:
        tiedosto.write(pelaaja.nimi + "\n")
        tiedosto.write(str(pelaaja.ika) + "\n")
        tiedosto.write(str(pelaaja.rahat) + "\n")
        tiedosto.write(pelaaja.sijainti.nimi + "\n")
        tiedosto.write(pelaaja.tarvikkeet[0] + "\n")
        tiedosto.write(str(pelaaja.yritykset) + "\n")
        for paikka in pelaaja.kaydyt_paikat:
            tiedosto.write(paikka + "\n")

def avaa_tallennettu_peli():
    with open("save.txt", "r", encoding="utf-8") as tiedosto:
        nimi = tiedosto.readline().strip()
        ikä = int(tiedosto.readline().strip())
        rahat = int(tiedosto.readline().strip())
        sijainti = tiedosto.readline().strip()
        tarvikkeet = tiedosto.readline().strip()
        yritykset = int(tiedosto.readline().strip())

        kaydyt_paikat = []

        for i in range(3 - yritykset):
            paikka = tiedosto.readline().strip()
            kaydyt_paikat.append(paikka)

    pelaaja = Pelaaja(nimi, ikä)
    pelaaja.rahat = rahat
    pelaaja.tarvikkeet.append(tarvikkeet)
    pelaaja.yritykset = yritykset
    pelaaja.kaydyt_paikat = kaydyt_paikat

    if sijainti == "Ranta":
        pelaaja.sijainti = rantap
    elif sijainti == "Tori":
        pelaaja.sijainti = torip
    elif sijainti == "Kirkko":
        pelaaja.sijainti = kirkkop

    return pelaaja

print("1 - Uusi peli")
print("2 - Jatka tallennettua peliä")
aloitusvalinta = input("Valitse: ")
if aloitusvalinta == "1":
    nimi = input("Syötä nimesi:")
    ikä = int(input("Syötä ikäsi:"))
    pelaaja = Pelaaja(nimi, ikä)
elif aloitusvalinta == "2":
    pelaaja = avaa_tallennettu_peli()


def aloita():
    print("Peli on aloitettu.")
    print(readfile("intro.txt"))
    print()
    print(readfile("ohjeet.txt"))
    tarvike = input("Kerro jokin tarvike jonka haluaisit ottaa matkaasi: ")
    pelaaja.tarvikkeet.append(tarvike)
    print("Olet ottanut mukaasi tarvikkeen", tarvike + ".")

    while pelaaja.rahat < 5 and pelaaja.yritykset > 0:
        print("Yrityksiä jäljellä:", pelaaja.yritykset)
        print("Minne haluaisit mennä?")
        print("Rannalle (1)")
        print("Torille (2)")
        print("Kirkolle (3)")

        reittivalinta = input("Valitse reitti 1, 2 tai 3: ")

        if reittivalinta == "1":
            ranta()
        elif reittivalinta == "2":
            tori()
        elif reittivalinta == "3":
            kirkko()
        else:
             print("Virheellinen valinta, valitse numero 1, 2 tai 3.")
    if pelaaja.rahat >= 5:
        print("Ansaitsit tarpeeksi rahaa päästäksesi kotiin!")
        print("Hyppäät bussiin kotia kohti. Voitit pelin!")
    else:
        print("Yrityksesi loppuivat.")
        print("Et saanut tarpeeksi rahaa kotimatkaa varten.")
        print("Hävisit pelin!")

def ranta():
    if "Ranta" in pelaaja.kaydyt_paikat:
        print("Olet jo käynyt rannalla. Valitse jokin muu paikka.")
        return
    
    pelaaja.kaydyt_paikat.append("Ranta")
    pelaaja.yritykset = pelaaja.yritykset - 1
    pelaaja.sijainti = rantap
    print("----------")
    print("Saavut rannalle.")
    print("----------")
    print("Rannalla sinua lähestyy ystävällinen herra, joka pyytää sinua auttamaan häntä rannalla roskien siivoamisessa.")
    print("Tartutko tarjoukseen?")
    print("Kyllä - 1")
    print("Ei - 2")
    valinta_ranta = input("Valitse 1 tai 2:")
    if valinta_ranta == "1":
        pelaaja.rahat = pelaaja.rahat + 2
        print("Autat miestä siivoamaan rannan. Saat hyvän mielen ja 2€.")
        print("Sinulla on nyt", pelaaja.rahat, "euroa.")
    elif valinta_ranta == "2":
        print("Kieltäydyt auttamasta. Jatkat matkaasi.")
    else:
        print("Virheellinen valinta, valitse 1 tai 2.")
def tori():
    if "Tori" in pelaaja.kaydyt_paikat:
        print("Olet jo käynyt torilla. Valitse jokin muu paikka.")
        return
    
    pelaaja.kaydyt_paikat.append("Tori")
    pelaaja.yritykset = pelaaja.yritykset - 1
    pelaaja.sijainti = torip
    print()
    print("Saavut torille.")
    print("Torimyyjä lähestyy sinua ja pyytää apuasi ")
    print("Kuinka paljon autat torimyyjää?")
    print("Hiukan - 1")
    print("Paljon - 2")
    print("En auta - 3")
    valinta_tori = input("Valitse 1, 2 tai 3:")
    if valinta_tori == "1":
        pelaaja.rahat = pelaaja.rahat + 1
        print("Autoit torimyyjää hieman ja sait 1 €.")
    elif valinta_tori == "2":
        pelaaja.rahat = pelaaja.rahat + 2
        print("Autoit torimyyjää paljon ja sait 2 €.")
    elif valinta_tori == "3":
        print("Päätät olla auttamatta torimyyjää.")
    else:
        print("Virheellinen valinta, valitse 1, 2 tai 3.")

def kirkko():
    if "Kirkko" in pelaaja.kaydyt_paikat:
        print("Olet jo käynyt kirkossa. Valitse jokin muu paikka.")
        return
    
    pelaaja.kaydyt_paikat.append("Kirkko")
    pelaaja.yritykset = pelaaja.yritykset - 1
    pelaaja.sijainti = kirkkop

    print("----------")
    print("Saavut kirkolle.")
    print("----------")
    print("Kirkkoherra lähestyy sinua ja pyytää apuasi.")
    print("Autatko kirkkoherraa?")
    print("Kyllä - 1")
    print("Ei - 2")
    valinta_kirkko = input("Valitse 1 tai 2:")
    if valinta_kirkko == "1":
        pelaaja.rahat = pelaaja.rahat + 2
        print("Autat kirkkoherraa ja saat palkaksi 2€.")
    elif valinta_kirkko == "2":
        print("Et auta kirkkoherraa. Jatkat matkaa.")
    else:
        print("Virheellinen valinta, valitse 1 tai 2.")

def info():
    print("Pelin on tehnyt Tuomas vuonna 2026.")
    print("Hallussa olevat tarvikkeet:")
    for tarvike in pelaaja.tarvikkeet: 
        print("-", tarvike)
    
def lopeta():
    print("Peli lopetetaan.")

if pelaaja.ika < 12:
    print("Valitettavasti peli on K-12, etkä täten voi pelata peliä.")

else: 
    print("Pelaajan nimi:", pelaaja.nimi, "ja", "Pelaajan ikä:", pelaaja.ika)
    komento = ""
    while komento != "lopeta":
        print()
        print("Valikko")
        print("aloita - aloittaaksesi pelin")
        print("lopeta - lopettaaksesi pelin")
        print("tallenna - tallentaaksesi pelin")
        print("info - katsoaksesi tietoja pelistä")         
        komento = input("Syötä komento:")
        if komento == "aloita":
            aloita()
        elif komento == "info":
            info()
        elif komento == "lopeta":
            lopeta()
        elif komento == "tallenna":
            tallenna_peli()
        else: print("Virheellinen komento.")
   

