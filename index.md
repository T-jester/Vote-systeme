# Modélisation des élections et étude des modes de scrutins.



### Contextualisation
Lors des élections présidentielles de 2022 je me suis fait la réfléxion que la façon dont ont effectue le vote pouvait influencer le candidat vainqueur. Ayant le cas de Lionel Jospin en 2017 en tête, je me suis demandé si le scrutin uninominal à deux tours, celui actuellement en place, était vraiment "le meilleur". 
  Dans le monde, de nombreux autres scrutins très différents sont utilisés. S'ils s'avèrent proposer des propriétées recherchées pour un vote<sup>[1](#propvote)</sup>, les pays les utilisant sont-ils plus démocratiques ?

Je me suis donc intéressé aux différents modes de scrutin afin d'essayer de les comparer et de voir si un conviendrait mieux à l'élection du président français.





### Méthode
Pour répondre à cette question j'ai d'abord du chercher une modélisation adéquate.

L'idée est de représenter une idée par un "vecteur d'adhérence" où chaque individu de la population étudiée est placé sur ce vecteur en fonction de son degré d'approbation de cette idée. On réunit finalement tous ces vecteurs dans un tenseur et on obtient ainsi un échiquier politique multi-dimentionnel qui nous permet de modéliser à quel point un individu est d'accord avec un politicien en fonction de leur distance l'un à l'autre<sup>[2](#distance)</sup>. On peut ainsi choisir la personne pour laquelle il un individu votera lorsqu'on simulera un mode de scrutin.

Afin d'obtenir une représentation réaliste j'ai décidé de me réstreindre aux élections présidentielles de 2022, j'ai donc placé les candidats de cette année dans le tenseur en fonction de leur programme politique<sup>[3](#programme)</sup>.

Pour la répartition de la population sur le tenseur, un sondage tourne de sorte à toucher un échantillon aussi représentatif que possible de la population électorale.

En implémentant différents modes de scrutin, on peut finalement les tester sur de larges échantillons de population et comparer les résultats facilement.







### Différents modes de scrutin utilisés 
- scrutin uninominal à 1 et 2 tours (actuellement en place pour la présidentielle en France)

- scrutin par notation (celui mis en place pour la primaire populaire)

- scrutin par classement ou préférentiel à 1 ou 2 tours 

- scrutin par approbation (utilisé dans quelques villes des États-Unis)

- scrutin alternatif (par exemple en Australie ou aux Fidji)

- scrutin de condorcet (randomisé ou non)






### Avancement
- [x] Construire l'environment
- [x] Implémenter les différents modes de scrutins
- [ ] Obtenir la répartition de la population sur le tenseur (en cours)
- [ ] Comparer les résultats obtenus
- [ ] Tester la fiabilité du modèle








### Faiblesses du modèle
- cela reste assez subjectif, j'ai choisi les questions des vecteurs d'approbations, j'ai choisi l'échelle, j'ai choisi la norme décidant de la distance d'un candidat à un électeur...
- le modèle à des limites : il est difficile de quantifier avec les vecteurs d'approbations les idées nouvelles apportées par des candidats ingénieux
- dans l'état actuel il n'est pas capable de modéliser le "vote utile" qui est un point important du choix d'un mode de scrutin



<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
  <sup>
  <a name="propvote">1</a>: Par exemple : <br> - l'unanimité : si une majorité préfère un candidat il doit être élu <br>
                                             - la non-dictature : le choix ne doit pas dépendre que d'un seul individu <br>
                                             - l'indépendance des options non pertinentes : échanger l'ordre de 2 candidat ne doit pas changer la position finale d'un candidat dont l'ordre n'a pas été impacté . <br>
  Le théorème d'Arrow stipule qu'il est impossible de réunir ces conditions avec un vote par classement.<br>
 <br>
 
  <a name="distance">2</a>: Je pense utiliser principalement la norme euclidienne bien que la norme 1 peut mériter qu'on s'y interesse.<br>
  
  <br>
  
  <a name="programme">3</a>: Je me suis aidé du site https://www.ifrap.org/comparateurs/presidentielle-2022
  </sup>










