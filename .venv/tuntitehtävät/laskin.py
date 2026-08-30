while True:
    print("1. Plus")
    print("2. Miinus")
    print("3. Kertolasku")
    print("4. Lopeta")


    valinta = input("Valitse:")
    if valinta == "4":
        break
    elif valinta not in ["1","2","3","4"]:
        print("Valitse luku 1-4.")
        continue

    luku1 = float(input("Anna eka numero: "))
    luku2 = float(input("Anna toka numero: "))

    if valinta == "1":
        print("Tulos:", luku1 + luku2)
    if valinta == "2":
        print("Tulos:", luku1 - luku2)
    if valinta == "3":
        print("Tulos:", luku1 * luku2)
    else:
        print("Virheellinen valinta.")







