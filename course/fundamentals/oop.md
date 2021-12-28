---
title: "Notions de programmation orientée objet"
abstract: "Un rapide tour dans le monde des objets, leurs attributs et leurs méthodes"
---

Python est un langage dit "multi-paradigmes", c'est à dire qu'il admet plusieurs manières de coder et de concevoir ses programmes. L'une d'entre elle est la programmation orientée objet (POO). La POO est un paradigme puissant, mais fait intervenir des concepts assez complexes (polymorphisme, héritage, etc.). Fort heureusement pour nous, Python n'impose pas de coder en POO. Cela étant, le fonctionnement interne de Python est fortement teinté de POO, et la plupart des *packages* les plus utilisés reposent à des degrés divers sur les objets. Nous allons donc étudier dans ce tutoriel les bases de la POO, afin de pouvoir être autonomes lorsque son usage est nécessaire.


## La programmation orientée objet


Vous avez peut être déjà entendu que Python était un langage de "programmation orientée objet". La POO est un paradigme de programmation qui permet de structurer les programmes autour d'une abstraction, l'**objet**, qui contient des **attributs** (caractéristiques de l'objet) et des **méthodes** (fonctions propres à l'objet) qui agissent sur lui-même. Afin d'illustrer cette définition un peu abstraite , on peut prendre l'exemple ([source](https://python.sdv.univ-paris-diderot.fr/19_avoir_la_classe_avec_les_objets/)) d'un objet "citron" qui contient les attributs "saveur" et "couleur", et une méthode "presser" qui permet d'extraire son jus.


## "Tout est un objet"


**En Python, tout est un objet** (au sens de la POO). Regardons ce que cela signifie en récupérant le type de différents objets que nous avons vus dans les précédents tutoriels.

```python
print(type(1))
print(type("bonjour"))
print(type([]))
print(type(()))
print(type({}))

def f(x):
    print(x)
          
print(type(f))
```

Ces éléments sont tous de type différent, mais ils ont un point commun : le terme `class`. De même que l'instruction `def` définit une fonction, l'instruction `class` définit une classe d'objets Python. Ainsi, chacun des objets utilisables en Python a une classe qui définit l'objet, ses attributs et ses méthodes.


## Définir ses propres objets


Regardons comment on peut utiliser l'instruction `class` pour définir notre objet "citron".

```python
class Citron:

    def __init__(self, couleur, qte_jus):
        self.saveur = "acide"
        self.couleur = couleur
        self.jus = qte_jus
        
    def recup_qte_jus(self):
        print("Il reste " + str(self.jus) + " mL de jus dans le citron.")
        
    def extraire_jus(self, quantite):
        if quantite > self.jus:
            print("Il n'y a pas assez de jus dans le citron pour la quantité demandée.")
        else:
            self.jus = max(0, self.jus - quantite)  # évite toute valeur négative de `jus`
```

Analysons la syntaxe de construction d'une classe d'objets :
- l'instruction `class` définit la **classe d'objets**. Différents objets pourront être créés selon le modèle défini par cette classe. Par convention, le nom de la classe doit commencer par une majuscule.
- la classe spécifie un certains nombres de fonctions. Dans ce contexte particulier, on appelle ces fonctions "**méthodes**" : ce sont des fonctions spécifiques à la classe d'objets définie.
- une première méthode bien spécifique, nommée `__init__`, est appelée le **constructeur**. Elle permet de définir les **attributs** attachés à cette classe d'objets. Il est possible de passer des paramètres à la fonction (comme `couleur` et `qte_jus`) pour définir des attributs propres à une **instance** de l'objet (plus de détails sur cette notion dans la section suivante).
- le constructeur a un paramètre obligatoire : `self`. C'est une référence aux **instances** qui vont être créées à partir de cette classe. Notons la syntaxe qui définit un attribut : `self.attribut = valeur`.
- les autres méthodes sont définies par l'utilisateur. Elles prennent également le `self` en paramètre, ce qui leur permet d'effectuer des opérations sur / à partir des attributs. Comme ce sont des fonctions, elles peuvent également admettre d'autres paramètres. Ainsi, la fonction `extraire_jus` prend un paramètre `quantite` qui définit quelle quantité de jus on extrait du citron lorsqu'on le presse.


## La classe et ses instances


La **classe** peut être vue comme la **recette qui permet de créer un objet** : elle définit les attributs et les méthodes que possèderont tous les objets définis à partir de cette classe. Définir une classe comme ci-dessus revient simplement à mettre cette recette dans l'environnement Python. Pour créer un objet selon cette classe, il faut l'**instancier**.

```python
citron1 = Citron(couleur="jaune", qte_jus=45)
citron2 = Citron(couleur="vert", qte_jus=32)

print(type(citron1))
print(type(citron2))
```

On a ici créé deux instances de la classe `Citron`. Ces deux instances sont autonomes : Python les voit comme deux objets bien distincts. Ils ont cependant été créés à partir de la même classe et ont donc le même type.

Cette distinction entre la classe et ses instances permet de mieux comprendre la signification du paramètre `self`. Il s'agit d'une référence aux instances qui vont être créées selon la classe, qui permet de spécifier leurs attributs et leurs méthodes. Lorsqu'on crée une instance donnée, celle-ci devient en quelque sorte le `self`.


## Attributs


Un attribut est une **variable associée à un objet**. Un attribut peut contenir n'importe quel objet Python.


### Accéder aux attributs


Une fois que l'objet est instancié, il est possible d'accéder à ses attributs. La syntaxe est simple : `instance.attribut`.

```python
print(citron1.couleur)
print(citron2.couleur)
print(citron1.jus)
print(citron2.jus)
```

On voit bien que les deux instances sont **autonomes** : bien qu'elles soient du même type, leurs attributs diffèrent.


### Modifier un attribut


Modifier un attribut d'une instance est très simple, la syntaxe est : `instance.attribut = nouvelle_valeur`.

```python
citron2.couleur = "rouge"
print(citron2.couleur)
```

Il est également possible d'ajouter un attribut selon la même logique : `instance.nouvel_attribut = valeur`. Cependant, ce n'est pas une bonne pratique de programmation, la classe servant précisément à définir les attributs que peuvent admettre les objets d'une classe donnée. On préférera donc généralement définir les attributs au sein de la classe plutôt qu'en dehors.


### Attributs de classe et attributs d'instance


Les deux instances que nous avons créées permettent d'illustrer les différents types d'attributs :
- les **attributs de classe**. Ce sont les attributs qui ont la même valeur pour toute instance créée selon cette classe. Ici, c'est l'attribut `saveur` : tous les citrons sont acides, il n'y a donc pas lieu de permettre de modifier ce paramètre lors de l'instanciation. En toute rigueur, on aurait donc même pu définir cet attribut hors du constructeur.
- les **attributs d'instance**. Ce sont les attributs dont la valeur peut varier entre les différentes instances créées selon une même classe. Ici, ce sont les attributs `couleur` et `jus` : il existe des citrons de différentes couleurs, et des citrons plus ou moins gros, qui auront donc des quantités de jus différentes. C'est donc à l'utilisateur de définir ces attributs lors de l'instanciation.


## Méthodes


Une méthode est une **fonction associée à un objet**. Elle peut utiliser ses attributs, les modifier, et faire intervenir d'autres méthodes de l'objet.


### Appeler une méthode


La syntaxe pour appeler une méthode d'un objet instancié est la suivante : `instance.methode(parametres)`.

```python
citron1.recup_qte_jus()
```

On peut faire deux remarques sur cette syntaxe. La première est qu'**une méthode est une fonction *attachée* à une instance d'un objet**. Contrairement aux fonctions définies via l'instruction `def`, les méthodes n'ont pas d'existence propre.

```python
recup_qte_jus()
```

La seconde remarque est qu'**on ne spécifie plus le paramètre `self` lorsqu'on manipule une instance**. L'instance est devenue le `self` (ou plutôt *un* self) elle-même. Le lien entre la méthode et son instance est déjà fait, puisqu'on ne peut pas utiliser la méthode sans appeler l'instance auparavant.


### Agir sur les attributs


Tout l'intérêt des méthodes est qu'elles peuvent accéder aux attributs, et ainsi réaliser des opérations à partir de ceux-ci, mais également les modifier. Reprenons notre exemple pour illustrer cette possibilité.

```python
citron1 = Citron(couleur="jaune", qte_jus=45)

citron1.recup_qte_jus()
citron1.extraire_jus(12)
citron1.recup_qte_jus()
```

La méthode `recup_qte_jus` permet simplement d'afficher la valeur d'un attribut de manière formattée. La méthode `extraire_jus` en revanche modifie durablement la valeur de l'attribut `jus`, ce que montre le second appel à `recup_qte_jus`.


## Quand utilise-t-on la POO ?


L'exemple précédent est intéressant car il illustre à la fois un avantage et un inconvénient de la POO.

Le fait que les objets possèdent des attributs permet de garder en mémoire **l'état d'une ressource** -- dans notre exemple, la quantité de jus contenu dans un objet de classe `Citron` donné. Pour prendre des exemples plus réalistes, cette propriété est intéressante et utilisée dans plusieurs cas :
- l'entraînement d'un modèle de machine-learning. Il est fréquent d'entraîner un modèle une première fois, et de vouloir ensuite continuer l'entraînement plus longtemps, ou bien avec d'autres données. Sauvegarder l'état dans une instance de la classe `Modele` permet de faire cela. C'est pourquoi la plupart des *packages* de machine-learning en Python sont fondés sur de la POO.
- le fonctionnement en continu d'une application web. Une telle application doit garder des choses en mémoire pour fournir à l'utilisateur une expérience fluide : le fait que l'utilisateur se soit connecté, son historique, etc. Là encore, la plupart des *frameworks* web (`Django`, `Flask`..) reposent sur de la POO.

Dans le même temps, le fait d'utiliser des objets qui gardent en mémoire un état peut **limiter la reproductibilité des analyses**. Pour illustrer cela, revenons à l'exemple du tutoriel : exécutez plusieurs fois d'affilée la cellule suivante.

```python
citron1.recup_qte_jus()
citron1.extraire_jus(12)
citron1.recup_qte_jus()
```

Les trois exécutions donnent des résultats différents, alors que le code éxécuté est strictement le même. Cela illustre bien le problème de reproductibilité : lorsqu'on utilise la POO, il faut bien faire attention à l'état des objets qui est conservé en mémoire, au risque de ne pas tomber sur les mêmes résultats lorsqu'on réplique une même analyse.


## Exercices


### Questions de compréhension


- 1/ "En Python, tout est un objet" : qu'est-ce que cette phrase signifie ?
- 2/ A quoi sert l'instruction `class` ?
- 3/ A quoi sert le constructeur `__init__` ?
- 4/ A quoi sert le `self` ? 
- 5/ Quelle est la différence entre une classe et une instance ?
- 6/ Qu'est-ce qu'un attribut ?
- 7/ Quelle est la différence entre une méthode et une fonction ?
- 8/ A quoi voit-on la différence entre un attribut et une méthode lorsqu'on les appelle ?
- 9/ Peut-on modifier un attribut avec une méthode ? Peut-on modifier un attribut en dehors d'une méthode ?
- 10/ Quand utilise-t-on généralement la POO ?

```python
# Testez votre réponse dans cette cellule

```

```python
# Exécuter cette cellule pour afficher la solution
%load -r 3-33 solutions.py
```

### De la masse au jus


Admettons que le jus contenu dans un citron soit une fonction proportionnelle de sa masse, défini de la manière suivante : $jus = \frac {masse} {4}$ où la masse est en grammes et le jus en mL.

Modifiez la classe `Citron`, reproduite dans la cellule suivante, de telle sorte que :
- lors de l'instanciation, l'utilisateur ne définit plus la quantité de jus, mais la masse du citron
- l'attribut `jus` est calculé selon la formule ci-dessus
- rajouter une méthode qui affiche "La masse du citron est x grammes."

Instanciez ensuite un nouveau citron est vérifiez que tout fonctionne comme prévu.

```python
class Citron:

    def __init__(self, couleur, qte_jus):
        self.saveur = "acide"
        self.couleur = couleur
        self.jus = qte_jus
        
    def recup_qte_jus(self):
        print("Il reste " + str(self.jus) + " mL de jus dans le citron.")
        
    def extraire_jus(self, quantite):
        if quantite > self.jus:
            print("Il n'y a pas assez de jus dans le citron pour la quantité demandée.")
        else:
            self.jus = max(0, self.jus - quantite)  # évite toute valeur négative de `jus`
```

```python
# Testez votre réponse dans cette cellule

```

```python
# Exécuter cette cellule pour afficher la solution
%load -r 37-60 solutions.py
```

### Comptes bancaires


Exercice librement inspiré de : [https://github.com/Pierian-Data/Complete-Python-3-Bootcamp](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp)

Nous avons vu que la POO était particulièrement intéressante lorsque l'on souhaite manipuler des objets qui gardent l'état d'une ressource. C'est par exemple le cas d'un compte bancaire, qui garde un solde et permet ou non certaines opérations en fonction de ce solde.

Implémenter une classe `Compte` avec :
- deux attributs : `titulaire` (nom du client) et `solde` (solde en euros du compte)
- une méthode `affiche_solde` qui affiche : "Le solde du compte de nom_client est x euros."
- une méthode `depot` qui admet un paramètre `montant`. Lorsqu'un dépôt est effectué, le solde du compte est incrémenté du montant du dépôt.
- une méthode `retrait` qui admet un paramètre `montant`. Lorsqu'un retrait est effectué : 
    - si le montant est inférieur au solde : le solde est décrémenté du montant, est on affiche "Retrait accepté.".
    - si le montant est supérieur au solde : on affiche "Retrait refusé : fonds insuffisants." et le solde est inchangé
- une méthode `transfert` qui admet un paramètre `montant` et un paramètre `destinataire` qui admet une autre instance de la classe `Compte` (i.e. un autre client). Par exemple, `client1.transfert(destinataire=client2, montant=1000)` a pour effet de :
    - si le montant est inférieur au solde de client1 : le solde de client1 est décrémenté du montant, le solde de client2 est incrémenté du montant.
    - si le montant est supérieur au solde de client1 : on affiche "Transfert refusé : fonds insuffisants." et les soldes des deux clients restent inchangés.
    
Créer deux clients et tester que les différentes fonctionnalités à implémenter marchent comme prévu.

```python
# Testez votre réponse dans cette cellule

```

```python
# Exécuter cette cellule pour afficher la solution
%load -r 64-119 solutions.py
```

```python

```
