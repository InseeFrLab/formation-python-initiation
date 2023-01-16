---
title: "Types de base et variables"
abstract: "Découverte des types de base (nombres et chaînes de caractères) et des variables."
---

Dans ce premier TP, nous allons découvrir les objets les plus fondamentaux de Python : les **nombres** et les **chaînes de caractère**. Nous allons également voir comment l'on peut assigner des objets à des **variables**, afin de réaliser des opérations avec ces objets.

## Nombres

### Types de nombres

Python propose différents objets de type numérique. Dans ce tutoriel, on va s'intéresser aux deux types principalement utilisés :
- les entiers (type `int` pour *integer*)
- les réels (type `float` pour nombres à virgule flottante)

De manière générale, on utilise la fonction `type` pour imprimer le type d'un objet Python.


```python
type(3)
```


```python
type(3.14)
```

Les fonctions `float` et `int` peuvent être utilisées pour passer d'un type à l'autre.


```python
# Conversion en float
float(3)
```


```python
# Conversion en float
type(float(3))
```


```python
# Conversion en int
int(3.79)
```

Attention à la conversion *float* -> *int*, qui tronque la partie décimale.

Les *floats* peuvent par ailleurs être écrits en notation scientifique :


```python
2e3
```


```python
type(2e3)
```

### Opérations arithmétiques de base


```python
# Addition
8 + 9
```


```python
# Soustraction
5 - 2
```


```python
# Multiplication
2 * 6
```


```python
# Division
9 / 4
```


```python
# Division par 0
3 / 0
```

C'était bien sûr prévisible. Mais il n'est pas rare d'avoir de telles erreurs dans le cadre de calculs statistiques, notamment avec *NumPy* ou *Pandas*, produisant une erreur similaire qu'il faut alors débugger.


```python
# Division euclidienne : quotient
9 // 4
```


```python
# Division euclidienne : reste
9 % 4
```


```python
# Puissance
2 ** 5
```


```python
# Racine carrée
5 ** 0.5
```


```python
# Ordre des opérations : convention usuelle
2 + 5 * (10 - 4)
```

## Chaînes de charactères

Les chaînes de caractères (ou *strings*) sont utilisées pour stocker de l'information textuelle. Plus précisément, elles peuvent stocker tout caractère de type [Unicode](https://fr.wikipedia.org/wiki/Unicode), ce qui inclut les lettres des différentes langues, mais également la ponctuation, les chiffres, les smileys, etc.

Un *string* se définit en mettant l'information entre apostrophes ou entre guillemets (anglais). 

### Définition


```python
# Première manière 
'mot'
```


```python
# Deuxième manière
"ça fonctionne aussi"
```


```python
# Mais attention au mélange des deux !
'l'apostrophe, quelle catastrophe'
```

Erreur de syntaxe : la seconde apostrophe est comprise comme la fin du *string*, et Python ne sait pas interpréter le reste de la séquence.

Il faut donc varier en cas de besoin :


```python
"l'apostrophe, aucun problème"
```

Même chose en sens inverse :

```python
'les guillemets, "aucun problème"'
```

### La fonction `print`

Le travail avec les *strings* est l'occasion de découvrir la très pratique et très utilisée fonction `print`. Elle affiche simplement l'argument qu'on lui passe entre parenthèses **et** un retour à la ligne par défaut.

```python
# Affichage de la chaîne "moi"
"moi"
```

```python
# Affichage de la chaîne "moi" avec print
print("moi")
```

On a vu jusqu'à maintenant que l'on pouvait simplement exécuter une cellule pour afficher le contenu d'un *string*. Mais est-ce cela marche avec plusieurs *strings* ?


```python
# Qui va être affiché ?
"moi"
"non moi"
```

On voit là un comportement caractéristique des notebooks Jupyter : seule la dernière valeur renvoyée dans une cellule est affichée. La fonction `print` permet de s'affranchir de cette limite.


```python
# Et cette fois ?
print("moi")
print("moi aussi")
```

### Longueur d'une chaîne

