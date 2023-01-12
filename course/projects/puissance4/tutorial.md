---
title: "Projet 1 - Puissance 4"
abstract: "Un projet de code pour mettre en pratique les éléments fondamentaux de Python : structures de données, boucles, fonctions, conditions."
---

Dans ce projet nous allons implémenter un puissance 4 avec une interface graphique assez sommaire. Pour y arriver, nous allons utiliser les objets fondamentaux de Python.

```python
import copy

import solutions
```

## Règles du jeu

Le but du jeu de Puissance 4 est d'aligner une suite de 4 pions de même couleur sur une grille comptant 6 rangées et 7 colonnes. Chaque joueur dispose de 21 pions d'une couleur (par convention, en général jaune ou rouge). Tour à tour, les deux joueurs placent un pion dans la colonne de leur choix, le pion coulisse alors jusqu'à la position la plus basse possible dans la dite colonne à la suite de quoi c'est à l'adversaire de jouer. Le vainqueur est le joueur qui réalise le premier un alignement (horizontal, vertical ou diagonal) consécutif d'au moins quatre pions de sa couleur. Si, alors que toutes les cases de la grille de jeu sont remplies, aucun des deux joueurs n'a réalisé un tel alignement, la partie est déclarée nulle.

Afin de simplifier le code de ce projet, on partira du principe que les alignements victorieux ne peuvent être qu'horizontaux ou verticaux. Les diagonales ne seront donc pas considérées (mais constituent un exercice intéressant pour aller plus loin !).

## Plan du projet

Nous allons décomposer la construction du jeu en différentes parties :
- initialisation de la grille
- représentation de la grille
- fonction de jeu
- détection d'une victoire (horizontale)
- détection d'une victoire (verticale)
- fin de partie

## Initialisation de la grille

L'objectif de cette partie est d'intialiser un objet Python qui représente une grille de puissance 4. Le choix que nous allons faire est de **représenter la grille comme une liste de listes**. Il s'agira d'une matrice 6x7 : on aura par conséquent une **liste de 6 élements** (qui représenteront les lignes de la grille), dont chacun des éléments sera une **liste contenant 7 éléments** (qui représenterons les pions). 

Chaque élément de la grille sera représenté par un *string*, qui pourra prendre trois valeurs :
- ' ' : s'il s'agit d'une case vide
- 'R' : s'il s'agit d'un pion rouge. 
- 'J' : s'il s'agit d'un pion jaune. 

Dans la fonction d'initialisation de la grille, chaque élément sera donc initialisé comme un ***string* contenant un espace**.

### Résultat attendu


```python
grille = solutions.initialise_grille()
grille
```


```python
print(f'Nombre de lignes : {len(grille)}')
print(f'Nombre de colonnes : {len(grille[0])}')
```

### A vous de jouer !


```python
def initialise_grille():
    # Votre code ici
    return grille
```


```python
# Vérification du résultat
grille = initialise_grille()
grille
```


```python
# Vérification du résultat
print(f'Nombre de lignes : {len(grille)}')
print(f'Nombre de colonnes : {len(grille[0])}')
```

## Représentation de la grille

Notre grille est initialisée, mais son affichage est assez sommaire. L'idée de cette partie est d'offrir une représentation plus visuelle du jeu pendant une partie.

Pour cela, nous allons créer **une fonction qui prend en entrée la grille précédemment initialisée et renvoie sa représentation** (via la fonction `print`). Les colonnes seront séparées par le caractère | (barre verticale).

**Indice** : une solution possible fait intervenir deux notions que nous avons vues dans les TP précédents : la concaténation de *strings* et la fonction `join` qui "joint" les éléments d'une liste en les séparant par un certain caractère. Pour rappel, voici un exemple qui utilise ces deux concepts : 


```python
l = ["a", "b", "c", "d", "e"]
l_join = "DEBUT " + ", ".join(l) + " FIN"
print(l_join)
```

### Résultat attendu


```python
solutions.affiche_grille(grille)
```

### A vous de jouer !


```python
def affiche_grille():
    # Votre code ici
```


```python
# Vérification du résultat
affiche_grille(grille)
```

## Fonction de jeu

Maintenant que nous pouvons représenter notre grille, intéressons-nous au coeur du puissance 4 : le jeu. L'objectif de cette partie est de **coder une fonction `tour` qui va modifier la grille lorsqu'un joueur joue son tour**.

