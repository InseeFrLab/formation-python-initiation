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
    for i, elem in enumerate(ligne):
        # Pour chaque élément de la ligne
        if elem in ["R", "J"] and i + 3 <= len(ligne) - 1:
            # Si l'élément est un pion et qu'il existe au moins 3 éléments à sa droite
            count_equal = 0
            for j in range(1, 4):
                # On compte le nombre de pions de même couleur à sa droite
                if elem == ligne[i+j]:
                    count_equal += 1
            if count_equal == 3:
                # Si le compteur vaut 3, c'est une victoire, la fonction retourne True
                if elem == "R":
                    print("Les pions rouges ont gagné, félicitations !")
                if elem == "J":
                    print("Les pions jaunes ont gagné, félicitations !")
                return True
    return False


def victoire_horizontale_grille(grille):
    for ligne in grille:
        # On teste le critère de victoire sur chaque ligne
        if victoire_ligne(ligne):
            return True
    return False


def victoire_verticale_grille(grille):
    for idx_colonne in range(7):
        # On récupère les éléments de la colonne dans une liste
        colonne = []
        for ligne in grille:
            colonne.append(ligne[idx_colonne])
        if victoire_ligne(colonne):
            # On teste l'existence d'une victoire
            return True
    return False


def victoire(grille):
    if victoire_horizontale_grille(grille) or victoire_verticale_grille(grille):
        return True
    return False


def tour_test_victoire(grille, colonne_a_jouer, couleur_pion):
    grille = copy.deepcopy(grille)
    grille = tour(grille, colonne_a_jouer, couleur_pion)
    if victoire(grille):
        print("FIN DE PARTIE")
    return grille
