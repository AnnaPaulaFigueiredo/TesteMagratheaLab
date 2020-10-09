from os import X_OK
import pandas as pd
from Preparacao import Preparacao


class NCM:

    def __init__(self):

        self.data = None

    def carregar(self):
        
        print("Carregando Data NCM...")
        self.data = pd.read_csv("Data/In/NCM.csv", encoding='latin-1', sep=";")

    def transformar(self):

        self.removerColunas( ["CO_UNID", "CO_SH6", "CO_PPE", "CO_PPI", "CO_FAT_AGREG", "CO_CUCI_ITEM", "CO_CGCE_N3", "CO_SIIT", "CO_ISIC_CLASSE", "CO_EXP_SUBSET", "NO_NCM_ESP"])
        self.removerDuplicados()
        self.removerLixosEmString("NO_NCM_POR")

    def removerColunas(self, colunas):
 
        print("Removendo Colunas...")
        print("Antes", self.data.columns)

        self.data = self.data.drop(columns=colunas)   

        print("Depois", self.data.columns)

      
    def lerInformacoes(self):

        print("Informações sobre o dataset de NCM, onde encontra-se os nomes dos produtos.")
        
        print("Primeiros 5 registros:")
        self.data.head()
            
        print("Estrutura")
        self.data.info()
            
        print("Linha x Colunas")
        print(self.data.shape)

    def removerDuplicados(self):
    
        print("Quantidade Antes do Drop Duplicates :", len(self.data))

        self.data.drop_duplicates()
        
        print("Depois:", len(self.data))

                
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
        
    def novoData(self):
        
        print("Salvando novo NCM...")
        self.data.to_csv("Data/Out/NCM_FORMATO_TESTE.csv", index=False, sep=";")