Cette fonction prend en entrée :
- la grille
- la colonne choisie par le joueur
- la couleur du pion ('R' pour le pion rouge, et 'J' pour le pion jaune)

et renvoie en sortie la grille actualisée suite au tour du joueur.

**Attention** : en Python, la numérotation commence à 0. La première colonne correspond donc à la colonne 0 du point de vue de l'indexation

### Résultat attendu


```python
grille = solutions.initialise_grille()  # Intialisation
grille = solutions.tour(grille=grille, colonne_a_jouer=2, couleur_pion="R")  # 1er tour de jeu
grille = solutions.tour(grille=grille, colonne_a_jouer=5, couleur_pion="J")  # 2ème tour de jeu
grille = solutions.tour(grille=grille, colonne_a_jouer=2, couleur_pion="J")  # 3ème tour de jeu
solutions.affiche_grille(grille)
```

### A vous de jouer !


```python
def tour(grille, colonne_a_jouer, couleur_pion):
    grille = copy.deepcopy(grille)  # Evite la modification de la grille initiale
    # Votre code ici
    return grille
```


```python
# Vérification du résultat
grille = initialise_grille()  # Intialisation
grille = tour(grille=grille, colonne_a_jouer=2, couleur_pion="R")  # 1er tour de jeu
grille = tour(grille=grille, colonne_a_jouer=5, couleur_pion="J")  # 2ème tour de jeu
grille = tour(grille=grille, colonne_a_jouer=2, couleur_pion="J")  # 3ème tour de jeu
affiche_grille(grille)
```

## Détection d'une victoire (horizontale)

Maintenant qu'il est possible de jouer effectivement à notre puissance 4, il faut pouvoir détecter une victoire pour mettre fin à la partie en cours. Pour se faire, on va simplifier le problème en le décomposant au maximum.

Dans un premier temps, on s'intéresse à la détection d'une victoire horizontale. Pour cela, on va s'aider de deux fonctions :
- une fonction `victoire_ligne` qui prend en entrée une ligne du puissance 4 (i.e. une liste de taille 7) et retourne `True` si jamais 4 pions consécutifs de même couleur se trouvent sur la ligne, et `False` sinon
- une fonction `victoire_horizontale_grille` qui prend en entrée une grille complète et retourne `True` si jamais une ligne de la grille remplit la condition précédente, et `False` sinon

### Résultat attendu


```python
# Détection d'une victoire (horizontale) sur une ligne
ligne1 = [" ", "R", "R", "R", "J", "J", " "]
ligne2 = [" ", "R", "R", "R", "R", "J", " "]

print(solutions.victoire_ligne(ligne1))  # Renvoie False
print()  # Retour à la ligne
print(solutions.victoire_ligne(ligne2))  # Renvoie True
```


```python
# Détection d'une victoire (horizontale) sur une grille
grille = solutions.initialise_grille()  # Intialisation
print(solutions.victoire_horizontale_grille(grille))  # Renvoie False
print()  # Retour à la ligne

grille = solutions.tour(grille=grille, colonne_a_jouer=2, couleur_pion="R")
grille = solutions.tour(grille=grille, colonne_a_jouer=3, couleur_pion="R")
grille = solutions.tour(grille=grille, colonne_a_jouer=4, couleur_pion="R")
grille = solutions.tour(grille=grille, colonne_a_jouer=5, couleur_pion="R")
solutions.affiche_grille(grille)
print()  # Retour à la ligne

print(solutions.victoire_horizontale_grille(grille))  # Renvoie True
```

### A vous de jouer !


```python
def victoire_ligne(ligne):
    # Votre code ici
```


```python
# Vérification du résultat
ligne1 = [" ", "R", "R", "R", "J", "R", " "]
ligne2 = [" ", "R", "R", "R", "R", "J", " "]

print(victoire_ligne(ligne1))  # Renvoie False
print(victoire_ligne(ligne2))  # Renvoie True
```


```python
def victoire_horizontale_grille(grille):
    # Votre code ici
```


```python
# Vérification du résultat
grille = initialise_grille()  # Intialisation
print(victoire_horizontale_grille(grille))  # Renvoie False

grille = tour(grille=grille, colonne_a_jouer=2, couleur_pion="R")
grille = tour(grille=grille, colonne_a_jouer=3, couleur_pion="R")
grille = tour(grille=grille, colonne_a_jouer=4, couleur_pion="R")
grille = tour(grille=grille, colonne_a_jouer=5, couleur_pion="R")
affiche_grille(grille)
print(victoire_horizontale_grille(grille))  # Renvoie True
```

