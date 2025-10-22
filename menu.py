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
    opcaoEscolhida = int(input("\nDigite o número da opção que você deseja acessar (1 a 7): "))
    
    while opcaoEscolhida < 1 or opcaoEscolhida >7:
        print("\n-------------Opção Incorreta, tente novamente:-------------\n")
                    
        opcaoEscolhida = int(input("\nDigite a opção que você deseja acessar (1 a 7): "))

    #Retorna a opção escolhida
    return opcaoEscolhida


#Converte a chave em uma lista numérica
def prepararChave(chaveNum):

    # Converte o número para string
    chaveStr = str(chaveNum)
    
 
    listaDeDigitos = [] 
    
    # Percorre a chave str e insere os caracteres na lista como inteiros.
    for digitoChar in chaveStr:
        
        listaDeDigitos.append(int(digitoChar))
        
    
    return listaDeDigitos


#Processo de criptografia
def criptografia(texto,chaveCript):
    
    if chaveCript <= 0:

        print("Chave inválida (deve ser > 0).")

    
    chaveDigitos = prepararChave(chaveCript)
    tamanhoChave = len(chaveDigitos)
    
    textoMinusc = texto.lower()
    
    textoCriptografado = ""
    
    #Variável de controle que percorre o digitos da chave, conforme é encontrado uma letra dentro do texto
    j = 0 
    

    for charTexto in textoMinusc:      

        #Verifica se é uma letra, se for, roda a criptografia
        if 'a' <= charTexto <= 'z':

        
            deslocamento = chaveDigitos[j % tamanhoChave]
            
    
            valorTexto = ord(charTexto) - ord('a')
            novoValor = (valorTexto + deslocamento) % 26
            textoCriptografado += chr(novoValor + ord('a'))
            
            # Avança o índice da chave
            j += 1
        
        else:
            # Se for um um caractere fora do alfabeto de a-z ele passa direto e insere no texto
            textoCriptografado += charTexto

    return textoCriptografado


#Processo de descriptografia
def descriptografia(textoCript,chaveDescript):
    
    
    if chaveDescript <= 0:
        print("Chave inválida (deve ser > 0).")
        return textoCript

    chaveDigitos = prepararChave(chaveDescript)
    tamanhoChave = len(chaveDigitos)
    
    textoDescript = ""
    j = 0 # Índice da chave
    
    for charCripto in textoCript:
        
        # Verifica se é uma letra
        if 'a' <= charCripto <= 'z':
            
            deslocamento = chaveDigitos[j % tamanhoChave]
            
           
            valorCripto = ord(charCripto) - ord('a')
            
            novoValor = (valorCripto - deslocamento + 26) % 26
            
            textoDescript += chr(novoValor + ord('a'))
            
            j += 1
        
        else:
            # Passa o caractere (espaço, etc.) direto
            textoDescript += charCripto
            
    return textoDescript


def criarArquivo(nomeArquivo):
    arq = open(nomeArquivo,"w")
    arq.close()

def criarArquivoIn():

    nomeArquivo = input("Digite o nome do arquivo a ser criado: ")
    criarArquivo(nomeArquivo)

    resp = input("Deseja escrever algo no arquivo ? (s/n) ")

    if resp == 's':
        texto = input("Digite o texto:")
        InserirArquivo(nomeArquivo,texto)

    elif resp == 'n':
        print("Retornando ao menu...")

    else:
        print("Opção não disponível. Retornando ao menu...")


#Escrever no arquivo usado na Criptografia e Descriptografia
def InserirArquivo(nomeArquivo,texto):

    arq = open(nomeArquivo,"a")
    arq.write(texto)
    arq.close()

#Insere o texto digitado ao final do arquivo
def InserirArquivoIn():

    nomeArquivo = input("Digite o nome do Arquivo em que você deseja escrever: ")
    texto = input("Digite o texto: ")
    InserirArquivo(nomeArquivo,texto)
    

#Ler arquivo usado na Criptografia e Descriptografia
def lerArquivo(nomeArquivo):
    arq = open(nomeArquivo,"r")
    textoLido = arq.read()
    arq.close()

    return textoLido

#Le e imprime o conteúdo de um arquivo
def lerArquivoIn():
    nomeArquivo = input("Digite o nome do Arquivo em que você deseja ler: ")
    
    print(f"Texto dentro de {nomeArquivo}: {lerArquivo(nomeArquivo)}")

#Faz a solicitação dos dados necessários para executar a criptografia, chama a função que realiza o processo, e coloca o resultado em um arquivo.
def criptografarArquivo():


    nomeArquivo = input("Digite o nome do arquivo a ser criptografado: ")
    texto = lerArquivo(nomeArquivo)
    nomeArquivoCript = input("Digite o nome para salvar o arquivo criptografado: ")

    chaveCript = int(input("Digite a chave de criptografia: "))
    textoCrip = criptografia(texto,chaveCript)

    criarArquivo(nomeArquivoCript)
    InserirArquivo(nomeArquivoCript,textoCrip)

    print(f"Texto criptografado: {textoCrip}")



#Faz a solicitação dos dados necessários para executar a descriptografia,chama a função que realiza o processo, e coloca o resultado em um arquivo.
def descriptografarArquivo():

    
    nomeArquivoCript = input("Digite o nome do arquivo a ser descriptografado: ")
    textoCript = lerArquivo(nomeArquivoCript)
    nomeArquivoDescript = input("Digite o nome para salvar o arquivo descriptografado: ")
    chaveDescript = int(input("Digite a chave de descriptografia: "))


    textoDescripto = descriptografia(textoCript,chaveDescript)

    criarArquivo(nomeArquivoDescript)
    InserirArquivo(nomeArquivoDescript,textoDescripto)
    print(f"Texto Descriptografado: {textoDescripto}")

    
    
#Remove um arquivo x
def removerArquivo():
    nomeArquivo = input("Digite o nome do arquivo a ser removido: ")
    os.remove(nomeArquivo)


#Realiza o processo de chamada das funções baseado no opção escolhida
def CondicionalOpcao(opcaoEscolhida):
    if opcaoEscolhida == 1:
        criarArquivoIn()

    elif opcaoEscolhida == 2:
        InserirArquivoIn()
        
    elif opcaoEscolhida == 3:
        lerArquivoIn()
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
    

    






