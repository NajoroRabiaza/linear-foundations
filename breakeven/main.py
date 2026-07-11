# ======================================================
# Projet : Seuil de rentabilite d'une application mobile
# Modele mathematique :
#   Cout total : C(n) = Cf + c * n
#   Recette : R(n) = r * n
#   Seuil n* : R(n*) = C(n*) => n* = Cf / ( r -c )
# ======================================================

# Parametres du modele
# on modifie ces trois valeurs pour varier les tests
Cf = 200_000 # cout fixe : paye meme sans aucun user
c = 150
r = 300


# fonctions du modele
def cout_total(n):
    return Cf + c * n

def recette(n):
    return r * n


print("Cout pour 500 user :", cout_total(500))
print("Recette pour 500 user :", recette(500))
print("Cout pour 1000 user :", cout_total(1000))
print("Recette pour 1000 user :", recette(1000))