import sys


def initialise_grille(n_lignes=6, n_colonnes=7):
    grille = []

    for ligne in range(n_lignes):
        colonne_espace_vide = [' ' for espace in range(n_colonnes)]
        grille.append(colonne_espace_vide)
    return grille


def affiche_grille(grille):
    for row in grille:
        print("| " + " | ".join(row) + " |")
