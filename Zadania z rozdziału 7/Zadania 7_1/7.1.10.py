# ZADANIE 7.1.10
# Napisz program drukujący na ekranie trójkąt. Wysokość trójkąta wczytujemy z klawiatury. Poniższy trójkąt
# ma wysokość wys=5.
# X
# XX
# X X
# X  X
# XXXXX

wysokosc = int(input("Podaj wysokość trójkąta: "))

for x in range(wysokosc+1):
    if 1 < x < wysokosc:
        print('X' + ' '*(x-1) + 'X')
    else:
        print('X' * (x + 1))