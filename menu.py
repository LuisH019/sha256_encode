import os
from util.sha256Encode import sha256Encode
from util.inputPlus import inputPlus
from util.keyHandler import saveKey, validateKey


def exibirMenu():
    op = 1
    while op:
        os.system('cls')
        print("===== MENU =====")
        print("Escolha: ")
        print("1. Codificar uma mensagem")
        print("2. Codificar um arquivo")
        print("3. Validar um arquivo")
        print("0. Sair")
        op = inputPlus("Digite: ", 0, 3)
        
        if op == 1:
            while op:
                os.system('cls')

                print("===== CODIFICAR MENSAGEM =====")
                
                original = input("Digite a mensagem a ser codificada: ")

                encoded = sha256Encode(original, 's')
                print("=========================")
                print("Mensagem codificada:", encoded)
                print("=========================")

                print("Deseja codificar outra mensagem?")
                print("1. Sim")
                print("0. Não")

                op = inputPlus("Digite: ", 0, 1)
            op = 1
            
        elif op == 2:
            while op:
                os.system('cls')

                print("===== CODIFICAR ARQUIVO =====")
                    
                fileName = input("Digite o nome do arquivo: ")

                encoded = sha256Encode(fileName, 'f')
                print("=========================")
                print("Chave do arquivo:", encoded)
                saveKey(fileName, encoded)
                print("=========================")

                print("Deseja codificar outro arquivo?")
                print("1. Sim")
                print("0. Não")

                op = inputPlus("Digite: ", 0, 1)
            op = 2
            
        elif op == 3:
            while op:
                os.system('cls')

                print("===== VALIDAR ARQUIVO =====")
                    
                fileName = input("Digite o nome do arquivo: ")

                encoded = sha256Encode(fileName, 'f')
                print("=========================")
                validateKey(fileName, encoded)
                print("=========================")

                print("Deseja validar outro arquivo?")
                print("1. Sim")
                print("0. Não")

                op = inputPlus("Digite: ", 0, 1)
            op = 2

    print("Saindo do programa...")

exibirMenu()