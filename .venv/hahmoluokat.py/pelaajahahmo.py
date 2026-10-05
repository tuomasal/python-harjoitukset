from .hahmo import Hahmo


class Pelaajahahmo(Hahmo):
    def __init__(self, nimi, tavaralista):
        super().__init__(nimi)
        self.tavaralista = tavaralista

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Tavaralista: {self.tavaralista}")
