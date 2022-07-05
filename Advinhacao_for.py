import random

def jogar():

    print("***************************************")
    print("***Bem vindo ao Jogo de Adivinhação!***")
    print("***************************************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    nivel = 0
    pontos = 1000


    print("Escolha o nível de dificuldade.")
    print("(1) Fácil  (2) Médio (3) Difícil")
    nivel = int(input("Nível: "))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    elif(nivel == 3):
        tentativas = 5
    else:
        print("Número inválido. Digite um número entre 1 e 3")

    for rodada in range(1,tentativas+1):
        print(f"\nTentativa: {rodada} de {tentativas}")
        chute = int(input("\nDigite o seu palpite entre 1 e 100: "))

        if(chute<1 or chute>100):
            print("\nVocê deve digitar um número entre 1 e 100")
            continue
        acertou = numero_secreto == chute
        menor = numero_secreto > chute
        if(acertou):
            print(f"\nVocê acertou e fez {pontos} pontos!")
            break
        elif(menor):
            print("\nVocê chutou para baixo!")
        else:
            print("\nVocê chutou para cima!")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

    print("\nFim do jogo")

    print(f"\nO numero secreto é {numero_secreto}")

if(__name__=="__main__"):
    jogar()