La fonction `len` permet de compter le nombre de caractères d'un *string*, tous caractères inclus (lettres, chiffres, espaces, ponctuation...).


```python
len("J'ai 19 charactères")
```

Le type "caractère" n'existe pas en Python : un caractère seul est défini comme un *string* de taille 1.


```python
print(type("a"))
print(len("a"))
```

### Indexation

En Python, un *string* est une **séquence**, c'est à dire une suite de caractères dans un ordre spécifique. Par conséquent, chaque caractère d'un *string* est indexé (Python connaît sa position), et l'on peut utiliser cet index pour extraire des caractères particuliers, des sous-chaînes de caractères, etc.

En Python, on utilise les crochets `[]` pour appeler l'index d'une séquence. Plus précisément, l'index fonctionne sur le modèle suivant : `x[a:b:c]` renvoie un *sub-string* du *string* `x` où `a` est la position du caractère de départ, `b` la position du caractère d'arrivée plus 1, et `c` le pas de l'indexation. Tout cela sera plus clair avec les exemples suivants.

Note importante : **l'indexation commence à 0 en Python**.


```python
"une séquence que l'on va indexer"
```


```python
# Premier élémént
"une séquence que l'on va indexer"[0]
```


```python
# Deuxième élémént
"une séquence que l'on va indexer"[1]
```


```python
# Dernier élémént
"une séquence que l'on va indexer"[-1]
```


```python
# Extraire tout à partir d'un certain caractère
"une séquence que l'on va indexer"[4:]
```


```python
# Extraire tout jusqu'à un certain caractère
"une séquence que l'on va indexer"[:12]
```


```python
# Extraire un sub-string
"une séquence que l'on va indexer"[4:12]
```


```python
# Extraire tous les 2 caractères, à partir de la 4 ème position
"une séquence que l'on va indexer"[4::2]
```


```python
# Inverser une séquence
"une séquence que l'on va indexer"[::-1]
```

A retenir : c'est bien parce qu'un *string* est considéré comme une séquence par Python que l'on peut l'indexer. Par exemple, indexer un nombre n'a pas de sens, et renvoie donc une erreur.


```python
2[3]
```

### Quelques propriétés utiles


```python
# Concaténation de strings
"mon adresse est : " + "10 rue des Peupliers"
```


```python
# Répétition
"echo - " * 5
```

### Quelques méthodes utiles

Les différents objets Python ont généralement des **méthodes** dites *built-in* (standard), qui permettent d'effectuer des opérations de base à partir de l'objet. 

Nous verrons dans un prochain chapitre en quoi consistent précisément les méthodes en Python. Pour le moment, on peut retenir que les méthodes s'utilisent selon le format `objet.methode(parametres)` où les paramètres sont optionnels.


```python
# Mettre en majuscules
"sequence 850".upper()
```


```python
# Mettre en minuscules
"sequence 850".lower()
```


```python
# Séparer les mots selon les espaces
"une séquence    à séparer".split()
```


```python
# Séparer les mots selon un caractère arbitraire
"pratique pour faire des sous-séquences".split("-")
```


```python
# Utiliser les strings comme templates
"mon adresse est : {}".format("10 rue des Peupliers")
```

