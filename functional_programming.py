#yan etki

A= 5

def impure_sum(b): #Dışardaki bir nesneden etkilenerek çıktı üreten fonksiyon çeşitleridir.
    return b + A

def pure_sum(a,b): #dışarıda her ne olursa olsun sonuç değişmez yan etkisiz fonksiyonlardır.
    return a + b

print(impure_sum(6))


