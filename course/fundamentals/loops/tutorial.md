---
title: "Boucles"
abstract: "Automatisation d'opérations répétitives à l'aide des boucles for et des boucles while."
---

Dans le tutoriel précédent, nous avons étudié les tests, qui permettent à un ordinateur de prendre des décisions selon des conditions spécifiées dans un programme. Nous allons à présent aller encore plus loin dans l'automatisation des opérations, grâce à la notion de **boucle**. Les boucles vont permettre de répéter plusieurs fois une instruction semblable sans avoir à réécrire le même code à chaque fois.

Pour illustrer cette idée, imaginons que l'on souhaite afficher chaque élément d'une liste. Pour l'instant, on ferait :

```python
gamme = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']

print(gamme[0])
print(gamme[1])
print(gamme[2])
```

Et ainsi de suite. On voit tout de suite qu'une telle opération serait impraticable pour une liste contenant des centaines d'éléments. Les boucles vont résoudre ce problème de manière élégante et efficiente.


## Boucles `for`


### Définition


Le premier type de boucles auquel nous allons nous intéresser est la boucle `for`. Une boucle `for` permet de parcourir les différents éléments contenus dans un objet dit **itérable**, et de réaliser des opérations avec ces éléments. Les objets itérables incluent notamment tous les objets séquentiels que nous avons vus jusqu'à présent : chaînes de caractères, listes, tuples, etc.

Illustrons le fonctionnement d'une boucle `for` en résolvant le problème exposé précédemment.

```python
for note in gamme:
    print(note)
```

### Syntaxe


Analysons la structure d'une boucle `for` :
- La première ligne spécifie une **instruction `for`**, et comme toute instruction en Python se termine par `:`. 
- Vient ensuite un **bloc d'instructions**, i.e. une suite d'opérations (une seule dans notre exemple) qui sera exécutée à chaque itération de la boucle. Ce bloc est visible par son **niveau d'indentation**, incrémenté de 1 par rapport à l'instruction. Le bloc s'arrête dès lors que l'indentation revient à son niveau initial.

Comme pour les instructions conditionnelles de type `if`/`else`, l'indentation est donc capitale. Si on l'oublie, Python renvoie une erreur.

```python
for note in gamme:
print(note)
```

### Fonctionnement


Regardons maintenant plus en détail ce que fait l'instruction `for`. Elle définit une **variable d'itération** (appelée `note` dans notre exemple), qui va parcourir les éléments de l'**itérateur** spécifié après le `in` (la liste `gamme` dans notre exemple). La syntaxe d'une boucle en Python se prête bien à une description littérale ; dans notre cas : "pour chaque note contenue dans la liste gamme, imprime la note".

Insistons sur le fait qu'une boucle définit une variable, sans que l'on ait besoin de passer par la syntaxe traditionnelle d'assignation `variable = valeur`. De plus, cette variable n'est pas supprimée une fois la boucle terminée, elle prend alors la valeur du dernier élément de l'itérateur.

```python
note
```

L'itérateur n'est pas nécessairement une liste, il peut être tout objet itérable. Cela inclut notamment tous les objets séquentiels que nous avons vu.

```python
for char in "YMCA":
    print(char)
    
print()  # Saut de ligne
    
t = (1, 2, 3, 4, 5)
for i in t:
    print(i*9)
```

La classe des objets itérables est cependant bien plus grande que les seuls objets séquentiels. Par exemple, on peut itérer sur les clés d'un dictionnaire, alors que l'on a vu dans un tutoriel précédent que ce n'était pas un objet séquentiel, puisqu'il n'y a pas de notion d'ordre dans un dictionnaire.

```python
inventaire = {'cafe': '500g', 'lait': '1,5L', 'cereales': '1kg'}
for key in inventaire:
    print(key)
    print(inventaire[key])
    print()  # Saut de ligne
```

### Itération sur des entiers avec la fonction `range`


En programmation, il est courant de vouloir itérer sur une suite d'entiers. Plutôt que de spécifier cette suite dans une liste, ce qui n'est pas très pratique si la suite est longue, on utilise pour ce faire la fonction `range(n)`. Celle-ci crée un objet itérable qui contient tous les entiers compris entre $0$ et $n-1$, et qui peut être utilisé dans le cadre d'une boucle.

Regardons par exemple comment on peut très simplement afficher une table de multiplication à l'aide de cette fonction.

```python
table = 9

for i in range(11):
    print(i, i*9)
```

### Itération sur les indices


On a vu qu'une boucle `for` avait pour principe d'itérer sur les *éléments* d'un itérable. Cependant, dans le cas d'un objet séquentiel comme une liste, on peut parfois vouloir itérer sur les *indices* de l'objet, afin de pouvoir manipuler à la fois les indices et les éléments contenus dans l'objet. Dans ce cas, la fonction `range` peut être utilisée en combinaison avec la fonction `len` pour créer un objet itérable qui contient exactement les indices de la liste initiale.

