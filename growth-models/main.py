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



def temps_doublement(resultats, N0):
    """
    Retourne le premier pas de temps ou la population a double,
    Retourne None si le doublement n'a jamais exister
    """
    for t in range(len(resultats)):
        if resultats[t] >= N0 * 2:
            return t
    return None


def afficher_resultats(lin, exp, log, N0):
    print("=" * 50)
    print("resultats de la simulation")
    print("=" * 50)
    print(f"Population initiale : {N0}")
    print(f"Pas de temps : {T}")
    print("-" * 50)

    print(f"lineaire : valeur finale = {lin[-1]:.2f}")
    t_lin = temps_doublement(lin, N0)
    if t_lin:
        print(f" doublement a t = {t_lin}")

    print(f"exponentiel : valeur finale = {exp[-1]:.2f}")
    t_exp = temps_doublement(exp, N0)
    if t_exp:
        print(f" doublement a t = {t_exp}")

    print(f"logistique : valeur finale = {log[-1]:.2f}")
    t_log = temps_doublement(log, N0)
    if t_log:
        print(f" doublement a t = {t_log}")
    else:
        print(f" doublement non atteint")

    print("=" * 50)



if __name__ == "__main__":
    lin = croissance_lineaire(N0, a, T)
    exp = croissance_exponentielle(N0, r, T)
    log = croissance_logistique(N0, r, K, T)
    afficher_resultats(lin, exp, log, N0)
    