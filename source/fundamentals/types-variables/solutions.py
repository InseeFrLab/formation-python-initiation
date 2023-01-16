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
b = "2022"

print(a1 + " " + b)
print(a2.format(b))
