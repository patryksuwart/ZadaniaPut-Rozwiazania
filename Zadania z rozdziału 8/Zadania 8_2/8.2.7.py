# ZADANIE 8.2.7
# Ile razy w podanym ciągu liczb wystąpił drugi co do wielkości największy element ciągu?

ile_liczb = int(input("Ile liczb chcesz podać?:  "))
liczby = []
ile = 0

for i in range(ile_liczb):
    liczby.append(int(input(f'Podaj {i+1} liczbę: ')))

najwieksza = max(liczby)

for x in range(len(liczby)):
    if najwieksza in liczby: liczby.remove(max(liczby))
    else: break

for l in liczby:
    if l == max(liczby):
        ile += 1

print(f'Liczba mniejsza od największej: {max(liczby)}')
print(f'Wystąpiła: {ile}', end = ' razy' if ile > 1 else ' raz')