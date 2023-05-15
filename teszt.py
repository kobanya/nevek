import magyar

jarasok = magyar.szotarbol_veletlen_kulcs(magyar.jaras, 15)  # 15 járás kiválasztása véletlenül
print(f'\n\nKiírás listaként: \n{jarasok}')

jaras_tordelve = magyar.ftordel(jarasok, 5)  # A járások kiírása tördelve, soronként 5

print(f'\n\nVéletlenül választott járások kiírása, tördelve : \n\n{jaras_tordelve}')

print()