## Détection d'une victoire (verticale)

A présent, on s'intéresse à la détection d'une victoire verticale. Par rapport à la situation précédente, la difficulté est que l'on ne peut pas directement boucler sur les colonnes. On va donc construire une fonction `victoire_verticale_grille` qui, pour chaque colonne :
- récupère les éléments de la colonne dans une liste
- applique à cette liste la fonction `victoire_ligne` pour vérifier la présence de 4 pions consécutifs de même couleur dans la colonne considérée

### Résultat attendu


```python
# Détection d'une victoire (verticale) sur une grille
grille = solutions.initialise_grille()  # Intialisation
print(solutions.victoire_verticale_grille(grille))  # Renvoie False
print()  # Retour à la ligne

grille = solutions.tour(grille=grille, colonne_a_jouer=2, couleur_pion="J")
grille = solutions.tour(grille=grille, colonne_a_jouer=2, couleur_pion="J")
grille = solutions.tour(grille=grille, colonne_a_jouer=2, couleur_pion="J")
grille = solutions.tour(grille=grille, colonne_a_jouer=2, couleur_pion="J")
solutions.affiche_grille(grille)
print()  # Retour à la ligne

print(solutions.victoire_verticale_grille(grille))  # Renvoie True
```

### A vous de jouer !


```python
def victoire_verticale_grille(grille):
    # Votre code ici
```


```python
# Vérification du résultat
grille = initialise_grille()  # Intialisation
print(victoire_verticale_grille(grille))  # Renvoie False
print()  # Retour à la ligne

grille = tour(grille=grille, colonne_a_jouer=2, couleur_pion="J")
grille = tour(grille=grille, colonne_a_jouer=2, couleur_pion="J")
grille = tour(grille=grille, colonne_a_jouer=2, couleur_pion="J")
grille = tour(grille=grille, colonne_a_jouer=2, couleur_pion="J")
affiche_grille(grille)
print()  # Retour à la ligne

print(victoire_verticale_grille(grille))  # Renvoie True
```

## Fin de partie

Dans notre version simplifiée du puissance 4, on peut à présent déclarer la **fin de partie : dès lors qu'une victoire horizontale ou verticale est détectée**.

On va donc pour commencer créer une fonction `victoire` qui prend la grille en entrée et renvoie `True` si une victoire horizontale **ou** verticale est détectée, et `False` sinon.

Dans l'idéal, on voudrait ne pas avoir à tester manuellement après chaque coup si la partie est terminée afin de limiter la duplication de code. On va donc ensuite créer une fonction `tour_test_victoire` qui :
- prend en entrée les mêmes *inputs* que la fonction `tour`
- va appeler la fonction `tour` pour réaliser le tour de jeu
- va tester après le tour de jeu si une victoire est détectée via la fonction `victoire`. Si une victoire est détectée, la fonction imprime "FIN DE PARTIE".

### Résultat attendu


```python
grille = solutions.initialise_grille()  # Intialisation
print("Tour 1")
grille = solutions.tour_test_victoire(grille=grille, colonne_a_jouer=2, couleur_pion="J")
print("Tour 2")
grille = solutions.tour_test_victoire(grille=grille, colonne_a_jouer=2, couleur_pion="J")
print("Tour 3")
grille = solutions.tour_test_victoire(grille=grille, colonne_a_jouer=2, couleur_pion="J")
print("Tour 4")
grille = solutions.tour_test_victoire(grille=grille, colonne_a_jouer=2, couleur_pion="J")
```


### A vous de jouer !


```python
def victoire(grille):
    # Votre code ici
```


```python
def tour_test_victoire(grille, colonne_a_jouer, couleur_pion):
    grille = copy.deepcopy(grille)
    # Votre code ici
    return grille
```


```python
# Vérification du résultat
grille = initialise_grille()  # Intialisation
print("Tour 1")
grille = tour_test_victoire(grille=grille, colonne_a_jouer=2, couleur_pion="J")
print("Tour 2")
grille = tour_test_victoire(grille=grille, colonne_a_jouer=2, couleur_pion="J")
print("Tour 3")
grille = tour_test_victoire(grille=grille, colonne_a_jouer=2, couleur_pion="J")
print("Tour 4")
grille = tour_test_victoire(grille=grille, colonne_a_jouer=2, couleur_pion="J")
```


```python

```