```python
gamme = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']

for i in range(len(gamme)):
    print("La note numéro " + str(i) + " de la gamme de do majeur est " + gamme[i])
```

Comme ce besoin est fréquent mais que le code ci-dessus n'est pas très lisible, il existe une fonction *built-in* de Python appelée `enumerate` qui permet d'itérer à la fois sur les objets et les indices. Il est donc préférable d'utiliser cette syntaxe, plus claire, et qui permet d'éviter certaines erreurs.

La fonction `enumerate` appliquée à un objet itérable renvoie un nouvel objet itérable qui contient l'ensemble des couples `(indice, élément)` contenus dans l'objet, sous forme de tuples. Comme c'est un objet de type particulier -- un générateur, que nous verrons dans un tutoriel plus avancé -- il faut lui appliquer la fonction `list` pour afficher son contenu.

```python
list(enumerate(gamme))
```

Regardons comment réécrire la boucle précédente avec cette nouvelle syntaxe.

```python
for i, note in enumerate(gamme):
    print("La note numéro " + str(i) + " de la gamme de do majeur est " + note)
```

NB : pour faire l'assignation de variables dans l'instruction `if`, on a utilisé une technique bien pratique que l'on avait déjà évoquée dans un exercice du tutoriel sur les listes et les tuples : le *tuple unpacking*. Illustrons le par un exemple :

```python
t = (1, 2, 3)
a, b, c = t
print(a)
print(b)
print(c)
```

## Boucles `while`


### Définition


Les boucles `while` fournissent une manière alternative de spécifier des procédures répétitives. L'idée n'est plus d'itérer sur un nombre d'objets fixé à l'avance, mais d'**itérer tant qu'une condition (test logique) est remplie**.

```python
i = 1
while i <= 5:
    print(i)
    i = i + 1
```

### Syntaxe


La différence essentielle avec la boucle `for` est l'instruction : c'est désormais une instruction `while`, suivie d'une condition (test), et comme toute instruction de `:`.

Pour le reste, le principe est le même : l'instruction `while` est suivi d'un bloc d'instructions, indenté d'un niveau, et qui s'exécute séquentiellement à chaque itération de la boucle.


### Critère d'arrêt


Une différence essentielle des boucles `while` par rapport aux boucles `for` tient au critère d'arrêt. Dans une boucle `for`, ce critère est clair : la boucle itère sur les éléments d'un objet itérable, nécessairement de taille finie. La boucle s'arrête donc lorsque chaque élément de l'itérable a été parcouru.

Dans une boucle `while` au contraire, le critère d'arrêt est donné par une condition logique, c'est donc l'utilisateur qui doit fixer le critère d'arrêt. Dans l'exemple, pour que la boucle s'arrête, il faut que la condition `i <= 5` devienne `False`, c'est à dire que `i` devienne strictement supérieur à $5$. On s'est assuré de cela en initialisant `i` à $1$ avant le début de la boucle, puis en incrémentant `i` d'une unité à chaque itération.

Que se passe-t-il si l'on oublie d'incrémenter `i` ? Le critère d'arrêt n'est jamais atteint, la boucle est donc infinie, et il faut utiliser le bouton "Stop" (carré noir) de Jupyter pour arrêter le programme en cours. Vérifions cela en incrémentant la mauvaise variable.

```python
i = 1
j = 1
while i <= 5:
    j = j + 1
```

```python
print(i)
print(j)
```

### L'instruction `break`


Une manière alternative de spécifier un critère d'arrêt est d'utiliser l'instruction `break`. Lorsque cette instruction est atteinte et exécutée, la boucle est immédiatement interrompue.

Illustrons son fonctionnement à l'aide d'un exemple. La première ligne crée une boucle infinie, dans la mesure où, par définition, `True` est toujours évalué à `True`. Le programme demande ensuite à l'utilisateur de taper un prénom, et ce infiniment jusqu'à que l'utilisateur tape le prénom attendu. Dans ce cas seulement, l'instruction `break` est atteinte et la boucle s'arrête. Le message "Bienvenue <votre_prenom>" s'affiche enfin, dans la mesure où le deuxième `print` n'est pas inclus dans la boucle.

```python
votre_prenom = "Romain"

while True:
    print("Veuillez entrer votre prénom.")
    prenom = input()
    if prenom == votre_prenom:
        break
print("Bienvenue " + votre_prenom)
```

Il est important de noter qu'une instruction `break` ne met fin qu'à la boucle de niveau directement supérieur à elle. Dans le cas d'une boucle à plusieurs niveaux, il est tout à fait possible que les opérations continuent même lorsqu'une instruction `break` a été atteinte. 

