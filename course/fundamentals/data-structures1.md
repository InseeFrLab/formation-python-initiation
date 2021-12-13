---
title: "Structures de données 1 : listes et tuples"
abstract: "Manipulation des structures de données séquentielles : listes et tuples"
---

Dans ce tutoriel, nous allons nous intéresser à des structures de données de base en Python : les **listes** et les **tuples**. Les structures de données peuvent être vues comme des conteneurs car ils permettent de stocker, d'organiser et d'accéder à des données. Les listes et les tuples sont des **conteneurs séquentiels** : les éléments qu'ils contiennent sont **ordonnés**, et leur position est enregistrée dans un **index**.

## Listes

### Définition

Dans le tutoriel précédent, nous avons vu que les chaînes de caractères étaient des **séquences** de caractères. Les listes sont également des séquences, c'est à dire des suites ordonnées d'éléments, mais plus générales : les éléments peuvent être de différente nature.

Les listes sont construites avec des crochets **[]**, et les éléments de la liste sont séparés par des virgules.

Assignons une première liste à une variable `a` :


```python
a = [1, 2, 3]
print(a)
```

La liste `a` est constituée d'entiers, mais une liste peut en pratique contenir des objets de tout type.


```python
b = ["une séquence", 56, "d"]
print(b)
```

Il est notamment possible de créer des listes de listes (et ainsi de suite), ce qui permet de créer des structures hiérarchiques de données.


```python
c = ["une séquence", 56, ["cette liste est imbriquée", 75, "o"]]
print(c)
```

Une liste imbriquée peut aussi être construite à partir de listes déjà définies.


```python
item1 = ["cafe", "500g"]
item2 = ["biscuits", "20"]
item3 = ["lait", "1L"]
inventaire = [item1, item2, item3]
print(inventaire)
```

On verra cependant dans le prochain tutoriel que les dictionnaires sont généralement des structures de données souvent plus adaptées que les listes pour représenter des données sous forme hiérarchique.

### Longueur d'une liste

Comme les chaînes de caractères, il est possible d'utiliser la fonction `len` pour compter le nombre d'éléments présents dans une liste.


```python
d = ["ceci", "est", "une", "liste"]
len(d)
```

### Indexation

Les listes étant des séquences, elles s'indexent de la même manière que les chaînes de caractères. Il est notamment important de se rappeler que la numérotation des positions commence à 0 en Python.


```python
# Troisième élément de la liste a
print(a[2])
```

Bien entendu, il n'est pas possible de demander un élément qui n'existe pas. Python renvoie une erreur nous indiquant que l'index demandé est hors limites.


```python
print(a[5])
```

Pour indexer une liste contenue dans une autre liste, on utilise une double indexation.


```python
# Premier élément de la sous-liste qui est à la deuxième position de la liste c
print(c[2][0])
```

En termes d'indexation, tout ce qui était possible sur les chaînes caractères l'est également avec les listes.


```python
# Tous les éléments à partir de la 1ère position
print(b[1:])
```


```python
# Inverser une liste
print(a[::-1])
```

### Modification d'éléments

Il est possible de modifier les éléments d'une liste manuellement, avec une syntaxe similaire à l'assignation de variable.


```python
# Réassignation d'un élément
d = [1, 2, "toto", 4]
d[2] = 3
print(d)
```


```python
# Substitution d'un élément
a = [1, 2, 3]
b = ["do", "re", "mi"]
b[0] = a[2]
print(b)
```

### Suppression d'éléments

L'instruction `del` permet de supprimer un élément par position. Les éléments qui se trouvaient après l'élément supprimé voient donc leur index réduit de 1.


```python
e = [1, "do", 6]
print(e)
print(e[2])

del e[1]
print(e)
print(e[1])
```

### Quelques propriétés utiles

Là encore, on retrouve des propriétés inhérentes aux séquences.


```python
# Concaténation
[1, 2, 3] + ["a", 12]
```


```python
# Réplication
["a", "b", "c"] * 3
```

### Quelques méthodes utiles

