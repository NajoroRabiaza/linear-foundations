# breakeven
Modele algebrique lineaire du seuil de rentabilite d'une application mobile

## Modele mathematique
C(n) = Cf + c * n (cout total)
R(n) = r * n (recette total)

Au seuil n* : R(n*) = C(n*)
=> n* = Cf / (r - c)

Avec les parametres du TD :
- Cf = 200 000 Ar (cout fixe)
- c = 150 Ar par user
- r = 300 Ar par user
- n* = 1333 user

## Lancer le projet

```bash
source venv/bin/activate
python3 breakeven/main.py
```

## Ce que produit le script
- Rapport de rentabilite dans le terminal
- Graphe 1 : courbes C(n) et R(n) avec le seuil n*
- Graphe 2 : evolution de n* quand la recette r varie de 200 a 500 Ar