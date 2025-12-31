class vendedor:
    nome=str(input("Nome do usuario: "))
    senha=int(input("Senha do usuario: "))
    if senha==1234 and nome=="Eduardo Moulin":
        print("Usuario liberado!!!")
        nomefuncionario=str(input("Qual o nome do vendedor: "))
        vendames=int(input("Informe quantas vendas foi realizadas esse mes: "))
        if vendames>=500:
            print(f"O {nomefuncionario} compriu a meta do mes!! e o seu rendimento foi {vendames-500} a mais do esperado")
        else:
            print(f"O {nomefuncionario} não cumpriu a meta do mes!! e o seu rendimento foi {vendames-500} a menos do esperado!!")
    else:
        print("A sua senha ou usuario esta errada!!");
        
vendedor()


