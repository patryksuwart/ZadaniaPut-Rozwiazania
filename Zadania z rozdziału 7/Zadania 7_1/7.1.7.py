# ZADANIE 7.1.7
# Napisz program drukujący na ekranie trójkąt. Wysokość trójkąta wczytujemy z klawiatury. Poniższy trójkąt
# ma wysokość wys=5.
#       X
#      XXX
#     XXXXX
#    XXXXXXX
#   XXXXXXXXX

wysokosc = int(input("Podaj wysokość trójkąta: "))

for x in range(wysokosc):
    if x == 0:
        print(' '* (wysokosc - x - 1) + 'X')
    else:
        print(' '* (wysokosc - x - 1) + 'X'*(2 * x + 1))