# Jogo de Forca para treinar suas habilidades em inglês
# Exercício python

import string  # importing string library function
import random  # importar palavras aleatoriamente
from palavras import palavras


def get_palavra_valida(palavras):
    # escolhe de modo aleatorio da lista de palavras
    palavra = random.choice(palavras)
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)

    return palavra


def forca():
    palavra = get_palavra_valida(palavras)
    letras_palavra = set(palavra)  # letras das palavras
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()  # letras digitadas como tentativa pelo usuario

    # pegar input pelo usuário
    letra_usuario = input('Tente adivinhar uma letra: ').upper()
    # se é caracter válido no alfabeto, que ainda nn usei,
    # então vou adicionar em letras usadas
    if letra_usuario in alfabeto - letras_usadas:
        letras_usadas.add(letra_usuario)
        # se letra tem na palavra então vou remover a letra da letras_palavras
        if letra_usuario in letras_palavra:
            letras_palavra.remove(letra_usuario)

    elif letra_usuario in letras_usadas:
        print('Você já testou está caracter, tente outro ;) ')
    else:
        print('Caracter inválido :( Tente novamente')


forca()
