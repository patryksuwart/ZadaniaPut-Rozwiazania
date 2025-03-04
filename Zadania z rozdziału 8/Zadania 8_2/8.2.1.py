# ZADANIE 8.2.1
# Napisz program wczytujący z klawiatury n liczb całkowitych. Program ma znaleźć największą spośród
# podanych liczb i wydrukować ją na ekranie.

ile_liczb = int(input("Ile liczb chcesz podać?:  "))
liczby = []

for i in range(ile_liczb):
    liczby.append(int(input(f'Podaj {i+1} liczbę: ')))

print(f'Największa liczba: {max(liczby)}')