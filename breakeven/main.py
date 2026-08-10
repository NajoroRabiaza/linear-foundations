# ======================================================
# Projet : Seuil de rentabilite d'une application mobile
# Bloc : linear-foundations
# Auteur : Amboaranajoro RAJAONARILALA
# ------------------------------------------------------
# 
# 
# Modele mathematique :
#   Cout total : C(n) = Cf + c * n
#   Recette : R(n) = r * n
#   
#   Au seuil n*, les deux sont egaux
#   r * n* = Cf + c * n*
#   n* (r - c) = Cf
#   n* = Cf / (r - c)
#   
#   (r - c) est le gain net reel par utilisateur
#   si r <= c, le seuil n'existe pas et chaque user fait perdre de l'argent
#   
# ======================================================

import matplotlib.pyplot as plt


# Parametres du modele
# on modifie ces trois valeurs pour varier les tests
Cf = 200_000 # cout fixe : paye meme sans aucun user
c = 150
r = 300


# fonctions du modele
def cout_total(n):
    """
    Calcule le cout total pour n users
    C(n) = Cf + c * n
    """
    return Cf + c * n

def recette(n):
    """
    calcule la recette totale pour n users
    R(n) = r * n
    """
    return r * n

def seuil_rentabilite():
    """
    Calcule le nombre minimal de users pour etre rentable
    n* = Cf / (r - c)
    afficher ValueError si r <= c car le seuil n'existe pas
    """
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



def afficher_graphe(n_etoile):
    # on genere 500 points entre 0 et 2 fois le seuil pour avoir une courbe lisse
    pas = (2 * n_etoile) / 500
    valeur_n = []
    i = 0
    while i<= 2*n_etoile:
        valeur_n.append(i)
        i += pas

    # on calcule cout et recette pour chaque valeur de n
    valeurs_cout = []
    valeurs_recette = []
    for n in valeur_n:
        valeurs_cout.append(cout_total(n))
        valeurs_recette.append(recette(n))

    # construction du graphe
    plt.figure(figsize=(10, 6))
    plt.plot(valeur_n, valeurs_cout, color="red", label="Cout total C(n)")
    plt.plot(valeur_n, valeurs_recette, color="green", label="Recette R(n)")

    # ligne verticae pointiller au seuil
    plt.axvline(x=n_etoile, color="gray", linestyle="--")

    # annotation du seuil
    plt.annotate(
        f"n* = {int(n_etoile)}",
        xy=(n_etoile, recette(n_etoile)),
        xytext=(n_etoile + 50, recette(n_etoile) - 40000),
    )

    plt.title("seuil de rentabilite d'une application mobile")
    plt.xlabel("Nombre d'user")
    plt.ylabel("Montant en Ariary")
    plt.legend()
    plt.grid(True)
    plt.show()


def afficher_analyse_sensibilite():
    # on fait varier r de 200 a 500 par pas de 50
    # et on observe comment n* change pour chaque valeur de r
    valeurs_r = []
    valeurs_n_etoile = []

    r_test = 200
    while r_test <= 500:
        # on ignore le cas ou r_test est egal a c car division par zero
        if r_test > c:
            n = Cf / (r_test - c)
            valeurs_r.append(r_test)
            valeurs_n_etoile.append(n)
        r_test += 50

    plt.figure(figsize=(10, 6))
    plt.plot(valeurs_r, valeurs_n_etoile, color="blue", marker="o")
    plt.title("Impact de la recette sur le seuil de rentabilite")
    plt.xlabel("Recette par utilisateur (ar)")
    plt.ylabel("seuil n* (nombre d'user)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    n_etoile = seuil_rentabilite()
    afficher_rapport(n_etoile)
    afficher_graphe(n_etoile)
    afficher_analyse_sensibilite()