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
    data = pd.read_csv("P2/espejoconcavo.csv")
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
                label='Distancia focal 3cm.')
    
    si5 = pd.DataFrame(data.si5)
    si5.columns = ["DistanciaImagenF5"]
    plt.scatter(s0,
                si5,
                color='r',
                label='Distancia focal 5cm.')

    # Adding axis labels
    plt.xlabel('Distancia del objeto al vértice [cm]')
    plt.ylabel('Distancia de la imagen [cm]')
    plt.title('Espejo Cóncavo')

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
    plt.title('Espejo Cóncavo')

    # Legend
    plt.legend(loc=0)
    plt.tight_layout()
    plt.grid()
    plt.show()







        # Convexo 

    # Ahora realizamos la lectura del csv usando pandas y limpiamos todos los datos de valores no numéricos con la función de pandas dropna.
    data = pd.read_csv("P2/espejoconvexo.csv")
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
                label='Distancia focal 3cm.')
    
    si5 = pd.DataFrame(data.si5)
    si5.columns = ["DistanciaImagenF5"]
    plt.scatter(s0,
                si5,
                color='r',
                label='Distancia focal 5cm.')

    # Adding axis labels
    plt.xlabel('Distancia del objeto al vértice [cm]')
    plt.ylabel('Distancia de la imagen [cm]')
    plt.title('Espejo Convexo')

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

    print("Convexo:\n",X,"\n",Y3," desv:",np.std(Y3),"\n",Y5," desv:",np.std(Y5))
    

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
    plt.title('Espejo Convexo')

    # Legend
    plt.legend(loc=0)
    plt.tight_layout()
    plt.grid()
    plt.show()



    """
    # Refracción
    # Caso A

    # Normal
    data = pd.read_csv("P1/refraccionA.csv")
    data.dropna(inplace=True)

    aire = pd.DataFrame(data.aire)
    aire.columns = ["Aire"]

    agua = pd.DataFrame(data.agua)
    agua.columns = ['Agua']

    plt.scatter(aire,
                agua,
                color='r',
                label='Dispersión de incidencia y refracción.')

    plt.xlabel('Ángulo de incidencia del Aire al Agua [°]')
    plt.ylabel('Ángulo de refracción en el Agua [°]')
    plt.title('Lecturas de ángulos entre Aire y Agua.')

    plt.legend(loc=0)
    plt.tight_layout()
    plt.grid()
    plt.show()

    # Cambio de Variable

    X = []
    Y = []
    for num in aire["Aire"]:
        X.append(math.sin(math.radians(float(num))))

    for num in agua["Agua"]:
        Y.append(math.sin(math.radians(float(num))))

    print("Caso A:\n",X,"\n",Y)


    plt.scatter(X,
                Y,
                color='r',
                label='Dispersión de incidencia y refracción.')

    plt.xlabel('Seno del ángulo de incidencia del Aire al Agua')
    plt.ylabel('Seno del ángulo de refracción en el Agua')
    plt.title('Seno de los ángulos, aplicado el cambio de variable.')


    parametros = minimosCuadrados(X,Y)

    recta = calculate(X, parametros[0], parametros[1])
    plt.plot(
        X,
        recta,
        linestyle='--',
        color='grey',
        label='Recta hallada por mínimos cuadrados\ny='+str(round(parametros[0],5))+'*x + ('+str(round(parametros[1],5))+')'
        )


    plt.legend(loc=0)
    plt.tight_layout()
    plt.grid()
    plt.show()

    # Caso B
    # Normal
    data = pd.read_csv("P1/refraccionB.csv")
    data.dropna(inplace=True)

    aire = pd.DataFrame(data.aire)
    aire.columns = ["Aire"]

    mA = pd.DataFrame(data.mysteryA)
    mA.columns = ['MysteryA']

    plt.scatter(aire,
                mA,
                color='r',
                label='Dispersión de incidencia y refracción.')

    plt.xlabel('Ángulo de incidencia del Aire a la Sustancia Misteriosa A [°]')
    plt.ylabel('Ángulo de refracción en la Sustancia Misteriosa A [°]')
    plt.title('Lecturas de ángulos entre Aire y Sustancia Misteriosa A.')

    plt.legend(loc=0)
    plt.tight_layout()
    plt.grid()
    plt.show()

    # Cambio de Variable

    X = []
    Y = []
    for num in aire["Aire"]:
        X.append(math.sin(math.radians(float(num))))

    for num in mA["MysteryA"]:
        Y.append(math.sin(math.radians(float(num))))

    print("Caso B:\n",X,"\n",Y)
    plt.scatter(X,
                Y,
                color='r',
                label='Dispersión de incidencia y refracción.')

    plt.xlabel(
        'Seno del ángulo de incidencia del Aire a la Sustancia Misteriosa A')
    plt.ylabel('Seno del ángulo de refracción en la Sustancia Misteriosa A')
    plt.title('Seno de los ángulos, aplicado el cambio de variable.')

    parametros = minimosCuadrados(X,Y)

    recta = calculate(X, parametros[0], parametros[1])
    plt.plot(
        X,
        recta,
        linestyle='--',
        color='grey',
        label='Recta hallada por mínimos cuadrados\ny='+str(round(parametros[0],5))+'*x + ('+str(round(parametros[1],5))+')'
        )

    plt.legend(loc=0)
    plt.tight_layout()
    plt.grid()
    plt.show()



# Caso C
    # Normal
    data = pd.read_csv("P1/refraccionC.csv")
    data.dropna(inplace=True)

    vidrio = pd.DataFrame(data.vidrio)
    vidrio.columns = ["Vidrio"]

    mB = pd.DataFrame(data.mysteryB)
    mB.columns = ['MysteryB']

    plt.scatter(vidrio,
                mB,
                color='r',
                label='Dispersión de incidencia y refracción.')

    plt.xlabel('Ángulo de incidencia del Vidrio a la Sustancia Misteriosa B [°]')
    plt.ylabel('Ángulo de refracción en la Sustancia Misteriosa B [°]')
    plt.title('Lecturas de ángulos entre Vidrio y Sustancia Misteriosa B.')

    plt.legend(loc=0)
    plt.tight_layout()
    plt.grid()
    plt.show()

    # Cambio de Variable

    X = []
    Y = []
    for num in vidrio["Vidrio"]:
        X.append(math.sin(math.radians(float(num))))

    for num in mB["MysteryB"]:
        Y.append(math.sin(math.radians(float(num))))

    print("Caso C:\n",X,"\n",Y)
    plt.scatter(X,
                Y,
                color='r',
                label='Dispersión de incidencia y refracción.')

    plt.xlabel(
        'Seno del ángulo de incidencia del Vidrio a la Sustancia Misteriosa B')
    plt.ylabel('Seno del ángulo de refracción en la Sustancia Misteriosa B')
    plt.title('Seno de los ángulos, aplicado el cambio de variable.')

    parametros = minimosCuadrados(X,Y)

    recta = calculate(X, parametros[0], parametros[1])
    plt.plot(
        X,
        recta,
        linestyle='--',
        color='grey',
        label='Recta hallada por mínimos cuadrados\ny='+str(round(parametros[0],5))+'*x + ('+str(round(parametros[1],5))+')'
        )

    plt.legend(loc=0)
    plt.tight_layout()
    plt.grid()
    plt.show()


    """
    return
