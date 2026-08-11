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