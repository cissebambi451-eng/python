temperatures = [12.5, 14 ,9.5,17, 21,19.5, 11]
moyenne = sum(temperatures)/ len(temperatures)
min=min(temperatures)
max= max(temperatures)
print(f"Moyenne : {moyenne:.2f}")
print(f"Min : {min} / Max:{max}")

compteur = 0
for temperature in temperatures:
    if temperature > 15:
        compteur = compteur + 1
       
print(f"Jours > 15 °C : {compteur}")

fahrenheit = []
for temperature in temperatures:
    f = temperature * 9 / 5 + 32
    # on ajoute chaque température convertie à la fin de la liste fahrenheit
    fahrenheit.append(f)
print(f"Fahrenheit : {fahrenheit}")

for jour , temperature in enumerate(temperatures , start=1):
    print(f"jour {jour} : {temperature} °C")