# ZADANIE 8.2.5
# Napisz program wczytujący z klawiatury n liczb całkowitych. Program ma znaleźć drugi co do wielkości
# wyraz podanego ciągu liczb (czyli liczbę mniejszą od największej liczby występującej w ciągu, ale większą od
# wszystkich pozostałych).

ile_liczb = int(input("Ile liczb chcesz podać?:  "))
liczby = []

for i in range(ile_liczb):
    liczby.append(int(input(f'Podaj {i+1} liczbę: ')))

najwieksza = max(liczby)

for x in range(len(liczby)):
    if najwieksza in liczby: liczby.remove(max(liczby))
    else: break

print(f'Liczba mniejsza od największej: {max(liczby)}')