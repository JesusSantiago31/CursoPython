### VISULAIZACION DE DATOS
print("Visualizacion de datos \n\n")
DATASET_RELATIVE_PATH = "/home/jesusssc/Simulacion/files/datasets/datasets/trec07p/data/inmail.1"
DATASET_FULL_INDEX_PATH = "/home/jesusssc/Simulacion/files/datasets/datasets/trec07p/full/index"

DATASET_PATH = "/home/jesusssc/Simulacion/files/datasets/datasets/NSL-KDD/KDDTrain+.txt"
LISTDIR_PATH ="/home/jesusssc/Simulacion/files/datasets/datasets/NSL-KDD"
LOAD_KDD = "/home/jesusssc/Simulacion/files/datasets/datasets/NSL-KDD/KDDTrain+.arff"
# Lectura del DataSet mediante funciones de Python
with open(DATASET_PATH) as train_set:
    df = train_set.readlines()

import pandas as pd
df = pd.read_csv(DATASET_PATH)
df

import os # Acceder al Sistema Operativo
print(" Accediendo a los Archivos \n\n")
print(os.listdir(LISTDIR_PATH))

# Lectura del DataSet que se encuentra en formato .arff
import arff

with open(LOAD_KDD, 'r') as train_set: # 'r' significa que es de lectura
    df = arff.load(train_set)
print("DATAFRAME KEYS\n\n")
print(df.keys())

# Parsear los atributos y obtener únicamente los nombres
atributos = [attr[0] for attr in df['attributes']] 
print("ATRIBUTOS")
print(atributos)

# Leer el DataSet con Pandas y facilitar su manipulación 
df = pd.DataFrame(df["data"], columns = atributos)
df

# Todo lo que se hizo anteriormente se hace en este segmento de código
def load_kdd_dataset(data_path):
    """"Lectura del Dataset NSL-KDD.""" # Esto si se muestra al usuario
    with open(data_path, 'r') as train_set: #Esto es una estructura de control
        dataset = arff.load(train_set) # Aquí se cargan los datos
    attributes = [attr[0] for attr in dataset['attributes']]
    return pd.DataFrame(dataset['data'], columns = attributes)

# Muestra el resultado de la función 
load_kdd_dataset(LOAD_KDD)

# Mostrar la información básica sobre el DataSet
df.info()

# Mostrar las funciones estadísticas sobre el DataSet
df.describe()
print(df.describe())

# Mostrar los valores únicos que tiene un atributo determinado
print(df["protocol_type"].value_counts())

print(df["class"].value_counts())

# Mostrar los valores de las características como un histograma
# %matplotlib inline
import matplotlib.pyplot as plt
df["protocol_type"].hist()