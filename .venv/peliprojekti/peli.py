from pelaaja import Pelaaja 
from paikka import Paikka

# Lukee valitusta tiedostosta tekstin ja palauttaa sen peliin 
def readfile(filename):
    with open(filename, "r", encoding="utf-8") as tiedosto:
        text = tiedosto.read()
    return text

# Luodaan peliin 3 paikkaa missä voi käydä
rantap = Paikka("Ranta")
torip = Paikka("Tori")
kirkkop = Paikka("Kirkko")

# Tallentaa pelaajan tiedot save.txt tiedostoon 
def tallenna_peli():
    # Jos pelaajalla ei ole sijaintia, hän ei ole vielä käynyt missään paikassa eli peli ei ole alkanut.
    if pelaaja.sijainti == None:
        print("Et voi tallentaa peliä ennen kuin olet aloittanut pelin.")
        return
    with open("save.txt", "w", encoding="utf-8") as tiedosto:
        tiedosto.write(pelaaja.nimi + "\n")
        tiedosto.write(str(pelaaja.ika) + "\n")
        tiedosto.write(str(pelaaja.rahat) + "\n")
        tiedosto.write(pelaaja.sijainti.nimi + "\n")
        tiedosto.write(pelaaja.tarvikkeet[0] + "\n")
        tiedosto.write(str(pelaaja.yritykset) + "\n")
        for paikka in pelaaja.kaydyt_paikat:
            tiedosto.write(paikka + "\n")

# Lukee tallennetun pelin tiedot save.txt tiedostosta ja ottaa sieltä pelaajan tiedot peliin
def avaa_tallennettu_peli():
    with open("save.txt", "r", encoding="utf-8") as tiedosto:
        nimi = tiedosto.readline().strip()
        ikä = int(tiedosto.readline().strip())
        rahat = int(tiedosto.readline().strip())
        sijainti = tiedosto.readline().strip()
        tarvikkeet = tiedosto.readline().strip()
        yritykset = int(tiedosto.readline().strip())

        kaydyt_paikat = []

        # Alussa yrityksiä on 3, joten tämä kertoo kuinka monessa paikassa pelaaja on jo käynyt
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
    # Luodaan uusi Pelaaja syöttämien tietojen perusteella
    pelaaja = Pelaaja(nimi, ikä)
elif aloitusvalinta == "2":
    pelaaja = avaa_tallennettu_peli()

# Aloittaa pelin ja pelaaja voi valita eri reittejä
def aloita():
    peli_tallennettu = False
    print("Peli on aloitettu.")
    print("----------")
    print(readfile("intro.txt"))
    print("----------")
    print(readfile("ohjeet.txt"))
    print("----------")
    tarvike = input("Kerro jokin tarvike jonka haluaisit ottaa matkaasi: ")
    pelaaja.tarvikkeet.append(tarvike)
    print("Olet ottanut mukaasi tarvikkeen", tarvike + ".")

# Peli jatkuu niin kauan kun pelaajalla on alle 5e rahaa ja yrityksiä jäljellä 
    while pelaaja.rahat < 5 and pelaaja.yritykset > 0:
        print("----------")
        print("Yrityksiä jäljellä:", pelaaja.yritykset)
        print("----------")
        print("Minne haluaisit mennä?")
        print("Rannalle (1)")
        print("Torille (2)")
        print("Kirkolle (3)")
        print("Tallenna ja sulje peli (4)")
        reittivalinta = input("Valitse reitti 1, 2, 3 tai 4: ")

        if reittivalinta == "1":
            ranta()
        elif reittivalinta == "2":
            tori()
        elif reittivalinta == "3":
            kirkko()
        elif reittivalinta == "4":
            tallenna_peli()
            print("Peli tallennettu. Peli lopetetaan.")
            peli_tallennettu = True
            break
        else:
             print("Virheellinen valinta, valitse numero 1, 2, 3 tai 4.")
    if peli_tallennettu: 
        return
    elif pelaaja.rahat >= 5:
        print("Ansaitsit tarpeeksi rahaa päästäksesi kotiin!")
        print("Hyppäät bussiin kotia kohti. Voitit pelin!")
    else:
        print("Yrityksesi loppuivat.")
        print("Et saanut tarpeeksi rahaa kotimatkaa varten.")
        print("Hävisit pelin!")

# Tehtävä rannalla jossa pelaaja voi ansaita rahaa
def ranta():
    # Tarkistetaan onko pelaaja käynyt jo rannalla 
    if "Ranta" in pelaaja.kaydyt_paikat:
        print("Olet jo käynyt rannalla. Valitse jokin muu paikka.")
        return
    # Lisätään ranta käytyihin paikkoihin ja vähennetään pelaajalta yksi yritys
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

# Tehtävä torilla jossa pelaaja voi ansaita rahaa
def tori():
    if "Tori" in pelaaja.kaydyt_paikat:
        print("Olet jo käynyt torilla. Valitse jokin muu paikka.")
        return
    
    pelaaja.kaydyt_paikat.append("Tori")
    pelaaja.yritykset = pelaaja.yritykset - 1
    pelaaja.sijainti = torip
    print("----------")
    print("Saavut torille.")
    print("----------")
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

# Tehtävä kirkossa jossa pelaaja voi ansaita rahaa
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

# Tarkistetaan että pelaaja on 12v tai yli
if pelaaja.ika < 12:
    print("Valitettavasti peli on K-12, etkä täten voi pelata peliä.")

else: 
    print("Pelaajan nimi:", pelaaja.nimi, "ja", "Pelaajan ikä:", pelaaja.ika)
    komento = ""
    # Päävalikko jossa pelaaja voi aloittaa, lopettaa ja tallentaa pelin. 
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
   

