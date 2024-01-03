# This is a sample Python script.
from pyvis.network import Network
import pandas as pd


def parseList(param):
    output = []
    if "|" not in param:
        output.append(param)
        return output
    else:
        return param.split("|")


if __name__ == '__main__':
    net = Network(notebook=True, cdn_resources="remote", select_menu=True, filter_menu=True)                    #Graph initialisieren
    df = pd.read_csv('list.CSV', sep=';')                                                         #CSV-Datei wird ausgelesen
    df["Parent Node"].fillna("leer", inplace=True)                                                              #Leere Felder werden gefüllt

    nameList = df['Name']                                                                                       #Zugriff auf Spalten
    parentList = df['Parent Node']
    indexList = df['Index']

    for index in indexList:                                                                                      #Iteriere über Liste
        if parentList[index] == "leer":
            net.add_node(nameList[index], title="Hauptprgramm", color="red")                                     #Fuege Hauptprogramme als rote Knoten ein
        else:
            net.add_node(nameList[index], title="Unterprogramm von " + parentList[index], color="blue")          #Fuege Unterprogramme als blaue Knoten ein

    for index in indexList:
        for parents in parseList(parentList[index]):
            if parentList[index] != "leer":
                net.add_edge(nameList[index], parents)                                                           #Fuege Kanten hinzu
    net.show('test.html')                                                                                        #Output html-Datei


