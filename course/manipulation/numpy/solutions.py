# -------------------------------------------------------------------------- #

# 1/ Les calculs sont vectorisés, ce qui simplifie grandement la syntaxe
# et réduit donc les risques d'erreur. Par ailleurs, les calculs sont optimisés
# automatiquement par NumPy, ce qui accroît très fortement les performances.

# 2/ Les données contenues dans un array doivent être de type homogène.
# Un array a une taille fixée lors de sa création.

# 3/ Tous les objets sont interprétés comme des chaînes de caractères.

# 4/ Créer une liste et la convertir ensuite en array via la 
# fonction np.array.

# 5/ L'attribut shape d'un array renvoie un tuple qui contient la taille
# de chaque dimension, et donc également le nombre de dimensions.

# 6/ Il existe des fonctions qui effectuent ces opérations, mais elles ne
# sont pas très utilisées en pratique, dans la mesure où un array est de
# taille fixée lors de sa création.

# 7/ Un masque booléen est un array de valeurs booléennes (True et False),
# que l'on va utiliser pour sélectionner des éléments d'un autre array.
# C'est notamment très pratique pour sélectionner des éléments selon une
# condition (test).

# 8/ Lorsqu'on effectue une opération entre un array et une valeur de taille 1
# (typiquement, un entier ou un réel), l'opération est appliquée à chaque
# élément de l'array.

# 9/ Le paramètre axis sert à spécifier la dimension selon laquelle on 
# souhaite performer une agrégation (fonction math, stat..).

# -------------------------------------------------------------------------- #

X = np.arange(10, 21)

print(X[[1, 3, 4]])
print(X[1:])
print(X[1:-1])
print(X[:3])
print(X[-5:])
print(X[::2])
print(X[::-1])

# -------------------------------------------------------------------------- #

Y = np.arange(0, 25).reshape((5, 5))

print(Y[3, 4])
print(Y[1, :])
print(Y[:, 3])
print(Y[1:4, 1:4])
print(Y[np.arange(0, 5), np.arange(0, 5)])

# -------------------------------------------------------------------------- #

X = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

Y = np.array([[10,11,12],
              [13,14,15],
              [16,17,18]])

print(3 * X)
print()
print(Y / X)
print()
print(np.log(Y))
print()
print(np.square(X))
print()
print(Y @ X)
print()
print(Y.T)

# -------------------------------------------------------------------------- #

a = np.ones((18,))
print(a)
print()

b = np.zeros((2, 3, 5))
print(b)
print()

c = np.full((4, 3), fill_value=5)
print(c)
print()

d = np.eye(5)
print(d)
print()

e = np.arange(0, 100)
print(e)
print()

x = np.arange(0, 100, step=2)
print(x)
print()

y = np.linspace(2.0, 3.0, num=5)
print(y)
print()

# -------------------------------------------------------------------------- #

X = np.random.normal(0, np.sqrt(2), 10000)

print(np.mean(X), np.var(X))

# -------------------------------------------------------------------------- #

N = 1000
U = np.random.uniform(-1, 1, size=(N, N))

np.all((U >= -1) & (U <= 1))

# -------------------------------------------------------------------------- #

X = np.random.randint(0, 50, size=(6, 6))

# Première possibilité : via les masques booléens
A = np.zeros((6, 6))
A[X > 25] = 1

# Deuxième possibilité : via la fonction np.where
B = np.where(X > 25, 1, 0)

print(X)
print()
print(A)
print()
print(B)

# -------------------------------------------------------------------------- #

X = np.array([[1, 1, 1, 0, 0], [0, 0, 0, 0, 1], [1, 0, 0, 0, 1],
              [1, 0, 0, 0, 0], [0, 1, 1, 1, 1]])

def shoot(x, y):
    if np.any(X == 1):
        if X[x, y] == 1:
            print("Touché !")
            X[x, y] = 2
        else:
            print("Raté !")
        print(X)
        print()
    else:
        print("Fin de partie !")
        
shoot(0, 1)
shoot(1, 0)
shoot(0, 2)

# -------------------------------------------------------------------------- #

values = np.array(["21", "46", "47", "23", "66", "82", "82"])

categories, pos = np.unique(values, return_inverse=True)
n_values = values.shape[0]
n_categories = categories.shape[0]

ohe = np.zeros((n_values, n_categories))
ohe[np.arange(n_values), pos] = 1
ohe

# -------------------------------------------------------------------------- #
