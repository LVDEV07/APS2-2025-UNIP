#Buscar Lógica Criptografia e Descriptografia
#Tratamento de erro para caso o usuário tente ler um arquivo que não foi criado.

import os
#Imprime o menu de opções
def menu():

    print("\nMenu de opções: \n")

    print("1- Criar Arquivo")
    print("2- Escrever no Arquivo")
    print("3- Ler Arquivo")
    print("4- Criptografar Arquivo")
    print("5 - Descriptografar Arquivo")
    print("6 - Remover Arquivo")
    print("7- Sair")

#Lê a opção escolhida e verifica se ela é válida.
def opcaoEscolhida():
    opcaoEscolhida = int(input("\nDigite o número da opção que você deseja acessar (1 a 7):"))
    
    while opcaoEscolhida < 1 or opcaoEscolhida >7:
        print("\n-------------Opção Incorreta, tente novamente:-------------\n")
                    
        opcaoEscolhida = int(input("\nDigite a opção que você deseja acessar (1 a 7): "))

    #Retorna a opção escolhida
    return opcaoEscolhida

#Processo de criptografia
def criptografia(nomeArquivo,nomeArquivoCript,chaveCript):
    print()

#Processo de descriptografia
def descriptografia(nomeArquivo,nomeArquivoDescript,chaveDescript):
    print()


def criarArquivo():
    nomeArquivo = input("Digite o nome do arquivo a ser criado: ")
    arq = open(nomeArquivo,"w")
    arq.close()


def InserirArquivo():

    nomeArquivo = input("Digite o nome do Arquivo em que você deseja escrever: ")
    arq = open(nomeArquivo,"a")
    texto = input("Digite o texto: ")
    arq.write(texto)
    arq.close()

#Le e imprime o conteúdo de um arquivo
def lerArquivo():
    nomeArquivo = input("Digite o nome do Arquivo em que você deseja ler: ")
    arq = open(nomeArquivo,"r")
    textoLido = arq.read()
    arq.close()
    print(f"Texto do {nomeArquivo} : {textoLido}")

#Faz a solicitação dos dados necessários para executar a criptografia, e chama a função que realiza o processo.
def criptografarArquivo():
    nomeArquivo = input("Digite o nome do arquivo a ser criptografado: ")
    nomeArquivoCript = input("Digite o nome para salvar o arquivo criptografado: ")
    chaveCript = int(input("Digite a chave de criptografia: "))
    criptografia(nomeArquivo,nomeArquivoCript,chaveCript)

#Faz a solicitação dos dados necessários para executar a descriptografia, e chama a função que realiza o processo.
def descriptografarArquivo():
    nomeArquivo = input("Digite o nome do arquivo a ser descriptografado: ")
    nomeArquivoCript = input("Digite o nome para salvar o arquivo descriptografado: ")
    chaveCript = int(input("Digite a chave de descriptografia: "))
    descriptografia(nomeArquivo,nomeArquivoCript,chaveCript)
    
#Remove um arquivo x
def removerArquivo():
    nomeArquivo = input("Digite o nome do arquivo a ser removido: ")
    os.remove(nomeArquivo)


#Realiza o processo de chamada das funções baseado no opção escolhida
def CondicionalOpcao(opcaoEscolhida):
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

    elif opcaoEscolhida == 7:
        print("Programa encerrado !")
        controle = False
        return controle
    
    if opcaoEscolhida != 7:
        controle = True
        return controle
    

    






