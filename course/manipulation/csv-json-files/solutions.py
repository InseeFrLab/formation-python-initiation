# -------------------------------------------------------------------------- #

# 1/ Un CSV est un fichier texte qui représente l'information brute d'un document
# type tableur. Chaque ligne du fichier représente une ligne du tableur, et les
# cellules d'une ligne sont séparées par des virgules. La première ligne peut
# continer un `header` (en-tête), c'est à dire le nom des colonnes, mais ce
# n'est pas toujours le cas.

# 2/ Simplicité de lecture et d'édition, universalité.

# 3/ Même si le format CSV est très simple, il présente certaines caractéristiques
# (délimiteur, caractère de fin de ligne, etc.) dont il faut tenir compte lorsqu'on
# lit ou édite du CSV. Le module csv fournit des fonctions qui tiennent compte
# de ces particularités.

# 4/ Non, on peut en théorie séparer les données par n'importe quel caractère
# ou suite de caractères. En pratique, il faut suivre la convention dans la
# majorité des cas, qui est d'utiliser une virgule.

# 5/ C'est la première ligne du fichier CSV, qui contient normalement les noms
# de variables, mais ce n'est pas toujours le cas.

# 6/ C'est le format majoritaire de réponse des API, qui sont très utilisées
# pour la diffusion et l'échange de données.

# 7/ Aux dictionnaires.

# 8/ Tous les objets dits sérialisables, ce qui inclut la plupart des objets
# de base que l'on a vus, mais pas les objets créés manuellement via des classes.

# 9/ La sérialisation d'un objet Python (sérialisable) consiste à convertir 
# la donnée contenue dans cet objet en une séquence d'octets, c'est à dire
# en un message qui peut être compris par n'importe quel ordinateur.

# 10/ Ce sont des fichiers texte. 

# 11/ Non, les fichiers JSON comme les fichiers CSV sont des fichiers texte.
# L'extension est une convention qui permet dans la grande majorité des cas
# de savoir ce que contient le fichier, mais elle ne peut pas le garantir.

# -------------------------------------------------------------------------- #

import json

data = {"id": 1, "nom": "Isidore", "age": 29}

with open("data_sorted.json", "w") as file_out:
    json.dump(data, file_out, sort_keys=True)

# -------------------------------------------------------------------------- #

import json

class Citron:

    def __init__(self, couleur, qte_jus):
        self.saveur = "acide"
        self.couleur = couleur
        self.jus = qte_jus
        
mon_citron = Citron(couleur="jaune", qte_jus=45)
mon_citron_dict = mon_citron.__dict__

json.dumps(mon_citron_dict)

# -------------------------------------------------------------------------- #

# Trouvons à l'aide d'une commande shell le séparateur utilisé
!head -n 3 nat2020.csv

with open('nat2020.csv', 'r') as file_in:
    # Lecture du fichier CSV existant
    reader = csv.reader(file_in, delimiter=';')
    with open('nat2020_corr.csv', 'w') as file_out:
        # Ecriture dans le nouveau fichier CSV
        writer = csv.writer(file_out)  # Par défaut, le délimiteur est la virgule
        for row in reader:
            writer.writerow(row)
            
# Vérification à l'aide d'une commande shell
!head -n 3 nat2020_corr.csv

# -------------------------------------------------------------------------- #

r = requests.get("https://api-adresse.data.gouv.fr/search/?q=comedie&type=street")
r_text = response.text
r_dict = json.loads(r_text)

with open('resultats_ban.csv', 'w') as file_out:
    header = ['nom', 'ville', 'code_commune', 'longitude', 'latitude']
    csv_writer = csv.writer(file_out)
    csv_writer.writerow(header)
    for result in r_dict['features']:
        nom = result['properties']['name']
        commune = result['properties']['city']
        code_commune = result['properties']['citycode']
        long, lat = result['geometry']['coordinates']
        row = [nom, commune, code_commune, long, lat]
        csv_writer.writerow(row)

# -------------------------------------------------------------------------- #

from pathlib import Path

path_dep = Path("dep/")
path_dep.mkdir(exist_ok=True)

with open('departement2021.csv', 'r') as file_in:
    csv_reader = csv.reader(file_in)
    next(csv_reader)  # Passe le header
    for row in csv_reader:
        reg = row[1]
        filename = reg + '.csv'
        path_reg_file = path_dep / filename  # Chemin du fichier csv region
        with open(path_reg_file, 'a') as file_reg_in:
                writer = csv.writer(file_reg_in)
                writer.writerow(row)

# -------------------------------------------------------------------------- #

from pathlib import Path

with open('departement2021.csv', 'r') as file_in:
    csv_reader = csv.reader(file_in)
    header = next(csv_reader)

dep_files_paths = list(Path("dep/").glob('*.csv'))

for path in dep_files_paths:
    # Lecture du fichier existant, dont on stocke les lignes dans une liste
    with open(path, 'r') as file_dep_in:
        reader = csv.reader(file_dep_in)
        dep_rows = []
        for row in reader:
            dep_rows.append(row)
    # On réécrit le fichier de sortie, en rajoutant au préalable le header
    with open(path, 'w') as file_dep_out:
        writer = csv.writer(file_dep_out)
        writer.writerow(header)
        for row in dep_rows:
            writer.writerow(row)

# -------------------------------------------------------------------------- #