Illustrons ce principe avec un exemple.

```python
i = 0
while i <= 5:
    for j in range(5):
        if j == 2:
            print("Break.")
            break
    i += 1
```

A chaque itération de la boucle `while`, une boucle `for` est lancée, qui atteint une instruction `break` à la troisième itération (lorsque `j` vaut 2). Cela a pour effet de mettre fin à la boucle `for`, mais pas à la boucle `while`, qui exécute la suite de ses instructions (l'incrémentation de `i` d'une unité) avant de passer à l'itération suivante.


### L'instruction `continue`


L'instruction `continue` permet de passer à l'itération suivante de la boucle.

Agrémentons l'exemple précédent pour illustrer son fonctionnement. Tant qu'un prénom différent de celui attendu est rentré, l'instruction `continue` est évaluée, et le programme continue à demander un prénom à l'utilisateur. Lorsque le bon prénom est rentré, le programme demande à l'utilisateur de rentrer un mot de passe. Si le mot de passe est celui attendu, l'instruction `break` est atteinte et exécutée, la boucle s'arrête. En cas de mauvais mot de passe en revanche, la boucle redémarre au début du bloc d'exécution, il faut donc de nouveau rentrer un prénom avant le mot de passe.

```python
votre_prenom = ""

while True:
    print("Veuillez entrer votre prénom.")
    prenom = input()
    if prenom != votre_prenom:
        continue
    print("Veuillez entrer votre mot de passe.")
    mdp = input()
    if mdp == "insee2021":
        break
print("Bienvenue " + votre_prenom)
```

NB : le code ci-dessus à seulement valeur d'exemple. Comme on le verra dans un prochain tutoriel sur les bonnes pratiques de code, il ne faut **jamais écrire de secrets (mots de passe, tokens..) en clair dans son code.**


## Exercices


### Questions de compréhension


- 1/ Comment fonctionne une boucle `for` ?
- 2/ La variable d'itération définie lors d'une boucle `for` persiste-t-elle en mémoire une fois la boucle terminée ?
- 3/ Que fait la fonction `range` ? Pourquoi est-elle particulièrement utile dans le cadre des boucles `for` ?
- 4/ Que fait la fonction `enumerate` ? Pourquoi est-elle particulièrement utile dans le cadre des boucles `for` ?
- 5/ Comment fonctionne une boucle `while` ?
- 6/ Quand s'arrête une boucle `while` ? En quoi cela diffère-t-il des boucles `for` ? 
- 7/ Que fait l'instruction `break` ?
- 8/ Que fait l'instruction `continue` ?

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 3-33 solutions.py
```

### Prédiction de résultats de boucles `while`


Essayer de prédire ce que vont produire les boucles `while` suivantes, et vérifiez vos résultats.

```python
# 1.
i = 0
while i <= 10:
    print(i)
    
# 2.
a = 1
while (a < 10):
    a += 1
    if a == 5:
        break
    print("Condition d'arrêt atteinte.")
    
# 3.
while False:
    print("hello world")

# 4.
while True:
    print("hello world")
    break

# 5.
while 5 >= 3:
    continue
    print("hello world")
```

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 37-51 solutions.py
```

### Effet d'une erreur d'indentation


