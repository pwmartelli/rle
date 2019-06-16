#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""compression_rle

Fonctions pour notebook sur la compression RLE

Auteurs : Martin Canals et Pierre-William Martelli

"""

import matplotlib.pyplot as plt
import numpy as np

PBM_EXERCICE = [0] * 25


def affichage_pbm(larg, haut, liste_pbm):
    """
    affichage_pbm(larg, haut, liste_pbm)

    Affiche une image donnee sous format PBM
    larg : nombre de pixels horizontaux
    haut : nombre de pixels verticaux
    liste_pbm : liste de 0 et de 1 qui represente l'image au format PBM

    """
    dims = (haut, larg)
    mat = np.zeros(dims)
    for row in range(dims[0]):
        for col in range(dims[1]):
            mat[row, col] = (liste_pbm[col + row * dims[1]] + 1) % 2

    plt.matshow(mat, cmap='gray')
    plt.show()


def mystere(liste):
    """
    mystere(liste)

    Fonction mystere. Prend une liste en argument, et renvoie une liste

    """
    retour = []
    bit = 0
    for i in range(len(liste)):
        for j in range(liste[i]):
            retour.append(bit)
        bit = (bit + 1) % 2
    return retour


def affichage_rle(larg, haut, liste_rle):
    """
    affichage_rle(larg, haut, liste_rle)

    Affiche une image donnee sous format RLE
    larg : nombre de pixels horizontaux
    haut : nombre de pixels verticaux
    liste_rle : liste de nombre qui represente l'image au format PBM

    """
    affichage_pbm(larg, haut, mystere(liste_rle))


def exercice_aleatoire():
    """
    exercice_aleatoire()

    Genere une image aleatoire de taille 5x5 au format PBM, et l'affiche

    """
    matrice_alea = np.random.randint(2, size=(5, 5))
    for row in range(5):
        for col in range(5):
            PBM_EXERCICE[col + row * 5] = matrice_alea[row, col]
    print('PBM_EXERCICE = ', PBM_EXERCICE)
    affichage_pbm(5, 5, PBM_EXERCICE)


def verif_exercice(rle_reponse):
    """
    verif_exercice()

    Teste si rle_reponse correpond a la compression RLE de PBM_EXERCICE, et
    l'affiche
    rle_reponse : tableau d'entiers, representant le format RLE d'une image

    """
    if mystere(rle_reponse) == PBM_EXERCICE:
        print('Exercice réussi !')
    else:
        print('Exercice non réussi...')
    if sum(rle_reponse) == 25:
        affichage_rle(5, 5, rle_reponse)
    else:
        print('La somme des entiers de votre tableau devrait être égale à 25 !'