A l'instar des chaînes de caractères, les listes ont de nombreuses méthodes *built-in*, qui s'utilisent selon le format `objet.methode(parametres)`. Les plus utiles sont présentées ci-dessous ; d'autres méthodes seront utilisées dans le cadre des exercices de fin de section.


```python
# Ajouter un élément
a = [1, 2, 3]
a.append(4)
print(a)
```


```python
# Supprimer un élément par position
b = ["do", "re", "mi"]
b.pop(0)
print(b)
```


```python
# Supprimer un élément par valeur
b = ["do", "re", "mi"]
b.remove("mi")
print(b)
```


```python
# Inverser une liste
l = [1, 2, 3, 4, 5]
l.reverse()
print(l)
```


```python
# Trouver la position d'un élément
b = ["a", "b", "c", "d", "e"]
b.index("d")
```

## Tuples

### Définition

Les **tuples** sont une autre structure de données basique en Python, semblable à celle des listes dans leur fonctionnement. Il y a cependant une différence fondamentale : là où les éléments d'une liste peuvent être modifiés par position comme on l'a vu précédemment, les tuples sont **non-modifiables** (*immutable*). Ainsi, les éléments d'un tuple ne peuvent pas être modifiés sans redéfinir complètement le tuple. 

Quand est-il pertinent d'utiliser un tuple plutôt qu'une liste ? En pratique, les tuples sont beaucoup moins fréquemment utilisés que les listes. On utilise généralement les tuples pour **stocker des données qui n'ont pas vocation à être modifiées** lors de l'éxécution de notre programme Python. Cela permet de se prémunir contre des problèmes d'intégrité de données, c'est à dire de modification non-voulues des données d'entrée. On s'évite ainsi parfois de longues et pénibles séances de debugging.

Une autre différence, mineure celle-ci, est que les tuples s'écrivent avec des **parenthèses** au lieu des crochets. Les différents éléments sont toujours séparés par des virgules.


```python
x = (1, 2, "mi", "fa", 5)
x
```

Afin de bien faire la différence avec l'usage normal des parenthèses (dans les calculs ou pour délimiter les expressions), un tuple à un seul élément se définit avec une virgule après le premier élément.


```python
x1 = ("a", )
x1
```

Vérifions qu'il est impossible de modifier ou d'ajouter un élément à un tuple.


```python
t = ("do", "rez", "mi")
t[1] = "re"
```


```python
t = ("do", "re", "mi")
t.append("fa")
```

### Fonctionnement

Les tuples s'indexent comme les listes.


```python
print(x[0])
print(x[3:5])
```

Et peuvent également s'utiliser de manière hiérarchique.


```python
t1 = ("a", "b", "c")
t2 = (1, 2, 3)
t3 = (t1, "et", t2)

print(t3)
print(t3[2][1])
```

Les tuples partagent certaines méthodes *built-in* avec les listes : celles qui ne provoquent pas de modification de l'objet.


```python
t = ("do", "re", "mi")
t.index("do")
```


```python
t = ("do", "re", "mi", "re", "do")
t.count("re")
```

### Conversion

Les fonctions `list` et `tuple` permettent de convertir une liste en tuple et inversement.


```python
tuple(["do", "re", "mi"])
```


```python
list((1, 2, 3, 4, 5))
```

Ces fonctions ont d'autres usages en pratique, que nous verrons en exercice.

## Exercices

### Questions de compréhension

- Pourquoi dit-on des listes et des tuples que ce sont des conteneurs ?
- Quel est le point commun entre les listes et les chaînes de caractères ?
- Comment est enregistré l'ordre des éléments dans une séquence en Python ?
- Quelle est la différence fondamentale entre une liste et un tuple ?
- Dans quel cas aura-t-on plutôt intérêt à utiliser un tuple qu'une liste ?
- Peut-on avoir des éléments de types différents (ex : `int` et `string`) dans une même liste ? Dans un même tuple ?

Si les réponses à ces questions ne sont pas encore claires, n'hésitez pas à revenir au tutoriel, ou bien à tester par vous-même dans une cellule.

