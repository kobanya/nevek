import magyar
import random


utca = random.sample(magyar.utca, k=5)                          # véletlenszerűen kiválasztott 5 utca
telepulesek = random.choices(magyar.telepules, k=5)             # véletlenül kiválasztott 5 magyar település neve
ferfi_keresztnev =random.choices(magyar.keresztnev_f, k=7)      # véletlenül kiválasztott 7 magyarférfi keresztnév
vezeteknevek= random.choices(magyar.vezeteknev, k=8)            # véletlenül kiválasztott 8 magyar vezetéknév

print('\n\nListát ad vissza , megadott elemszámmal :\n')
print(telepulesek)
print(utca)
print(ferfi_keresztnev)
print(vezeteknevek)

print()
print()
print()

