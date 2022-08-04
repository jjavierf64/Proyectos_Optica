import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import re
#primero se importan las librerias que se van a necesitar para realizar el codigo.

#Ahora realizamos la lectura del csv usando pandas y limpiamos todos los datos de valores no numéricos con la función de pandas dropna.
data = pd.read_csv("reflexion.csv")
data.dropna(inplace=True)

#Luego, asignamos los datos de cada columna a una variable.
anguloI=pd.DataFrame(data.anguloI)
anguloI.columns = ['ÁnguloI']
anguloRX=pd.DataFrame(data.anguloRX)
anguloRX.columns=["ÁnguloRX"]
plt.style.use('ggplot')
plt.scatter(anguloI,anguloRX,color= 'r',label='Dispersión de incidencia y reflexión.')

# Adding axis labels
plt.xlabel('Ángulo de incidencia [°]')
plt.ylabel('Ángulo de reflexión [°]')
plt.title('Lecturas de ángulos.')

#Legend
plt.legend(loc=0)
plt.tight_layout()
plt.grid()
plt.show()
