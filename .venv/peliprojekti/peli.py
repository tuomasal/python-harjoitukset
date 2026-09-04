nimi = input("Syötä nimesi:")
ikä = int(input("Syötä ikäsi:"))

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
            print("Peli on aloitettu.")
        elif komento == "info":
            print("Pelin on tehnyt Tuomas vuonna 2026.")
        elif komento == "lopeta":
            print("Peli lopetetaan.")
        else: print("Virheellinen komento.")
   

