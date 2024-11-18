from html.parser import HTMLParser 
DATASET_RELATIVE_PATH = "/home/jesusssc/Simulacion/files/datasets/datasets/trec07p/data/inmail.1"

inmail = open(DATASET_RELATIVE_PATH).read()
print(inmail)