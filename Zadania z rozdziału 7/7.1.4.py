# ZADANIE 7.1.4
# Napisz program drukujący na ekranie literę A złożoną z literek A. Wielkość litery A wczytujemy z
# klawiatury.
#           A
#          A A
#         A   A
#        AAAAAAA
#       A       A
#      A         A

size = int(input("Podaj wielkość litery A: "))

for a in range(size):
    if a == size // 2:
        print(' '* (size - a - 1) + 'A' * (size + 1) )
    elif a == 0:
        print(' '* (size - a - 1) + 'A')
    else:
        print(' '* (size - a - 1) + 'A' + ' ' * (2 * a - 1) + 'A')