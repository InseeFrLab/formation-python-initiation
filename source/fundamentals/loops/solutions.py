# -------------------------------------------------------------------------- #

# 1/ Une boucle `for` définit une variable d'itération qui va parcourir
# chaque élément d'un objet itérable. A chaque itération, une série
# d'instructions est effectuée.

# 2/ Oui, et sa valeur finale est égale à la dernière valeur de l'objet itérable.

# 3/ La fonction `range(n)` crée un objet itérable qui contient tous les entiers
# compris entre 0 et n-1. Elle est très utilisée comme itérable dans les boucles
# `for` car elle permet d'itérer sur une séquence d'entiers sans avoir à mettre
# celle-ci dans une liste à la main.

# 4/ La fonction `enumerate` appliquée à un objet itérable renvoie un nouvel objet
# itérable qui contient l'ensemble des couples (indice, élément) associés à
# l'objet initial, sous forme de tuples. Dans le cadre d'une boucle `for`, elle
# permet d'itérer à la fois sur les éléments d'un itérable et sur les positions
# de ces éléments.

# 5/ Une boucle `while` exécute une série d'instructions de manière répétée
# tant que la condition logique spécifiée évalue à True.

# 6/ Une boucle `while` s'arrête dès lors que la condition logique spécifiée
# évalue à False. Si ce cas ne se produit jamais, une boucle `while` peut
# donc être infinie. A l'inverse, une boucle `for` peut être très longue mais
# jamais infinie, dans la mesure où elle s'arrête dès lors qu'elle a terminé
# de parcourir l'objet.

# 7/ L'instruction `break` force la boucle de niveau directement supérieur à
# se terminer.

# 8/ L'instruction `continue` force la boucle de niveau directement supérieur
# à passer à l'itération suivante.

# -------------------------------------------------------------------------- #

# 1. Boucle infinie car le i n'est jamais incrémenté, la condition est donc
# toujours vérifiée. 0 va s'imprimer à l'infini.

# 2. La boucle va s'arrêter à la 4ème itération, lorsque a vaut 5.
# Cependant, le print est mal indenté => il va s'imprimer 3 fois au lieu d'1.

# 3. False évalue à False => la boucle ne s'exécute pas du tout. Aucun output.

# 4. True évalue à True => la boucle est théoriquement infinie, mais il y a un
# break. Il va donc y avoir une seule itération, soit un seul print de
# "hello world"

# 5. 5 >= 3 évalue à True => la boucle est infinie.
# Le continue est exécuté à chaque itération avant que le print ne puisse
# s'exécuter. La boucle tourne à l'infini, mais sans output.

# -------------------------------------------------------------------------- #

# Le premier programme est correct.
# Dans le second, le second `print` n'est pas correctement indenté
# En conséquence, il s'exécute à chaque itération et non pas juste lorsque
# nb == 5.

# -------------------------------------------------------------------------- #

gamme = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']

i = 0
while i <= (len(gamme) - 1):
    # On soustrait 1 à la longueur de `gamme` car l'index maximal est 6
    print("La note numéro " + str(i) + " de la gamme de do majeur est " + gamme[i])
    i += 1

# -------------------------------------------------------------------------- #

n_cible = 78

l = [12, 98, 65, 39, 78, 55, 119, 27, 33]

for i, n in enumerate(l):
    if n == n_cible:
        print("Le nombre " + str(n) + " est à la position " + str(i) + " de la liste.")
        break

# NB : version plus efficiente sans boucle
if n_cible in l:
    pos = l.index(n_cible)
    print("Le nombre " + str(n_cible) + " est à la position " + str(pos) + " de la liste.")

# -------------------------------------------------------------------------- #

n_termes = 20
num1 = 0
num2 = 1

for i in range(n_termes):
    print(num1)
    num3 = num1 + num2
    num1 = num2
    num2 = num3

# -------------------------------------------------------------------------- #

tables = {}

for i in range(13):
    tables[i] = {}
    for j in range(13):
        tables[i][j] = i*j

print(tables[2][3])
print(tables[9][5])
print(tables[12][7])

# -------------------------------------------------------------------------- #

x = [8, 18, 6, 0, 15, 17.5, 9, 1]

current_min = x[0]
current_max = x[0]
for n in x[1:]:
    if n <= current_min:
        current_min = n
    if n >= current_max:
        current_max = n

print(current_min == min(x))
print(current_max == max(x))

# -------------------------------------------------------------------------- #

x = [8, 18, 6, 0, 15, 17.5, 9, 1]
n = len(x)

somme_moy = 0
for x_i in x:
    somme_moy += x_i
moyenne = somme_moy / n

somme_var = 0
for x_i in x:
    somme_var += (x_i - moyenne)**2
variance = somme_var / n

print(moyenne)
print(variance)

# Vérification avec les fonctions du package numpy
import numpy as np
print(np.mean(x))
print(np.var(x))

# -------------------------------------------------------------------------- #

print(list(range(10)))

print(list(range(10, 21)))

print(list(range(30, 41, 2)))

print(list(range(10, 100, 10)))

print(list(range(20, 9, -1)))

# -------------------------------------------------------------------------- #

juste_prix = 15

while True:
    print("Proposer un nombre entre 1 et 50.")
    p = input()
    p = int(p)
    if p < juste_prix:
        print("trop bas !")
    elif p > juste_prix:
        print("trop haut !")
    else:
        break

print("dans le mille !")

# -------------------------------------------------------------------------- #
