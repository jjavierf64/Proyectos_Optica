import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import re
from minimosCuadrados import minimosCuadrados

# primero se importan las librerias que se van a necesitar para realizar el codigo.


def calculate(data_x,k,b):
    datay=[]
    for x in data_x:
        datay.append(k*x+b)
    return datay



def run():

    # Cóncavo 
    # Ahora realizamos la lectura del csv usando pandas y limpiamos todos los datos de valores no numéricos con la función de pandas dropna.
    data = pd.read_csv("P3/lenteconvergente.csv")
    data.dropna(inplace=True)

    # Luego, asignamos los datos de cada columna a una variable.
    s0 = pd.DataFrame(data.s0)
    s0.columns = ['DistanciaObjeto']
    si3 = pd.DataFrame(data.si3)
    si3.columns = ["DistanciaImagenF3"]
    plt.style.use('ggplot')
    plt.scatter(s0,
                si3,
                color='orange',
                label='Distancia focal 4cm.')
    
    si5 = pd.DataFrame(data.si5)
    si5.columns = ["DistanciaImagenF5"]
    plt.scatter(s0,
                si5,
                color='r',
                label='Distancia focal 5cm.')

    # Adding axis labels
    plt.xlabel('Distancia del objeto al vértice [cm]')
    plt.ylabel('Distancia de la imagen [cm]')
    plt.title('Lente convergente')

    # Legend
    plt.legend(loc=0)
    plt.tight_layout()
    plt.grid()
    plt.show()


    # Cambio de Variable 
    
    X = []
    Y3 = []
    Y5 = []
    for num in s0["DistanciaObjeto"]:
        X.append(1/num)

    for num in si3["DistanciaImagenF3"]:
        Y3.append(1/num)

    for num in si5["DistanciaImagenF5"]:
        Y5.append(1/num)

    print("Cóncavo:\n",X,"\n",Y3," desv:",np.std(Y3),"\n",Y5," desv:",np.std(Y5))




    plt.scatter(X,
                Y3,
                color='orange',
                label='Inverso de distancia focal 3cm.')
    plt.scatter(X,
                Y5,
                color='r',
                label='Inverso de distancia focal 5cm.')

    
    parametros3 = minimosCuadrados(X,Y3)

    recta = calculate(X, parametros3[0], parametros3[1])
    plt.plot(
        X,
        recta,
        linestyle='--',
        color='lightblue',
        label='Recta hallada por mínimos cuadrados para una distancia focal de 3cm\ny='+str(round(parametros3[0],5))+'*x + ('+str(round(parametros3[1],5))+')'
        )
    
    parametros5 = minimosCuadrados(X,Y5)

    recta = calculate(X, parametros5[0], parametros5[1])
    plt.plot(
        X,
        recta,
        linestyle='--',
        color='darkblue',
        label='Recta hallada por mínimos cuadrados para una distancia focal de 5cm\ny='+str(round(parametros5[0],5))+'*x + ('+str(round(parametros5[1],5))+')'
        )

    # Adding axis labels
    plt.xlabel('Inverso de distancia del objeto al vértice [cm ^-1]')
    plt.ylabel('Inverso de distancia de la imagen [cm ^-1]')
    plt.title('Lente Convergente')

    # Legend
    plt.legend(loc=0)
    plt.tight_layout()
    plt.grid()
    plt.show()
    return
