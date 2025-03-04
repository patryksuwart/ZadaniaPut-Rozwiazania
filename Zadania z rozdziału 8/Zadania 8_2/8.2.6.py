# ZADANIE 8.2.6
# Napisz program wczytujący z klawiatury n liczb całkowitych. Program ma znaleźć drugi co do wielkości
# (ciut większy od najmniejszego) wyraz podanego ciągu liczb (czyli liczbę większą od najmniejszej ale mniejszą
# od każdej innej).

ile_liczb = int(input("Ile liczb chcesz podać?:  "))
liczby = []

for i in range(ile_liczb):
    liczby.append(int(input(f'Podaj {i+1} liczbę: ')))

najmniejsza = min(liczby)

for x in range(len(liczby)):
    if najmniejsza in liczby: liczby.remove(min(liczby))
    else: break

print(f'Liczba większa od najmniejszej: {min(liczby)}')