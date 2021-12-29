# -------------------------------------------------------------------------- #

# 1/ L'utilisation de fonction permet de réduire la duplication du code
# et de mieux isoler les différents blocs logiques d'un programme.

# 2/ Une fonction prend en entrée des arguments, réalise une action
# donnée via un ensemble d'instructions, et renvoient un résultat
# en sortie.

# 3/ Les fonctions "boîtes noires" sont les fonctions dont on ne connaît
# pas le code lorsqu'on les éxécute, comme les fonctions built-in de Python
# (len, range..). Elles s'opposent aux fonctions créées par l'utilisateur.

# 4/ Quand on définit une fonction via l'instruction def, on met en mémoire
# le code de la fonction. Ce n'est que quand on appelle la fonction que ce
# code s'éxécute, et renvoie un résultat.

# 5/ Autant que l'on souhaite.

# 6/ Par position : on passe les arguments dans l'ordre où ils ont été
# spécifiés lors de la définition de la fonction.
# Par mot-clé : on passe les arguments en les nommant.

# 7/ Modifier le comportement par défaut d'une fonction, tel qu'il a été
# voulu par son concepteur.

# 8/ D'abord les arguments obligatoires, puis les arguments optionnels.

# 9/ Non, une fonction renvoie toujours un objet.
# Si l'on ne spécifie pas d'instruction return, la fonction renvoie 
# la valeur None, qui est un objet de type NoneType.

# 10/ Non, une fonction renvoie un seul objet. En revanche, si l'on veut
# qu'une fonction renvoie plusieurs résultats, il suffit de les mettre dans
# un objet conteneur (liste, tuple, dictionnaire..).

# 11/ Elles disparaissent et ne peuvent donc pas être réutilisées dans le
# scope global.

# -------------------------------------------------------------------------- #

def puissance(x, y):
    return x**y

puissance(2, 3)

# -------------------------------------------------------------------------- #

# f1. Valeur : 5 ; Type : int

# f2. Valeur : '' ; Type : str

# f3. Valeur : None ; Type : NoneType

# f4. Valeur : None ; Type : NoneType

# f5. Valeur : None ; Type : NoneType

# f6. Valeur : 'test ok' ; Type : str

# f7. Valeur : 'test not ok' ; Type : str

# f8. Erreur : z n'est pas défini

# f9. Valeur : 13 ; Type : int

# -------------------------------------------------------------------------- #

z = 3

def f1(x, y):
    z = 5
    return x + y + z

def f2(x, y, z=1):
    return x + y + z

def f3(x, y):
    return x + y + z

total = f1(2, 3) + f2(3, 1) + f3(1, 0)

print(f1(2, 3))  
# c'est la variable z locale à f1 qui est utilisée -> f1 renvoie 10

print(f2(3, 1))  
# c'est la variable z locale à f1 qui est utilisée
# sa valeur par défaut est 1 -> f2 renvoie 5

print(f3(1, 0)) 
# c'est la variable z globale qui est utilisée -> f3 renvoie 4

print(total)

# -------------------------------------------------------------------------- #

def calculatrice(a, b):
    return a+b, a-b, a*b, a/b

add, sub, mult, div = calculatrice(5, 3)
print(add, sub, mult, div)

# -------------------------------------------------------------------------- #

def dedup(l, sort=False):
    l_dedup = list(set(l))
    if sort:
        l_dedup.sort()
    return l_dedup

l = ["a", "a", "b", "c"]
print(dedup(l))  # Comportement par défaut : pas de tri
print(dedup(l, sort=True))  # Comportement modifié : tri

# -------------------------------------------------------------------------- #

def multiplier(l):
    print("Il y a " + str(len(l)) + " nombres dans la liste.")
    c = 1
    for x in l:
        c *= x  # Equivalent à : c = c * x
    return c

l = [2, 8, 3]
multiplier(l)

# -------------------------------------------------------------------------- #

def mean(x):
    n = len(x)
    somme_moy = 0
    for x_i in x:
        somme_moy += x_i
    moyenne = somme_moy / n
    return moyenne

def var(x, mode="population"):
    n = len(x)
    moyenne = mean(x)
    somme_var = 0
    for x_i in x:
        somme_var += (x_i - moyenne)**2
    if mode == "population":
        variance = somme_var / n
    elif mode == "sample":
        variance = somme_var / (n-1)
    return variance

x = [8, 18, 6, 0, 15, 17.5, 9, 1]
print(mean(x))
print(var(x))  # population
print(var(x, mode="sample"))  # échantillon

# Vérification avec les fonctions de la librairie numpy
import numpy as np
print(np.mean(x))
print(np.var(x))  # population
print(np.var(x, ddof=1))  # sample

# -------------------------------------------------------------------------- #

def factorielle(n):
    if n == 0:
        # Critère d'arrêt
        return 1
    else:
        return n * factorielle(n-1)

factorielle(5)

# -------------------------------------------------------------------------- #
