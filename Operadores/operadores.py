# -*- coding: utf-8 -*-

def calcular(clown,wrist):
    WHEIGHT_CLOWN = 112
    WHEIGHT_WRIST = 75

    result = (WHEIGHT_CLOWN*clown)+(WHEIGHT_WRIST*wrist)

    return result

def datos():
    clown = int(input("Introduce la cantidad de payasos de juguete a vender: "))
    wrist = int(input("Introduce la cantidad de muñecas que serán vendidos: "))

    total_wheigth = calcular(clown, wrist)

    print('El peso total es {} gramos'.format(total_wheigth))

if __name__ == '__main__':
    datos()