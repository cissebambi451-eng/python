for temperature in [-3, 0, 15, 31]:

    if temperature < 0:
        print(f"{temperature} °C : gel")
    elif temperature < 15:
        print(f"{temperature} °C : froid")
    elif temperature < 25:
     print(f"{temperature} °C : doux")
else:
    print(f"{temperature} °C : chaud")

for annee in [2024, 1900, 2000]:
    if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
        print(f"{annee} : bissextile")
    else:
        print(f"{annee} : non bissextile")