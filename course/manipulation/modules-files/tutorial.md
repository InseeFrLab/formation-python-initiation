---
title: "Manipulation de fichiers"
abstract: "Manipulation de fichiers externes : import de modules et lecture/écriture de fichiers texte."
---

Dans les tutoriels précédents, nous avons utilisé systématiquement des variables pour stocker des données et réaliser des opérations sur celles-ci. Cette façon de faire peut suffire dans le cadre d'une session Python donnée, comme ici dans un notebook Jupyter ou bien dans un programme. 

Mais que se passe-t-il par exemple si l'on souhaite conserver les sorties des calculs réalisés ou bien des données transformées une fois la session terminée ? Il nous faut alors sauvegarder ces éléments dans un fichier, à un endroit où ces données vont persister dans le temps en vue d'une utilisation ultérieure. Dans ce tutoriel, nous allons voir comment **lire et écrire des fichiers avec Python**.


## Quelques notions sur les modules et les *packages*


Avant de parler de manipulation de fichiers, nous devons faire un bref détour par le monde des modules et des ***packages*** (librairies). 

Jusqu'à maintenant, nous avons essentiellement utilisé des objets et des instructions standards de Python, qui ne nécessitaient donc pas d'import tiers. Dans ce tutoriel et tous ceux qui vont suivre, nous allons réaliser des opérations plus complexes (intéragir avec un système de fichiers, faire du calcul vectoriel, manipuler des données tabulaires, etc.) qu'il serait très coûteux, inefficient, et avec un potentiel d'erreur énorme, de coder à la main en utilisant les objets de base de Python. 

C'est pourquoi nous allons utiliser des *packages*, sortes de boîtes à outils  remplies de **fonctions** et de **classes** développées par d'autres (généralement de manière communautaire) et qui permettent de réaliser des opérations complexes à moindre coût.


### Terminologie


