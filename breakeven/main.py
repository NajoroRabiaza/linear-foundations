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

def seuil_rentabilite():
    # n* = Cf / (r-c)
    # on divise par (r-c) et pas par r seulement car chaque user
    # coutte aussi c, donc le gain net reel par user est (r-c)
    if r-c <= 0:
        raise ValueError("la recette par user doit etre > au cout variable")

    n_etoile = Cf / (r-c)
    return n_etoile


def afficher_rapport(n_etoile):
    print("=" * 50)
    print("Rapport de rentabilite")
    print("=" * 50)
    print(f"Cout fixe : {Cf} Ar")
    print(f"Cout par user : {c} Ar")
    print(f"recette par user : {r} Ar")
    print(f"gain net par user : {r-c} Ar")
    print("-" * 50)
    print(f"seuil de rentabilite : {int(n_etoile)} user")
    print("-" * 50)
    print(f"en dessous de {int(n_etoile)} users, l'appli perd de l'argent")
    print(f"au dela de {int(n_etoile)} users, l'appli est rentable")
    print(f"cout a ce seuil : {int(cout_total(n_etoile))} Ar")
    print(f"recette a ce seuil : {int(recette(n_etoile))} Ar")
    print("=" * 50)


# test d'execution
n_etoile = seuil_rentabilite()
afficher_rapport(n_etoile)