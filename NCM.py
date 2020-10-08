from os import X_OK
import pandas as pd

from InfoData import InfoData
from Preparacao import Preparacao


class NCM:

    def __init__(self):

        self.data = None
        self.infoData = None
        self.preparacao = None

    def carregar(self):
        
        print("Carregando Data...")

        self.data = pd.read_csv("Data/In/NCM.csv", encoding='latin-1', sep=";")
       
    def lerInformacoes(self):

        print("\nInformações sobre o dataset de NCM, onde encontra-se os nomes dos produtos.")

        self.infoData = InfoData(self.data)
        self.infoData.lerInformacoes()

    def prepararData(self):

        self.preparacao = Preparacao(self.data)
        self.data = self.preparacao.removerColunas(["CO_UNID", "CO_SH6", "CO_PPE", "CO_PPI", "CO_FAT_AGREG", "CO_CUCI_ITEM", "CO_CGCE_N3", "CO_SIIT", "CO_ISIC_CLASSE", "CO_EXP_SUBSET", "NO_NCM_ESP"])
        self.removerLixosEmString("NO_NCM_POR")
        
        
                   
   # TEM COMO OTMIZAR E NÂO ESTÀ REMOVENDO OS INICIOS E FINAIS DE " 
    def removerLixosEmString(self, coluna):

        print("Removendo Lixos ...")
        # Para Coluna POR
        for i in range(0, len(self.data)):    

           
            string =  self.data.loc[i , coluna]
           
            if '"' in string:

                string = string.rstrip('"')
                string = string.lstrip('"')
                string = string.replace('"', " ")
            
            if ";" in string:

                string = string.replace(";", " ")

            string = " ".join(string.split()) 
   
            
            self.data.loc[i , coluna] = string


        print("TIPO DA ESTRUTURA APÓS REMOVER LIXOS ", type(self.data))
        
    def novoData(self):
        
        print("Salvando novo NCM...")
        self.data.to_csv("Data/Out/NCM_FORMATO_TESTE.csv", index=False, sep=";")