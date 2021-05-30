import random

def conversor(opcion):
    if opcion == 1:
        return 'piedra'
    elif opcion == 2:
        return 'papel'
    elif opcion == 3:
        return 'tijera'
    else:
        return print('Ingrese una opcion valida')

def juez(player, player2):
    if piedra == True  


def bienvenida():
    print('Bienvenidos a Piedra, Papel o Tijera')
    player = int(input('''escriba el número de su elección : 
    1- Piedra
    2- Papel
    3- Tijera 
    opcion: '''))
    player = conversor(player)
    print('player 1 eligio {}'.format(player))
    player_2 = random.randint(1,3)
    player_2 = conversor(player_2)    
    print('player 2 eligio {}'.format(player_2))    



def area_triangulo():
    base = int(input('ingrese la base del triangulo: '))
    altura = int(input('ingrese la altura del triangulo: '))
    area = (base*altura)/2
    print('el area de su triangulo es {}'.format(area))


def run():
    bienvenida()



if __name__ == '__main__':
    run()
