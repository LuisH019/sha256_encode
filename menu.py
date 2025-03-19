import os
import time
from encode import encode
from util.inputPlus import inputPlus


def exibirMenu():
    op = 1
    while op:
        os.system('cls')

        print("===== CODIFICAR =====")

        original = input("Digite a mensagem a ser codificada: ")

        encoded = encode(original)
        print("=========================")
        print("Mensagem codificada:", encoded)
        print("=========================")

        print("Deseja codificar outra mensagem?")
        print("1. Sim")
        print("0. Não")

        op = inputPlus("Digite: ", 0, 1)

    print("Saindo do programa...")

exibirMenu()