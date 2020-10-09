# Análise da Importação e Exportação no Brasil

O produto tem como objetivo analisar a base de dados públicos disponibilizados pelo governo, referentes ao volume de importações e exportações do país. Extraindo as seguintes informações:

- Top3 produtos exportados/importados por Estado(UF) nos anos de 2017, 2018 e 2019.
- Top3 produtos exportados/importados por mês e Estado(UF) no ano de 2019.
- Representatividade do valor de exportação/importação em relaçao ao total do país no ano de 2019.

## Links para acesso às bases utilizadas

[Layout dos Dados](http://www.mdic.gov.br/index.php/comercio-exterior/estatisticas-de-comercio-exterior/base-de-dados-do-comercio-exterior-brasileiro-arquivos-para-download)

[Base Exportação](http://www.mdic.gov.br/balanca/bd/comexstat-bd/ncm/EXP_COMPLETA.zip)

[Base Importação](http://www.mdic.gov.br/balanca/bd/comexstat-bd/ncm/IMP_COMPLETA.zip)

[Base Ncm](http://www.mdic.gov.br/balanca/bd/tabelas/NCM.csv)


## Construído com

- Python 3.8.5
- MongoDb 
- Linux Manjaro 3.8.5

### Passos para a execução
  
  1. Instale o Python e suas Bibliotecas
  
  * [Python](https://www.python.org/downloads/)
  
  * [Pandas](https://pandas.pydata.org/getting_started.html)
  
  * [Plotly](https://pypi.org/project/plotly/)
    
  * [Pymongo](https://pypi.org/project/pymongo/)
  
  2. Instale o docker
  
  * [Docker](https://docs.docker.com/get-docker/)
  
  * * 2.1 Inicialize o docker
  
  * * 2.2 Instale o mongo via docker 
  
  * * 2.3 Inicialize mongo
  
  3. Faça o dowload das bases de dados 
  
  * [Base Exportação](http://www.mdic.gov.br/balanca/bd/comexstat-bd/ncm/EXP_COMPLETA.zip)

  * [Base Importação](http://www.mdic.gov.br/balanca/bd/comexstat-bd/ncm/IMP_COMPLETA.zip)

  * [Base Ncm](http://www.mdic.gov.br/balanca/bd/tabelas/NCM.csv)
  
  * * 3.1 Transfira os arquivos para a pasta Data -> In 
  
  4.  Abra o terminal na pasta baixada pelo GIT e digite o comando:
  
  ```python main.py ```



## Fases do Projeto

### Carregamento e Transformação dos Dados

- Foram carregadas as bases .csv utilizando a biblioteca pandas do python.
- Análise primária da estrutura da base em relação às colunas necessárias, elementos null, elementos incondizentes: por exemplo, estados não definidos.
- Filtragem dos anos e colunas necessárias.
- Salvou em novos .csv na pasta Data -> Out
- Carregamento dos dados já filtrados utilizando o banco de dados não relacional MongoDb.
- Foi realizado querys para fazer a busca no banco de dados.
- O dataset de importação e exportação foram cruzados com o ncm, para buscar o nome do produto.
- Operações de limpeza para as strings foram efetuadas.

### Visualização

- Os dados foram pesquisados no MongoDb.
- A filtragem dos dados para gerar os dashboards foram feitas também através do pandas.
- Para gerar os dashboards foi utilizado a biblioteca plotly.
- Foi então foram disponibilizadas as informações nos dashboards interativos. 
