class Lentokone:
    def __init__(self, nimi, bensatankin_maksimi):
        self.nimi = nimi
        self.bensatankin_maksimi = bensatankin_maksimi
        self.bensatankin_nykyinen = 0
    def tankkaa(self):
        tankkiin_mahtui = self.bensatankin_maksimi - self.bensatankin_nykyinen
        self.bensatankin_nykyinen = self.bensatankin_maksimi
        print("Tankkiin mahtui", tankkiin_mahtui, "litraa bensaa")
    def tulosta_tiedot(self):
        print("Nimi", self.nimi)
        print("Bensatankin maksimimäärä", self.bensatankin_maksimi, "litraa")
        print("Nykyinen bensan määrä tankissa", self.bensatankin_nykyinen, "litraa")

class Lentokenttä:
    def __init__(self, nimi,):
        self.nimi = nimi 
        self.koneet = []
    def koneiden_tiedot(self):
        self.koneet[0].tulosta_tiedot()
        self.koneet[1].tulosta_tiedot()
        self.koneet[2].tulosta_tiedot()


kone1 = Lentokone("Airbus A321NEO", 32940)
kone2 = Lentokone("ATR 72-500", 6397)
kone3 = Lentokone("Antonov AN-225", 375000)

kentta = Lentokenttä("Oulu")

kentta.koneet.append(kone1)
kentta.koneet.append(kone2)
kentta.koneet.append(kone3)

kone3.tankkaa()
kone1.tankkaa()

kentta.koneiden_tiedot()