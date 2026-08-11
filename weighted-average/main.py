# ===========================================================
# Projet : moyenne ponderer et detection de risque academique
# Bloc : linear-foundations
# Auteur : RAJAONARILALA Amboaranajoro
# -----------------------------------------------------------
# Modele mathematique :
# Moyenne ponderer : M = sum(note_i * coef_i) / sum(coef_i)
# 
# C est exactement la meme formule que l'esperance en probabilite
# E[X] = sum(x_i * p_i)
# La seule difference :les coef sont normaliser en probabilites
# ===========================================================

import matplotlib.pyplot as plt

# donnees : listes de tuples (matiere, note, coefficient)
matieres = [
    ("Algorithmiques", 12.5, 4),
    ("Mathematiques", 8.0, 4),
    ("Base de donnees", 14.0, 3),
    ("Anglais", 11.0, 2),
    ("Systemes", 7.5, 3),
    ("Genie logiciel", 13.0, 2),
    ("Modelisation", 9.5, 3),
]

def moyenne_ponderee(matieres):
    """
    calcule la moyenne ponderee d'une liste de matieres
    M = sum(note * coef) / sum(coef)
    """
    total_points = 0
    total_coefs = 0

    for matiere, note, coef in matieres:
        total_points += note * coef
        total_coefs += coef

    return total_points / total_coefs


# Test rapide
moyenne = moyenne_ponderee(matieres)
print(f"moyenne generale : {moyenne:.2f}")


def detection_risque(matieres, seuil=10.0):
    """
    Retourne la liste des matieres en dessous du seuil
    trier par note de croissance (la plus dangereuse en premier)
    """
    en_danger = []

    for matiere, note, coef in matieres:
        if note < seuil:
            en_danger.append((matiere, note, coef))

    # tri par note croissante
    en_danger.sort(key=lambda x: x[1])

    return en_danger


def matiere_critique(matieres, seuil=10.0):
    """
    retourne la matiere en dessous du seuil avec le coefficient le plus elevee
    c'est ce qui tire le plus la moyenne vers le bas
    """
    critique = None
    coef_max = 0

    for matiere, note, coef in matieres:
        if note < seuil and coef > coef_max:
            critique = (matiere, note, coef)
            coef_max = coef

    return critique


def afficher_rapport(matieres):
    moyenne = moyenne_ponderee(matieres)
    en_danger = detection_risque(matieres)
    critique = matiere_critique(matieres)

    print("=" * 50)
    print("rapport academique")
    print("=" * 50)
    print(f"moyenne generale : {moyenne:.2f} / 20")

    if moyenne >= 10:
        print("statut : admis")
    else:
        print("statut : en echec")

    print("-" * 50)
    print(f"matieres en danger ({len(en_danger)}) :")
    for matiere, note, coef in en_danger:
        print(f" {matiere:<20} note={note} coef={coef}")

    print("-" * 50)
    if critique:
        print(f"matiere critique : {critique[0]} (note={critique[1]}, coef={critique[2]})")
        print("c'est elle qui tire le plus la moyenne vers le bas")
    print("=" * 50)


def afficher_graphe(matieres):
    """
    trace un graphe en barre horizontale
    si note < 10 c'est rouge sinon c'est vert
    """

    noms = []
    notes = []
    couleurs = []

    for matiere, note, coef in matieres:
        noms.append(f"{matiere} (coef {coef})")
        notes.append(note)
        if note < 10:
            couleurs.append("red")
        else:
            couleurs.append("green")

    plt.figure(figsize=(10, 6))
    plt.barh(noms, notes, color=couleurs)

    # ligne verticale au seuil 10
    plt.axvline(x=10, color="black", linestyle="--", label="Seuil 10")

    # ligne verticale pour la moyenne generale
    moyenne = moyenne_ponderee(matieres)
    plt.axvline(x=moyenne, color="blue", linestyle="-", label=f"moyenne {moyenne:.2f}")

    plt.title("notes par matiere")
    plt.xlabel("note / 20")
    plt.xlim(0, 20)
    plt.legend()
    plt.grid(axis="x")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    afficher_rapport(matieres)
    afficher_graphe(matieres)