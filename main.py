# 1 - misol
numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
musbat_kvadratlar = [x**2 for x in numbers if x > 0]
print(musbat_kvadratlar)


# 2 - misol
uchga_bolinadigan = [x for x in range(1, 51) if x % 3 == 0]
print(uchga_bolinadigan)


# 3 - misol
satr = input("Matn kiriting: ")
katta_harflar = [harf.upper() for harf in satr]
print(katta_harflar)


# 4 - misol
numbers = [1, 3, 5, 7, 9, 2, 10]
beshdan_kattalar = [x for x in numbers if x > 5]
print(beshdan_kattalar)


# 5 - misol
tub_sonlar = [x for x in range(2, 101) if all(x % i != 0 for i in range(2, int(x**0.5)+1))]
print(tub_sonlar)


# 6 - misol
satr = input("Matn kiriting: ")
unlilar = [harf for harf in satr if harf.lower() in 'aeiouаеиоуюяёў']
print(unlilar)


# 7 - misol
numbers = [2, 4, 6, 8]
index_kopaytma = [x * i for i, x in enumerate(numbers)]
print(index_kopaytma)


# 8 - misol
numbers = [int(x) for x in input("Sonlarni vergul bilan kiriting: ").split(",")]
juft_ikkilangan = [x * 2 for x in numbers if x % 2 == 0]
print(juft_ikkilangan)


# 9 - misol
satrlar = ["salom", "kitob", "maktab", "kompyuter", "dars"]
uzun_satrlar = [s for s in satrlar if len(s) > 5]
print(uzun_satrlar)


# 10 - misol
toq_kvadratlar = [x**2 for x in range(1, 21) if x % 2 != 0]
print(toq_kvadratlar)
