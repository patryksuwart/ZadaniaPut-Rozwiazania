# ZADANIE 7.1.14
# Napisz program drukujący na ekranie kwadrat. Długość boku kwadratu wczytujemy z klawiatury. Poniższy kwadrat ma bak długości 4.

# KKKK
# KKKK
# KKKK
# KKKK

dlugosc = int(input("Podaj długość boku kwadratu: "))

for k in range(dlugosc):
    print('K'*dlugosc)