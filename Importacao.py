from ValoresPorEstadoEtotalPais2019 import gerarEstadoEmRelacaoTotPais
from Top3ProdMesEstado2019 import gerarTop3ProdMesEstado
import pandas as pd
from Preparacao import Preparacao
from pymongo import ASCENDING, MongoClient
import plotly.express as px
from Top3ProdAnualEstado import gerarTop3ProdAnualEstado


class Importacao:

    def __init__(self):

        self.data = None

    def carregar(self):  

        print("Carregando Data IMP...")
        
        self.data = pd.read_csv("Data/In/IMP_COMPLETA.csv",  encoding='utf-8', sep=";" )
        
        self.lerInformacoes()  


    def transformar(self):
        
        self.removerColunas(["CO_UNID", "CO_VIA", "CO_URF", "CO_PAIS", "QT_ESTAT"])
        self.filtrarAno()
        self.removerDuplicados()
        self.removerUF()
        self.verificarNull()
    
    def lerInformacoes(self):
        
        print("Informações do dataset final ...")
        print("Primeiros 5 registros:")
        self.data.head()
            
        print("Estrutura")
        self.data.info()
            
        print("Linha x Colunas")
        print(self.data.shape)
            
    
    def removerColunas(self, colunas):
 
        print("Removendo Colunas...")
        print("Antes", self.data.columns)

        self.data = self.data.drop(columns=colunas)   

        print("Depois", self.data.columns)

    def removerLinhas(self, indices):

        print("Removendo Linhas...")
        print("Antes len:", len(self.data))

        self.data = self.data.drop(index=indices)
        
        print("Depois len:", len(self.data))


    def filtrarAno(self):

        print("Filtrando Anos 2017-2018-2019...")

        anos = [2017, 2018, 2019]
        remover = self.data.query("CO_ANO not in @anos").index 
        
        self.removerLinhas(remover)

    def removerDuplicados(self):
    
        print("Quantidade Antes do Drop Duplicates :", len(self.data))

        self.data.drop_duplicates()
        
        print("Depois:", len(self.data))

    
    def removerUF(self):

        print("Removendo UFs não condizentes com a realidade atual ...")
        
        print("TIPO DE DATA :", type(self.data))
        print(self.data.head())

        listaDeEstados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", 
                        "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE","PI", "RJ",
                        "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
        remover = None
        remover = self.data.query("SG_UF_NCM not in @listaDeEstados").index

        if len(remover) > 0:

            self.removerLinhas(remover)
        
        else:
            print("Não há elementos para serem removidos.")
        

    def verificarNull(self):
        
        print("Quantidade de registros null:")
        print(self.data.isnull().sum())


    def novoData(self):

        print("Salvando novo EXP...")
        self.data.to_csv("Data/Out/IMP_FORMATO_TESTE.csv", index=False, sep=";")

    def visualizarDados(self):

        cliente = MongoClient('localhost', 27017)
        banco = cliente.MagratheaLabs
        albumImp = banco.IMP_FORMATO_TESTE
        
        gerarTop3ProdAnualEstado(albumImp, px.colors.sequential.Cividis, "Importados")
        gerarTop3ProdMesEstado(albumImp, "Importados" , px.colors.sequential.Aggrnyl )
        gerarEstadoEmRelacaoTotPais(albumImp, "Importados" , px.colors.sequential.RdBu)


