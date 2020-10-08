from ValoresPorEstadoEtotalPais2019 import gerarEstadoEmRelacaoTotPais
from Top3ProdMesEstado2019 import gerarTop3ProdMesEstado
import pandas as pd
from InfoData import InfoData
from Preparacao import Preparacao
from pymongo import ASCENDING, MongoClient
import plotly.express as px
from Top3ProdAnualEstado import gerarTop3ProdAnualEstado


class Exportacao:

    def __init__(self):

        self.data = None
        self.infoData = None
        self.preparacao = None
    

    def carregar(self):  

        print("Carregando Data...")
        self.data = pd.read_csv("Data/In/EXP_COMPLETA.csv",  encoding='utf-8', sep=";")
        
    def lerInformacoes(self):

        print("Informações sobre o dataset de exportação.")

        self.infoData = InfoData(self.data)

        self.infoData.lerInformacoes()

    def prepararData(self):

        self.preparacao = Preparacao(self.data)    
        self.data = self.preparacao.filtrarAno()
        self.data = self.preparacao.removerDuplicados()
        self.data = self.preparacao.removerColunas(["CO_UNID", "CO_VIA", "CO_URF"])
        self.data = self.preparacao.removerUF()
        self.verificarNull()
    
    def verificarNull(self):
        
        print("Quantidade de registros null:")
        print(self.data.isnull().sum())
    
    # Operação Única Diferente
    def novoData(self):

        print("Salvando novo EXP...")
        self.data.to_csv("Data/Out/EXP_FORMATO_TESTE.csv", index=False, sep=";")

    def visualizarDados(self):

        cliente = MongoClient('localhost', 27017)
        cliente = MongoClient('mongodb://localhost:27017/')
        banco = cliente.Magrathea
        albumExp = banco.EXP_FORMATO_TESTE
        
        gerarTop3ProdAnualEstado(albumExp, px.colors.cyclical.Edge, "Exportados")
        #gerarTop3ProdMesEstado(albumExp, "Exportados" , px.colors.sequential.Aggrnyl )
        #gerarEstadoEmRelacaoTotPais(albumExp, "Exportados" , px.colors.sequential.RdBu)


