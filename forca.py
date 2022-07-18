import random


def jogar():

    mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()


    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)


    print(letras_acertadas)


    enforcou = False
    acertou = False
    erros = 0
    acertos = 0
    while(not enforcou and not acertou):

        chute = pede_chute()
        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        mensagem_vencedor()
    else:
        mensagem_enforcado()



def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao Jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra?")
    chute = chute.lower().strip()
    return chute

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def mensagem_vencedor():
    print("Você ganhou!!")

def mensagem_enforcado():
    print("Você foi enforcado!")

if(__name__=="__main__"):
    jogar()