from Exportacao import Exportacao
from Importacao import Importacao
from NCM import NCM


def main():

    #Bloco de Operações para o dataSet Exportação
    exp = Exportacao()
    #exp.carregar()
    #exp.lerInformacoes()
    #exp.prepararData()
    #exp.novoData()
    #colocar aqui operações do bd
    exp.visualizarDados()

    #Bloco de Operações para o dataSet Importação
    #importacao = Importacao()
    '''importacao.carregar()
    importacao.lerInformacoes()
    importacao.prepararData()
    importacao.novoData()'''
    #importacao.visualizarDados()

    #Bloco de operações para o NCM
    '''  ncm = NCM()
    ncm.carregar()
    ncm.lerInformacoes()
    ncm.prepararData()
    ncm.novoData()'''




if __name__ == "__main__":
    main()