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
    """
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
    
    parametros4 = minimosCuadrados(X,Y5)

    recta = calculate(X, parametros4[0], parametros4[1])
    plt.plot(
        X,
        recta,
        linestyle='--',
        color='darkblue',
        label='Recta hallada por mínimos cuadrados para una distancia focal de 5cm\ny='+str(round(parametros4[0],5))+'*x + ('+str(round(parametros4[1],5))+')'
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

    """

    #######################################
    ######## Lentes Divergentes 
    # Ahora realizamos la lectura del csv usando pandas y limpiamos todos los datos de valores no numéricos con la función de pandas dropna.
    data = pd.read_csv("P3/lentedivergente.csv")
    data.dropna(inplace=True)

    # Luego, asignamos los datos de cada columna a una variable.
    s0 = pd.DataFrame(data.s0)
    s0.columns = ['DistanciaObjeto']
    h0 = pd.DataFrame(data.h0)
    h0.columns = ['TamañoObjeto']

    si2 = pd.DataFrame(data.si2)
    si2.columns = ["DistanciaImagen2"]
    hi2 = pd.DataFrame(data.hi2)
    hi2.columns = ['TamañoImagen2']

    si4 = pd.DataFrame(data.si4)
    si4.columns = ["DistanciaImagen4"]
    hi4 = pd.DataFrame(data.hi4)
    hi4.columns = ['TamañoImagen4']

    # Grafica
    plt.style.use('ggplot')
    plt.scatter(s0,
                si2,
                color='orange',
                label='Distancia focal 2cm.')
    plt.scatter(s0,
                si4,
                color='r',
                label='Distancia focal 4cm.')

    # Adding axis labels
    plt.xlabel('Distancia del objeto al lente [cm]')
    plt.ylabel('Distancia de la imagen [cm]')
    plt.title('Lente divergente')

    # Legend
    plt.legend(loc=0)
    plt.tight_layout()
    plt.grid()
    plt.show()


    # Cambio de Variable 
    
    X = []
    Y2 = []
    Y4 = []
    for num in s0["DistanciaObjeto"]:
        X.append(1/num)

    for num in si2["DistanciaImagen2"]:
        Y2.append(1/num)

    for num in si4["DistanciaImagen4"]:
        Y4.append(1/num)

    print("Divergente:\n",X,"\n",Y2," desv:",np.std(Y2),"\n",Y4," desv:",np.std(Y4))




    plt.scatter(X,
                Y2,
                color='orange',
                label='Inverso de distancia focal 2cm.')
    plt.scatter(X,
                Y4,
                color='r',
                label='Inverso de distancia focal 4cm.')

    
    parametros2 = minimosCuadrados(X,Y2)

    recta = calculate(X, parametros2[0], parametros2[1])
    plt.plot(
        X,
        recta,
        linestyle='--',
        color='lightblue',
        label='Recta hallada por mínimos cuadrados para una distancia focal de 2cm\ny='+str(round(parametros2[0],5))+'*x + ('+str(round(parametros2[1],5))+')'
        )
    
    parametros4 = minimosCuadrados(X,Y4)

    recta = calculate(X, parametros4[0], parametros4[1])
    plt.plot(
        X,
        recta,
        linestyle='--',
        color='darkblue',
        label='Recta hallada por mínimos cuadrados para una distancia focal de 4cm\ny='+str(round(parametros4[0],5))+'*x + ('+str(round(parametros4[1],5))+')'
        )

    # Adding axis labels
    plt.xlabel('Inverso de distancia del objeto al lente [cm ^-1]')
    plt.ylabel('Inverso de distancia de la imagen [cm ^-1]')
    plt.title('Lente Divergente')

    # Legend
    plt.legend(loc=0)
    plt.tight_layout()
    plt.grid()
    plt.show()


    return
