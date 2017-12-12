""" programme à compléter du kPPV"""
import csv

nbExParClasse = 50
nbApprent = 25
nbCaract = 4
nbClasse = 3

def lectureFichierCSV():
    with open("iris.data", 'r')as fic:
        lines = csv.reader(fic)
        dataset = list(lines)
    #print(dataset[0], len(dataset))
    for i in range(len(dataset)):
        for j in range(nbCaract):
            dataset[i][j] = float(dataset[i][j])
    #print(dataset[0])
    return(dataset)

def calculDistances(data, dataset):
    """ retourne les distances entre data et la partie apprentissage de dataset"""
    distances = []
    
	#-------- A faire... --------
	
    return(distances)

def calculClasse(distances):
    """ retourne le numéro de la classe déterminé à partir des distances """
    
	#-------- A faire... --------

    return(classe)

if __name__ == "__main__":
    print("Début programme kPPV")
    dataset = lectureFichierCSV()

    # Calcule et affiche la matrice de confusion et le taux de reco
    
	#-------- A faire... --------

#--------------------------------- Fin kPPV -----------------------------------