# growth-models

Comparaison de trois modeles de croissance de population et diagramme de bifurcation du modele logistique

## Modeles implementes
Lineaire : N(t) = N0 + a * t
Exponentiel : N(t) = N0 * (1 + r) ** t
Logistiques : N(t+1) = N(t) = r*N(t) * (1 - N(t) / K)

## Diagramme de bifurcation
Carte logistique normalisee : x(t+1) = r * x(t) * (1 - x(t))

- r < 3.0 : point fixe stable
- r > 3.0 : oscillants
- r > 3.57 : chaos deterministe

## Lancer le projet
```bash
source venv/bin/activate
python3 growth-models/main.py
```

## ce que produit le script
- rapport de simulation avec valeurs finales et temps de doublement
- graphe de comparaison des trois modeles
- diagramme de bifurcation