---
title: "Fonctions"
abstract: "Rendre son code mieux structuré et plus lisible avec les fonctions."
---

Dans les précédents tutoriels, nous avons étudié le fonctionnement des tests et des boucles, qui permettent de rédiger des programmes Python qui prennent des décisions automatisées. En pratique, un programme va généralement être constitué de différents blocs, qui exécutent chacun une action ou un groupe d'actions (ex : import des données, nettoyage des données, modélisation statistique, etc.). Par ailleurs, certaines de ces actions sont amenées à être répétées avec une légère différence au fil d'un programme (ex : importer plusieurs jeux de données différents). Il va être utile de modéliser chacune de ces actions par une **fonction**, sorte de mini-programme au sein du programme global. Utiliser des fonctions est une **bonne pratique** de programmation, dans la mesure où elles rendent plus explicite la structure logique du code et permettent de réduire la duplication de code.


## Définition


Une **fonction** peut être définie comme un bloc de code structuré qui : 
- prend un ensemble d'**arguments** (des objets Python) en entrée
- effectue une **action spécifique** via un ensemble d'instructions
- **renvoie** un résultat (un objet Python) en sortie

Nous avons déjà vu et utilisé un certains nombres de fonctions dans les tutoriels précédents (`range`, `len`, etc.). Nous avons également utilisé des **méthodes**, qui sont simplement des fonctions *attachées* à un type d'objet particulier. Utilisons une fonction bien connue pour illustrer leur fonctionnement général.

```python
len('do re mi fa sol')
```

Dans cet exemple, la fonction `len` :
- prend un argument en entrée (une chaîne de caractères)
- calcule le nombre de caractères présent dans cette chaîne
- renvoie ce nombre en sortie

L'"ensemble d'instructions" qui permettent de calculer la longueur de la chaîne n'est pas connu. En tant qu'utilisateur, on a seulement besoin de savoir ce que prend la fonction en entrée et ce qu'elle renvoie en sortie. Cela vaut pour les cas dans lesquels on utilise des fonctions natives de Python ou bien des fonctions issus de librairies Python auxquelles on fait confiance. On parle de "boîtes noires" pour caractériser de telles fonctions.

En pratique, on va vouloir définir ses propres fonctions pour structurer son code et le réutiliser dans les analyses. 


## Syntaxe


L'instruction `def` permet de définir une fonction.

```python
def accueil(prenom):
    msg = "Salutations " + prenom + " !"
    return msg
```

Analysons la syntaxe de la definition d'une fonction : 
- une instruction `def` qui :
    - spécifie le nom de la fonction (ici, `accueil`)
    - spécifie les arguments attendus entre parenthèse (ici, un seul argument : `prenom`)
    - se termine par `:` comme les différentes instructions que nous avons vues
- un ensemble d'opérations qui seront effectuées par la fonction, qui doivent être indentées d'un niveau par rapport à l'instruction `def`
- une instruction `return`, qui spécifie ce que la fonction va renvoyer lorsqu'elle sera appelée (ici, le contenu de la variable `msg`).


Le fait de **définir** une fonction comme ci-dessus revient à rendre disponible dans l'environnement Python le code de la fonction. Ce n'est que lorsque celle-ci est **appelée** dans le code, avec des arguments, que le code contenu est exécuté et produit un résultat.

```python
accueil("Miranda")
```

Comme expliqué en introduction, tout l'intérêt d'une fonction est de pouvoir réutiliser du code sans avoir à le dupliquer dans le programme.

```python
accueil("Romuald")
```

## Passage d'arguments


### Principe


Lorsqu'on appelle une fonction en lui spécifiant des arguments, on dit qu'on lui "passe" des arguments. Ces arguments deviennent alors des variables qui peuvent être utilisées dans le contexte de la fonction. A l'inverse d'une boucle `for` par exemple, les variables créées ne persistent pas après l'appel de la fonction

```python
def addition(x, y):
    return x + y
```

```python
addition(5, 3)
```

```python
x  # La variable ne persiste pas en mémoire après l'appel de la fonction
```

NB : on verra plus en détails ce comportement plus loin dans le tutoriel, à travers les concepts de variables globales et de variables locales.


### Nombre d'arguments


Le nombre d'arguments que l'on peut passer à une fonction est variable. En toute rigueur, il est possible de définir une fonction qui n'a besoin d'aucun argument, même si c'est rarement utile en pratique.

```python tags=[]
def neuf():
    return 9
```

```python tags=[]
a = neuf()
a
```

### Passage par position et passage par mot-clé


