
def run():
    print('bienvenido al conversor de millas a kilometros')
    prendido = True
    while prendido == True:
        menu = int(input('''Ingrese su opcion:
        1- Medir millas a kilometros
        2- Medir kilometros a millas
        3. exit
        opcion: '''))
        if menu == 1:
            millas = int(input('Ingrese sus millas: '))
            kilometros = round(millas/0.621371, 2)
            print('en {} millas hay {} kilometros'.format(millas, kilometros)) 
        elif menu == 2:
            kilometros = int(input('Ingrese sus kilometros: '))
            millas = round(millas*0.621371, 2)
            print('en {} kilometros hay {} millas'.format(kilometros, millas)) 
        elif menu == 3:
            prendido = False
        else:
            print('Ingrese una opcion valida')
      

       



if __name__ == '__main__':
    run()
