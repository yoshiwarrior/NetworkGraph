# This is a sample Python script.
from pyvis.network import Network
import pandas as pd


if __name__ == '__main__':
    net = Network(notebook=True, cdn_resources="remote", select_menu=True, filter_menu=True)                    #Graph initialisieren
    df = pd.read_csv('list.CSV', sep=';')                                                         #CSV-Datei wird ausgelesen
    df["Parent Node"].fillna("leer", inplace=True)                                                              #Leere Felder werden gefüllt

    nameList = df['Name']                                                                                       #Zugriff auf Spalten
    parentList = df['Parent Node']
    indexList = df['Index']

    for index in indexList:                                                                                      #Iteriere über Liste
        if parentList[index] == "leer":
            net.add_node(nameList[index], title="Hauptprgramm", color="red")                                     #Füge Haptprogramme als rote Nodes ein
        else:
            net.add_node(nameList[index], title="Unterprogramm von " + parentList[index], color="blue")          #Füge Unterprogramme als blaue Nodes ein
            net.add_edge(nameList[index], parentList[index])                                                     #Füge Kante zwischen Nodes ein
    net.show('test.html')                                                                                        #Output html-Datei


