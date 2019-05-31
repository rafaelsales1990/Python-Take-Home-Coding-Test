# -*- coding: utf-8 -*-
"""
Created on Sat May 25 17:47:38 2019

@author: Rafael Sales

"""
#importando as bibliotecas necessárias para trabalhar com arquivo JSON 
# e acessar os tópicos dos eventos da url.
import json
from sseclient import SSEClient as sse
from datetime import datetime
import pyodbc as pdb


#Configurando a conexão com o banco de dados
conn = pdb.connect('Driver={SQL Server};'
                      'Server=DESKTOP-OMPS0B3;'
                      'Database=DBWIKI;'
                      'Trusted_Connection=yes;')

 
#armazenamento da URL que desejamos capturar os eventos.
url = 'https://stream.wikimedia.org/v2/stream/recentchange'

#Execução do comando de "captura" das mensagens e armazenando o resultado na 
# variável
mensagens = sse(url)

#Carrego cursor da conexão para a varíavel onde será executada a QUERY dobanco de dados
cursor = conn.cursor()
#iteração for para percorrer as mensagens capturadas na variável 'mensagens'
for evento in mensagens:
    #verifica se o evento é do tipo "message"
    if evento.event == 'message':
    #Tentativa de carregar o evento para JSON, nesse momento casso ocorra erro o código é 
    #direcionado para o except 
        try:
            #parse no formato do JSON que será carregado 
            alteracao = json.loads(evento.data)
            alteracao
        except ValueError:
            continue
        #verifica na chave "bot" é verdadeira ou false
        if alteracao['bot'] == False:
            #inserção dos dados no banco de dados.            
            cursor.execute("exec [SP_INSERT_RC] '{}', '{}', '{}', '{}', '{}'".format(datetime.utcfromtimestamp(alteracao['timestamp']).strftime('%Y%m%d %H:%M:%S'),alteracao["user"], alteracao["namespace"],alteracao["title"].replace("'",""),alteracao["server_name"]))
            cursor.commit()
            
                
            


