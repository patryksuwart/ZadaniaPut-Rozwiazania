# ZADANIE 7.1.13
# Napisz program drukujący na ekranie krzyż. Wysokość krzyżyka wczytujemy z klawiatury. Poniższy krzyż
# ma wysokość wys=3.
#       #
#       #
#       #
#    #######
#       #
#       #
#       #

wysokosc = int(input("Podaj wysokość krzyża: "))

for hashtag in range((wysokosc*2)+1):
    if hashtag == (wysokosc//2)+2:
        print('#' *((wysokosc*2)+1))
    else:
        print(' ' * wysokosc + '#')
