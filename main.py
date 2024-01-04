from pyvis.network import Network
import pandas as pd


def parseList(param):
    output = []
    if "," not in param:
        output.append(param)
        return output
    else:
        return param.split(",")


def setColor(firma):
    if firma == "A":
        return "blue"
    elif firma == "B":
        return "green"


#TODO nicht nur als Text anzeigen, sondern als Attribut hinterlegen ->wrapper Klasse?
def setNodeTitle(index):
    title = ""
    if parentList[index] == "leer":
        title += "Hauptprogramm"
    else:
        title += "Unterprogramm von " + parentList[index].replace(",", " und ")
    title += "\nFirma: " + firmaList[index] + "\nVerantwortlicher: " + personList[index]
    title += "\nFachbreich: " + bereichList[index]
    return title


def addNodes():
    for index in indexList:
        net.add_node(nameList[index], title=setNodeTitle(index), color=setColor(firmaList[index]))               #Fuege Hauptprogramme mit Farbe je nach Firma ein


def addEdges():
    for index in indexList:
        for parents in parseList(parentList[index]):
            if parentList[index] != "leer":
                net.add_edge(nameList[index], parents)                                                           #Fuege Kanten hinzu


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

    addNodes()
    addEdges()

    net.show("test.html")                                                                                        #Output html-Datei