En Python, les fonctions admettent deux modes de passage des arguments : 
- le **passage par position**, qui correspond à celui que nous avons vu dans tous les exemples précédents : les arguments sont passés à la fonction dans l'ordre dans lequel ils ont été définis, sans avoir à préciser le nom du paramètre.
- le **passage par mot-clé** : on précise le nom du paramètre lors du passage de l'argument, ce qui permet de ne pas avoir à suivre l'ordre indiqué lors de la définition.

Illustrons cette différence à partir d'une fonction qui réalise simplement une division.

```python
def division(x, y):
    return x / y
```

```python
division(4, 2)  # Passage par position
```

```python
division(x=4, y=2)  # Passage par mot-clé
```

Dans le cas du passage par position, le respect de l'ordre est impératif.

```python
print(division(0, 5))
print(division(5, 0))
```

Dans le cas du passage par mot-clé, l'ordre n'a plus d'importance.

```python
print(division(x=0, y=5))
print(division(y=5, x=0))
```

### Arguments obligatoires et arguments optionnels


Lorsqu'on définit une fonction, il est fréquent de vouloir faire cohabiter des arguments que doit absolument spécifier l'utilisateur, et des arguments optionnels qui spécifient un comportement par défaut de la fonction, mais peuvent également être modifiés si nécessaire. 

Regardons par exemple comment on peut modifier le comportement de la fonction `print` à l'aide d'un argument optionnel.

```python
print("bonjour")
print("bonjour")
```

```python
print("bonjour", end=' ')
print("bonjour")
```

On a modifié le comportement du premier appel à `print` via le paramètre optionnel `end`. Par défaut, cette valeur est fixée à `'\n'`, soit un retour à la ligne. On l'a modifié dans la deuxième cellule à un espace, d'où la différence de résultat.

Cet exemple illustre également le lien entre le caractère obligatoire ou non d'un argument et sa modalité de passage :
- en général, les **arguments obligatoires** sont **passés par position**. Ils peuvent également être passés par mot-clé, mais dans la mesure où ils sont "attendus", on les passe généralement par position pour être plus concis
- les **arguments optionnels** doivent être **passés par mot-clé**, afin de bien marquer qu'on modifie le comportement par défaut de la fonction


Comment spécifier qu'un argument est optionnel lorsqu'on définit une fonction soi-même ? Simplement en spécifiant une valeur par défaut de l'argument. Par exemple, construisons une fonction qui concatène deux chaînes de caractères, et laisse à l'utilisateur l'option de spécifier un séparateur.

```python
def concat_string(str1, str2, sep=''):
    return str1 + sep + str2
```

```python
concat_string('bonjour', 'bonjour')  # Comportement par défaut
```

```python
concat_string('bonjour', 'bonjour', sep=', ')  # Comportement modifié
```

Cet exemple illustre également la règle lorsqu'on a un mélange d'arguments positionnels et par mot-clé : **les arguments positionnels doivent toujours être placés avant les arguments par mot-clé**.


## Renvoi de résultats


### Principe


On a vu :
- que toute fonction renvoie un résultat en sortie
- que l'instruction `return` permet de spécifier ce résultat

Lorsque la fonction est appelée, elle est évaluée à la valeur spécifiée par `return`, et cette valeur peut alors être récupérée dans une variable et utilisée dans des calculs ultérieurs, et ainsi de suite.

```python
def division(x, y):
    return x / y
```

```python
a = division(4, 2)
b = division(9, 3)
division(a, b)  # 2 / 3
```

Remarque importante : **lorsqu'une instruction return est atteinte dans une fonction, le reste de la fonction n'est pas exécuté**.

```python
def test(x):
    return x
    print("vais-je être affiché ?")
    
test(3)
```

### La valeur `None`


Une fonction renvoie nécessairement un résultat lorsqu'elle est appelée... mais que se passe-t-il si l'on ne spécifie pas d'instruction `return` ?

```python
def accueil(prenom):
    print("Salutations " + prenom + " !")
    
x = accueil("Léontine")
print(x)
print(type(x))
```

Comme attendu, la fonction a imprimé un message de bienvenue dans la console. Mais on n'a pas spécifié de valeur à retourner. Comme un objet doit malgré tout être retourné par définition, Python renvoie la valeur `None`, qui est un objet particulier, de type `NoneType`, et qui représente l'absence de valeur. Son seul intérêt est de bien marquer la différence entre une valeur réelle et l'absence de valeur.

Pour tester si un objet a pour valeur `None`, on utilise une syntaxe particulière : 

```python
x is None  # et non pas x == None
```

### Renvoyer plusieurs résultats


