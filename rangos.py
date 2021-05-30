def logica(inferior, superior, comparacion):
    if inferior <= comparacion and superior >= comparacion:
        print('su numero esta dentro del rango')
        print(comparacion)
    else:
        print(comparacion)
        print('Ingrese un numero que este en el rango')


def run():
    inicio = True
    while inicio == True:
        menu = int(input('''
************************************************************************************
        Bienvenido al juego de rangos numericos
            Presione 1 para jugar o 2 para salir
            opcion:  '''))
        if menu == 1:
            inferior = int(input('Ingrese el rango inferior: '))
            superior = int(input('Ingrese el rango superior: '))
            comparacion = int(input('Ingrese el numero de comparacion: '))
            logica(inferior, superior, comparacion)
        elif menu ==2:
            inicio = False
        else:
            print('Ingrese una opcion valida')

            


if __name__ == '__main__':
    run()