Tout ceci n'est qu'un aperçu des innombrables opérations possibles sur les *strings*. La [documentation officielle](https://docs.python.org/3/library/stdtypes.html#string-methods) liste l'ensemble des méthodes *built-in* disponibles. Les exercices du chapitre et les mini-projets de fin de partie seront l'occasion de découvrir d'autres utilisations.

## Variables

Jusqu'ici, nous avons dû définir à chaque fois notre objet avant de pouvoir lui appliquer une transformation. Comment faire si l'on veut réutiliser un objet et lui appliquer plusieurs transformations ? Ou faire des opérations à partir de différents objets ?

Pour cela, on va assigner les objets à des variables.

### Assignation et opérations

L'assignation se fait suivant le format : `nom_de_la_variable = objet`. Cela permet ensuite de réaliser des opérations à partir de ces variables.


```python
x = 5
x
```


```python
type(x)
```


```python
x + 5
```


```python
y = x + 2*x
y
```

Contrairement à d'autres langages de programmation, Python est dit *dynamiquement* typé : il est possible de réassigner une variable à un objet de type différent. Cela facilite la lecture et le développement, mais peut parfois générer des problèmes difficiles à débugger... Il faut donc toujours bien faire attention que le type de la variable est bien celui que l'on s'imagine manipuler.


```python
x = 3
x = "blabla"
type(x)
```

Il y a naturellement certaines contraintes sur les opérations selon les types des objets.


```python
x = "test"
y = 3
x + y
```

Il est par contre possible d'harmoniser les types en amont :

```python
x = "test"
y = 3
z = str(y)
x + z
```

### Incrémentation

Il est fréquent d'utiliser une variable comme un compteur, en l'incrémentant à chaque fois qu'un évènement donné apparaît par exemple.


```python
a = 0
print(a)
a = a +1
print(a)
```

Cette pratique est tellement fréquente qu'il existe des opérateurs spéciaux pour les opérations arithmétiques courantes.


```python
a = 0
a += 1
a
```


```python
b = 5
b *= 3
b
```

## Exercices

### Exercice 1

Afficher le type de x lorsque : 
- x = 3
- x = "test"
- x = 3.5


```python
# Tapez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 2-9 solutions.py
```

### Exercice 2



Calculer la somme des longueurs de chacune des chaînes de caractères suivantes : 
- "une première chaîne"
- "et une deuxième"
- "jamais deux sans trois"


```python
# Tapez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 12-16 solutions.py
```

### Exercice 3

Quel est le type adapté pour définir un code postal ?

Essayer de définir les codes postaux suivants au format `int` et au format `string` :
- 92120
- 02350

Que concluez-vous ?


```python
# Tapez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 19-26 solutions.py
```

### Exercice 4

Compter le nombre de fois où la lettre e est présente dans la chaîne suivante :
"Je fais un comptage des e."

**Indice** : on peut utiliser la méthode *built-in* [count](https://docs.python.org/fr/3/library/stdtypes.html#str.count).


```python
# Tapez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 29-30 solutions.py
```

### Exercice 5

Repérer la première position où la lettre e est présente dans la chaîne suivante : "Je fais un comptage des e."

**Indice** : on peut utiliser la méthode *built-in* [find](https://docs.python.org/fr/3/library/stdtypes.html#str.find).


```python
# Tapez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 33-34 solutions.py
```

### Exercice 6

Supprimer les espaces superflus au début et à la fin de la chaîne suivante :

**Indice** : on peut utiliser la méthode *built-in* [strip](https://docs.python.org/fr/3/library/stdtypes.html#str.strip).

```python
# Tapez votre réponse dans cette cellule
a = "    Un string très mal formatté.         "
```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 37-38 solutions.py
```

### Exercice 7

Le caractère `\` permet d'échapper (neutraliser) un caractère spécial au sein d'une chaîne de caractères. Trouvez comment ce caractère permet de résoudre le problème lié à l'utilisation de guillemets (ou d'apostrophes) dans une chaîne définie par des guillemets (apostrophe).

**Indice** : des exemples d'utilisation sont disponibles dans la [documentation officielle](https://docs.python.org/fr/3.8/reference/lexical_analysis.html#literals).


```python
# Tapez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 41 solutions.py
```

### Exercice 8

Réaliser la suite d'opérations suivantes à l'aide des opérateurs d'incrémentation, et imprimer la valeur finale :
- initialiser une variable à 1
- lui soustraire 5
- la multiplier par 4
- lui ajouter 22


```python
# Tapez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 44-48 solutions.py
```

### Exercice 9

Considérons les deux séquences suivantes :
- "nous sommes en"
- "2022"

Trouvez à partir du tutoriel deux manières différentes de les utiliser pour composer la séquence "nous sommes en 2022".

**Indice** : l'une des deux méthodes implique de modifier (légèrement) une des deux séquences.


```python
# Exécuter cette cellule pour afficher la solution
%load -r 51-56 solutions.py
```


```python

```
