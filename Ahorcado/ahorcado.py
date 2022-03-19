# -*- coding: utf-8 -*-
from ast import If
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
        |
        |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
    |   |
        |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|   |
        |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|\  |
        |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|\  |
    |   | 
   /    |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        |
        ==========''','''
        
        '''
]

WORDS = ['casa','botella', 'aguila','cubo','piramide']

def random_word():
    idx = random.randint(0,len(WORDS)-1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print("\033[1;31m"+IMAGES[tries])
    print('')
    print(hidden_word)
    print("\033[2;32m"+'<-------------------------------------->')


def run():
    word = random_word()

    hidden_word = ['_'] * len(word)

    tries = 0

    while True:
        display_board(hidden_word,tries)
        current_letter = str(input('Ingresa una letra: '))

        letter_indexes = []

        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes)== 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word,tries)
                print('')
                print('!Has perdido¡ La palabra correcta es {}'.format(word))

                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter
            letter_indexes = [] 
        
        try:
            hidden_word.index('_')
        except ValueError:
            print('!Felicidades¡ Ganaste. La palabra es: {}'.format(word))
            break

def menu():
    while True:
        print('[1] Jugar ')
        print('[2] Acerca de ')
        print('[3] Salir ')
        seleccion = int(input("Selecciona un numero: "))

        if  seleccion == 1:
            run()
        elif seleccion == 2:
            print("\033[1;33m" + k4to)
        else:
            break

if __name__ == '__main__':

    
    k4to = '''
     _  _     _    _  _  _      
 /_//_`/ `/_// /  /_// //_/     
/ //_,/_,/ //_/  /  /_// \      
                                
             ____  _              _ 
       /_//_/ /  / /  /|,//_//  / /
      /`\  / /  /_/  /  /  //_,/_/'''
   
    bien = '''
888888b.  8888888 8888888888 888b    888 888     888 8888888888 888b    888 8888888 8888888b.   .d88888b.   .d8888b.  
888  "88b   888   888        8888b   888 888     888 888        8888b   888   888   888  "Y88b d88P" "Y88b d88P  Y88b 
888  .88P   888   888        88888b  888 888     888 888        88888b  888   888   888    888 888     888 Y88b.      
8888888K.   888   8888888    888Y88b 888 Y88b   d88P 8888888    888Y88b 888   888   888    888 888     888  "Y888b.   
888  "Y88b  888   888        888 Y88b888  Y88b d88P  888        888 Y88b888   888   888    888 888     888     "Y88b. 
888    888  888   888        888  Y88888   Y88o88P   888        888  Y88888   888   888    888 888     888       "888 
888   d88P  888   888        888   Y8888    Y888P    888        888   Y8888   888   888  .d88P Y88b. .d88P Y88b  d88P 
8888888P" 8888888 8888888888 888    Y888     Y8P     8888888888 888    Y888 8888888 8888888P"   "Y88888P"   "Y8888P"
'''
    print("\033[1;33m" + bien)
    menu()