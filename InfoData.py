class InfoData:

    def __init__(self, data):

        self.data = data
        

    def lerInformacoes(self):

        self.head()
        self.estrutura()
        self.qntLinhasColunas()
         
    def head(self):
     
        print("Primeiros 5 registros:")
        print(self.data.head())

    def estrutura(self):

        print("Estrutura:")
        print(self.data.info())

    def qntLinhasColunas(self):

        print("Linhas x Colunas:")
        print(self.data.shape)

    