edad = int (input("Cual es tu edad?    ...     "))

if edad <= 0:
    print("Nadie puede tener esa edad")

elif edad >= 1 and edad <= 17:
    print("Eres menor de edad")

elif edad <= 100:
    print("Eres mayor de edad.")

else:
    print("Edad no valida.")