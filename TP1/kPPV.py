""" programme à compléter du kPPV"""
import csv
import numpy
from scipy.spatial import distance

nbExParClasse = 50
nbApprent = 25
nbCaract = 4
nbClass = 3
kPPV = 1
classFound = []


def comp(v1, v2):
    if v1[0] < v2[0]:
        return -1
    elif v1[0] > v2[0]:
        return 1
    else:
        return 0


def conv(v):
    return v


def lectureFichierCSV():
    with open("iris.data", 'r')as fic:
        lines = csv.reader(fic)
        dataset = list(lines)
    # print(dataset[0], len(dataset))
    for i in range(len(dataset)):
        for j in range(nbCaract):
            dataset[i][j] = float(dataset[i][j])
    # print(dataset[0])
    return (dataset)


def calculDistances(data, dataset):
    """ retourne les distances entre data et la partie apprentissage de dataset"""
    distances = []

    currentClass = None
    nbSamplesCurrentClassRead = 0

    for datasetRow in dataset:
        if currentClass != datasetRow[4]:
            currentClass = datasetRow[4]
            nbSamplesCurrentClassRead = 0
            classFound.append(currentClass)

        if nbSamplesCurrentClassRead < nbApprent:
            nbSamplesCurrentClassRead += 1
            dist = distance.euclidean(data, [datasetRow[0], datasetRow[1], datasetRow[2], datasetRow[3]])
            distances.append([dist, currentClass])

    return distances


def calculClasse(distances, kPPV):
    """ retourne le numéro de la classe déterminé à partir des distances """

    sortedDistances = sorted(distances)
    tableNbClass = []

    for className in classFound:
        tableNbClass.append([0, className])

    for i in range(kPPV):
        classRead = sortedDistances[i][1]
        for j in range(nbClass):
            if classRead == tableNbClass[j][1]:
                tableNbClass[j][0] += 1

    return (max(tableNbClass))[1]


def generateConfusionMatrix(dataset, kPPV):
    confusionMatrix = numpy.zeros((nbClass, nbClass))
    indexCurrentClass = 0
    nbSamplesCurrentClassRead = 0
    currentClass = classFound[0]

    for datasetRow in dataset:
        if (currentClass != datasetRow[4]):
            currentClass = datasetRow[4]
            nbSamplesCurrentClassRead = 0
            indexCurrentClass += 1

        if nbSamplesCurrentClassRead >= nbApprent:
            distances = calculDistances([datasetRow[0], datasetRow[1], datasetRow[2], datasetRow[3]], dataset)
            confusionMatrix[classFound.index(calculClasse(distances, kPPV))][indexCurrentClass] += 1

        nbSamplesCurrentClassRead += 1

    return confusionMatrix


def recognitionRate(confusionMatrix):
    nbSuccess = 0
    nbTotal = 0

    for i in range(nbClass):
        for j in range(nbClass):
            if (i == j):
                nbSuccess += confusionMatrix[i][j]
            nbTotal += confusionMatrix[i][j]

    return 100 * nbSuccess / nbTotal


if __name__ == "__main__":
    print("Début programme kPPV")
    dataset = lectureFichierCSV()

    data = [1, 1, 1, 1]

    distances = calculDistances(data, dataset)

    print(distances)
    print(calculClasse(distances, kPPV))
    confusionMatrix = generateConfusionMatrix(dataset, kPPV)
    print(confusionMatrix)
    print(recognitionRate(confusionMatrix), "%")

    # Calcule et affiche la matrice de confusion et le taux de reco

    # -------- A faire... --------

    # --------------------------------- Fin kPPV -----------------------------------
