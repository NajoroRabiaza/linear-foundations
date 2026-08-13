# weighted-average
Modele de moyenne ponderee avec detection de risque academique

## modele mathematique
M = sum(note_i * coef_i) / sum(coef_i)

structurellement identique a l'esperance en probabilites :
E[X] = sum(x_i * p_i)

## lancer le projet
```bash
source venv/bin/activate
python3 weighted-average/main.py
```

## ce que le script produit :
- rapport academique avec status admis ou echec
- matieres en danger triees par note en croissance
- matiere critique qui tire le plus la moyenne vers le bas
- simulation de note minimale requise dans une matiere future
- graphe en barres horizontales colorer par seuil