### Exercice

Créez 4 listes portant les noms des 4 saisons, contenant chacune les noms des mois associés (les mois de changement de saison seront attribué à la saison précédente). Puis créez une liste `saison` contenant les 4 listes. Essayez de prévoir ce que vont renvoyer (type de l'objet, nombre d'éléments et contenu) les instructions suivantes, puis vérifiez le. 

- `saisons`
- `saisons[0]`
- `saisons[0][0]`
- `saisons[1][-1]`
- `saisons[2][:3]`
- `saisons[1][1:2] + saisons[-1][3:]`
- `saisons[2:]`
- `saisons + saisons[0]`
- `saisons[3][::]`
- `saisons[3][::-1]`
- `saisons * 3`


```python
# Testez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 3-41 solutions.py
```

### Exercice

En ajoutant, supprimant et modifiant des éléments, nettoyez la liste suivante pour qu'elle contienne les notes de musique "do re mi fa sol la si" dans le bon ordre.

`l = ["do", "re", "re", "re", "fa", "sol", "solsi", "la"]`


```python
# Testez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 45-56 solutions.py
```

### Exercice

Proposez deux méthodes pour inverser la liste `["une", "liste", "quelconque"]`. Quelle est la différence majeure entre les deux méthodes ?


```python
# Testez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 60-75 solutions.py
```

### Exercice

Nous avons vu que l'instruction `ma_liste.pop(i)` supprimait le i-ème élément de la liste `ma_liste`. A l'aide de la documentation Python ou d'une recherche sur Google, déterminez le comportement par défault de cette méthode, c'est à dire ce qu'il se passe lorsqu'on ne donne aucun paramètre à la fonction `pop`. Vérifiez que vous observez bien ce comportement à l'aide d'un exemple de votre choix.


```python
# Testez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 79-81 solutions.py
```

### Exercice

Il existe beaucoup d'autres méthodes *built-in* pour les listes que celles que nous avons déjà vues. Par exemple : `min` et `max`. Vérifiez leur comportement : 
- sur une liste composée uniquement d'objets numériques (`int` et `float`) ;
- sur une liste composée uniquement de chaînes de caractères ;
- sur une liste composée d'un mélange d'objets numériques et textuels.


```python
# Testez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 85-91 solutions.py
```

### Exercice

Essayer de créer une liste vide. Vérifiez son type. Quel intérêt cela pourrait-il avoir ?


```python
# Testez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 95-107 solutions.py
```

### Exercice

Dans le tutoriel, nous avons vu les fonctions `list` et `tuple` qui permettent de passer d'un type à l'autre. En réalité, le fonctionnement de ces fonctions est plus subtil : le code `list(mon_objet)` renvoie la "version liste" de cet objet, de la même manière par exemple que `str(3)` renvoie `'3'`, c'est à dire la version *string* de l'entier `3`.

A l'aide de la fonction `list`, trouver les "versions liste" des objets suivants :
- le tuple `a = (1, 2, 3)` ;
- la chaîne de caractères `b = "bonjour"` ;
- l'entier `c = 5`


```python
# Testez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 111-125 solutions.py
```

### Exercice

Nous avons vu que les tuples avaient la particularité d'être non-modifiables. Mais est-ce que cette propriété se transfère de manière récursive ? Par exemple, est-ce qu'une liste contenue dans un tuple est-elle même non-modifiable ? Vérifiez à l'aide d'un exemple de votre choix.


```python
# Testez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 129-134 solutions.py
```

### Exercice

Lisez la partie concernant l'agrégation et la dissociation de séquences dans la [documentation Python](https://docs.python.org/fr/3/tutorial/datastructures.html#tuples-and-sequences). C'est une propriété souvent utilisée en pratique. Vérifiez qu'elle fonctionne sur les différents objets séquentiels que nous avons vus jusqu'à maintenant (chaînes de caractères, listes et tuples).


```python
# Testez votre réponse dans cette cellule

```


```python
# Exécuter cette cellule pour afficher la solution
%load -r 138-145 solutions.py
```


```python

```
