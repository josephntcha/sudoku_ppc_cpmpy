# Sudoku – Résolution par programmation par contraintes

## Le problème

Le Sudoku se joue sur une grille de 9 × 9 cases, découpée en 9 blocs de 3 × 3.
Il faut remplir chaque case avec un chiffre de 1 à 9 en respectant trois règles :

1. **Lignes** : chaque ligne contient les chiffres de 1 à 9, sans répétition.
2. **Colonnes** : chaque colonne contient les chiffres de 1 à 9, sans répétition.
3. **Blocs** : chaque bloc 3 × 3 contient les chiffres de 1 à 9, sans répétition.

Ce projet modélise le Sudoku comme un **problème de satisfaction de contraintes (CSP)** :

- **Variables** : une variable entière par case, soit 81 variables `grid[i, j]`.
- **Domaine** : chaque variable prend une valeur dans `{1, …, 9}`.
- **Contraintes** : une contrainte `AllDifferent` sur chacune des 9 lignes, des 9 colonnes et des 9 blocs, soit 27 contraintes.

Le modèle est écrit avec la bibliothèque [CPMpy](https://cpmpy.readthedocs.io/) et résolu par le solveur **OR-Tools** (CP-SAT) de Google. Le programme affiche ensuite une grille complète qui respecte toutes les règles.

> Le script part pour l'instant d'une grille vide : il produit donc une grille de Sudoku valide quelconque. Pour résoudre une grille précise, il suffit d'ajouter des contraintes du type `grid[i, j] == valeur` pour chaque case déjà remplie.


## Prérequis

- Python 3.12 (ou une version 3.x récente)
- `pip`

## Installation et exécution

Python est un langage interprété : il n'y a pas d'étape de compilation. Il suffit d'installer les dépendances puis de lancer le script.

### 1. Créer l'environnement virtuel

Cette étape n'est nécessaire que si le dossier `venv/` n'existe pas encore.

```bash
python -m venv venv
```

### 2. Activer l'environnement virtuel

**Windows (PowerShell)** :

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (invite de commandes cmd)** :

```cmd
venv\Scripts\activate.bat
```

**Linux / macOS** :

```bash
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install cpmpy 
```

### 4. Lancer le programme

```bash
python sudoku.py
```
