nimi = input("Syötä nimesi:")
ikä = int(input("Syötä ikäsi:"))

tarvikkeet = []
rahat = 0

def aloita():
    print("Peli on aloitettu.")
    tarvike = input("Kerro jokin tarvike jonka haluaisit ottaa matkaasi: ")
    tarvikkeet.append(tarvike)

    print("Olet ottanut mukaasi tarvikkeen", tarvike + ".")

    print()
    print("Olet eksynyt kaupungilla ja tarvitset rahaa kotiinpääsyyn.")
   
    while rahat < 5:
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

def ranta():
    global rahat
    print("Saavut rannalle.")
    print()
    print("Rannalla sinua lähestyy ystävällinen herra, joka pyytää sinua auttamaan häntä rannalla roskien siivoamisessa.")
    print("Tartutko tarjoukseen?")
    print("Kyllä - 1")
    print("Ei - 2")
    valinta_ranta = input("Valitse 1 tai 2:")
    if valinta_ranta == "1":
        rahat = rahat + 2
        print("Autat miestä siivoamaan rannan. Saat hyvän mielen ja 2€.")
        print("Sinulla on nyt", rahat, "euroa.")
    elif valinta_ranta == "2":
        print("Kieltäydyt auttamasta. Jatkat matkaasi.")
    else:
        print("Virheellinen valinta, valitse 1 tai 2.")
def tori():
    global rahat
    print()
    print("Saavut torille.")
    print("Torimyyjä lähestyy sinua ja pyytää apuasi ")
    print("Autatko torimyyjää?")
    print("Kyllä - 1")
    print("Ei - 2")
    valinta_tori = input("Valitse 1 tai 2:")
    if valinta_tori == "1":
        rahat = rahat + 2
        print("Autoit torimyyjää ja sait vaivanpalkaksi 2€.")
        print("Sinulla on nyt", rahat, "euroa.")
    elif valinta_tori == "2": 
        print("Kieltäydyt auttamasta. Jatkat matkaa.")
    else:
        print("Virheellinen valinta, valitse 1 tai 2.")

def kirkko():
    global rahat
    print()
    print("Saavut kirkolle.")
    print("Kirkkoherra lähestyy sinua ja pyytää apuasi muutaman hautakiven nostamisessa.")
    print("Autatko kirkkoherraa?")
    print("Kyllä - 1")
    print("Ei - 2")
    valinta_kirkko = input("Valitse 1 tai 2:")
    if valinta_kirkko == "1":
        rahat = rahat + 2
        print("Autat kirkkoherraa ja saat palkaksi 2€.")
    elif valinta_kirkko == "2":
        print("Et auta kirkkoherraa. Jatkat matkaa.")
    else:
        print("Virheellinen valinta, valitse 1 tai 2.")
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
   

