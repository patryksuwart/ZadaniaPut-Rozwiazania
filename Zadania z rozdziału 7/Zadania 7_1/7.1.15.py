# ZADANIE 7.1.15
# Napisz program drukujący na ekranie liczby. Wysokość wczytujemy z klawiatury. Oto wydruk dla
# wysokości h =5:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

wysokosc = int(input("Podaj wysokość liczb: "))
for w in range(1, wysokosc + 1):
    for i in range(1, w+1):
        print(i, end = ' ')
    print()