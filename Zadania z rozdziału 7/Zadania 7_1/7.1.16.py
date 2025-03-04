# ZADANIE 7.1.16
# Napisz program drukujący na ekranie liczby. Wysokość wczytujemy z klawiatury. Oto wydruk dla
# wysokości h =5:
# 1
# 2 4
# 3 6 9
# 4 8 12 14
# 5 10 15 20 25

wysokosc = int(input("Podaj wysokość liczb: "))
for w in range(1, wysokosc + 1):
    for i in range(1, w+1):
        print(i*w, end = ' ')
    print()
