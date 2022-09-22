class Students():
    def __init__ (self, predmet, ocene, vp_st, ime, letnik):
        self.ocene = {predmet,ocene}
        self.vp_st = vp_st
        self.ime = ime
        self.letnik = letnik

    def Oceni(self):
        self.ocene = input("ocena je:")
    
    def Napreduj(self):
        self.letnik += 1
        print("Zdaj je " + str(self.letnik) + " letnik")


class Fakulteta():
    def __init__(self, spisek):
        self.studenti = {}
    






        