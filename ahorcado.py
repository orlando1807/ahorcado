import string
from random import choice

palabras = ['banano','manzana','perro','avion','gato','hipopotamo','murcielago','automovil','celular']
vida = 6

palabra = choice(palabras)
nueva_palabra = []
for letra in palabra:
    print('_', end=' ')
    nueva_palabra.append('_')
lista_incorrecta = []
while vida > 0:
    print()
    letra = input('Ingrese una letra: ')
    letra = letra.lower()
    lista_posiciones = []
    if(len(letra)==1 and letra in string.ascii_letters):
        if letra in palabra:
            index = 0
            for ltr in palabra:
                if ltr == letra:
                    lista_posiciones.append(index)
                index += 1
        else:
            lista_incorrecta.append(letra)
            vida -= 1
            print(f'Tu lista de letras incorrecta es: {lista_incorrecta} y te quedan {vida} vidas')
    else:
        print("Debes ingresar una letra.")

    index = 0
    for letra in palabra:
        if index in lista_posiciones:
            print(letra,end=' ')
            nueva_palabra[index] = letra
        else:
            print(f'{nueva_palabra[index]}', end=' ')
        index += 1
    palabra_unida = ''.join(nueva_palabra)
    if palabra_unida == palabra:
        print()
        print('Felicidades GANASTE!')
        break

if vida == 0:
    print()
    print(f'Perdiste la palabra ganadora era {palabra}')