# -------------------------------------------------------------------------- #

# Questions de compréhension

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

# Exercice 1

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

# Si les données sont sous forme de colonnes : à partir d'un dictionnaire
data_dict = {
    'enseigne': data_list1[0],
    'produit': data_list1[1],
    'quantite': data_list1[2],
    'prix': data_list1[3]
}

df_from_dict = pd.DataFrame(data_dict)

# Si les données sont sous forme de lignes : à partir d'une liste de listes
columns = ['enseigne', 'produit', 'quantite', 'prix']
df_from_list = pd.DataFrame(data_list2, columns=columns)

# Vérification
df_from_dict.equals(df_from_list)

# -------------------------------------------------------------------------- #

# Exercice 2

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

# Exercice 3

# Partie 1 : import et exploration des données

# Importer un fichier CSV depuis une URL
url = "https://www.insee.fr/fr/statistiques/fichier/2540004/nat2021_csv.zip"
df_prenoms = pd.read_csv(url, sep=";")

# Visualisation des données
df_prenoms.head(10)
df_prenoms.sample(n=50)

# Informations générales sur les données
df_prenoms.info()

# Partie 2 : nettoyage des données

# Colonne preusuel
print(df_prenoms[df_prenoms["preusuel"].isna()])
prop_rares = df_prenoms.groupby("preusuel")["nombre"].sum()["_PRENOMS_RARES"] / df_prenoms["nombre"].sum()
print(prop_rares)  # ~ 2 % de la base
df_prenoms = df_prenoms.replace('_PRENOMS_RARES', np.nan)

# Colonne annais
prop_xxxx = df_prenoms.groupby("annais")["nombre"].sum()["XXXX"] / df_prenoms["nombre"].sum()
print(prop_xxxx)  # ~ 1 % de la base
df_prenoms = df_prenoms.replace('XXXX', np.nan)

# Suppression des valeurs manquantes
df_prenoms = df_prenoms.dropna()

# Conversions de types
df_prenoms['annais'] = pd.to_numeric(df_prenoms['annais'])
df_prenoms['sexe'] = df_prenoms['sexe'].astype('category')

# Vérification
df_prenoms.info()

#### Partie 3 : Statistiques descriptives sur les naissances

# Filtrage des données
df_prenoms_post_1946 = df_prenoms[df_prenoms["annais"] >= 1946]

# Nombre total de naissances par sexe
births_per_sex = df_prenoms_post_1946.groupby('sexe')['nombre'].sum()
print(births_per_sex)

# Cinq années avec le plus grand nombre de naissances
top5_years = df_prenoms_post_1946.groupby('annais')['nombre'].sum().nlargest(5)
print(top5_years)

#### Partie 4 : Analyse des prénoms

# Nombre total de prénoms uniques
total_unique_names = df_prenoms['preusuel'].nunique()
print(total_unique_names)

# Nombre de personnes possédant un prénom d'une seule lettre
single_letter_names = df_prenoms[df_prenoms['preusuel'].str.len() == 1]['nombre'].sum()
print(single_letter_names)

# Fonction de popularité
def popularite_par_annee(df, prenom):
    # Filtrer le DataFrame pour ne garder que les lignes correspondant au prénom donné
    df_prenom = df[df['preusuel'] == prenom]

    # Grouper par année, sommer les naissances et identifier l'année avec le maximum de naissances
    df_agg = df_prenom.groupby('annais')['nombre'].sum()
    annee_max = df_agg.idxmax()
    n_max = df_agg[annee_max]

    print(f"Le prénom '{prenom}' a été le plus donné en {annee_max}, avec {n_max} naissances.")

# Test de la fonction avec un exemple
popularite_par_annee(df_prenoms, 'ALFRED')

