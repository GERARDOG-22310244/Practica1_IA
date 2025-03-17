print('Saludos Guerrero, ¿Que desea comprar? \n \n' +
    'Items disponibles \n \n' +
    'Espadas \n \n' +
    '1. Espada nivel 1 -- 100 Monedas de oro \n' +
    '2. Espada nivel 2 -- 1500 Monedas de oro \n' +
    'Escudos \n \n' +
    '3. Escudo nivel 1 -- 75 Monedas de oro \n' +
    '4. Escudo nivel 2 -- 1200 Monedas de oro \n')

comprar = [3]

dinero = 1500

espadaLV1 = 150

espadaLV2 = 1200

EscudoLV1= 100

EscudoLV2 = 750

if 0 in comprar or comprar == []:
    print("Especifica un numero entre 1 y 4")

if 1 in comprar:
    dinero = dinero - espadaLV1

if 2 in comprar:
    dinero = dinero - espadaLV2

if 3 in comprar:
    dinero = dinero - EscudoLV1

if 4 in comprar:
    dinero = dinero - EscudoLV2

if dinero < 0:
    print("No te alcanza el dinero para eso")

if comprar == [1] or comprar == [2] or comprar == [3] or comprar == [4]:
    print("Te quedan " + str(dinero) + "Monedas de oro")
    print("Se agrego el/los objetos a tu inventario.")