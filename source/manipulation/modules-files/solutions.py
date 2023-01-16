# -------------------------------------------------------------------------- #

# 1/ un **module** est un fichier texte (portant l'extension .py pour bien
# marquer le lien à Python) contenant un ensemble de définitions (de **classes**,
# de **fonctions**) et d'instructions

# 2/ Un package est une collection de modules.

# 3/ Cela surcharge la mémoire si l'on a besoin que de quelques fonctions,
# et cela réduit la lisibilité puisqu'on ne sait pas directement de
# quel module provient quelle fonction.

# 4/ Elle permet d'interagir avec le système de fichiers avec une syntaxe de POO
# unifiée, quel que soit l'environnement sur lequel on travaille.

# 5/ Nom de fichier et chemin du dossier qui contient le fichier.

# 6/ C'est le répertoire dans lequel la session Python courante est ouverte.
# Dans le cadre d'un notebook Jupyter, c'est par défaut le dossier qui le contient.

# 7/ Chemin absolu (complet) et chemin relatif (relatif au répertoire courant).
# Un chemin absolu se reconnaît car il part toujours de la racine du système 
# de fichiers.

# 8/ Fichiers textes et fichiers binaires (tout ce qui n'est pas du texte).

# 9/ r : lecture. w : écriture. a : appending

# 10/ Cette syntaxe fait intervenir un context manager, qui gère la connexion 
# au fichier (ouverture et fermeture) pour nous.

# 11/ Car l'objet représentant le fichier en Python est un itérable.

# -------------------------------------------------------------------------- #

import numpy as np

with open("notes.txt", "r") as file_in:
    notes = file_in.read()
    
notes = notes.split()
notes_num = []
for n in notes:
    notes_num.append(int(n))
    
print(np.mean(notes_num))
print(np.std(notes_num))

# -------------------------------------------------------------------------- #

notes = []

with open("notes_clean.txt", "r") as file_in:
    for n in file_in:
        notes.append(int(n))
        
with open("notes_mentions.txt", "w") as file_out:
    for n in notes:
        if n >= 10:
            mention = "admis"
        else:
            mention = "recalé"
        file_out.write(str(n) + " " + mention + "\n")

# -------------------------------------------------------------------------- #

supp = [(16, 3), (11, 1), (3, 5)]

with open("notes_clean.txt", "a") as file_out:
    for elem in supp:
        note_finale = elem[0] - elem[1]
        note_finale = max(0, note_finale)
        file_out.write(str(note_finale) + "\n")

# -------------------------------------------------------------------------- #

from pathlib import Path

txt_files_paths = list(Path.cwd().glob('*.txt'))

for path in txt_files_paths:
    with open(path, "r") as file_in:
        content = file_in.read()
        if "sol" in content:
            print(path)

# -------------------------------------------------------------------------- #
