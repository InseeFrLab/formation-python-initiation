# -------------------------------------------------------------------------- #

# 1/ Ils n'ont que deux valeurs : True et False. Les autres types ont une infinité de valeurs possibles.

# 2/ Inputs : deux valeurs. Output : valeur booléenne.

# 3/ Tous types d'objets. En pratique cependant, il n'y a pas beaucoup de sens à
# comparer des objets de type différent, le résultat sera généralement `False`.

# 4/ L'opérateur `=` assigne une valeur à une variable.
# L'opérateur `==` teste l'égalité de deux objets.

# 5/ Inputs : deux valeurs booléennes, ou deux expressions qui renvoient des booléens.
# Output : valeur booléenne.

# 6/ L'opérateur `and` renvoie `True` si ses deux inputs valent `True`, 
# et `False` dans tous les autres cas.
# L'opérateur `or` renvoie `True` si au moins un de ses deux inputs vaut `True`,
# et `False` dans le cas où ils valent tous les deux `False`.
# L'opérateur `not` renvoie `False` si son input est `True`, et `True` sinon.

# 7/ Dans les deux cas, il s'agit de tests. On parle de condition lorsque les
# expressions sont utilisées dans le cadre des structures conditionnelles.

# 8/ L'instruction conditionnelle commence par une instruction `if`, `else` ou `elif`,
# qui se termine par `:`. Vient ensuite, indenté de un niveau, un bloc d'opérations
# qui ne s'exécute que si l'instruction vaut `True`.
# Le bloc se termine lorsque l'indentation revient à son niveau initial.

# 9/ Oui, les instructions conditionnelles peuvent s'imbriquer à l'infini (en théorie)
# Il faut simplement faire attention à respecter les niveaux d'indentation.

# 10/ Seule l'instruction `if` est obligatoire.

# -------------------------------------------------------------------------- #

# `'Simon' in ['simon', 'oceane', 'veronique']` : False
# `[1, 2, 3] == ['1', '2', '3']` : False
# `'x' != 'x'` : False
# `(9 > 5) and (3 == 5)` : False
# `(3 > 2 and 5 >= 1) or (5 <= 9 and 6 > 12)` : True
# `not (9 > 2*3)` : False
# `not (9 > (2*3))` : False
# `not ((7 > 8) or (5 <= 5))` : False
#  `(True and True) or (True == False)` : True
# `(not False) or (not True)` : True

# -------------------------------------------------------------------------- #

# x = 1
# l = ['c']
# Messages imprimés : 'Initialisation' et 'Négatif'

# x = 5
# l = ['b']
# Messages imprimés : 'Initialisation' et 'Négatif'

# x = 10
# l = ['a']
# Messages imprimés : 'Initialisation'

# -------------------------------------------------------------------------- #

people = ["Romuald", "Ursula", "Jean-Vincent", "Philomène"]

if len(people) > 3:
    print('Trop de monde.')

print(people)    
people.remove("Jean-Vincent")
print(people)

if len(people) > 3:
    print('Trop de monde.')

# -------------------------------------------------------------------------- #

p = input()
p = int(p)

if p < 15:
    print("trop bas !")
elif p > 15:
    print("trop haut !")
else:
    print("dans le mille !")

# -------------------------------------------------------------------------- #

# `0` : False
# `1` : True
# `12` : True
# `-1`: True
# '' (*string* vide): False
# ' ' (*string* contenant seulement un espace): True
# `[]` (liste vide): False
# `['']` (liste contenant seulement un *string* vide): True
# `{}`: False
# `{-1}`: True

# -------------------------------------------------------------------------- #

print(5 < 7 <= 8 < 18)

print(5 < 7 and 7 <= 8 and 8 < 18)

# Une comparaison en chaîne peut se réécrire avec des opérateurs `and`.
# Logique : il faut que chaque comparaison soit vraie pour que l'ensemble le
# soit aussi.
# En pratique, la version avec les `and` est même préférable pour la lisibilité.

# -------------------------------------------------------------------------- #

print(int(True))  
# un Booléen évalué comme entier donne bien la valeur binaire associée

print(True + 3)  
# les Booléens se comportent comme leur valeur entière associée dans les calculs

# -------------------------------------------------------------------------- #

print("a" > "b")
print("a" < "b")
print("abricot" > "avocat")
print("abricot" < "avocat")
print("1" > "2")
print("1" < "2")
print("A1" < "A2")

# La relation d'ordre utilisée est l'ordre alphanumérique : chaque caractère
# est pris individuellement, et les ordres sont A < Z et 1 < 9

# -------------------------------------------------------------------------- #

diff = 3 - 2.7

print(diff == 0.3)  # False, contre toute attente.

print(diff)
# En Python, les nombres flottants sont toujours des valeurs approchées.
# On peut donc avoir ce genre de surprise dans les calculs.

tolerance = 0.0001
new_test = (0.3 - tolerance) < diff < (0.3 + tolerance)
print(new_test)
# Ce test permet de tester l'égalité entre diff et 0.3 de manière approchée,
# en permettant une certaine tolérance dans la comparaison.

# -------------------------------------------------------------------------- #
