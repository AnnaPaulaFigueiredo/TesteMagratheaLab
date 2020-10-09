from pymongo import ASCENDING, MongoClient
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def gerarEstadoEmRelacaoTotPais(dataBase, nome, cor):
    
        query = {"CO_ANO": 2019}
        filtroAno = list(dataBase.find(query, {"SG_UF_NCM": 1, "VL_FOB": 1}))
        df = pd.DataFrame(filtroAno)

        
        # QUNTIDADE EXP POR ESTADO 2019
        estados = list(df.SG_UF_NCM.unique())

    
        relacaoDolarUF = df.groupby(by="SG_UF_NCM")["VL_FOB"].sum()
   
        uf = relacaoDolarUF.index
        valorDolarUF = relacaoDolarUF.values
        
        titulo = "Representatividade Total de " + nome +" por Estado no Ano de 2019"      

        data = {
            "UF": uf,
            "Valor US$": valorDolarUF
        }
        
        fig = px.pie(data, names="UF", values="Valor US$", title=titulo, color_discrete_sequence=cor)
        fig.update_traces(textposition='inside', textinfo='percent+label')

        fig.show()

        nameSave = "representatividade-" + nome + "dolar-UF-2019.html"
        fig.write_html("Results/"+nameSave)