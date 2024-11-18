from html.parser import HTMLParser 
DATASET_RELATIVE_PATH = "/home/jesusssc/Simulacion/files/datasets/datasets/trec07p/data/inmail.1"
DATASET_FULL_INDEX_PATH = "/home/jesusssc/Simulacion/files/datasets/datasets/trec07p/full/index"
DATASET_PATH = "/home/jesusssc/Simulacion/files/datasets/datasets/trec07p"

p = Parser()
p.parse(DATASET_RELATIVE_PATH)
print(p)