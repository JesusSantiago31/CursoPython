# Script convertido desde un cuaderno de Jupyter

# Importar bibliotecas necesarias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, recall_score, f1_score, precision_score
from pandas import DataFrame
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from graphviz import Source
from sklearn.tree import export_graphviz
import os
import warnings
warnings.filterwarnings('ignore')


# Android adware and general malware dataset (CIC-AAGM2017)
#print("# Android adware and general malware dataset (CIC-AAGM2017) \n")

# Imports
#print("## Imports\n")

# Funciones Auxiliares
#print("## Funciones Auxiliares\n")

def train_val_test_split(df, rstate=42, shuffle=True, stratify=None):
    strat = df[stratify] if stratify else None
    train_set, test_set = train_test_split(
        df, test_size=0.4, random_state=rstate, shuffle=shuffle, stratify=strat)
    strat = test_set[stratify] if stratify else None
    val_set, test_set = train_test_split(
        test_set, test_size=0.5, random_state=rstate, shuffle=shuffle, stratify=strat)
    return (train_set, val_set, test_set)

# Remover etiquetas
def remove_labels(df, label_name):
    X = df.drop(label_name, axis=1)
    y = df[label_name].copy()
    return (X, y)

def evaluate_result(y_pred, y, y_prep_pred, y_prep, metric):
    print(metric.__name__, "WITHOUT preparation:", metric(y_pred, y, average='weighted'))
    print("_________________________________________________________________________________________________________________________________________________________________")
    print(metric.__name__, "WITH preparation:", metric(y_prep_pred, y_prep, average='weighted'))
    print("_________________________________________________________________________________________________________________________________________________________________")

#print("### 1.- Lectura del Dataset\n")
df = pd.read_csv('datasets/datasets/TotalFeatures-ISCXFlowMeter.csv')

#print("### 2.- Visualizar los datos\n")
#print("#### Buscando Correlaciones\n")
#print(df.head(10))
#df.head(10)
#df.info()
#print(df['calss'].value_counts())

# Copiar el DataSet y transformar la variable de salida a numérica para calcular las correlaciones
X = df.copy()
X['calss'] = X['calss'].factorize()[0]
corr_matrix = X.corr()
#print(corr_matrix['calss'].sort_values(ascending=False))
#print(X.corr())
X.corr()

# Se puede llegar a valorar y quedarse con aquellas que tengan mayor correlacion 
corr_matrix[corr_matrix["calss"]> 0.05]
#print(corr_matrix[corr_matrix["calss"]> 0.05])

#print("# 3.- División del DataSet")
train_set, val_set, test_set = train_val_test_split(X)
X_train, y_train = remove_labels(train_set, 'calss')
X_val, y_val = remove_labels(val_set, 'calss')
X_test, y_test = remove_labels(test_set, 'calss')

#print("## 4.- Escalar el DataSet")
scaler = RobustScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
X_val_scaled = scaler.fit_transform(X_val)

# Transformar un DataFrame de pandas
X_train_scaled = DataFrame(X_train_scaled, columns=X_train.columns, index=X_train.index)
#print(X_train_scaled.head(10))

#print(X_train_scaled.describe())

#print("## 5.- Árbol de Decisión")
MAX_DEPTH = 20
clf_tree = DecisionTreeClassifier(max_depth=MAX_DEPTH, random_state=42)
clf_tree.fit(X_train, y_train)

#print(clf_tree.fit(X_train, y_train))
clf_tree_scaled = DecisionTreeClassifier(max_depth=MAX_DEPTH, random_state=42)
clf_tree_scaled.fit(X_train_scaled, y_train)
#print(clf_tree_scaled.fit(X_train_scaled, y_train))

y_train_pred = clf_tree.predict(X_train)
y_train_prep_pred = clf_tree_scaled.predict(X_train_scaled)
evaluate_result(y_train_pred, y_train, y_train_prep_pred, y_train, f1_score)

# Predecir el dataset de validación
y_pred = clf_tree.predict(X_val)
y_pred_prep = clf_tree_scaled.predict(X_val_scaled)
evaluate_result(y_pred, y_val, y_pred_prep, y_val, f1_score)


#print("# 6.- Visualizando el límite de decisión")
X_train_reduced = X_train[['min_flowpktl', 'flow_fin']]
clf_tree_reduced = DecisionTreeClassifier(max_depth=2, random_state=42)
clf_tree_reduced.fit(X_train_reduced, y_train)
#print(clf_tree_reduced.fit(X_train_reduced, y_train))

def plot_decision_boundary(clf, X, y, plot_training=True, resolution=1000):
    mins = X.min(axis=0) - 1
    maxs = X.max(axis=0) + 1
    x1, x2 = np.meshgrid(
        np.linspace(mins[0], maxs[0], resolution),
        np.linspace(mins[1], maxs[1], resolution))
    X_new = np.c_[x1.ravel(), x2.ravel()]
    y_pred = clf.predict(X_new).reshape(x1.shape)
    custom_cmap = ListedColormap(['#fafab0', '#9898ff', '#a0faa0'])
    plt.contourf(x1, x2, y_pred, alpha=0.3, cmap=custom_cmap)
    custom_cmap2 = ListedColormap(['#7d7d58', '#4c4c7f', '#507d50'])
    plt.contour(x1, x2, y_pred, cmap=custom_cmap2, alpha=0.8)
    if plot_training:
        plt.plot(X[:, 0][y == 0], X[:, 1][y == 0], "yo", label="normal")
        plt.plot(X[:, 0][y == 1], X[:, 1][y == 1], "bs", label="adware")
        plt.plot(X[:, 0][y == 2], X[:, 1][y == 2], "g^", label="malware")
        plt.axis([mins[0], maxs[0], mins[1], maxs[1]])
    plt.xlabel('min_flowpktl', fontsize=14)
    plt.ylabel('flow_fin', fontsize=14, rotation=90)

# Guardar el gráfico del límite de decisión
plt.figure(figsize=(12, 6))
plot_decision_boundary(clf_tree_reduced, X_train_reduced.values, y_train)
decision_boundary_path = os.path.join('graph1.png')
plt.savefig(decision_boundary_path)
plt.close()  # Cerrar la figura para liberar memoria
#print(f"Gráfica de límite de decisión guardada en: {decision_boundary_path}")

# Pintamos el árbol para compararlo con la representación gráfica anterior
dot_file = os.path.join("android_malware.dot")
png_file = os.path.join("graph2")

export_graphviz(
    clf_tree_reduced,
    out_file=dot_file,
    feature_names=X_train_reduced.columns,
    class_names=["benign", "adware", "malware"],
    rounded=True,
    filled=True
)

# Renderizar el archivo DOT a PNG
Source.from_file(dot_file).render(filename=png_file, format='png', cleanup=True)
#print(f"Representación del árbol guardada en: {png_file}.png")
