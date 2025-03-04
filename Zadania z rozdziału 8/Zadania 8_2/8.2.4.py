# ZADANIE 8.2.4
# Napisz program wczytujący z klawiatury n liczb całkowitych. Program ma znaleźć najmniejszą spośród
# podanych liczb oraz wydrukować na ekranie informację mówiącą o tym, ile razy najmniejsza liczba wystąpiła w
# podanym ciągu liczb.

ile_liczb = int(input("Ile liczb chcesz podać?:  "))
liczby = []
ile = 0

for i in range(ile_liczb):
    liczby.append(int(input(f'Podaj {i+1} liczbę: ')))

for l in liczby:
    if l == min(liczby):
        ile += 1

print(f'Najmniejsza liczba: {min(liczby)}')
print(f'Wystąpiła: {ile}', end = ' razy' if ile > 1 else ' raz')