a = []
for n in range(10):
	sayi = int(input('Sayiyi gir: '))
	a.append(sayi)

toplam=0
ortalama=0
for i in range(0,len(a)):
      toplam+=a[i]
 
ortalama=toplam/len(a)


print("En buyuk sayi :", max(a), "En kucuk sayi :", min(a), "Ortalama :",ortalama)