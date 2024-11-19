# REGRESION LOGÍSTICA 

# En esta fase se facilita el preprocesamiento de correos electrónicos que poseen código HTML.
print("\nLogistic Regression\n\n ")
from html.parser import HTMLParser 
DATASET_RELATIVE_PATH = "/home/jesusssc/Simulacion/files/datasets/datasets/trec07p/data/inmail.1"
DATASET_FULL_INDEX_PATH = "/home/jesusssc/Simulacion/files/datasets/datasets/trec07p/full/index"
DATASET_PATH = "/home/jesusssc/Simulacion/files/datasets/datasets/trec07p"

# Se crea el constructor
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = [] # Ingerir los datos
    
    def handle_data(self, d): # Maneja los datos
        self.fed.append(d)


    def get_data(self):
        return ''.join(self.fed)
        
# Esta función se encarga de eliminar los tags HTML que se encuentren en el texto de los correos electrónicos
def strip_tags(html):
    s = MLStripper()
    s.feed(html) # Alimentar el html
    return s.get_data()

# Ejemplo de eliminación de los tags HTML de un texto
t = '<tr><td align="left"><ahref="../../issues/51/16.html#article">Phrack World News </a><td>'
strip_tags(t)

import email
import string
import nltk

class Parser:

    def __init__(self):
        self.stemmer = nltk.PorterStemmer()
        self.stopwords = set(nltk.corpus.stopwords.words('english'))
        self.punctuation = list(string.punctuation)

    def parse(self, email_path):
        """Parse an email."""
        with open(email_path, errors = 'ignore') as e:
            msg = email.message_from_file(e)
        return None if not msg else self.get_email_content(msg)

    def get_email_content(self, msg):
        """Extract the email content."""
        subject = self.tokenize(msg['Subject'])if msg['Subject'] else []
        body = self.get_email_body(msg.get_payload(),
                                   msg.get_content_type())
        content_type = msg.get_content_type()
        # Return the content of the email
        return{"subject": subject,
              "body": body,
              "content_type": content_type}

    def get_email_body(self, payload, content_type):
        """Extract the body of the email."""
        body = []
        if type(payload) is str and content_type == 'text/plain':
            return self.tokenize(payload)
        elif type(payload) is str and content_type == 'text/html':
            return self.tokenize(strip_tags(payload))
        elif type(payload) is list:
            for p in payload:
                body += self.get_email_body(p.get_payload(),
                                           p.get_content_type())
        return body

    def tokenize(self, text):
        """Transform a text string in tokens. Perform two main actions, clean the punctuation symbols and do stemming of the text"""
        for c in self.punctuation:
            text = text.replace(c, "")

        text = text.replace("\t"," ")
        text = text.replace("\n"," ")
        tokens = list(filter(None, text.split(" ")))
        # Stemming of the tokens
        return [self.stemmer.stem(w) for w in tokens if w not in self.stopwords]

inmail = open(DATASET_RELATIVE_PATH).read()
print(" \nCORREO ELECTRÓNICO .RAW \n")
print(inmail)

#/home/jesusssc/Simulacion/files/datasets/datasets/trec07p/data/inmail.1
#files/datasets/datasets/trec07p/data/inmail.1

# Parsing del correo electrónico

p = Parser()
print("\nPARSING DEL CORREO ELECTRÓNICO \n\n")
print(p.parse(DATASET_RELATIVE_PATH))

# Lectura de indices

index = open(DATASET_FULL_INDEX_PATH ).readlines()

import os



def parse_index(path_to_index, n_elements): #Acceder a la ruta
    ret_indexes = []
    index = open(path_to_index).readlines()
    for i in range(n_elements):
        mail = index[i].split("../")#Especificar que es una ruta
        label = mail[0]
        path = mail [1][:-1] #Evitamos el desbordamiento, evitando el salto
        ret_indexes.append({"label": label, "email_path": os.path.join(DATASET_PATH, path)})# Señalamos la dirección de el dataset

    return ret_indexes

