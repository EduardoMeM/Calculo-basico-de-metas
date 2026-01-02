from tkinter import *
import tkinter as tk

import requests

def pegar_cotacao():
    requisicao=requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") 
    requisicao_dic=requisicao.json()
    cotacao_dolar=requisicao_dic["USDBRL"] ["bid"]
    cotacao_euro=requisicao_dic["EURBRL"] ["bid"]
    cotacao_btc=requisicao_dic["BTCBRL"] ["bid"]
    texto_cotacao['text']=f'''
           Dólar:{cotacao_dolar}
           Euro:{cotacao_euro}
           Bitcoin {cotacao_btc} '''
    
    

janela=Tk()

janela.title("Cotação do bitcoin")

janela.geometry("300x300")

usuario= Label(janela,text="Usuario: Eduardo")
usuario.grid(column=0,row=0, padx=10,pady=10) 


texto_orienta= Label(janela,text="Clique em baixo para saber a cotação atual da moeda")
texto_orienta.grid(column=0,row=1, padx=10,pady=10)

botao=Button(janela,text="clique aqui!",command=pegar_cotacao)
botao.grid(column=0,row=2, padx=10,pady=10)

texto_cotacao=Label(janela,text="")
texto_cotacao.grid(column=0,row=3, padx=10,pady=10)

janela.mainloop()



