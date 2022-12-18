class bloklar():
    def __init__(self, blok1, blok2):

        self.buyuk_x1 = max(blok1[0], blok1[2])
        self.buyuk_y1 = max(blok1[1], blok1[3])
        self.kucuk_x1 = min(blok1[0], blok1[2])
        self.kucuk_y1 = min(blok1[1], blok1[3])
        self.blok_merkez1 = ((self.buyuk_x1 + self.kucuk_x1) / 2, (self.buyuk_y1 + self.kucuk_y1) / 2)

        self.buyuk_x2 = max(blok2[0], blok2[2])
        self.buyuk_y2 = max(blok2[1], blok2[3])
        self.kucuk_x2 = min(blok2[0], blok2[2])
        self.kucuk_y2 = min(blok2[1], blok2[3])
        self.blok_merkez2 = ((self.buyuk_x2 + self.kucuk_x2) / 2, (self.buyuk_y2 + self.kucuk_y2) / 2)

    def konumlar(self):
        if self.kucuk_y2 == self.buyuk_y1 and self.kucuk_y1 == 0 and self.buyuk_y2 > self.buyuk_y1:
            if self.kucuk_x1 < self.blok_merkez2[0] < self.buyuk_x1:
                return 1
                # blok1 altta blok2 üstte
            else:
                return 2
        elif self.kucuk_y1 == self.buyuk_y2 and self.kucuk_y2 == 0 and self.buyuk_y1 > self.buyuk_y2:
            if self.kucuk_x2 < self.blok_merkez1[0] < self.buyuk_x2:
                return 1
                # blok2 altta blok1 üstte
            else:
                return 2
        else:
            return 0
    def ek_parca(self):
        if self.kucuk_y2 == self.buyuk_y1 and self.kucuk_y1 == 0:
            if abs(self.kucuk_x2 - self.blok_merkez1[0]) > abs(self.buyuk_x2 - self.blok_merkez1[0]):
                blok3_kucukx = self.buyuk_x2
                blok3_buyukx = self.buyuk_x1 + abs(self.kucuk_x1 - self.kucuk_x2)
                blok3_kucuky = self.kucuk_y2
                blok3_buyuky = self.buyuk_y2
                return [blok3_kucukx,blok3_buyuky,blok3_buyukx,blok3_kucuky]
            elif abs(self.kucuk_x2 - self.blok_merkez1[0]) < abs(self.buyuk_x2 - self.blok_merkez1[0]):
                blok3_kucukx = self.kucuk_x1 - abs(self.buyuk_x2-self.buyuk_x1)
                blok3_buyukx = self.kucuk_x2
                blok3_kucuky = self.kucuk_y2
                blok3_buyuky = self.buyuk_y2
                return [blok3_kucukx, blok3_buyuky, blok3_buyukx, blok3_kucuky]
        elif self.kucuk_y1 == self.buyuk_y2 and self.kucuk_y2 == 0:
            if abs(self.kucuk_x1 - self.blok_merkez2[0]) > abs(self.buyuk_x1 - self.blok_merkez2[0]):
                blok3_kucukx = self.buyuk_x1
                blok3_buyukx = self.buyuk_x2 + abs(self.kucuk_x2 - self.kucuk_x1)
                blok3_kucuky = self.kucuk_y1
                blok3_buyuky = self.buyuk_y1
                return [blok3_kucukx,blok3_buyuky,blok3_buyukx,blok3_kucuky]
            elif abs(self.kucuk_x1 - self.blok_merkez2[0]) < abs(self.buyuk_x1 - self.blok_merkez2[0]):
                blok3_kucukx = self.kucuk_x2 - abs(self.buyuk_x1-self.buyuk_x2)
                blok3_buyukx = self.kucuk_x1
                blok3_kucuky = self.kucuk_y1
                blok3_buyuky = self.buyuk_y1
                return [blok3_kucukx, blok3_buyuky, blok3_buyukx, blok3_kucuky]

    def alan_hesap(self):
        if self.konumlar() == 1 or self.kucuk_y2 > self.buyuk_y1 or self.kucuk_x1 > self.buyuk_y2:
            alan = (abs(self.buyuk_x1 - self.kucuk_x1) * abs(self.buyuk_y1 - self.kucuk_y1)) + (abs(self.buyuk_x2 - self.kucuk_x2) * abs(self.buyuk_y2 - self.kucuk_y2))
            return alan
        elif self.konumlar() == 0:
            if self.buyuk_y2 > self.buyuk_y1 > self.kucuk_y2 > self.kucuk_y1:
                ortak = abs(self.buyuk_y1 - self.kucuk_y2) * abs(self.buyuk_x2 - self.kucuk_x2)
                alan = (abs(self.buyuk_x1 - self.kucuk_x1) * abs(self.buyuk_y1 - self.kucuk_y1)) + (abs(self.buyuk_x2 - self.kucuk_x2) * abs(self.buyuk_y2 - self.kucuk_y2))
                return (alan - ortak)
            elif self.buyuk_y1 > self.buyuk_y2 > self.kucuk_y1 > self.kucuk_y2:
                alan = (abs(self.buyuk_x1 - self.kucuk_x1) * abs(self.buyuk_y1 - self.kucuk_y1)) + (abs(self.buyuk_x2 - self.kucuk_x2) * abs(self.buyuk_y2 - self.kucuk_y2))
                ortak = abs(self.buyuk_y2 - self.kucuk_y1) * abs(self.buyuk_x1 - self.kucuk_x1)
                return (alan - ortak)
            else:
                alan = (abs(self.buyuk_x1 - self.kucuk_x1) * abs(self.buyuk_y1 - self.kucuk_y1)) + (
                            abs(self.buyuk_x2 - self.kucuk_x2) * abs(self.buyuk_y2 - self.kucuk_y2))
                return alan

    def firmus_kontrol(self):
        if self.konumlar() == 1:
            return ("FIRMUS",self.alan_hesap())
        elif self.konumlar() == 2:
            return ("ADDENDUM",self.ek_parca())
        elif self.konumlar() == 0:
            return ("DAMNARE",self.alan_hesap())

def firmus_mu(blok1,blok2):
    b = bloklar(blok1,blok2)
    return b.firmus_kontrol()

print(firmus_mu([-0.5,10,-6,13],[-7,0,3,10]))
print(firmus_mu([0.5,19,9.5,9],[3.8,9,5.5,0]))
print(firmus_mu([-8,11,2,5],[1,0,-2,5]))
print(firmus_mu([-7,5,7,10],[9.5,12.6,-1,10]))
print(firmus_mu([-3,7,5,15],[-7,0,7,5]))
print(firmus_mu([6,4,3.9,-1],[0.5,14.2,9.5,4]))
print(firmus_mu([0,0,2.4,5.2],[-8.7,10,0,0]))
print(firmus_mu([0,10,-8.7,0],[-4,9,-1,14]))


