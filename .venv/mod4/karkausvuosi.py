vuosiluku = int(input("Kirjoita jokin vuosiluku:"))
if vuosiluku % 100 == 0:
    if vuosiluku % 400 == 0:
         print("Antamasi vuosi on karkausvuosi.")
elif vuosiluku % 4 == 0:
    print("Antamasi vuosi on karkausvuosi.")
else: print("Antamasi vuosiluku ei ole karkausvuosi harmillisesti.")