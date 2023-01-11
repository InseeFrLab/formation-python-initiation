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
    
    if grille[0][colonne_a_jouer] != " ":
        # Si la colonne choisie n'a aucune case vide, on renvoie une erreur
        raise ValueError("La colonne choisie est déjà complète.")
    else:
        # Sinon, on parcourt la colonne du bas vers le haut jusqu'à arriver sur une case vide
        # On ajoute alors le pion dans cette case
        ligne = 5
        while grille[ligne][colonne_a_jouer] != ' ':
            ligne -= 1
        grille[ligne][colonne_a_jouer] = couleur_pion

    return grille


def victoire_ligne(ligne):
    n_R = ligne.count("R")
    n_J = ligne.count("J")
    if n_R == 4:
        print(f'Les pions rouges ont gagné, félicitations !')
        return True
    if n_J == 4:
        print(f'Les pions jaunes ont gagné, félicitations !')
        return True
    return False


def victoire_horizontale_grille(grille):
    for ligne in grille:
        if victoire_ligne(ligne):
            return True
    return False


def victoire_verticale_grille(grille):
    for idx_colonne in range(7):
        colonne = []
        for ligne in grille:
            colonne.append(ligne[idx_colonne])
        if victoire_ligne(colonne):
            return True
    return False
