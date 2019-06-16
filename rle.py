#============================#
# Conversion de PBM vers RLE #
#============================#

# Lecture du fichier au format PBM
def lecture_PBM(nom):
    retour=[0]*3

    fichier=open(nom,'r')
    lignes=fichier.readlines()

    dim=lignes[2].split(' ')
    retour[0]=int(dim[0]) # nb de pixels en largeur
    retour[1]=int(dim[1].replace('\n','')) # nb de pixels en hauteur

    retour[2]=''
    for i in range(3,len(lignes)):
        retour[2]=retour[2]+lignes[i].replace('\n','')

    retour[2]=list(retour[2]) # conversion du troisième argument de sortie en liste

    # conversion du troisieme argument de sortie en liste d'entiers
    for i in range(len(retour[2])):
        retour[2][i]=int(retour[2][i])

    fichier.close()
    return(retour)

# Conversion du PBM vers RLE
def conversion_PBM_vers_RLE(listePBM):
    listeRLE = []
    en_cours = 0 # contient 0 ou 1 selon ce qu'on lit
    cpt = 0
    for c in listePBM:
        if c == en_cours:
            cpt = cpt + 1
        else:
            listeRLE.append(cpt)
            en_cours = (en_cours + 1) % 2 # en cours change en 0 ou 1
            cpt = 1
    listeRLE.append(cpt)
    return listeRLE

# Conversion RLE vers PBM
def conversion_RLE_vers_PBM(listeRLE):
    listePBM = []
    en_cours = 0
    for i in range(len(listeRLE)):
        for j in range(listeRLE[i]):
            listePBM.append(en_cours)
        en_cours = (en_cours + 1) % 2
    return listePBM

#====================#
# Fonction affichage #
#====================#

# A donner aux eleves (contient biblio HP)
import matplotlib.pyplot as plt
import numpy as np

def affichage_PBM(nx,ny,liste):
    dims=(ny,nx)
    mat=np.zeros(dims)
    for row in range(dims[0]):
        for col in range(dims[1]):
            mat[row,col]=(liste[col+row*dims[1]]+1)%2
            #mat[row,col]=liste[col+row*dims[1]]

    plt.matshow(mat,cmap='gray')
    plt.show()

    return -1






