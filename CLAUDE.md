# project-euler

Résolution des problèmes Project Euler en Python.

## Environnement

- Gestion des dépendances : `uv` (jamais `pip` ni `venv` à la main)
- Tests : `uv run pytest`
- Ajout d'une dépendance : `uv add <paquet>`

## Méthode de travail

- TDD en baby steps : un test qui échoue, le code minimal, refactoring.
  Ne jamais écrire plusieurs tests d'avance.
- Un commit par cycle vert. Message à l'impératif présent.
- Ne pas passer à l'étape suivante sans mon accord explicite.

## Code

- Nommage métier, pas technique : `est_premier`, pas `check_num`.
  Le vocabulaire du problème mathématique prime sur le jargon d'implémentation.
- Une fonction = une intention. Extraire dès qu'un commentaire
  devient nécessaire pour expliquer un bloc.
- Type hints systématiques.
- Séparer le calcul pur de l'entrée/sortie.

## Ce que je ne veux pas

- Optimisation prématurée : d'abord une solution correcte et lisible.
- Solutions copiées depuis les forums Project Euler.
- Docstrings qui paraphrasent le nom de la fonction.