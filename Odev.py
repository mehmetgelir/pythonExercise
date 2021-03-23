s = 0
tek_sayac = 0
cift_sayac = 0
tek_toplam = 0
cift_toplam = 0

for sayi in range(1,7):
	s = int(input("sayi giriniz"))
	if s%2 == 1:
		tek_sayac +=1
		tek_toplam += s
	else:
		cift_sayac +=1
		cift_toplam += s
print(tek_sayac," adet tek sayi vardir, toplamlari", tek_toplam)
print("Tek sayilarin ortalamasi", tek_toplam/tek_sayac)

print(cift_sayac," adet cift sayi vardir, toplamlari", cift_toplam)
print("cift sayilarin ortalamasi", cift_toplam/cift_sayac)