# Ex 1
x = 3
print(type(x))

x = "test"
print(type(x))

x = 3.5
print(type(x))

# Ex 2
a = "une première chaîne"
b = "et une deuxième"
c = "jamais deux sans trois"

len(a) + len(b) + len(c)

# Ex 3
cp1_int = 92120
cp1_str = "92120"

print(cp1_int, cp1_str) # Pas de problème

cp2_int = 02350 
# Erreur : Python n'accepte pas de définir un entier qui commence par un 0.
# Il faut donc définir les codes postaux comme des strings.

# Ex 4
a = "Je fais un comptage des e."
a.count('e')

# Ex 5
a = "Je fais un comptage des e."
a.find('e')

# Ex 6
a = "    Un string très mal formatté.         "
a.strip()

# Ex 7
"juste un \"petit\" test"

# Ex 8
a = 1
a -= 5
a *= 4
a += 22
print(a)

# Ex 9
a1 = "nous sommes en"
a2 = "nous sommes en {}"
b = "2024"

print(a1 + " " + b)
print(a2.format(b))

# Ex 10
# Premier problème : composition de strings avec des valeurs numériques
# La concaténation directe renvoie une erreur -> il faut au préalable
# convertir la valeur numérique en string
a1 = "nous sommes en"
b = 2024

# print(a1 + " " + b)  # Erreur
print(a1 + " " + str(b))

# Deuxième problème : juxtaposition de multiples chaînes de caractères
# La syntaxe devient vite illisible, car il faut ajouter les séparateurs (espace)
# manuellement entre chaque partie.
a = "nous sommes en"
b = "2024"
c = "et je m'appelle"
d = "Miranda"

print(a + " " + b + " " + c + " " + d)

# Troisième problème : composition de chaînes de caractères avec injection de variables
# La syntaxe reste illisible, car il faut injecter les valeurs dans chaque chaîne
a = "nous sommes en {}"
b = "2024"
c = "et je m'appelle {}"
d = "Miranda"

print(a.format(b) + " " + c.format(d))

# Solution : avec les f-strings
# Beaucoup plus lisible !
annee = 2024
prenom = "Miranda"

print(f"nous sommes en {annee} et je m'appelle {prenom}")
