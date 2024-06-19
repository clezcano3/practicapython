import pandas as pd
from generators.generadorDecibelios import generarDatosRuidos

def construirDataRuido():
    datosRuidos = generarDatosRuidos()
    ruidoDataFrame= pd.DataFrame(datosRuidos,columns=["id","nivel","ruido","comuna"])
    ruidoDataFrame.to_csv('ruidos.csv',index=False)


construirDataRuido()