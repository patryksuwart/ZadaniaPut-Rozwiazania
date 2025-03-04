# ZADANIE 7.1.19
# Napisz program drukujący na ekranie liczby. Ilość liczb wczytujemy z klawiatury. Oto wydruk dla ile = 5:
# 0, 3, 6, 9, 12

ile = int(input("Podaj ilość liczb: "))

for i in range(ile):
    if i == 0:
        print(i, end = ', ')
    else:
        print(i*3, end = ', ')