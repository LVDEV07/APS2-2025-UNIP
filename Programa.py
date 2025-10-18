import menu

print("\nSeja Bem-Vindo ao nosso programa !")

controle = True
while controle:
    menu.menu()
    opcaoEscolhida = menu.opcaoEscolhida()
    controle  = menu.CondicionalOpcao(opcaoEscolhida)





