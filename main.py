from pyvis.network import Network
import pandas as pd


def parseList(param):
    output = []
    if "," not in param:
        output.append(param)
        return output
    else:
        return param.split(",")


def setColor(param):
    if param == "A":
        return "blue"
    elif param == "B":
        return "green"


if __name__ == "__main__":
    net = Network(notebook=True, cdn_resources="remote", select_menu=True, filter_menu=True)                    #Graph initialisieren
    df = pd.read_csv("list.CSV", sep=";")                                                         #CSV-Datei wird ausgelesen
    df["Parent Node"].fillna("leer", inplace=True)                                                              #Leere Felder werden gefüllt

    nameList = df["Name"]                                                                                       #Zugriff auf Spalten
    firmaList = df["Firma"]
    bereichList = df["Fachbereich"]
    personList = df["Verantwortlicher"]
    parentList = df["Parent Node"]
    indexList = df["Index"]

    for index in indexList:                                                                                      #Iteriere über Liste
        if parentList[index] == "leer":
            net.add_node(nameList[index], title="Hauptprogramm", color=setColor(firmaList[index]))               #Fuege Hauptprogramme mit Farbe je nach Firma ein
        else:
            net.add_node(nameList[index], title="Unterprogramm von " + parentList[index], color=setColor(firmaList[index]))          #Fuege Unterprogramme

    for index in indexList:
        for parents in parseList(parentList[index]):
            if parentList[index] != "leer":
                net.add_edge(nameList[index], parents)                                                           #Fuege Kanten hinzu
    net.show("test.html")                                                                                        #Output html-Datei


