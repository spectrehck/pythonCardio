def run():
    inicio = True
    while inicio == True:
        print('*********************************************************')
        menu = int(input('''bienvenido al calculador de volumen del cilindro: 
            Seleccione el metodo de calculo:
            1- V = B * h
            2- V = pi * r**2 * h
            3- Salir
            opcion:  '''))
        if menu == 1:
            base = int(input('Ingrese la base de su cilindro: '))
            altura = int(input('Ingrese la altura de su cilindro: '))
            volumen = base*altura
            volumen = round(volumen,2)
            print('el volumen de su cilindro es: {}'.format(volumen))

        elif menu == 2:
            pi = 3.141516
            radio = int(input('Ingrese el radio de su cilindro: '))
            altura = int(input('Ingrese la altura de su cilindro: '))
            volumen = pi*radio**2*altura
            volumen = round(volumen,2)
            print('el volumen de su cilindro es: {}'.format(volumen))

        elif menu == 3:
                inicio = False

        else:
                print('Ingrese una opcion valida')

if __name__ == '__main__':
    run()
