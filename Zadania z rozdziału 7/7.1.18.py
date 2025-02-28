# ZADANIE 7.1.18
# Napisz program drukujący na ekranie liczby. Wysokość wczytujemy z klawiatury. Oto wydruk dla
# wysokości h =5:
# 2,
# 4,5,
# 8,9,10,
# 16,17,18,19,
# 32,33,34,35,36,

wysokosc = int(input("Podaj wysokość liczb: "))
liczba = 2
for w in range(wysokosc):
    start = liczba
    for i in range(w + 1):
        print(liczba, end=',')
        liczba += 1
    print()
    liczba = start * 2