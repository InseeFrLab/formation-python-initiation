# -------------------------------------------------------------------------- #

# 1/ Cela signifie que tous les objets Python (nombres, strings, listes, etc..)
# sont des objets au sens de la POO : ils ont des attributs et des méthodes,
# qui sont définis par une classe.

# 2/ L'instruction `class` sert à définir une classe d'objets.

# 3/ Le constructeur `__init__` est un méthode spéciale qui permet à 
# l'utilisateur de définir les attributs d'un objet.

# 4/ Le self sert de référence à l'instance au sein de la classe. Il souligne
# qui va porter les attributs et les méthodes une fois l'objet instancié.

# 5/ La classe est la "recette" qui définit toutes les caractéristiques de l'objet.
# Mais l'objet n'est vraiment créée que lorsque la classe est instanciée, c'est à
# dire lorsqu'on crée une instance selon cette classe.

# 6/ Un attribut est une variable associée à un objet.

# 7/ Une méthode est une fonction particulière : elle est associée à un objet
# et n'existe pas indépendamment de lui.

# 8/ La présence de parenthèses permet de différencier l'appel d'un attribut
# et l'appel d'une méthode.
# Appel d'un attribut : instance.attribut
# Appel d'une méthode : instance.methode() avec d'éventuels paramètres.

# 9/ Oui, c'est même un des usages principaux des méthodes.
# Mais on peut également modifier un atrribut manuellement.

# 10/ Lorsque l'on manipule des objets dont on souhaitent qu'ils conservent
# l'état d'une ressource au sein d'un programme.

# -------------------------------------------------------------------------- #

class Citron:

    def __init__(self, couleur, masse):
        self.saveur = "acide"
        self.couleur = couleur
        self.masse = masse
        self.jus = masse / 4
        
    def recup_masse(self):
        print("La masse du citron est " + str(self.masse) + " grammes.")
        
    def recup_qte_jus(self):
        print("Il reste " + str(self.jus) + " mL de jus dans le citron.")
        
    def extraire_jus(self, quantite):
        if quantite > self.jus:
            print("Il n'y a pas assez de jus dans le citron pour la quantité demandée.")
        else:
            self.jus = max(0, self.jus - quantite)  # évite toute valeur négative de `jus`
            
citron = Citron("jaune", 500)

citron.recup_masse()
citron.recup_qte_jus()

# -------------------------------------------------------------------------- #

class Compte:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
        
    def affiche_solde(self):
        print("Le solde du compte de " + self.titulaire + " est " + str(self.solde) + " euros.")
        
    def depot(self, montant):
        self.solde += montant
    
    def retrait(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            print("Retrait accepté.")
        else:
            print("Retrait refusé : fonds insuffisants.")
            
    def transfert(self, destinataire, montant):
        if self.solde >= montant:
            destinataire.solde += montant
            self.solde -= montant
        else:
            print("Transfert refusé : fonds insuffisants.")
            
client1 = Compte("Bernard", 2000)
client2 = Compte("Bianca", 5000)

client1.affiche_solde()
client2.affiche_solde()

print()  # saut de ligne

client1.depot(1000)
client1.affiche_solde() # +1000

print()

client2.retrait(6000)
client2.affiche_solde() # aucun changement

print()

client2.retrait(1000)
client2.affiche_solde() # -1000

print()

client2.transfert(client1, 5000)
client2.affiche_solde() # aucun changement

print()

client2.transfert(client1, 2000)
client2.affiche_solde() # - 2000
client1.affiche_solde() # + 2000

# -------------------------------------------------------------------------- #
