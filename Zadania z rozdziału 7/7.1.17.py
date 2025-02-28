# ZADANIE 7.1.17
# Napisz program drukujący na ekranie liczby. Wysokość wczytujemy z klawiatury. Oto wydruk dla
# wysokości h =5:
# 0
# 3 6
# 6 9 12
# 9 12 15 18
# 12 15 18 21 24

wysokosc = int(input("Podaj wysokość liczb: "))
for w in range(wysokosc):
    for i in range(w + 1):
        print((w * 3) + (i * 3), end=' ')
    print()