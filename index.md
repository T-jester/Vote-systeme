# Présentation du projet d'étude des modes de scrutins

N'hésitez pas à aller voir le [code](https://github.com/T-jester/Vote-systeme/blob/main/Voting%20system.py) sur mon GitHub.


### Contextualisation
Tout d'habord commençons par une petite contextualisation. Lors des électuions de 2022 en France il y a eu une primaire populaire pour sélectionner un candidat représentant pour la gauche. Cette élection utilisait un vote par valeur, c'est à dire que chaque individus évaluait chaque candidat avec une appréciation allant de Insuffisant à Très Bien. Cette méthode étant différante de celle en vigueur pour les élections présidentielles, je me suis demandé si l'un d'eux était meilleur que l'autre.



### Méthode
Pour répondre à cette question j'ai d'abord du chercher une modélisation adéquate.

L'idée est de représenter une idée par un "vecteur d'adhérence" où le vecteur représente une idée et chaque individus de la population est placé en fonction de son degré d'approbation de cette idée. On réuni finalement tous ces vecteurs dans un tenseur de dimention n avec n le nombre d'oppinions considérés.

Afin d'obtenir une représentation réaliste j'ai décidé de me réstreindre à ces élections présidentielles de 2022 pour lesquelles j'ai placé les candidats se résentant dans le tenseur.

Pour la répartition de la population je suis en train de préparer un sondage que je transmettrai à un échantillon aussi représentatif de la population électorale que possible.

En implémentant différents modes de scrutin, on pourrait alors les comparer (cf le [code](https://github.com/T-jester/Vote-systeme/blob/main/Voting%20system.py)).


### Différents modes de scrutin utilisés :
-scrutin uninominal à 1 et 2 tours (actuellement en place pour la présidentielle)

-scrutin par notation (celui mis en place pour la primaire populaire)

-scrutin par classement ou préférentiel à 1 ou 2 tours (par exemple en Australie ou aux Fidji)

-scrutin par approbation (utilisé dans quelques villes des États-Unis)



### Quelques remarques :
Ce projet est encore en cours, j'actualiserai cette page en fonction des avancements.

J'essaye autant que possible pour l'instant en faire un projet personnel, j'ai bien conscience que de grands mathématiciens se sont penchés sur ce sujet avant moi mais j'aimerai pour l'instant me faire ma propre idée avant de me pencher sur leur recherches.

Ceci n'a pas pour but de trouver de nouveaux résultats, juste de me faire mener une recherche car ça m'amuse :)