Une fonction renvoie par définition **un** résultat, qui peut être tout objet Python. Comment faire si l'on souhaite renvoyer plusieurs résultats ? On peut simplement enregistrer les différents résultats dans un conteneur (liste, tuple, dictionnaire, etc.), qui peut lui contenir un grand nombre d'objets.

En pratique, il est très fréquent de renvoyer un *tuple* lorsque l'on souhaite renvoyer plusieurs objets. En effet, les *tuples* ont la propriété de *tuple unpacking*, que nous avons vues à plusieurs reprises dans les précédents tutoriels. Cette propriété rend possible une syntaxe très pratique et élégante pour l'assignation des résultats d'une fonction à des variables.

```python
def puissances(x):
    return x**2, x**3, x**4

a, b, c = puissances(2)

print(a)
print(b)
print(c)
```

## Variables locales et variables globales


Nous avons vu en introduction que les fonctions pouvaient être vues comme des mini-programmes dans un programme global. Cette interprétation nous donne l'occasion d'aborder rapidement la notion de *scope* (contexte) en Python. Un *scope* est une sorte de conteneur à objets Python, auxquels il est possible d'accéder seulement dans le cadre de ce *scope*. 

Tous les objets (variables, fonctions, etc.) que l'on définit lors d'une session Python sont enregistrés dans le ***scope* global** de Python. Ces objets peuvent alors être accédés à n'importe quel endroit du programme, y compris au sein d'une fonction. Lorsque c'est le cas, on parle de **variables globales**.

```python
x = 5  # variable globale

def ajoute(y):
    return x + y

ajoute(6)
```

La variable `x` n'a pas été passée en argument à la fonction `ajoute` ni été définie dans le cadre de cette fonction. Pourtant, on peut l'appeler au sein de la fonction. Cela permet de partager des éléments entre plusieurs fonctions. 


En revanche, les arguments passés à une fonction ou bien les variables définies dans le cadre d'une fonction sont des **variables locales** : elles n'existent que dans le contexte spécifique de la fonction, et ne peuvent pas être réutilisées une fois que celle-ci s'est exécutée.

```python
def ajoute(y):
    z = 5  # variable locale
    return z + y

ajoute(6)
print(z)
```

Au sein d'un contexte donné, chaque variable est unique. En revanche, il est possible d'avoir des variables qui portent le même nom dans des contextes différents. Regardons par exemple ce qui se passe lorsque l'on crée une variable dans le contexte d'une fonction, alors qu'elle existe déjà dans le contexte global.

```python
x = 5  # variable globale

def ajoute(y):
    x = 10
    return x + y

ajoute(6)
```

C'est un bon exemple d'un principe plus général : **c'est toujours le contexte le plus local qui prime**. Lorsque Python effectue l'opération `x + y`, il va chercher les valeurs de `x` et de `y` d'abord dans le contexte local, puis, seulement s'il ne les trouve pas, dans le contexte supérieur -- en l'occurence, le contexte global.


NB : on verra dans un prochain tutoriel sur les bonnes pratiques qu'**il est préférable de limiter au strict minimum l'utilisation de variables globales**, car elles réduisent la reproductibilité des analyses.


## Exercices


### Questions de compréhension


- 1/ Pourquoi dit-on que l'utilisation de fonctions dans un programme est une bonne pratique de développement ?
- 2/ Quelles sont les trois caractéristiques d'une fonction ?
- 3/ Qu'est-ce qu'une fonction "boîte noire" ? A quelles autres fonctions s'oppose-t-elle ?
- 4/ Que se passe-t-il quand on définit une fonction ? Et quand on l'appelle ?
- 5/ Combien d'arguments peut-on passer à une fonction ?
- 6/ Quelles sont les deux modalités de passage d'arguments à une fonction ?
- 7/ Quelle est l'utilité de passer des arguments optionnels à une fonction ?
- 8/ Dans quel ordre doivent être passés les arguments d'une fonction si celle-ci a à la fois des arguments obligatoires et optionnels ?
- 9/ Existe-il des fonctions qui ne renvoient rien ?
- 10/ Une fonction peut-elle renvoyer plusieurs objets ?
- 11/ Que deviennent les variables du *scope* local d'une fonction une fois que la fonction a été appelée ?

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 3-38 solutions.py
```

### Fonction puissance


Créer une fonction `puissance` qui prend en entrée deux nombres `x` et `y` et renvoie la fonction puissance $x^y$.

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 42-45 solutions.py
```

### Prédiction de valeurs retournées par des fonctions


Soit `x = 5` et `y = 3` des arguments que l'on passe à chacune des fonctions définies dans la cellule suivante. Prédire ce que vont retourner les fonctions (valeur et `type` de l'objet), et vérifier vos réponses.

