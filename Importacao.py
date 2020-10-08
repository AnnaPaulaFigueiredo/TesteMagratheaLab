from Top3ProdMesEstado2019 import gerarTop3ProdMesEstado
from Top3ProdAnualEstado import gerarTop3ProdAnualEstado
from ValoresPorEstadoEtotalPais2019 import gerarEstadoEmRelacaoTotPais
import pandas as pd
from InfoData import InfoData
from Preparacao import Preparacao
from pymongo import ASCENDING, MongoClient
import plotly.express as px

class Importacao:

    def __init__(self):

        self.data = None
        self.infoData = None
        self.preparacao = None


    def carregar(self):  

        print("Carregando Data...")
        self.data = pd.read_csv("Data/In/IMP_COMPLETA.csv",  encoding='utf-8', sep=";")
        
    def lerInformacoes(self):

        print("\nInformações sobre o dataset de importcação.")

        self.infoData = InfoData(self.data)

        self.infoData.lerInformacoes()

    def prepararData(self):

        self.preparacao = Preparacao(self.data) 
        listaColunas = ["CO_UNID", "CO_VIA", "CO_URF"]
        self.data = self.preparacao.removerColunas(listaColunas)   
        self.data = self.preparacao.filtrarAno()
        self.data = self.preparacao.removerUF()
        self.data = self.preparacao.removerDuplicados()
     
        self.verificarNull()
    
    def verificarNull(self):
        
        print("Quantidade de registros null:")
        print(self.data.isnull().sum())
    
    # Operação Única Diferente
    def novoData(self):

        print("Salvando novo IMP...")
        self.data.to_csv("Data/Out/IMP_FORMATO_TESTE.csv", index=False, sep=";")

    def visualizarDados(self):

        cliente = MongoClient('localhost', 27017)
        cliente = MongoClient('mongodb://localhost:27017/')
        banco = cliente.Magrathea
        albumImp = banco.IMP_FORMATO_TESTE
        
        gerarTop3ProdAnualEstado(albumImp, px.colors.cyclical.mrybm, "Importado")
        #gerarTop3ProdMesEstado(albumImp, "Importado" , px.colors.sequential.thermal )
        #gerarEstadoEmRelacaoTotPais(albumImp, "Importado", px.colors.sequential.RedGy)