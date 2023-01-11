import copy


def initialise_grille(n_lignes=6, n_colonnes=7):
    grille = []

    for ligne in range(n_lignes):
        colonne_espace_vide = [' ' for espace in range(n_colonnes)]
        grille.append(colonne_espace_vide)
    return grille


def affiche_grille(grille):
    for row in grille:
        print("| " + " | ".join(row) + " |")

        
def tour(grille, colonne_a_jouer, couleur_pion):
    grille = copy.deepcopy(grille)
    
    # Test de la validité de la couleur du pion
    err_couleur = 'La couleur du pion doit être "J" ou "R".'
    assert couleur_pion in ["J", "R"], err_couleur
    
    # Test de la validité de la colonne
    err_colonne = "La colonne à jouer doit être comprise entre 0 et 6."
    assert (colonne_a_jouer >= 0 and colonne_a_jouer <= 6), err_colonne
    
    # Test si la colonne choisie n'est pas déjà complète
    err_full = "La colonne choisie est déjà complète."
    assert grille[0][colonne_a_jouer] == " ", err_full
    
    # On parcourt la colonne du bas vers le haut jusqu'à arriver sur une case vide
    # On ajoute alors le pion dans cette case
    ligne = 5
    while grille[ligne][colonne_a_jouer] != ' ':
        ligne -= 1
    grille[ligne][colonne_a_jouer] = couleur_pion

    return grille