def parse_email(index):
    p = Parser()
    pmail = p.parse(index["email_path"])
    return pmail, index["label"]

indexes = parse_index(DATASET_FULL_INDEX_PATH,10)
print("\n\n         INDEXES \n\n")
print(indexes)

# Cargar el índice y las etiquetas en memoria
index = parse_index(DATASET_FULL_INDEX_PATH, 1)

# Leemos el primer correo
import os
open(index[0]["email_path"]).read()

# Parsear el primer correo
mail, label = parse_email(index[0])
print("\n\n         CLASIFICACION \n")
print("El correo es: ", label ," \n")
print(mail)

from sklearn.feature_extraction.text import CountVectorizer

# Preparación del email en una cadena de texto
prep_email = [" ".join(mail['subject']) + " ".join(mail['body'])]

vectorizer = CountVectorizer()
X = vectorizer.fit(prep_email)

print("\n\n e-mail: ", prep_email, "\n")
print("Caracteristicas de entrada: ", vectorizer.get_feature_names_out(), "\n")

X = vectorizer.transform(prep_email)
print("\n Values: \n", X.toarray() )

from sklearn.preprocessing import OneHotEncoder

prep_email = [[w] for w in mail ['subject'] + mail['body']]
enc = OneHotEncoder(handle_unknown = 'ignore')
X = enc.fit_transform(prep_email)


print("\n\n Features: ", enc.get_feature_names_out(), "\n")
print("\n  Values:  \n", X.toarray())

## Funciones auxiliares para el preprocesamiento del DataSet

def create_prep_dataset(index_path, n_elements):
    X = []
    y = []
    indexes = parse_index(index_path, n_elements)
    for i in range(n_elements):
        print("\r Parsing email: {0} ". format(i+1), end = '')
        mail, label = parse_email(indexes[i])
        X.append(" ".join(['subject']) + " ".join(mail['body']))
        y.append(label)
    return X,y

# Leer únicamente un subconjunto de 1000 correos electrónicos

X_train, y_train = create_prep_dataset(DATASET_FULL_INDEX_PATH, 1000)
X_train

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)

print(X_train.toarray())
print("\n Features ", len(vectorizer.get_feature_names_out()))

import pandas as pd 
pd.DataFrame(X_train.toarray(), columns=[vectorizer.get_feature_names_out()])

y_train

from sklearn.linear_model import LogisticRegression
#classification
clf = LogisticRegression()
clf.fit(X_train, y_train)

## Prediccion
# Lectura de un DataSet (DS) de correos nuevos

# Leer 1500 correos de nuestro DataSet y quedarnos unicamente con los 500 ultimos
# correos electrónicos, los cuales no se han utilizado para entrenar el algoritmo

X, y = create_prep_dataset(DATASET_FULL_INDEX_PATH, 150)
X_test = X [100:]
y_test = y [100:]

X_test = vectorizer.transform(X_test)

y_pred = clf.predict (X_test)
y_pred

print (" Predicción \n ", y_pred)
print (" \nEtiquetas reales", y_test)

from sklearn.metrics import accuracy_score
print ("Accuracy: {:.3f}".format(accuracy_score(y_test, y_pred)))

## Aumentando el DataSet
# Leer 20,000 correos electrónicos 
X, y = create_prep_dataset(DATASET_FULL_INDEX_PATH, 20000)

# Utilizamos 15,000 correos para entrenar el algoritmo y 5,000 para realizar pruebas
X_train, y_train = X[:15000], y[:15000]
X_test, y_test = X[15000:], y[15000:]

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)

clf = LogisticRegression()
clf.fit(X_train, y_train)

X_test = vectorizer.transform(X_test)
y_pred = clf.predict(X_test)

from sklearn.metrics import accuracy_score
print ("Accuracy: {:.3f}".format(accuracy_score(y_test, y_pred)))