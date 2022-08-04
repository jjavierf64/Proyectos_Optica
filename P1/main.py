import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import re
# primero se importan las librerias que se van a necesitar para realizar el codigo.


def run():

    # Ahora realizamos la lectura del csv usando pandas y limpiamos todos los datos de valores no numéricos con la función de pandas dropna.
    data = pd.read_csv("P1/reflexion.csv")
    data.dropna(inplace=True)

    # Luego, asignamos los datos de cada columna a una variable.
    anguloI = pd.DataFrame(data.anguloI)
    anguloI.columns = ['ÁnguloI']
    anguloRX = pd.DataFrame(data.anguloRX)
    anguloRX.columns = ["ÁnguloRX"]
    plt.style.use('ggplot')
    plt.scatter(anguloI,
                anguloRX,
                color='r',
                label='Dispersión de incidencia y reflexión.')

    # Adding axis labels
    plt.xlabel('Ángulo de incidencia [°]')
    plt.ylabel('Ángulo de reflexión [°]')
    plt.title('Lecturas de ángulos.')

    # Legend
    plt.legend(loc=0)
    plt.tight_layout()
    plt.grid()
    plt.show()

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

    plt.legend(loc=0)
    plt.tight_layout()
    plt.grid()
    plt.show()



    return
