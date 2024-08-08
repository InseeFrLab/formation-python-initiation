# Formation - Initiation à Python

*Auteur : Romain Avouac*

*Contributeurs : Yves-Laurent Bénichou, Olivier Chateau, Thomas Faria, Antoine Palazzolo*

## Site associé

Le site web associé à la formation est déployé à [cette adresse](https://inseefrlab.github.io/formation-python-initiation/).

## Déploiement à partir du SSP Cloud

Ce projet contient les supports de cours de l'auto-formation d'initiation à Python proposée sur le [SSP Cloud](https://datalab.sspcloud.fr/home). A partir de la [page de la formation](https://www.sspcloud.fr/formation?search=&path=%5B%22Initiation%20%C3%A0%20Python%22%5D), les différents chapitres peuvent être déployés en un clic sous la forme d'un Notebook Jupyter.

## Génération des notebooks

Afin de favoriser la reproductibilité de la formation, les sources des supports de cours sont disponibles au format `.qmd` ([Quarto](https://quarto.org/)) dans le dossier `source/`. Les notebooks `Jupyter` (format `.ipynb`) exécutables associés peuvent être générés en suivant les étapes suivantes :
- [installer Quarto](https://quarto.org/docs/get-started/)
- cloner le dépôt de la formation :

```bash
git clone https://github.com/InseeFrLab/formation-python-initiation.git
cd formation-python-initiation
```

- installer les packages `Python` nécessaires :

```bash
pip install -r requirements.txt
```

- générer les notebooks :

```bash
quarto render --profile notebooks
```
