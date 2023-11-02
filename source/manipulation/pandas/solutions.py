# -------------------------------------------------------------------------- #

# 1/ Un DataFrame dans Pandas est une structure de données bidimensionnelle,
# comparable à un tableau ou une feuille de calcul Excel.
# Dans le contexte Python, on peut le comparer à un dictionnaire d'arrays NumPy,
# où les clés sont les noms des colonnes et les valeurs sont les colonnes elles-mêmes.

# 2/ La différence principale entre un array NumPy et une Series Pandas est que
# la Series peut contenir des données étiquetées, c'est-à-dire qu'elle a un index
# qui lui est associé, permettant des accès et des manipulations par label.

# 3/ Un DataFrame est essentiellement une collection de Series. Chaque colonne
# d'un DataFrame est une Series, et toutes ces Series partagent le même index,
# qui correspond aux étiquettes des lignes du DataFrame.

# 4/ Les données dans un DataFrame Pandas sont structurées en colonnes et en lignes.
# Chaque colonne peut contenir un type de données différent (numérique,
# chaîne de caractères, booléen, etc.), et chaque ligne représente une observation.

# 5/ L'index dans un DataFrame Pandas sert à identifier de manière unique chaque ligne
# du DataFrame. Il permet d'accéder rapidement aux lignes, de réaliser des jointures,
# de trier les données et de faciliter les opérations de regroupement.

# 6/ Pour explorer un DataFrame inconnu, on peut utiliser df.head() pour voir les
# premières lignes, df.tail() pour les dernières, df.info() pour obtenir un résumé
# des types de données et des valeurs manquantes, et df.describe() pour des
# statistiques descriptives.

# 7/ Assigner le résultat d'une opération à une nouvelle variable crée une copie du
# DataFrame avec les modifications appliquées. Utiliser une méthode avec inplace=True
# modifie le DataFrame original sans créer de copie, ce qui peut être plus
# efficace en termes de mémoire.

# 8/ Pandas représente les valeurs manquantes avec l'objet `nan` (Not a Number)
# de `Numpy` pour les données numériques et avec None ou pd.NaT pour les dates/temps.
# Ces valeurs manquantes sont généralement ignorées dans les calculs de fonctions
# statistiques, ce qui peut affecter les résultats si elles ne sont pas
# traitées correctement.

# 9/ Concaténer consiste à assembler des DataFrames en les empilant verticalement
# ou en les alignant horizontalement, principalement utilisé lorsque les DataFrames
# ont le même schéma ou lorsque vous souhaitez empiler les données.
# Les jointures, inspirées des opérations JOIN en SQL, combinent les DataFrames sur la
# base de valeurs de clés communes et sont utilisées pour enrichir un ensemble de
# données avec des informations d'un autre ensemble.

# 10/ Le chaînage de méthodes permet de combiner plusieurs opérations en une seule
# expression de code. Cela peut améliorer l'efficacité en évitant les assignations
# intermédiaires et en rendant le code plus fluide et plus facile à lire.
# Cela favorise également un style de programmation fonctionnel où les données
# passent à travers une chaîne de transformations de manière fluide.

# -------------------------------------------------------------------------- #

