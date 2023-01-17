---
title: "Projet 2 - Analyse du recensement de la population"
abstract: "Ce projet a pour objectif de reproduire une analyse standard à laquelle un statisticien peut être confronté. Il repose sur l'utilisation de la librairie pandas et des librairies de visualisation usuelles (matplotlib, seaborn)"
---

Le but de ce projet est de réaliser une analyse statistique rapide d'un jeu de données dont le format n'est pas directement optimisé pour une analyse en python. Nous allons utiliser exclusivement la librairie `pandas` pour l'analyse de données. Pour reproduire au mieux une situation à laquelle vous pouvez être confronté, nous vous invitons vivement à consulter la documentation de la librairie ([docs](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)).


Nous allons nous intéresser à l’estimation de la population au 1er janvier de chaque année, cette estimation étant effectuée à partir des recensements et des modèles d’évolution de la population. Les données sont accessibles sur le site de l'Insee à l'adresse suivante : [https://www.insee.fr/fr/statistiques/1893198](https://www.insee.fr/fr/statistiques/1893198).
Une copie du fichier a été déposé dans un *bucket* et peut être télécharger via cet url : [https://minio.lab.sspcloud.fr/tfaria/public/estim-pop-dep-sexe-aq-1975-2022.ods](https://minio.lab.sspcloud.fr/tfaria/public/estim-pop-dep-sexe-aq-1975-2022.ods).

```python
import copy
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import seaborn as sns

import solutions
```

## Partie 1 : Téléchargement et mise en forme des données

Avant d'effectuer le téléchargement des données avec python il est nécessaire de connaitre le format de nos données. Dans notre cas, il s'agit du format Excel (`.xlsx`). De plus, il peut être utile de regarder à quoi ressemble les données que l'on souhaite importer, notamment lorsque leur format n'est pas standard. Ainsi, avant de commencer prenez le temps de jeter un oeil aux données.

### Question 0 

Téléchargez les données en cliquant sur ce [lien](https://minio.lab.sspcloud.fr/tfaria/public/estim-pop-dep-sexe-aq-1975-2022.ods) et ouvrez le avec votre logiciel tableur préféré. Analysez la structure des données.

### Question 1

Définissez la fonction `load_data()` qui n'a pas de paramètre et renvoie un `Dict` où les **clés** correspondent aux noms des onglets de notre fichier et les **valeurs** correspondent aux données des différentes feuilles de calcul. Pour cela, utilisez une fonction de la librairie `pandas` en spécifiant les bons paramètres.

#### Résultat attendu

```python
data = solutions.load_data()
data["2022"]
```

#### À vous de jouer !

```python
def load_data():
    # Votre code ici
    return data
```

### Question 2 

Maintenant que les données sont importées nous allons les mettre sous la forme d'un seul `DataFrame` dont les colonnes sont : 
- `genre` ;
- `age` ;
- `population` ;
- `dep_code` ;
- `dep` ;
- `annee`.

2.1 - Pour ce faire créez une fonction `reshape_data_by_year(df, year)` qui prend en argument un DataFrame issu de votre Dict `data` et une année donnée. 


#### Résultat attendu

```python
annee = 2022
df = solutions.reshape_table_by_year(data[f"{annee}"], annee)
```

#### À vous de jouer !

```python
def reshape_table_by_year(df, year):
    # Votre code ici
    return df
```

2.2 - Créez une fonction `reshape_data(data)` qui produit un `DataFrame` avec les données pour toutes les années entre 1975 et 2022.

#### Résultat attendu

```python
df = solutions.reshape_data(data)
```

#### À vous de jouer !

```python
def reshape_data(data):
    # Votre code ici
    return df
```

## Partie 2 : Visualisation des données

Nous avons maintenant un jeu de données prêt à être analyser ! Commençons tout d'abord par visualiser l'évolution de la population pour différents départements.

### Question 3

Ecrivez une fonction `plot_population_by_gender_per_department(df, department_code)` qui renvoie un graphique représentant l'évolution de la population dans un département donné. Utilisez la librairie `matplotlib`.
Vous pouvez regarder les données de la Haute Garonne (31), du Loir-et-Cher (41) et de la Réunion (974) pour constater des disparités d'évolutions.

#### Résultat attendu

```python
solutions.plot_population_by_gender_per_department(df, "31")
```

#### À vous de jouer !

```python
def plot_population_by_gender_per_department(data, department_code):
    # Votre code ici
```

### Question 4

Afin de comparer 2 graphiques il est parfois utile de les afficher côte à côte. Grâce à la méthode `subplots()` de `matplotlib` cela est très facile à réaliser en python. Pour le constater, nous allons représenter la pyramide des âges de la France en 1975 et en 2022.



4.1- Définissez la fonction `get_age_pyramid_data(df, year)` qui, à partir du DataFrame généré par la fonction `reshape_data()`, renvoie un DataFrame avec les colonnes `age`, `Femmes`, `Hommes`. La colonne `age` doit contenir toutes les tranches d'âges présentes dans le jeu de données, les colonnes `Femmes/Hommes` correspond à la population féminine/masculine pour une tranche d'âge donnée. Par des soucis graphique, la colonne `Hommes` sera au préalable multipliée par -1.

```python
pyramide_data = solutions.get_age_pyramid_data(df, 2022)
```

#### À vous de jouer !

```python
def get_age_pyramid_data(df, year):
    # Votre code ici
    return df
```

4.2- Définissez la fonction `plot_age_pyramid(df, year, ax=None)` qui représent la pyramide des âges de la France pour une année donnée. Vous pouvez vous inspirer de ce qui a été fait dans ce [blog](https://maciejtarsa.medium.com/plotting-a-population-pyramid-in-python-52be034968b0).

```python
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(15,6))

solutions.plot_age_pyramid(df, 1975, ax=ax1)
solutions.plot_age_pyramid(df, 2022, ax=ax2)
```

#### À vous de jouer !

```python
def plot_age_pyramid(df, year, ax=None):
    if ax is None:
        ax = plt.gca()
    # Votre code ici
    return df
```

## Partie 3 : Une introduction aux données géographiques (facultatif ?)

### Question 5 