Source : [python.sdv.univ-paris-diderot.fr](https://python.sdv.univ-paris-diderot.fr/06_tests/)


Afin de visualiser l'importance de l'indentation dans les blocs d'instruction, essayez de prédire ce que vont respectivement retourner les deux programmes suivants. Lequel a l'effet attendu ?

```python
nombres = [4, 5, 6]
for nb in nombres:
    if nb == 5:
        print("Le test est vrai")
        print("car la variable nb vaut {nb}")
```

```python tags=[]
nombres = [4, 5, 6]
for nb in nombres:
    if nb == 5:
        print("Le test est vrai")
    print("car la variable nb vaut {nb}")
```

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 55-58 solutions.py
```

### Convertir une boucle `for` en boucle `while`


Réécrivez la boucle `for` suivante à l'aide d'une boucle `while`.

```python tags=[]
gamme = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']

for i, note in enumerate(gamme):
    print("La note numéro " + str(i) + " de la gamme de do majeur est " + note)
```

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 62-68 solutions.py
```

### Recherche d'un élément dans une liste


Soit un entier cible `n_cible` et une liste d'entiers `l` tels que définis dans la cellule suivante. A l'aide d'une boucle `for` et de la fonction `enumerate` :
- vérifier si l'entier cible est présent dans la liste `l`. 
- si oui, afficher le message 'Le nombre `n_cible` est à la position `i` de la liste', et mettre fin à la boucle.

```python
n_cible = 78

l = [12, 98, 65, 39, 78, 55, 119, 27, 33]
```

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 72-84 solutions.py
```

### Suite de Fibonacci

<!-- #region tags=[] -->
La suite de Fibonacci se définit de la manière suivante : 
- les deux premiers nombres sont 0 et 1
- chaque autre nombre de la suite s'obtient en additionnant les deux nombres qui le précèdent

Ecrire un programme permettant de calculer les $n$ premiers termes de la suite à l'aide d'une boucle `for`.
<!-- #endregion -->

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 88-96 solutions.py
```

### Dictionnaire des tables de multiplication

<!-- #region tags=[] -->
A l'aide de deux boucles `for` imbriquées, construire un dictionnaire `tables` permettant de réaliser les tables de multiplication jusqu'à la table de 12. Requêtez votre dictionnaire pour vérifier sa pertinence.

Voici quelques exemples de requête que doit renvoyer votre dictionnaire : 
- tables[2][3] -> 6
- tables[9][5] -> 45
- tables[12][7] -> 84
<!-- #endregion -->

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 100-109 solutions.py
```

### Calcul du minimum et du maximum d'une série "à la main"

<!-- #region tags=[] -->
Calculer le minimum et le maximum de la série de valeurs suivantes, sans utiliser les fonctions `min` et `max` de Python. 

x = [8, 18, 6, 0, 15, 17.5, 9, 1]
<!-- #endregion -->

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 113-124 solutions.py
```

### Calcul de moyenne et de variance "à la main"

<!-- #region tags=[] -->
Calculer la moyenne et la variance de la série de valeurs suivantes, sans utiliser des fonctions déjà codées : 

x = [8, 18, 6, 0, 15, 17.5, 9, 1]

Pour rappel, les formules sont :
- moyenne : $$\bar{x} = {\frac {1}{n}}\sum_{i=1}^{n}x_{i}$$
- variance : $$\sigma^2 = {\frac {1}{n}}\sum_{i=1}^{n} (x_{i}-\bar{x})^2$$

NB : 
- n à la puissance k s'écrit en Python `n**k`
- en pratique, il ne faut surtout pas essayer de recoder soi-même ce genre de fonctions, mais utiliser des fonctions issues de packages adaptés, comme `numpy`.
<!-- #endregion -->

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 128-147 solutions.py
```

### Usage avancé de la fonction `range`

<!-- #region tags=[] -->
Nous avons vu plus haut l'usage basique de la fonction `range` : `range(n)` crée un objet itérable qui contient l'ensemble des entiers de $0$ à $n-1$. Les usages possibles de cette fonction sont cependant plus complets, et parfois utiles dans le cadre de problèmes précis.

La syntaxe complète de la fonction est `range(start, stop, step)` où :
- `start` est l'entier à partir duquel commence la séquence d'entiers
- `stop` est l'entier avant lequel se termine la séquence d'entiers
- `step` est le pas, i.e. la valeur de l'incrément entre chaque entier de la séquence.

Seul le paramètre `stop` est obligatoire, c'est celui qui est utilisé lorsqu'on appelle `range(n)`.

En utilisant la fonction `range`, afficher :
- l'ensemble des entiers de 0 à 10 (10 exclu)
- l'ensemble des entiers de 10 à 20 (20 inclus)
- l'ensemble des nombres pairs compris entre 30 et 40 (40 inclus)
- l'ensemble des multiples de 10 entre 1 et 100 (100 exclu)
- l'ensemble des entiers de 10 à 20 (20 inclus), dans l'ordre inverse (de 20 à 10)
<!-- #endregion -->

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 151-159 solutions.py
```

### Le juste prix, version améliorée

<!-- #region tags=[] -->
Dans le précédent tutoriel, nous avons codé un jeu du juste prix. Mais il était un peu limité, puisqu'il fallait réexécuter le code à chaque étape du jeu. A l'aide de boucles, réécrivez le jeu de manière complètement automatique.

Rappel des règles : 

**En utilisant `input` et les instructions `if`, `elif` et `else`**, coder le programme suivant : 
- demander une valeur à l'utilisateur, qui sera stockée dans une variable `p`
- si `p` est strictement inférieur à $15$, imprimer (avec la fonction `print`) le message "trop bas !".
- si `p` est strictement supérieur à $15$, imprimer le message "trop haut !".
- si `p` est égal à $15$, imprimer le message "dans le mille !"

Attention, `input` renvoie par défaut une chaîne de caractère. Il faut donc convertir la valeur de `p` au format entier (via la fonction `int`) pour que le jeu fonctionne.
<!-- #endregion -->

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python tags=[]
# Exécuter cette cellule pour afficher la solution
%load -r 163-178 solutions.py
```

```python

```
