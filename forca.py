def jogar():


    print("*********************************")
    print("***Bem vindo ao Jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra?")
        chute = chute.lower().strip()
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print(f"Econtrei a letra {chute} na posição {index}")
            index = index + 1
        print("jogando...")


    print("Fim de Jogo!")


if(__name__=="__main__"):
    jogar()