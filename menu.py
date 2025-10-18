#Buscar Lógica Criptografia e Descriptografia
#Tratamento de erro para caso o usuário tente ler um arquivo que não foi criado.

import os

def menu():

    print("\nMenu de opções: \n")

    print("1- Criar Arquivo")
    print("2- Escrever no Arquivo")
    print("3- Ler Arquivo")
    print("4- Criptografar Arquivo")
    print("5 - Descriptografar Arquivo")
    print("6 - Remover Arquivo")
    print("7- Sair")

def opcaoEscolhida():
    opcaoEscolhida = int(input("\nDigite o número da opção que você deseja acessar (1 a 7):"))
    
    while opcaoEscolhida < 1 or opcaoEscolhida >7:
        print("\n-------------Opção Incorreta, tente novamente:-------------\n")
                    
        opcaoEscolhida = int(input("\nDigite a opção que você deseja acessar (1 a 7): "))


    return opcaoEscolhida

def criptografia(nomeArquivo,nomeArquivoCript,chaveCript):
    print()

#Buscar Lógica
def descriptografia(nomeArquivo,nomeArquivoDescript,chaveDescript):
    print()

def criarArquivo():
    nomeArquivo = input("Digite o nome do Arquivo a ser criado: ")
    arq = open(nomeArquivo,"w")
    arq.close()


def InserirArquivo():

    nomeArquivo = input("Digite o nome do Arquivo em que você deseja escrever: ")
    arq = open(nomeArquivo,"a")
    texto = input("Digite o texto a ser criptografado: ")
    arq.write(texto)
    arq.close()

    

def lerArquivo():
    nomeArquivo = input("Digite o nome do Arquivo em que você deseja ler: ")
    arq = open(nomeArquivo,"r")
    textoLido = arq.read()
    arq.close()
    print(f"Texto do {nomeArquivo} : {textoLido}")

def criptografarArquivo():
    nomeArquivo = input("Digite o nome do arquivo a ser criptografado: ")
    nomeArquivoCript = input("Digite o nome para salvar o arquivo criptografado: ")
    chaveCript = int(input("Digite a chave de criptografia: "))
    criptografia(nomeArquivo,nomeArquivoCript,chaveCript)


def removerArquivo():
    nomeArquivo = input("Digite o nome do arquivo a ser removido: ")
    os.remove(nomeArquivo)


def descriptografarArquivo():
    print()

def CondicionalOpcao(opcaoEscolhida):

    while opcaoEscolhida != 7:

        if opcaoEscolhida == 1:
            criarArquivo()

        elif opcaoEscolhida == 2:
            InserirArquivo()
        
        elif opcaoEscolhida == 3:
            lerArquivo()
        elif opcaoEscolhida == 4:
            criptografarArquivo()
        elif opcaoEscolhida == 5:
            descriptografarArquivo()

        elif opcaoEscolhida == 6:
            removerArquivo()

        break

    if opcaoEscolhida == 7:
        print("Programa encerrado !")
        controle = False
        return controle
    
    else:
        controle = True
        return controle
    

    






