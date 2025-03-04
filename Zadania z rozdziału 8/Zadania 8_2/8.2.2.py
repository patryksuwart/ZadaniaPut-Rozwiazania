# ZADANIE 8.2.2
# Napisz program wczytujący z klawiatury n liczb całkowitych. Program ma znaleźć najmniejszą spośród
# podanych liczb i wydrukować ją na ekranie.

ile_liczb = int(input("Ile liczb chcesz podać?:  "))
liczby = []

for i in range(ile_liczb):
    liczby.append(int(input(f'Podaj {i+1} liczbę: ')))

print(f'Najmniejsza liczba: {min(liczby)}')