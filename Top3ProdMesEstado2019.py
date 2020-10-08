from operator import index
from numpy.core.shape_base import stack
from pandas.core import groupby
from pymongo import MongoClient
import pandas as pd
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import numpy as np
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

def gerarTop3ProdMesEstado(dataBase, nome , cor ):
    
        cliente = MongoClient('localhost', 27017)
        cliente = MongoClient('mongodb://localhost:27017/')
        banco = cliente.Magrathea
        albumNcm = banco.NCM_FORMATO_TESTE
       
       
        dfFinal = pd.DataFrame(columns=["ANO", "MES", "UF", "CO_NCM","KG_LIQUIDO"])

        #for estado in listaDeEstados:
        # colocar todos os estados
        listaDeEstados = list(dataBase.distinct("SG_UF_NCM"))
        
        for estado in listaDeEstados:

            for mes in range(1, 13):
                
                # Dados vem agrupados por ANO, ESTADO, e MES
                query = {"$and":[ {"CO_ANO":2019}, {"SG_UF_NCM": str(estado)}, {"CO_MES":mes}, ]}
                filtroAno = list(dataBase.find(query, { "CO_NCM": 1, "KG_LIQUIDO": 1}))
                    
                try:

                    dfFiltro = pd.DataFrame(filtroAno)
                            
                    ordenaTop3 = dfFiltro.groupby("CO_NCM")["KG_LIQUIDO"].sum().sort_values(ascending=False)
                    listaDeCodigo = list(ordenaTop3.head(3).index)
                    listaKgLiquido = list(ordenaTop3.head(3).values)
                

                    dicionario = { "ANO": 2019 , "MES": mes, "UF": estado, "CO_NCM": listaDeCodigo, "KG_LIQUIDO": listaKgLiquido }
                    dfFinal = dfFinal.append(dicionario, ignore_index=True)

                    
                except:
                    pass
            
            plotarGrafico(dfFinal, albumNcm, str(estado), nome, cor)
   


def limparStringDoFormatoLista(string: str):

        string = string.replace("[", "")
        string = string.replace("]", "")
        string = string.replace("'", "")
        
        return string

def plotarGrafico(dfFinal, albumNcm, estado, nome, cor):

        # Configuração do SubPlot    
        linha = 1
        coluna = 1
        figSubplot = make_subplots(
                                    rows=3, cols=4,
                                    specs=[[{"type": "bar"}, {"type": "bar"}, {"type": "bar"}, {"type": "bar"}],
                                            [{"type": "bar"}, {"type": "bar"}, {"type": "bar"}, {"type": "bar"}],
                                            [{"type": "bar"}, {"type": "bar"}, {"type": "bar"}, {"type": "bar"}]],
                                    subplot_titles=("Janeiro","Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" ))

        # terão seu tamanho len = 12, cada
        
    

        for mes in range(1, 13):
            
            try:

                prodMes = list(dfFinal.query("MES == @mes & UF == @estado")["CO_NCM"])
                quantidade = list(dfFinal.query("MES == @mes & UF == @estado")["KG_LIQUIDO"])

                qntProd1 = int(quantidade[0][0])
            
                qntProd2 = int(quantidade[0][1])

                qntProd3 = int(quantidade[0][2])

                
                codProd1 = int(prodMes[0][0])
                codProd2 = int(prodMes[0][1])
                codProd3 = int(prodMes[0][2])
            



                nomeProd1 = pd.DataFrame(list(albumNcm.find({"CO_NCM": codProd1 }, {"NO_NCM_POR": 1})))
                nomeProd2 = pd.DataFrame(list(albumNcm.find({"CO_NCM": codProd2 }, {"NO_NCM_POR": 1})))
                nomeProd3 = pd.DataFrame(list(albumNcm.find({"CO_NCM": codProd3 }, {"NO_NCM_POR": 1})))
                
                nomeProd1 = limparStringDoFormatoLista(str(nomeProd1["NO_NCM_POR"].values))
                nomeProd2 = limparStringDoFormatoLista(str(nomeProd2["NO_NCM_POR"].values))
                nomeProd3 = limparStringDoFormatoLista(str(nomeProd3["NO_NCM_POR"].values))

                figSubplot.add_trace(go.Bar(x=["Produto 1", "Produto 2", "Produto 3"],
                                                    y=[qntProd1, qntProd2, qntProd3],
                                                    hovertext=[nomeProd1, nomeProd2, nomeProd3],
                                                    width=[0.50, 0.50, 0.50], 
                                                    marker_color= cor,
                                                    ), row=linha,col=coluna)
                
                coluna = coluna + 1
                linha = linha + 1
                if (coluna == 5):
                    coluna = 1
                if( linha == 4):
                    linha = 1
            except:
                pass

        figSubplot.update_layout(showlegend=False, title_text="Top3 Produtos " + nome + " pelo "+ estado + " por mês, no Ano de 2019")
        figSubplot.show()
        nameSave = "top3-" + nome + "2019-UF-" + estado + ".html"
        figSubplot.write_html("Results/"+nameSave)



