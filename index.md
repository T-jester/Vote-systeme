# Modélisation d'un vote et étude des modes de scrutins.



### Contextualisation
Lors des élections présidentielles de 2022 je me suis fait la réfléxion que la façon dont ont effectue le vote pouvait influencer le candidat sortant et, ayant le cas de Jospin en 2017 en tête, je me suis demandé si le scrutin uninominal à deux tours, celui actuellement en place, était vraiment le plus performant. En effet de nombreux autres pays utilisent des scrutins radicalement différents, sont-ils plus démocratiques ?

Je me suis donc intéressé aux différents modes de scrutin afin d'essayer de les comparer et de voir si un conviendrait mieux à l'élection du président français.



### Méthode
Pour répondre à cette question j'ai d'abord du chercher une modélisation adéquate.

L'idée est de représenter une idée par un "vecteur d'adhérence" où le vecteur représente une idée et chaque individus de la population est placé sur ce vecteur en fonction de son degré d'approbation de cette idée. On réuni finalement tous ces vecteurs dans un tenseurformant l'environment de l'étude.

Afin d'obtenir une représentation réaliste j'ai décidé de me réstreindre à ces élections présidentielles de 2022 pour lesquelles j'ai placé les candidats dans le tenseur.

Pour la répartition de la population un sondage est transmis à un échantillon aussi représentatif que possible de la population électorale.

En implémentant différents modes de scrutin, on pourrait alors les comparer.


### Différents modes de scrutin utilisés :
-scrutin uninominal à 1 et 2 tours (actuellement en place pour la présidentielle en France)

-scrutin par notation (celui mis en place pour la primaire populaire)

-scrutin par classement ou préférentiel à 1 ou 2 tours (par exemple en Australie ou aux Fidji)

-scrutin par approbation (utilisé dans quelques villes des États-Unis)



### Quelques remarques :
Ce projet est encore en cours, j'actualiserai cette page en fonction des avancements.

J'essaye autant que possible pour l'instant en faire un projet personnel, j'ai bien conscience que de grands mathématiciens se sont penchés sur ce sujet avant moi mais j'aimerai pour l'instant me faire ma propre idée avant de me pencher sur leur recherches.

Ceci n'a pas pour but de trouver de nouveaux résultats, juste de me faire mener une recherche car ça m'amuse :)
