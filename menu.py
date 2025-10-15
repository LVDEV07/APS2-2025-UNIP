#Tratamento de erro para caso o usuário tente ler um arquivo que não foi criado.

def menu():

    print("Seja Bem-Vindo ao nosso programa ! \n")

    print("Menu de opções: \n")

    print("1- Criar Arquivo")
    print("2- Inserir no Arquivo")
    print("3- Ler Arquivo")
    print("4- Criptografar Arquivo")
    print("5 - Descriptografar Arquivo")
    print("6- Sair")

    opcaoEscolhida = int(input("\nDigite o número da opção que você deseja acessar (1 a 6):"))
    
    while opcaoEscolhida < 1 or opcaoEscolhida >6:
        print("\n-------------Opção Incorreta, tente novamente:-------------\n")
                    
        opcaoEscolhida = int(input("\nDigite a opção que você deseja acessar (1 a 6): "))


    return opcaoEscolhida


def criarArquivo():
    nomeArquivo = input("Digite o nome do Arquivo a ser criado: ")
    arq = open(nomeArquivo,"a")
    arq.close()

def InserirArquivo(nomeArquivo,):
    arq = open(nomeArquivo,"a")
    texto = input("Digite o texto a ser criptografado: ")
    arq.write(texto)
    arq.close()

def lerArquivo(nomeArquivo):
    arq = open(nomeArquivo,"r")
    textoLido = arq.read(nomeArquivo)
    arq.close()

    print(textoLido)

def criptografarArquivo(nomerquivo):
    print()

def descriptografarArquivo(nomerquivo):
    print()

def selecionarOpcao(opcaoEscolhida):
    

    return opcaoEscolhida






