#formatar cada tabela para os dados que eu quero
class Preparacao:

    def __init__(self, data):
        
        self.data = data
 
    def removerDuplicados(self):
    
        print("\nQuantidade Antes do Drop Duplicates :", len(self.data))

        self.data.drop_duplicates()
        
        print("Depois:", len(self.data))
        
        return self.data

    def removerColunas(self, colunas):

        print("\nRemovendo Colunas...")
        print("Antes", len(self.data.columns))

        self.data = self.data.drop(columns=colunas)   

        print("Depois", len(self.data.columns))

        return self.data

    def removerLinhas(self, indices):

        print("\nRemovendo Linhas...")
        print("Antes", len(self.data))

        self.data = self.data.drop(index=indices)
        
        print("Depois", len(self.data))

        return self.data

    def filtrarAno(self):
        
        print("Filtrando Anos 2017-2018-2019...")
        
        remover = None
        anos = [2017, 2018, 2019]
        remover = self.data.query("CO_ANO not in @anos")

        if len(remover) > 0:

            indices = self.data.query("CO_ANO not in @anos").index
            self.data = self.removerLinhas(indices)
        
        else:
            print("Não há elementos para serem removidos.")

        return self.data
    
    def removerUF(self):

        print("Removendo UFs não condizentes com a realidade atual ...")

        listaDeEstados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", 
                        "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE","PI", "RJ",
                        "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
        remover = None
        remover = self.data.query("SG_UF_NCM not in @listaDeEstados")

        if len(remover) > 0:

            indices = self.data.query("SG_UF_NCM not in @listaDeEstados").index
            self.data = self.removerLinhas(indices)
        
        else:
            print("Não há elementos para serem removidos.")
        
        return self.data 

    #SEMPRE VERIFICAR SE EXISTEM LINHAS A SEREM REMOVIDAS PARA NÃO DAR ERRO 
   
    
