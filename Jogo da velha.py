def criaMatriz():
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    return mat


def apresentaMatriz(mat):
    print(mat[0][0], "|", mat[0][1], "|", mat[0][2])
    print("-" * 10)
    print(mat[1][0], "|", mat[1][1], "|", mat[1][2])
    print("-" * 10)
    print(mat[2][0], "|", mat[2][1], "|", mat[2][2])


def posicaoOcupada(matriz, posicao):
    if matriz[posicao[0]][posicao[1]] == "X" or matriz[posicao[0]][posicao[1]] == "O":
        return True
    return False

def resgistraJogada(mat, jogador, posicao):
    mat[posicao[0]][posicao[1]] = jogador
    return mat

def trocaJogador(jogador):
    if jogador == "X":
        return "O"
    return "X"

def verificaJogador(mat, jogador):
    if mat[0][0] == jogador and mat[0][1] == jogador and mat[0][2] == jogador:
        return True
    if mat[1][0] == jogador and mat[1][1] == jogador and mat[1][2] == jogador:
        return True
    if mat[2][0] == jogador and mat[2][1] == jogador and mat[2][2] == jogador:
        return True

    if mat[0][0] == jogador and mat[1][0] == jogador and mat[2][0] == jogador:
        return True
    if mat[0][1] == jogador and mat[1][1] == jogador and mat[2][1] == jogador:
        return True
    if mat[0][2] == jogador and mat[1][2] == jogador and mat[2][2] == jogador:
        return True

    if mat[0][0] == jogador and mat[1][1] == jogador and mat[2][2] == jogador:
        return True
    if mat[0][2] == jogador and mat[1][1] == jogador and mat[2][0] == jogador:
        return True

    return False

print("Bem vindo ao jogo da velha")
print("desafie o seu amigo para uma partida de jogo da velha")
print("regras:")
print("O jogo comeca com uma matriz 3x3")
print("cada jogador escolhe uma posicao da matriz")
print("o primeiro a completar 3 posicoes do mesmo jogador vence")
print("a posicao escolhida deve ser um numero de 1 a 9")

matriz = criaMatriz()
jogador = "X"
c = 0
while c < 9:
    apresentaMatriz(matriz)
    jogador = trocaJogador(jogador)
    while True:
        posicao = int(input("Escolha uma posicao: "))
        if posicao > 9 or posicao < 1:
            print("Posicao invalida")
            continue
        if posicaoOcupada(matriz, [int((posicao - 1) / 3), (posicao - 1) % 3]):
            print("Posicao ocupada")
            continue
        break
    matriz = resgistraJogada(matriz, jogador, [int((posicao - 1) / 3), (posicao - 1) % 3])
    if verificaJogador(matriz, jogador):
        apresentaMatriz(matriz)
        print("O jogador", jogador, "venceu")
        break
    c += 1
    
       
 