# -------------------------------------------------------------------------- #

# 1/ Non, les dictionnaires et les sets sont des collections non-ordonnées d'objet.

# 2/ Pour les valeurs : n'importe quel type d'objet.
# Pour les clés, on se restreint généralement aux chaînes de caractères et/ou entiers.

# 3/ Des données de type hiérarchique.

# 4/ Non, les clés sont uniques.

# 5/ Un set ne comporte que des éléments uniques et s'écrit avec des accolades.
# Il peut donc être vu comme un dictionnaire particulier ne contenant que des clés.

# 6/ Par définition, les éléments d'un set sont unique.
# Transformer une liste en set supprime donc les doublons.

# 7/ Du fait de l'unicité des éléments, Python peut garder en mémoire
# la position des différents éléments. Les tests d'appartenance sont donc
# fortement optimisés par rapport à lorsqu'on les effectue avec une liste.

# -------------------------------------------------------------------------- #

print(list(resultats.keys()))

print(resultats["6emeA"]["Miranda"]["notes"]["histoire"])

print(list(resultats["6emeB"]["Hypolyte"]["notes"].values()))

print(list(resultats["6emeB"].keys()))

print(list(resultats["6emeA"]["Miranda"]["notes"].keys()))

print(list(resultats["6emeA"]["Miranda"]["notes"].keys()) 
      + list(resultats["6emeB"]["Josephine"]["notes"].keys()))

print(list(resultats["6emeA"]["Miranda"]["notes"].values()) 
      + list(resultats["6emeB"]["Josephine"]["notes"].values()))

# -------------------------------------------------------------------------- #

cv = {
    "marc": {"poste": "manager", "experience": 7, "hobbies": ["couture", "frisbee"]},
    "miranda": {"poste": "ingénieure", "experience": 5, "hobbies": ["trekking"]}
}

print(len(cv))
print(len(cv["marc"]))

# La fonction len appliquée à un dictionnaire compte le nombre de clés

# -------------------------------------------------------------------------- #

inventaire = {'cafe': '500g', 'lait': '1,5L'}

print(inventaire.pop('cafe'))
print(inventaire.pop('orange', 'indisponible'))

# 1ère différence : lorsqu'on supprime une clé existante avec la méthode pop,
# la valeur associée à la clé est retournée.
# L'opération del ne retourne rien (en fait, un objet de type None)
# 
# 2ème différence : la méthode pop permet de spécifier une valeur par défaut
# en cas de non-existence de la clé, et donc ne retourne pas d'erreur dans ce cas.
# L'opération del retourne nécessairement une erreur lorsque la clé n'existe pas.

# -------------------------------------------------------------------------- #

inventaire = {'cafe': '500g', 'lait': '1,5L'}

inventaire['eau'] = inventaire.pop('lait')

inventaire

# -------------------------------------------------------------------------- #

animaux = {'chats': 5, 'chiens': 12}

print(animaux.keys())
print('chats' in animaux.keys()) 
# True : 'chats' est bien dans les clés de `animaux`

print()
print(animaux.values())
print('chats' in animaux.values()) 
# False : 'chats' n'est pas une valeur de `animaux`

print()
print(animaux)
print('chats' in animaux) 
# True : ce test est strictement équivalent à 'chats' in animaux.keys()

# -------------------------------------------------------------------------- #

inventaire = {'cafe': '500g', 'lait': '1,5L'}

cle = 'chocolat'

if cle in inventaire.keys():
    del inventaire[cle]
    
# On utilise un test d'appartenance : si la clé existe dans les clés
# du dictionnaire, elle est supprimée. Sinon, il ne se passe rien.
# Cette syntaxe deviendra plus claire avec le prochain tutoriel.

# -------------------------------------------------------------------------- #

x = "cdabcdabcdabcdabcdabcdabcdabcdabcdab"
l = list(set(x))
l.sort()
l

# -------------------------------------------------------------------------- #

cyrano1 = 'C’est un roc ! … c’est un pic ! … c’est un cap !'
cyrano2 = 'Que dis-je, c’est un cap ? … C’est une péninsule !'

# Question 1

inter = list(set(cyrano1) & set(cyrano2))
print(inter)

# Question 2

union = list(set(cyrano1) | set(cyrano2))
print(union)

# -------------------------------------------------------------------------- #

x = ['a', 'b', 'c', 'd'] * 1000000
print(x[:10])

x_set = set(x)
print(x_set)

%time 'e' in x
%time 'e' in x_set

# Le test d'appartenance initial se chiffre en millisecondes.
# Celui réalisé sur le set se chiffre en microsecondes.
# Le test est beaucoup plus rapide lorsqu'on convertit en set au préalable.

# -------------------------------------------------------------------------- #
