def jogar():


    print("*********************************")
    print("***Bem vindo ao Jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    print(letras_acertadas)

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra?")
        chute = chute.lower().strip()
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
               letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)


    print("Fim de Jogo!")


if(__name__=="__main__"):
    jogar()