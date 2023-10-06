#pido el nombre
nombre = input("¿Cual es tu nombre?: ")
#pido la edad
edad = int(input("¿Cual es tu edad?: "))
#comentario sobre la edad
if edad > 30:
    input(f"Estas muy joven para tener {edad} años")
else:
    input(f"Estas muy viejo para tener {edad} años")
#pido la altura 
altura = float(input("¿Cual es tu altura en metros?: "))
#incluyo el nombre en la frase del siguiente input
texto_interpolado = f"Hola {nombre}, un placer conocerte, ¿Dónde vives? "
#obtengo la ciudad usando el texto interpolado
ciudad = input(texto_interpolado)
#le pregunto cual es su comida favorita
comida_favorita = input(f" ¿Cual es tu comida favorita? ")
#comentario sobre su comida favorita
input(f"{nombre} siendo de {ciudad}, es raro que te guste {comida_favorita}")
#le pregunto a donde va a ir hoy por la tarde
lugar_tarde = input(f"Dime {nombre}, ¿a donde vas a ir esta tarde? ")
#me despido educadamente
despedida_adios = input(f"Espero que te lo pases bien {nombre}, mañana nos vemos")