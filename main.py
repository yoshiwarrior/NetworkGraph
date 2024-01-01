# This is a sample Python script.
from pyvis.network import Network
import pandas as pd


if __name__ == '__main__':
    net = Network(notebook=True, cdn_resources="remote", select_menu=True, filter_menu=True)
    df = pd.read_csv('list.CSV', sep=';')
    df["Parent Node"].fillna("leer", inplace=True)
    parent = df['Parent Node']
    count = 0
    for x in df['Name']:
        net.add_node(x, title = "Unterprgramm von " + parent[count])
        if parent[count] == "leer":
            count += 1
            continue
        else:
            net.add_edge(x, parent[count])
            count += 1
    net.show('test.html')


