# -*- coding: utf-8  -*-


def palindrome2(word): #Palabra inversa con notación de slice
    reversed_word = word[::-1]

    if reversed_word == word:
        return True
    return False


def palindrome(word): #Palabra inversa con un for
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0,letter)
    
    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True
    
    return False

if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))

    result = palindrome2(word)

    if result is True:
        print('{} sí es un palindromo.'.format(word))
    else:
        print('{} no es un palindromo.'.format(word))