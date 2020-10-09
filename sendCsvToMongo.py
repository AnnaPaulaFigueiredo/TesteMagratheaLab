from pymongo import MongoClient


def exp(myDb):

    exp = myDb["EXP_FORMATO_TESTE"]

    csv = open("Data/Out/EXP_FORMATO_TESTE.csv", 'r')

    line = csv.readline()
    line = csv.readline()

    while line:
        
        values = line.split(";")
        data = {}
        try:
            data["CO_ANO"] = int(values[0])
        except:
            data["CO_ANO"] = None

        try:
            data["CO_MES"] = int(values[1])
        except:
            data["CO_MES"] = None

        try:
            data["CO_NCM"] = int(values[2])
        except:
            data["CO_NCM"] = None
        
        try:
            data["SG_UF_NCM"] = values[3]
        except:
            data["SG_UF_NCM"] = None
        
        try:
            data["KG_LIQUIDO"] = int(values[4])
        except:
            data["KG_LIQUIDO"] = None

        try:
            data["VL_FOB"] = int(values[5])
        except:
            data["VL_FOB"] = None


        exp.insert_one(data)
        line = csv.readline()

def ncm(myDb):

    ncm = myDb["NCM_FORMATO_TESTE"]
    csv = open("Data/Out/NCM_FORMATO_TESTE.csv", 'r')

    line = csv.readline()
    line = csv.readline()

    # validou as posicões e inseriu no bd
    
    while line:
        
        values = line.split(";")
        data = {}

        try:
            data["CO_NCM"] = int(values[0])            
        except :
            data["CO_NCM"] = None            
            
        try:
            data["NO_NCM_POR"] = values[1]            
        except :
            data["NO_NCM_POR"] = None            
        
        try:
            data["NO_NCM_ING"] = values[2]            
        except :
            data["NO_NCM_ING"] = None  


        
        # comando de inserção no banco mesmo
        ncm.insert_one(data)
        line = csv.readline()

def imp(myDb):
    
    imp = myDb["IMP_FORMATO_TESTE"]
    csv = open("Data/Out/IMP_FORMATO_TESTE.csv", 'r')

    line = csv.readline()
    line = csv.readline()

    while line:
    
        values = line.split(";")
        data = {}
        try:
            data["CO_ANO"] = int(values[0])
        except:
            data["CO_ANO"] = None

        try:
            data["CO_MES"] = int(values[1])
        except:
            data["CO_MES"] = None

        try:
            data["CO_NCM"] = int(values[2])
        except:
            data["CO_NCM"] = None
        
        try:
            data["SG_UF_NCM"] = values[3]
        except:
            data["SG_UF_NCM"] = None
        
        try:
            data["KG_LIQUIDO"] = int(values[4])
        except:
            data["KG_LIQUIDO"] = None

        try:
            data["VL_FOB"] = int(values[5])
        except:
            data["VL_FOB"] = None

        imp.insert_one(data)
        line = csv.readline()

def enviarMongo():

    print("Enviando para o MongoDb...")
    client = MongoClient('localhost', 27017)
    myDb = client["MagratheaLabs"]
    
    print("EXP")
    exp(myDb)
    
    print("NCM")
    ncm(myDb)
    
    print("IMP")
    imp(myDb)
    
    print("DONE.")

