# -------------------------------------------------------------------------- #

printemps = ["avril", "mai", "juin"]
ete = ["juillet", "aout", "septembre"]
automne = ["octobre", "novembre", "decembre"]
hiver = ["janvier", "fevrier", "mars"]

saisons = [printemps, ete, automne, hiver]

l = saisons
print(type(l), len(l), l, "\n")

l = saisons[0]
print(type(l), len(l), l, "\n")

l = saisons[0][0]
print(type(l), len(l), l, "\n")

l = saisons[1][-1]
print(type(l), len(l), l, "\n")

l = saisons[2][:3]
print(type(l), len(l), l, "\n")

l = saisons[1][1:2] + saisons[-1][3:]
print(type(l), len(l), l, "\n")

l = saisons[2:]
print(type(l), len(l), l, "\n")

l = saisons + saisons[0]
print(type(l), len(l), l, "\n")

l = saisons[3][::]
print(type(l), len(l), l, "\n")

l = saisons[3][::-1]
print(type(l), len(l), l, "\n")

l = saisons * 3
print(type(l), len(l), l, "\n")

# -------------------------------------------------------------------------- #

l = ["do", "re", "re", "re", "fa", "sol", "solsi", "la"]

del l[1]  # On aurait aussi pu utiliser : l.pop(1)
l[2] = "mi"
del l[5]
l.append("si")

print(l)

# NB : cet exemple visait simplement à pratiquer la modification et la 
# suppression d'éléments. En pratique, il aurait été bien plus simple de
# directement créer la liste correcte.

# -------------------------------------------------------------------------- #

l1 = ["une", "liste", "quelconque"]
l1.reverse()
print(l1)

l2 = ["une", "liste", "quelconque"]
print(l2[::-1])
print(l2)

# La méthode `reverse` modifie la liste "en place" : la liste est durablement
# inversée après l'avoir exécutée. En revanche, la méthode qui inverse la liste
# via l'indexation renvoie une nouvelle liste et ne modifie pas l'existante.
# Pour que ce changement soit durable, il faudrait donc écraser la liste extistante,
# ou bien en créer une nouvelle.

l2 = l2[::-1]
print(l2)

# -------------------------------------------------------------------------- #

l = ["do", "re", "mi"]
l.pop()
print(l)

# -------------------------------------------------------------------------- #

a = [5, 800, 9.92, 0]
b = ["do", "re", "mi", "fa", "sol"]
c = [1, "melange", "des", 2]

print(min(a), max(a))
print(min(b),max(b))
print(min(c), max(c))  # Erreur : il n'existe pas de relation d'ordre pertinente

# -------------------------------------------------------------------------- #

l = []
print(l)
print(type(l))

# On peut donc effectivement créer une liste vide. Mais quel intérêt ?
# Un usage très fréquent est d'initialiser une liste, que l'on va ensuite 
# remplir au fur et à mesure des itérations d'une boucle. Les boucles feront 
# l'objet d'un prochain tutoriel ; mais voici un exemple simple d'un tel usage

for i in range(10):
    l.append(i)
    
print(l)

# -------------------------------------------------------------------------- #

a = (1, 2, 3)
print(list(a))

b = "bonjour"
print(list(b))

c = 5
print(list(c))

# La dernière expression renvoie une erreur : un entier n'est pas une séquence,
# une "version liste" n'a donc pas sens.
# On peut par contre bien entendu créer une liste avec pour seul élément 5
# (à exécuter dans une nouvelle cellule)
d = [5]
print(d)

# -------------------------------------------------------------------------- #

t = (1, 2, ["une", "liste"])
t[2][0] = 26
print(t)

# Verdict : la non-modifiabilité ne s'applique qu'au premier niveau.
# Elle ne se transfère pas aux sous-éléments.

# -------------------------------------------------------------------------- #

x, y, z = "abc"
print(y)

a, b, c, d = ["do", "re", "mi", "fa"]
print(c)

r, s, t, u = ("un", "tuple", "de", "test")
print(r)