def popularite_par_decennie(df, sexe):
    # Filtrage sur le sexe
    df_sub = df[df["sexe"] == sexe]

    # Calcul de la variable décennie
    df_sub["decennie"] = (df_sub["annais"] // 10) * 10

    # Calculer la somme des naissances pour chaque prénom et chaque décennie
    df_counts_decennie = df_sub.groupby(["preusuel", "decennie"])["nombre"].sum().reset_index()

    # Trouver l'indice du prénom le plus fréquent pour chaque décennie
    idx = df_counts_decennie.groupby("decennie")["nombre"].idxmax()

    # Utiliser l'indice pour obtenir les lignes correspondantes du DataFrame df_counts_decennie
    df_popularite_decennie = df_counts_decennie.loc[idx].set_index("decennie")

    return df_popularite_decennie

# Test de la fonction avec un exemple
popularite_par_decennie(df_prenoms, sexe=2)

# -------------------------------------------------------------------------- #

# Exercice 4

# Partie 1 : Exploration des données sur les populations légales communales

## Import
df_pop_communes = pd.read_csv("data/communes.csv", sep=";")

## Information générales
df_pop_communes.sample(10)
df_pop_communes.info()
df_pop_communes.describe()

## Suppression des communes sans population
n_communes_0_pop = df_pop_communes[df_pop_communes["PTOT"] == 0].shape[0]
print(n_communes_0_pop)
df_pop_communes = df_pop_communes[df_pop_communes["PTOT"] > 0]

## Supression des colonnes superflues
df_pop_communes = df_pop_communes.drop(columns=["PMUN", "PCAP"])

## Corrélation entre longueur du nom de commune et population
df_pop_communes_stats = df_pop_communes.copy()
df_pop_communes_stats['longueur'] = df_pop_communes_stats['COM'].str.len()
df_pop_communes_stats['longueur'].corr(df_pop_communes_stats['PTOT'])

# Partie 2 : Exploration des données sur les émissions communales

## Import
url_ademe = "https://data.ademe.fr/data-fair/api/v1/datasets/igt-pouvoir-de-rechauffement-global/data-files/IGT%20-%20Pouvoir%20de%20r%C3%A9chauffement%20global.csv"
df_emissions = pd.read_csv(url_ademe)

## Information générales
df_emissions.sample(10)
df_emissions.info()
df_emissions.describe()

## Des lignes avec toutes les valeurs d'émission manquantes ?
df_emissions_num = df_emissions.select_dtypes(['number'])
only_nan = df_emissions_num[df_emissions_num.isnull().all(axis=1)]
only_nan.shape[0]

## Calcul des émissions totales par commune
df_emissions['emissions_totales'] = df_emissions.sum(axis = 1, numeric_only = True)
df_emissions

## Affichage des principales communes émettrices
df_emissions.sort_values(by="emissions_totales", ascending=False).head(10)

## Corrélation entre émissions totales et émissions par secteur
df_emissions.corrwith(df_emissions["emissions_totales"], numeric_only=True)

## Affichage des principaux départements émetteurs
df_emissions["dep"] = df_emissions["INSEE commune"].str[:2]
df_emissions.groupby("dep").agg({"emissions_totales": "sum"}).sort_values(by="emissions_totales", ascending=False).head(10)

# Partie 3 : Vérifications préalables pour la jointure des sources de données

## Affichage des doublons dans les noms de communes
doublons = df_pop_communes.groupby('COM').count()['DEPCOM']
doublons = doublons[doublons>1]
doublons = doublons.reset_index()
doublons

## Mise en relation avec les codes commune
df_pop_communes_doublons = df_pop_communes[df_pop_communes["COM"].isin(doublons["COM"])]
df_pop_communes_doublons.sort_values('COM')

## Les codes commune identifient-ils de manière unique les communes ?
(df_pop_communes_doublons.groupby("DEPCOM")["COM"].nunique() != 1).sum()

## Observations qui sont dans les pop légales mais pas dans les données d'émissions
df_pop_communes[~df_pop_communes["DEPCOM"].isin(df_emissions["INSEE commune"])]

## Observations qui sont dans les données d'émissions mais pas dans les pop légales
df_emissions[~df_emissions["INSEE commune"].isin(df_pop_communes["DEPCOM"])]

# Partie 4 : Calcul d'une empreinte carbone par habitant pour chaque commune

## Jointure des sources de données
df_emissions_pop = pd.merge(df_pop_communes, df_emissions, how="inner", left_on="DEPCOM", right_on="INSEE commune")
df_emissions_pop

## Calcul d'une empreinte carbone
df_emissions_pop["empreinte_carbone"] = df_emissions_pop["emissions_totales"] / df_emissions_pop["PTOT"]

## Affichage des communes avec les empreintes carbones les plus élevées
df_emissions_pop.sort_values("empreinte_carbone", ascending=False).head(10)

# -------------------------------------------------------------------------- #

# Exercice 5

# Partie 1

## Import des données
df_valeurs = pd.read_csv('data/serie_glaces_valeurs.csv', delimiter=';',
                         skiprows=4, names=["periode", "indice", "code"])
df_metadata = pd.read_csv('data/serie_glaces_metadonnees.csv', delimiter=';',
                          skiprows=5, names=["code", "signification"])

# Partie 2

## Fusion des deux DataFrames sur les codes
df_merged = pd.merge(df_valeurs, df_metadata, how='left', on='code')

## Retrait des observations avec les codes 'Q' et 'P'
df_clean = df_merged[df_merged['code'] == "A"]
df_clean = df_clean[["periode", "indice"]]

# Partie 3

## Conversion des types des colonnes
df_clean.info()
df_clean['periode'] = pd.to_datetime(df_clean['periode'])
df_clean['indice'] = pd.to_numeric(df_clean['indice'])
df_clean.info()

# Partie 4

## Calcul de l'évolution de l'indice d'une période à l'autre
df_clean['indice_prec'] = df_clean['indice'].shift(1)
df_clean['evo'] = ((df_clean['indice'] - df_clean['indice_prec']) / df_clean['indice_prec']) * 100

## Méthode alternative
df_clean['evo_alt'] = df_clean['indice'].pct_change(periods=1) * 100

# Partie 5

## Calcul de l'évolution glissante sur 12 mois
df_clean["evo_glissement_annuel"] = df_clean['indice'].pct_change(periods=12) * 100
df_clean.head(20)
