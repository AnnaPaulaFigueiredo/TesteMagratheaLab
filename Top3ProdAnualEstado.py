from _plotly_utils.colors import named_colorscales
from pymongo import ASCENDING, MongoClient
import pandas as pd
import plotly.graph_objects as go
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px

def gerarTop3ProdAnualEstado(dataBase, cor, nome):
    
    dfFiltrado = filtrarTop3(dataBase)
    listaDeEstado = list(dataBase.distinct("SG_UF_NCM"))


    cliente = MongoClient('localhost', 27017)
    cliente = MongoClient('mongodb://localhost:27017/')
    banco = cliente.Magrathea
    albumNcm = banco.NCM_FORMATO_TESTE

    plotarGrafico(dfFiltrado, albumNcm, listaDeEstado, cor, nome)


def limparStringDoFormatoLista(string: str):
   
    string = string.replace("[", "")
    string = string.replace("]", "")
    string = string.replace("'", "")
    return string

def filtrarTop3(dataBase):
    
    listaDeEstado = list(dataBase.distinct("SG_UF_NCM"))
    

    dfFinal = pd.DataFrame(columns=["ANO", "SG_UF_NCM", "CO_NCM","KG_LIQUIDO"])

   

    for estado in listaDeEstado:
        
        # Dados vem agrupados por ANO, ESTADO, e MES
        query = {"SG_UF_NCM": str(estado)} 
        filtroUF = list(dataBase.find(query))
                
        try:

            dfFiltro = pd.DataFrame(filtroUF)
            ordenaTop3 = dfFiltro.groupby("CO_NCM")["KG_LIQUIDO"].sum().sort_values(ascending=False)
            listaDeCodigo = list(ordenaTop3.head(3).index)
            listaKgLiquido = list(ordenaTop3.head(3).values)

            dicionario = { "ANO": "2017 - 2019", "SG_UF_NCM": estado, "CO_NCM": listaDeCodigo, "KG_LIQUIDO": listaKgLiquido }
            dfFinal = dfFinal.append(dicionario, ignore_index=True)
        
        except:
            pass
        
    return dfFinal

def plotarGrafico(df, albumNcm, listaDeEstado, cor, nome):

    # Configuração do SubPlot    
    linha = 1
    coluna = 1
    figSubplot = make_subplots(
                                rows=6, cols=5,
                                specs=[
                                        [{"type": "bar"}, {"type": "bar"}, {"type": "bar"}, {"type": "bar"}, {"type": "bar"}],
                                        [{"type": "bar"}, {"type": "bar"}, {"type": "bar"}, {"type": "bar"}, {"type": "bar"}],
                                        [{"type": "bar"}, {"type": "bar"}, {"type": "bar"}, {"type": "bar"}, {"type": "bar"}],
                                        [{"type": "bar"}, {"type": "bar"}, {"type": "bar"}, {"type": "bar"}, {"type": "bar"}],
                                        [{"type": "bar"}, {"type": "bar"}, {"type": "bar"}, {"type": "bar"}, {"type": "bar"}],
                                        [{"type": "bar"}, {"type": "bar"}, {"type": "bar"}, {"type": "bar"}, {"type": "bar"}],
                                        ],
                                subplot_titles=("Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará",
                                                "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão", 
                                                "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará",
                                                "Paraíba",  "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
                                                "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima",
                                                "Santa Catarina", "São Paulo", "Sergipe", "Tocantins","","","",""))

    # terão seu tamanho len = 12, cada
    
   
  
    for estado in  listaDeEstado :
        
        try:
            
           

            prodMes = list(df.query("SG_UF_NCM== @estado")["CO_NCM"])
            quantidade = list(df.query("SG_UF_NCM == @estado")["KG_LIQUIDO"])

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

            if "," in nomeProd1:

                np1 = nomeProd1.split(",")
                np1 = np1[0]
            
            else:
                np1 = nomeProd1.split()
                np1 = np1[0]

            produtos = ["P1", "P2", "P3"]
            qnt = [qntProd1, qntProd2, qntProd3]

            




            figSubplot.add_trace(go.Bar(x = produtos,
                                        y = qnt,
                                        hovertext=[nomeProd1, nomeProd2, nomeProd3],
                                        width=[0.50, 0.50, 0.50], 
                                        marker_color=cor,
                                        ), row=linha,col=coluna)
            coluna = coluna + 1
            
            if coluna == 6:
                
                linha = linha + 1
                coluna = 1
            

        
        except:
            pass
        
    figSubplot.update_layout(height=1400, width=1400, showlegend=False, title_text="Top3 Produtos " + nome + " pelo Brasil entre 2017 - 2019")
    figSubplot.show()
    nameSave = "top3-" + nome + "-UF-2017-2019.html"
    figSubplot.write_html("Results/"+nameSave)
    

    
    

