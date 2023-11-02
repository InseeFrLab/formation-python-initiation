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

# -------------------------------------------------------------------------- #

data_list1 = [
    ['Carrefour', 'Casino', 'Lidl', 'Carrefour', 'Casino', 'Lidl'],
    ['01.1.1', '02.1.1', '01.1.1', '03.1.1', '01.1.1', '02.1.1'],
    [3, 2, 7, 5, 10, 1],
    [1.50, 2.30, 0.99, 5.00, 1.20, 3.10]
]

data_list2 = [
    ['Carrefour', '01.1.1', 3, 1.50],
    ['Casino', '02.1.1', 2, 2.30],
    ['Lidl', '01.1.1', 7, 0.99],
    ['Carrefour', '03.1.1', 5, 5.00],
    ['Casino', '01.1.1', 10, 1.20],
    ['Lidl', '02.1.1', 1, 3.10]
]

# 1ère possibilité : à partir d'un dictionnaire
data_dict = {
    'enseigne': data_list1[0],
    'produit': data_list1[1],
    'quantite': data_list1[2],
    'prix': data_list1[3]
}

df_from_dict = pd.DataFrame(data_dict)

# 2ème possibilité : à partir d'une liste de listes
columns = ['enseigne', 'produit', 'quantite', 'prix']
df_from_list = pd.DataFrame(data_list2, columns=columns)

# Vérification
df_from_dict.equals(df_from_list)

# -------------------------------------------------------------------------- #

# Sélection des données de la première ligne
print(df.iloc[0])

# Sélection de toutes les données de la colonne 'prix'
print(df.loc[:, 'prix'])

# Sélection des lignes pour l'enseigne 'Carrefour' uniquement
print(df.loc[df['enseigne'] == 'Carrefour'])

# Sélection des quantités achetées pour les produits classifiés '01.1.1' (Pain)
print(df.loc[df['produit'] == '01.1.1', 'quantite'])

# Sélection des données des colonnes 'enseigne' et 'prix' pour toutes les lignes
print(df.loc[:, ['enseigne', 'prix']])

# Sélection des lignes où la quantité achetée est supérieure à 5
print(df.loc[df['quantite'] > 5])

# Sélection des lignes où les transactions qui ont eu lieu après 15h
print(df.loc[df['date_heure'].dt.hour > 15])

# Sélection des lignes où les transactions ont eu lieu le "2022-01-03"
print(df.loc[df['date_heure'].dt.date == pd.to_datetime('2022-01-03').date()])

# -------------------------------------------------------------------------- #