Commençons par quelques brefs éléments de terminologie pour bien se repérer dans l'écosystème Python : 
- un **module** est un fichier texte (portant l'extension .py pour bien marquer le lien à Python) contenant un ensemble de définitions (de **classes**, de **fonctions**) et d'instructions, que l'on peut importer dans un environnement Python afin de les utiliser.
- un **package** est un ensemble de modules réunis dans un même répertoire

Par exemple, nous allons voir en détails dans la prochaine partie l'utilisation de `numpy`. `numpy` est un *package* qui permet de faire du calcul scientifique sur des objets multidimensionnels. Pour ce faire, `numpy` met à disposition un nombre gigantesque de fonctions et d'outils. Toutes les mettre dans un seul et même module serait franchement illisible. Ainsi, `numpy` est structuré en différents modules qui groupent les fonctions réalisant des opérations similaires : les fonctions générant de l'aléatoire dans le module `random`, celles réalisant de l'algèbre linéaire dans le module `linalg`, etc.


### Import de module


Pour pouvoir exploiter les fonctions d'un module et les différents modules qui constituent un *package*, il nous faut en premier lieu les importer.

La syntaxe est très simple, illustrons là à travers un exemple.

```python
import random
random.randint(0, 100)
```

Nous avons importé le module `random` (complet) de la librairie standard de Python via l'instruction `import`. Ensuite, nous avons fait appel à la fonction `randint` contenue dans le module `random`, qui renvoie un nombre aléatoire entre `a` et `b` ses paramètres.


On aurait pu également importer *seulement* la fonction `randint` en utilisant la syntaxe `from module import fonction`. Il n'est alors plus nécessaire de spécifier le nom du module lorsqu'on appelle la fonction.

```python
from random import randint
randint(0, 100)
```

Enfin, il arrive parfois de voir la syntaxe `from module import *` (`*` s'appelle le *wildcard*) qui a pour effet d'importer en mémoire *toutes* les fonctions du module. Nous verrons cependant dans le chapitre sur les bonnes pratiques que ce n'est pas une bonne idée en général.


### Import de *package*


Un *package* est simplement une collection de modules, structurée selon une arborescence. La syntaxe pour importer un *package* est analogue à celle pour importer un module, mais généralement plus longue.

Par exemple, regardons à nouveau comment utiliser la fonction `randint`, mais cette fois celle de `numpy` (qui fait la même chose).

```python
import numpy
```

```python
numpy.random.randint(0, 100)
```

On a importé le package `numpy`, qui nous a permis d'accéder via son module `random` à la fonction `randint`. Là encore, on aurait pu importer directement la fonction.

```python
from numpy.random import randint
```

```python
randint(0, 100)
```

En pratique, la première syntaxe est préférable : il est toujours plus lisible de montrer explicitement d'où vient la fonction que l'on appelle. Pour réduire la verbosité, il est fréquent de donner un ***alias*** aux packages que l'on importe. Voici les trois plus fréquents, que l'on rencontrera très souvent dans les tutoriels du prochain chapitre sur la manipulation de données. 

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

On peut alors utiliser ces *alias* pour appeler des modules et des fonctions.

```python
x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x))
```

### Installation de *packages*


L'installation de *packages* tiers en Python est un sujet à la fois très simple et très complexe. Très simple car la syntaxe strictement nécessaire pour installer un *package* dans un notebook Jupyter se résume à `!pip install nom_du_package` (le `!` permettant d'envoyer la commande au terminal). Mais très complexe dans la mesure où beaucoup de considérations techniques interviennent derrière cette simple commande (environnement d'éxécution, choix du gestionnaire de *packages*, gestion des dépendances, etc.). En l'occurence, tous les *packages* nécessaires au cours de cette formation sont déjà installés. Nous reviendrons plus en détails sur ce sujet dans la dernière partie sur les bonnes pratiques de développement à adopter en Python.


## Manipulation de fichiers


### Intéragir avec le système de fichiers local


Pour pouvoir lire et écrire des fichiers avec Python, il nous faut d'abord comprendre comment ceux-ci sont représentés sur le système de fichiers (*file system*) local, et comment Python interagit avec ce dernier. 

**Le module pathlib**

Pour ce faire, nous allons utiliser de manière répétée le module `pathlib` et en particulier la classe `Path`. Ce module permet d'intéragir avec le système de fichiers sous forme d'objets, en manipulant des attributs et leurs méthodes. Pas de panique, nous avons vu tout ce qu'il nous fallait savoir à ce propos dans le précédent tutoriel.

```python
from pathlib import Path
```

**Propriétés d'un fichier**

Un fichier a deux propriétés : 
- un **nom de fichier**
- un **chemin** (*path*), qui spécifie sa localisation dans le système de fichiers.

A titre d'exemple, regardons les fichiers qui se trouvent dans notre répertoire courant (par défaut, le dossier dans lequel se trouve ce notebook). La méthode à utiliser s'appelle `cwd`, pour *current working directory*.

```python
Path.cwd()
```

Le chemin de notre répertoire courant est contenu dans un objet `PosixPath`, ce qui signifie simplement que `pathlib` a compris que nous étions sur un environnement de type Unix (les serveurs du SSP Cloud sont sous Linux). Si vous exécutiez ce notebook en local sur un ordinateur Windows, l'objet serait `WindowsPath`. Concrètement, cela ne change pas grand chose pour vous mais c'est en fait assez important : les systèmes de fichiers n'utilisent pas les mêmes conventions entre les différents environnements (ex : les séparateurs entre dossiers dans un chemin ne sont pas les mêmes), mais `pathlib` vous permet d'interagir avec ces différents systèmes de manière harmonisée.


Maintenant, listons tous les fichiers contenus dans notre répertoire courant. On utilise pour cela une seconde méthode `glob` qui va simplement renvoyer tous les fichiers dont le nom a une certaine structure. Par exemple, `.glob('*.txt')` va récupérer tous les fichiers dont l'extension est `.txt` et `.glob('test.*')` va récupérer tous les fichiers dont le nom est `test`, quelle que soit leur extension. Ici, on récupère tous les fichiers en utilisant des *wildcards* `*` aux deux positions.

Cette méthode renvoie un objet un peu spécial (un *générateur*). Si vous vous rappelez bien, on avait déjà rencontré le même cas avec la fonction `range`. Il suffit d'appeler la fonction `list` sur le tout pour afficher les résultats de manière lisible.

```python
Path.cwd().glob('*.*')
```

```python
list(Path.cwd().glob('*.*'))
```

On retrouve notre notebook, un fichier qui contient les solutions des exercices du tutoriel, et un certains nombres de fichier texte qui vont servir d'exemples dans la suite du tutoriel. Si l'on prend le notebook par exemple, on distingue bien :
- son nom de fichier : `tutorial.ipynb`
- son chemin : `/home/jovyan/work/formation/`


**Chemins absolus et chemins relatifs**

Il y a deux manières possibles de spécifier le chemin d'un fichier : 
- de manière **absolue**, le chemin commence alors par la racine (`/` en Unix, `C:\` en Windows, etc.). Les chemins renvoyés ci-dessus sont donc absolus.
- de manière **relative**, i.e. relativement au répertoire courant du programme Python. Dès lors qu'un chemin ne commence pas par la racine, `pathlib` va le considérer relatif.

Cette distinction va s'avérer assez importante par la suite, lorsqu'il sera question de lire et d'écrire des fichiers.


**Former des chemins**

En pratique, ce qui nous intéresse est de pouvoir constituer nos propres chemins -- qu'ils soient absolus ou relatifs au répertoire courant -- afin de spécifier où se trouvent les fichiers que nous souhaitons lire ou bien où doivent se trouver les fichiers que l'on souhaite écrire.

`pathlib` offre une syntaxe très intuitive pour constituer des chemins, très similaire à la concaténation des chaînes de caractères que nous avons déjà vue. Au lieu d'un `+`, on va cette fois utiliser un `/` pour concaténer les différentes parties d'un chemin.

Par exemple, essayons de reconstruire le chemin complet de ce notebook. On peut commencer par trouver le chemin du *home* directory, qui est le dossier standard dans lequel se trouvent tous les fichiers de l'utilisateur.

```python
Path.home()
```

On peut alors concaténer les différents sous-dossier et le nom de fichier du notebook pour obtenir le chemin complet vers celui-ci.

```python
path_nb = Path.home() / 'work' / 'formation' / 'tutorial.ipynb'
path_nb
```

On retrouve bien exactement le même chemin que celui obtenu en listant les fichiers présents dans le répertoire courant. 


**Plus sur `pathlib`**

Nous n'avons vu qu'un aperçu des outils qu'offre le module `pathlib` pour interagir avec le système de fichiers local. La [documentation officielle](https://docs.python.org/fr/3/library/pathlib.html) présente de manière exhaustive ces possibilités. Nous présenterons dans ce tutoriel et dans les suivants d'autres méthodes issues de cette librairie, à mesure que l'occasion se présente. Pour l'heure, nous en savons suffisamment pour lire et écrire des fichiers sur le système de fichiers.


### Fichiers texte et fichiers binaires


En programmation, on est généralement amenés à manipuler deux grandes familles de fichiers bien différentes : 
- les **fichiers texte**. Ils ne contiennent que des caractères textuels standards -- techniquement, qui respectent le standard [Unicode](https://fr.wikipedia.org/wiki/Unicode) -- sans informations de *formatting* (police, couleur, etc.). Les fichiers *.txt* ou encore les scripts Python finissant en *.py* sont des exemples de fichiers texte. Ces fichiers peuvent être lus avec n'importe quel éditeur de texte.
- les **fichiers binaires**. Ce sont en fait tous les autres types de fichiers : fichiers compressés (*.zip*, *tar.gz*, etc.), documents PDFs, images, programmes, etc. Ouvrir un tel fichier avec un éditeur de texte produit généralement une grande suite de caractères incompréhensibles, car la représentation textuelle n'est pas adaptée à ces données.

Comme vous pouvez l'imaginer, ces deux types de fichier se traitent avec des outils différents. Par ailleurs, du fait de la diversité des fichiers binaires, chacun de ses fichiers nécessite un traitement particulier. Dans un contexte de programmation, on est cependant principalement à manipuler du code, qui est une donnée textuelle. On va donc s'intéresser uniquement à l'**écriture et à la lecture de fichiers texte** dans ce tutoriel, mais il est important de savoir reconnaître des données binaires lorsqu'on est amené à en traiter.


### Ouvrir un fichier


Demander à Python d'ouvrir un fichier revient à ouvrir une connexion entre l'environnement Python sur lequel vous êtes et le fichier. Tant que cette connexion est ouverte, il est possible de manipuler le fichier. 

Pour ouvrir un fichier, on utilise la fonction `open`. On va par exemple ouvrir le fichier `gamme.txt` qui a été mis dans le répertoire courant.

```python
path_gamme = Path.cwd() / 'gamme.txt'
file_in = open(path_gamme, 'r')
file_in
```

La fonction `open` renvoie un objet de type `_io.TextIOWrapper `, qui spécifie le **mode d'encodage** du fichier et le **mode d'ouverture**.

L'encodage et le décodage sont des sujets techniques, que nous aborderons plus en détail dans un futur tutoriel. Pour le moment, retenons que le mode d'encodage par défaut est l'`UTF-8`, et qu'il n'y a jamais vraiment de bonne raison de choisir un autre mode. 

En revanche, le **mode d'ouverture** est très important. Il y a trois modes principaux :
- `r` : **lecture seule**. Le fichier ne peut qu'être lu, mais pas modifié. C'est le mode par défaut lorsqu'on ne spécifie aucun mode.
- `w` : **écriture**. Il est possible dans ce mode d'écrire sur un fichier. **Attention : si un fichier avec le même nom existe déjà, il sera automatiquement écrasé.**
- `a` : **appending**. Ce mode ne permet que de rajouter des lignes à la fin d'un fichier existant.

Une fois le fichier ouvert, on peut réaliser des opérations sur ce fichier à l'aide de méthodes attachées à l'objet qui le représente. On verre dans la section suivante ce que fait la méthode `readlines`.

```python
file_in.readlines()
```

Une fois les manipulations terminées, on ferme la connexion avec la méthode `close`. Il n'est alors plus possible de manipuler le fichier.

```python
file_in.close()
```

En pratique, on oublie facilement de fermer la connexion à un fichier, ce qui peut créer des erreurs pénibles. Il existe une syntaxe qui permet d'éviter ce problème en utilisant un **context manager** qui gère toute la connexion pour nous.

```python
with open(path_gamme, 'r') as file_in:
    lines = file_in.readlines()
    
lines
```

Cette syntaxe est beaucoup plus lisible : grâce à l'indentation, on voit clairement les opérations qui sont effectuées tant que le fichier est ouvert, et ce dernier est automatiquement fermé dès lors que l'on revient au niveau initial d'indentation. On préférera toujours utiliser cette syntaxe si possible, c'est une bonne pratique de programmation. 


### Lire un fichier


Une fois un fichier ouvert, on peut vouloir lire son contenu. Il existe différentes manières de faire. Une méthode simple et élégante est de parcourir le fichier à l'aide d'une boucle, ce qui est rendu possible par le fait que l'objet Python représentant le fichier est **itérable**.

```python
with open(path_gamme, 'r') as file_in:
    for line in file_in:
        print(line)
```

Dans notre exemple, nous avons simplement affiché les lignes, mais on peut faire de nombreuses choses à partir des données présentes dans le fichier texte : les stocker dans un objet Python, les utiliser pour faire des calculs, ne conserver que les lignes qui répondent à une condition donnée via une instruction `if`, etc.


Il existe également des méthodes toutes faites pour lire le contenu d'un fichier. La plus basique est la méthode `read`, qui retourne l'ensemble du fichier comme une (potentiellement très longue) chaîne de caractères.

```python
with open(path_gamme, 'r') as file_in:
    txt = file_in.read()
    
txt
```

C'est rarement très utile : on préfère en général récupérer individuellement les lignes d'un fichier. La méthode `readlines` parcourt le fichier complet, et renvoie une liste dont les éléments sont les lignes du fichier, dans l'ordre d'apparition.

```python
with open(path_gamme, 'r') as file_in:
    l = file_in.readlines()
    
l
```

Notons que chaque élément de la liste (sauf le dernier) se termine par le caractère spécial `\n` ("retour à la ligne") qui marque simplement la fin de chaque ligne dans un fichier texte. C'est la présence (cachée) de ce même caractère à la fin de chaque appel à la fonction `print` qui fait que l'on revient à la ligne à chaque fois que l'on utilise un `print`.


### Écrire dans un fichier


L'écriture dans un fichier est très simple, elle s'effectue à l'aide de la méthode `write`. Par exemple, écrivons dans un fichier ligne à ligne les différents éléments contenus dans une liste.

```python
ex = ["ceci", "est", "un", "exemple", "très", "original"]

with open("test.txt", "w") as file_out:
    for elem in ex:
        file_out.write(elem)
```

Tout semble s'être passé sans encombre. On peut vérifier que notre fichier a bien été crée via une commande dans le terminal.

```python
!ls
```

Il est bien là. Vérifions maintenant que son contenu est bien celui que l'on souhaitait.

```python
with open("test.txt", "r") as file_out:
    print(file_out.read())
```

Les différents éléments de notre liste se sont fusionnés en un seul bloc de texte ! C'est parce que, contrairement à la fonction `print` par exemple, la fonction `write` n'ajoute pas automatiquement le caractère de retour à la ligne. Il faut l'ajouter manuellement.

```python
with open("test.txt", "w") as file_out:
    for elem in ex:
        file_out.write(elem + "\n")
        
with open("test.txt", "r") as file_out:
    print(file_out.read())
```

C'est beaucoup mieux. 

Quelques remarques supplémentaires sur l'écriture de fichiers :
- mieux vaut le répéter : **utiliser le mode d'ouverture `\w` pour un fichier écrase complètement son contenu**. Lorsqu'on a réécrit notre fichier avec les sauts de ligne, on a complètement écrasé l'ancien.
- pourquoi a-t-on pu mettre juste le nom du fichier dans la fonction `open` et pas un objet `Path` comprenant le chemin complet vers le fichier que l'on souhaitait crééer ? C'est parce que Python l'a automatiquement interprété comme un **chemin relatif** (à notre répertoire courant) du fait de l'absence de racine.
- on ne peut écrire dans un fichier **que des éléments de type `str`** (chaîne de caractère). Si un des éléments de la liste ci-dessus avait été de type `int` ou `float` par exemple, il aurait fallu le convertir via la fonction `str()` avant de l'écrire dans le fichier. Sinon, Python aurait renvoyé une erreur.


## Exercices


### Questions de compréhension


- 1/ Qu'est-ce qu'un module ?
- 2/ Qu'est ce qu'un package ?
- 3/ Pourquoi n'est-ce pas une bonne pratique d'importer toutes les fonctions d'un module avec la syntaxe `from module import *`
- 4/ Quels sont les avantages de la librairie `pathlib` ?
- 5/ Quelles sont les deux propriétés d'un fichier qui permettent de repérer sa position dans le système de fichiers ?
- 6/ Qu'est-ce que le répertoire courant ?
- 7/ Quelles sont les deux manières de spécifier un chemin ? Comment Python fait-il la différence entre les deux ?
- 8/ Quels sont les deux grandes familles de fichiers que l'on est amenés à manipuler en programmation ?
- 9/ Quels sont les différents modes d'ouverture d'un fichier ?
- 10/ Pourquoi est-il préférable d'utiliser la syntaxe `with open(...) as ...` pour ouvrir un fichier ?
- 11/ Pourquoi peut-on parcourir les lignes d'un fichier à l'aide d'une boucle ?

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python
# Exécuter cette cellule pour afficher la solution
%load -r 3-32 solutions.py
```

### Moyenne et écart-type des notes obtenues à un examen 


*Exercice inspiré de : [python.sdv.univ-paris-diderot.fr](https://python.sdv.univ-paris-diderot.fr/07_fichiers/)*

Le fichier texte `notes.txt` se trouve dans votre répertoire courant. Il contient les notes obtenues par 50 élèves à un examen. Problème : toutes les notes ont été écrites sur une même ligne, avec un espace à chaque fois. Ouvrez ce fichier et calculez la moyenne et l'écart-type des notes.

Indices :
- les chaînes de caractère ont une méthode `split` qui permet de séparer du texte selon un caractère donné
- il faudra convertir les notes au format numérique pour pouvoir leur appliquer des fonctions mathématiques
- vous pouvez utiliser les fonctions du package `numpy` pour calculer les statistiques demandées

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python
# Exécuter cette cellule pour afficher la solution
%load -r 36-47 solutions.py
```

### Admis ou recalé


*Exercice inspiré de : [python.sdv.univ-paris-diderot.fr](https://python.sdv.univ-paris-diderot.fr/07_fichiers/)*

Le fichier texte `notes_clean.txt` se trouve dans votre répertoire courant. Il contient les notes obtenues par 50 élèves à un examen. Contraitement à l'exercice précédent, les notes sont cette fois bien écrites : une note par ligne.

Écrire un script Python qui :
- stocke chaque note au format `int` dans une liste
- réécrit les notes dans un fichier `notes_mentions.txt` avec sur chaque ligne la note, suivie d'un espace, suivi de la mention "admis" si la note est supérieure ou égale à 10, et "recalé" sinon.

Par exemple, les trois premières lignes de ce nouveau fichier devraient être :
```
5 recalé
5 recalé
18 admis
```

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python
# Exécuter cette cellule pour afficher la solution
%load -r 51-63 solutions.py
```

### Retardataires


3 élèves n'avaient pas rendu leur copie dans les temps pour l'examen : 
- Miranda a obtenu 16 et a rendu son devoir avec 3 jours de retard
- Paolo a obtenu 11 et a rendu son devoir avec 1 jour de retard
- Isidore a obtenu 3 et a rendu son devoir avec 5 jours de retard.

Chaque élève aura une note finale égale à la note obtenue moins le nombre de jours de retard. Une note ne pouvant être négative, elle sera remplacée par 0.

Les informations nécessaires ont été placées dans une liste dans la cellule suivante). A l'aide d'une boucle sur cette liste, **ajouter** (sans réécrire complètement le fichier !). les notes au fichier `notes_clean.txt` (sans la mention).

NB : si vous avez écrasé le contenu d'un fichier par erreur, vous pouvez retrouver les fichiers propres sur le [dépôt GitHub associé à la formation](https://github.com/InseeFrLab/formation-python-initiation/tree/main/course/manipulation/modules-files).

```python
supp = [(16, 3), (11, 1), (3, 5)]
```

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python
# Exécuter cette cellule pour afficher la solution
%load -r 67-73 solutions.py
```

### Scanner des fichiers


Écrire un programme qui réalise les opérations suivantes : 
- dans le répertoire courant, lister les chemins des fichiers dont l'extension est `.txt` (la syntaxe a été vue dans la partie sur `pathlib`)
- faire une boucle qui parcourt ces chemins et ouvre chaque fichier séquentiellement
- pour chaque fichier, faire un test d'appartenance (rappel de la syntaxe : `if pattern in string: ...`) pour tester si le fichier contient le mot "sol"
- si le fichier contient le mot "recalé", imprimer son chemin absolu dans la console (seul le chemin du fichier `gamme.txt` devrait donc apparaître)

```python tags=[]
# Testez votre réponse dans cette cellule

```

```python
# Exécuter cette cellule pour afficher la solution
%load -r 77-85 solutions.py
```

```python

```
