'''
A ideia do nosso jogo é termos que acertar um número secreto. Quando o programa estiver rodando, teremos que digitar um
número e o programa dirá se acertamos ou erramos o número, com várias tentativas e níveis.
'''
import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")


    # numero_secreto = 42
    # Utilizando a função random para gerar o número secreto de forma aleatória.
    # numero_secreto = round((random.random() * 100)) # random.random gera um número aleatório entre 0.0 e 1.0 (nesse caso não é o ideal)
    numero_secreto = round(random.randrange(1, 101)) # random.randrange gera um número aleatório entre 1 e 100 (nesse caso é o ideal)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # Descomentar em caso de utilização com o laço While
    # rodada = 1

    # Adicionando laço com While
    # while(rodada <= total_de_tentativas):

    # Adicionando mesma condição com laço For
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("O seu chute foi maior que o número secreto.")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    # Descomentar em caso de utilização com o laço While
    #     rodada = rodada + 1

    print("Fim do jogo!")
    print('#######################')

if(__name__ == "__main__"):
    jogar()