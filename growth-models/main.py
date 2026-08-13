# =======================================================
# Projet : simulateur de croissance
# Bloc : linear-foundations
# Autheur: Amboaranajoro RAJAONARILALA
# =======================================================
# On a trois modele de croissance pour une population N(t):
# 
#   lineaire : N(t) = N0 + a * t
#   Exponentiel : N(t) = N0 * (1 + r) ** t
#   Logistique : N(t+1) = N(t) + r * N(t) * (1 - N(t) / k)
# =======================================================

# Paramatres du modele
N0 = 100 # population initiale
r = 0.1 # taux de croissance
a = 10 # increment lineaire par pas de temps
K = 1000 # capacite limite (logistique seulement)
T = 50 # nombre de pas de temps


def croissance_lineaire(N0, a , T):
    """
    N(t) = N0 + a * t
    la croissance est constante, independante de la taille actuel.
    """
    resultats = []
    for t in range(T+1):
        resultats.append(N0 + a * t)
    return resultats


def croissance_exponentielle(N0, r, T):
    """
    N(t) = N0 * (1 + r) ** t
    chaque individu produit r nouveaux individus a chaque pas
    """
    resultats = []
    for t in range(T+1):
        resultats.append(N0 * (1 + r) ** t)
    return resultats


def croissance_logistique(N0, r, K, T):
    """
    N(t+1) = N(t) + r * N(t) * (1 - N(t) / K)
    croissance exponentielle freiner par la capacite limiter K.
    et quand N se rapproche de K, le terme (1 - N/K) tend vers 0.
    """
    resultats = [N0]
    for t in range(T):
        N_actuel = resultats[-1]
        N_suivant = N_actuel + r * N_actuel * (1 - N_actuel / K)
        resultats.append(N_suivant)
    return resultats


# test rapide
lin = croissance_lineaire(N0, a, T)
exp = croissance_exponentielle(N0, r, T)
log = croissance_logistique(N0, r, K, T)

print(f"lineaire : debut={lin[0]} fin={lin[-1]:.2f}")
print(f"exponentiel : debut={exp[0]} fin={exp[-1]:.2f}")
print(f"logistique : debut={log[0]} fin={log[-1]:.2f}")