```python
def f1(x):
    return x

def f2(x):
    return ''

def f3(x):
    print("Hello World")
    
def f4(x, y):
    print(x + y)
    
def f5(x, y):
    x + y
    
def f6(x, y):
    if x >= 3 and y < 9:
        return 'test ok'
    else:
        return 'test not ok'
    
def f7(x, y):
    return f6(2, 8)

def f8(x, y, z):
    return x + y + z

def f9(x, y, z=5):
    return x + y + z
```

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 49-65 solutions.py
```

### Variables globales et variables locales


Que vaut la variable `total` dans le programme suivant ?

```python tags=[]
z = 3

def f1(x, y):
    z = 5
    return x + y + z

def f2(x, y, z=1):
    return x + y + z

def f3(x, y):
    return x + y + z

total = f1(2, 3) + f2(3, 1) + f3(1, 0)
print(total)
```

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 69-93 solutions.py
```

### Calculatrice

<!-- #region tags=[] -->
Ecrire une fonction `calculatrice` qui :
- prend deux nombres en entrée
- renvoie l'addition, la soustraction, la multiplication et la division de ces deux nombres en sortie

Utiliser la propriété de *tuple unpacking* pour assigner les résultats à des variables en une seule ligne.
<!-- #endregion -->

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 97-101 solutions.py
```

### Dédupliquer une liste

<!-- #region tags=[] -->
Ecrire une fonction qui :
- prend en entrée une liste d'éléments quelconques
- renvoie une nouvelle liste constituée des éléments uniques de la liste initiale
- permet via un paramètre optionnel de trier ou non la liste finale par ordre alphanumérique. Le comportement par défaut doit être de ne pas trier.

Indice : la procédure a été abordée dans le tutoriel sur les dictionnaires et les sets.
<!-- #endregion -->

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 105-113 solutions.py
```

### Multiplier les éléments d'une liste

<!-- #region tags=[] -->
Ecrire une fonction qui :
- prend en entrée une liste de nombres
- imprime : "Il y a $n$ nombres dans la liste." avec $n$ le nombre effectif
- multiplie tous les éléments de la liste (sans utiliser de fonction pré-codée)
- retourne le résultat
<!-- #endregion -->

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 117-125 solutions.py
```

### Variance dans une population et variance dans un échantillon

<!-- #region tags=[] -->
Dans un exercice du précédent tutoriel, nous avons codé "à la main" le calcul de la variance d'une liste de nombres, à partir de la formule : $$\sigma^2 = {\frac {1}{n}}\sum_{i=1}^{n} (x_{i}-\bar{x})^2$$

En toute rigueur, cette formule est valide lorsqu'on calcule la **variance en population complète**. Si l'on n'observe qu'un échantillon de la population, on ne calcule pas la variance mais on l'estime, et il faut alors utiliser la formule suivante pour obtenir un **estimateur sans biais de la vraie variance** : $$s^2 = {\frac {1}{n-1}}\sum_{i=1}^{n} (x_{i}-\bar{x})^2$$.

Pour tenir compte de cette distinction :
- coder une fonction `mean`  qui calcule la moyenne comme dans l'exercice du tutoriel précédent
- coder une fonction `var`  qui calcule la variance comme dans l'exercice du tutoriel précédent (en appelant la fonction `mean` pour calculer la moyenne)
- modifier la fonction `var` afin de permettre à l'utilisateur de choisir la méthode de calcul via un paramètre optionnel `mode` (valeur par défaut : 'population' pour le calcul via la formule en population ; valeur alternative : 'sample' pour le calcul via la formule en échantillon)

Comparer les valeurs obtenues dans les deux cas avec ce que renvoie la fonction *black box* `var` de la librarie `numpy` (cf. corrigé de l'exercice du tutoriel précédent pour la syntaxe, et voir la [doc](https://numpy.org/doc/stable/reference/generated/numpy.var.html) de la fonction et en particulier le paramètre `ddof` pour faire varier la méthode de calcul).
<!-- #endregion -->

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 129-158 solutions.py
```

### Fonctions récursives : factorielle

<!-- #region tags=[] -->
Les fonctions récursives sont des fonctions qui s'appellent elles-mêmes dans le corps de la fonction, ce qui entraîne des appels infinis jusqu'à atteindre un critère d'arrêt.

Un bon exemple de fonction récursive est la fonction qui calcule la factorielle d'un entier. La factorielle d'un entier naturel $n$ est le produit des nombres entiers strictement positifs inférieurs ou égaux à n. Par exemple : $5! = 5*4*3*2*1 = 120$.

Coder cette fonction et vérifier qu'elle fonctionne correctement.
<!-- #endregion -->

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 162-169 solutions.py
```


