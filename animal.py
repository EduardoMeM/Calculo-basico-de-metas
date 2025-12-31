class ANIMAL:
    def __init__(self,tipo,som,come,dorme):
        self.tipo=tipo
        self.som=som
        self.come=come
        self.dorme=dorme

    def comer(fome):
        if fome==True:
            print("Pegar a racao. ")
        elif fome==False:
            print("Guardar racao.")

    def passear(sair):
        if sair<3:
            print("Lembrar de passear tres vezes ao dia,para o animal nao faca xixi dentreo de casa>")
        else:
            print(f"Muito bem o animal ja saiu tres vezes ao dia.")
            return sair

    def irdormir(sono):
        while sono>=10 or sono>=22:
            print("Vai dormir seu bicho estar com sono")
            return sono



    
a1=ANIMAL("cachorro","au au","racao","as 22 hs")
a2=ANIMAL("cobra","siiisiiiss","rato","as 3 hs")
a3=ANIMAL("peixe","nenhum som","ração","nunca")
print(a1.come,a1.tipo,a1.som,a1.dorme)
ANIMAL.irdormir(sono=11)
ANIMAL.passear(sair=2)
ANIMAL.comer(fome=True)
print(f"O meu animal é um {a1.tipo} que faz {a1.som},come {a1.come}, e dorme {a1.dorme} ")
print(f"O meu animal é um {a2.tipo} que faz {a2.som},come {a2.come}, e dorme {a2.dorme} ")
print(f"O meu animal é um {a3.tipo} que faz {a3.som},come {a3.come}, e dorme {a3.dorme} ")
        
        