print("Python ile object oriented programlama mantığı işlenecektir.")

class veriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []

    def __init__(self):
        self.bildigi_diller = [] #Her bir nesnenin kendine has array değerleri olacağı anlamına gelir.

    def dilEkle(self, bildigi_diller):
        self.bildigi_diller.append(bildigi_diller)

class calisanlar(veriBilimci) : #veri bilimciden miras almış oldu.
    def __init__(self):
        self.adi = ''
        self.soyadi = ''
        self.adress = ''




ali = veriBilimci()
ali.bildigi_diller.append('Py')
print(ali.bildigi_diller)


veli = veriBilimci()
veli.sql = 'Hayır'
veli.bildigi_diller.append('C++')



print(veli.bildigi_diller)
print(ali.bildigi_diller)
print(dir(veriBilimci))


