from NCM import NCM
from Exportacao import Exportacao
from Importacao import Importacao
from sendCsvToMongo import enviarMongo
import datetime



def main():

    tempoInicio = datetime.datetime.now()
    # Bloco de Operações para o dataSet Exportação
    exp = Exportacao()
    exp.carregar()
    exp.lerInformacoes()
    exp.transformar()
    exp.lerInformacoes()
    exp.novoData()

    # Bloco de Operações para o dataSet Importação
    imp = Importacao()
    imp.carregar()
    imp.lerInformacoes()
    imp.transformar()
    imp.lerInformacoes()
    imp.novoData()

    # Bloco de operações para o NCM
    ncm = NCM()
    ncm.carregar()
    ncm.lerInformacoes()
    ncm.transformar()
    ncm.lerInformacoes()
    ncm.novoData()
    
    # Subir para o MongoDb os arquivos formatados pronto para as análises
    enviarMongo()

    # Visualizar os Resultados

    exp.visualizarDados()
    imp.visualizarDados()

    print("Tempo gasto: " + str(datetime.datetime.now() - tempoInicio))

if __name__ == "__main__":
    main()