print("Bem vindo ao Jogo de Adivinhação!")

numero_secreto = 42
tentativas = 3
rodada = 1

while(rodada <= tentativas):
    print("Tentativa:", rodada,"de", tentativas)
    chute = int(input("Digite o seu palpite entre 1 e 100: "))

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = numero_secreto == chute
    menor = numero_secreto > chute
    if  acertou:
        print("Você acertou!")
        break
    elif menor:
        print("Você chutou para baixo!")
    else:
        print("Você chutou para cima!")
    rodada += 1
print("Fim do jogo")