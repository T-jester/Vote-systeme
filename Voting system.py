import numpy as np
import matplotlib.pyplot as plt


N_OPPINIONS = 1
DX = 51
N_POLITICIANS = 3
POP_SIZE = DX**N_OPPINIONS//10

X_LABEL_NAME = "Aime Immigration"
Y_LABEL_NAME = "Aime Nucleaire"


# loi(int, size = N_POLITICIANS)
loi_pop = loi_pol = np.random.randint


"""
0 = Rien
n>0 = Nombre de Votant
-1 = Politicien
"""

def generate_tensor_space(N_OPPINIONS,DX) :
    """ Génère un tenseur de la forme (DX,DX,...,DX) avec N_OPPINIONS DX """
    rez = [0 for _ in range(DX)]
    for _ in range(N_OPPINIONS-1) :
        rez = [rez for _ in range(DX)]
    return np.array(rez)


def choose_population(TENSOR_SPACE, POP_SIZE,loi_pop) :
    """ Place la population sur le tenseur selon la loi loi_pop """
    assert POP_SIZE < len(TENSOR_SPACE)**N_OPPINIONS
    rez = []
    for _ in range(POP_SIZE) :
        a = tuple(loi_pop(DX,size = N_OPPINIONS))
        TENSOR_SPACE[a] += 1
        rez.append(a)
    return list(set(rez))


def choose_politicians(N_POLITICIANS, TENSOR_SPACE,loi_pol) :
    """ Place les politiciens sur le tenseur selon la loi loi_pol """
    assert N_POLITICIANS < len(TENSOR_SPACE)**N_OPPINIONS -POP_SIZE
    rez = []
    for _ in range(N_POLITICIANS) :
        a = tuple(loi_pol(DX,size = N_OPPINIONS))
        while TENSOR_SPACE[tuple(a)] != 0 :
            a = tuple(loi_pol(DX,size = N_OPPINIONS))
        TENSOR_SPACE[a] = -1
        rez.append(a)
    return rez


## INITIALISATION
TENSOR_SPACE = generate_tensor_space(N_OPPINIONS,DX)
SHAPE = TENSOR_SPACE.shape
POP = choose_population(TENSOR_SPACE, POP_SIZE,loi_pop)
POLITICIANS = choose_politicians(N_POLITICIANS, TENSOR_SPACE,loi_pol)

## Différentes normes : les VOTANTS choisiront les POLITICIANS les plus proche selon le choix de la norme

norm_1 = lambda p : np.sum(np.abs(p))
norm_e = lambda p : np.linalg.norm(p)
norm_inf = lambda p : np.abs(p).max()



def pts_to_dte(point,shape) :
    """ Transforme un point du tenseur en son rang après flatten """
    rez = 0
    for k in range(len(shape)) :
        rez += np.prod(shape[k+1:])*point[k]
    return int(rez)


def dte_to_pts(k,shape) :
    """ Récupère le rang du flatten et renvoie sa position dans le tenseur """
    p = k
    rez = []
    for j in range(len(shape)) :
        temp = int(np.prod(shape[(j+1):]))
        rez.append(p // temp)
        p %= temp
    return np.array(rez)




def voisins(p,r,norm = norm_e) : 
    """ Renvoie les points de B(p,r) où B est la boule r*unité pour la norme norm (compléxité très haute) """
    flattenTS = TENSOR_SPACE.flatten()
    p = np.array(p)
    a = TENSOR_SPACE.shape
    rez = []
    for k in range(len(flattenTS)) :

        if flattenTS[k] == 1 :
            pos = dte_to_pts(k,a)
            n = norm(p - pos)
            if  n > 0 and n <= r :
                rez.append(pos)
    return np.array(rez)


def exist(p,shape) :
    """ Renvoie True si le point p est dans le tenseur """
    n = len(p)
    assert n == len(shape)
    for k in range(n) :
        if p[k]<0 or p[k]>=shape[k] :
            return False
    return True



def voisins_norm_1(point,r) :
    """ Renvoie les points de B(p,r) où B est la boule r*unité pour la norme 1 (compléxité moindre) """

    rez = []

    if exist([point[0],point[1]+int(r)],SHAPE) and TENSOR_SPACE[tuple([point[0],point[1]+int(r)])]>0 :
        rez.append([point[0],point[1]+int(r)])

    if exist([point[0],point[1]-int(r)],SHAPE) and TENSOR_SPACE[tuple([point[0],point[1]-int(r)])]>0 :
        rez.append([point[0],point[1]-int(r)])


    for k in range(r+1) :
        for j in range(1,r-k+1) :
            if exist([point[0]+j ,point[1]+k],SHAPE) and TENSOR_SPACE[tuple([point[0]+j ,point[1]+k])]>0:
                rez.append([point[0]+j ,point[1]+k])

            if exist([point[0]-j ,point[1]-k],SHAPE) and TENSOR_SPACE[tuple([point[0]-j ,point[1]-k])]>0:
                rez.append([point[0]-j ,point[1]-k])

            if exist([point[0]-j ,point[1]+k],SHAPE) and TENSOR_SPACE[tuple([point[0]-j ,point[1]+k])]>0:
                rez.append([point[0]-j ,point[1]+k])

            if exist([point[0]+j ,point[1]-k],SHAPE) and TENSOR_SPACE[tuple([point[0]+j ,point[1]-k])]>0:
                rez.append([point[0]+j ,point[1]-k])

            if exist([point[0] ,point[1]+k],SHAPE) and TENSOR_SPACE[tuple([point[0] ,point[1]+k])]>0:
                rez.append([point[0] ,point[1]+k])

            if exist([point[0] ,point[1]-k],SHAPE) and TENSOR_SPACE[tuple([point[0] ,point[1]-k])]>0:
                rez.append([point[0] ,point[1]-k])

    return rez








def closest(l, norm) :
    """ Renvoie le plus petit élément de la liste l selon la norme norm """
    assert len(l) != 0
    val = l[0]
    for elem in l :
        if norm(elem) < norm(val) :
            val = elem
    return val


def barycentre(POP) :
    """ Prend une population repéré par des tuples et renvoie le barycentre de ces points """
    rez = np.zeros(shape = N_OPPINIONS, dtype = float)
    for ppl in POP :
        rez += np.array(ppl)*TENSOR_SPACE[ppl]
    return rez / POP_SIZE


def arround(v) :
    """ Arrondit les coordonnées du vecteur v """
    return np.array([round(x) for x in v])

## Méthodes de scrutin

# 1: scrutin uninominal (Présidentielle France)
def vote_uninominal(norm = norm_e) :
    dico = {pol : 0 for pol in POLITICIANS}

    for ppl in POP :
        dico[closest(POLITICIANS,lambda a : norm(np.array(a) -np.array(ppl)))] += TENSOR_SPACE[ppl]
    return dico



# Quelques normes en plus
norm_vote_abs = lambda p : 1-norm_inf(p)/DX
norm_vote_euc= lambda p : 1-np.linalg.norm(p)/np.linalg.norm(SHAPE)
norm_vote_1 = lambda p : 1-norm_1(p)/(len(p)*DX)


# 2: scrutin par notation (Primaire populaires France)
def vote_note(norm = norm_vote_1) :
    dico = {pol : 0 for pol in POLITICIANS}

    for pol in POLITICIANS :
        for ppl in POP :
            dico[pol] += TENSOR_SPACE[ppl] * norm(np.array(pol)-np.array(ppl))
        dico[pol] = round(dico[pol]/POP_SIZE, ndigits = 3)
    return dico



# 3: scrutin par classement 
def vote_ranking(norm = norm_e) :
    dico = {pol : 0 for pol in POLITICIANS}

    for ppl in POP :
        val = sorted(POLITICIANS,key = lambda a : norm(np.array(a)-np.array(ppl)))
        for k in range(len(val)) :
            dico[val[k]] += k * TENSOR_SPACE[ppl]
    return dico



# 4: scrutin par aprobabiton (fav <3)
def vote_support(r = DX//N_POLITICIANS) :
    dico = {pol : 0 for pol in POLITICIANS}

    for pol in POLITICIANS :
        for neigh in voisins_norm_1(pol,r) :
            dico[pol] += TENSOR_SPACE[tuple(neigh)]
    return dico




# 5: scrutin alternatif (Australie)

def vote_alternatif(norm = norm_vote_euc) :
    dico = {pol : 0 for pol in POLITICIANS}
    n = len(dico)
    pol = POLITICIANS[:]
    while True :

        temp = {pol : 0 for pol in POLITICIANS}
        for ppl in POP :
            temp[closest(pol,lambda a : norm(np.array(a) -np.array(ppl)))] += TENSOR_SPACE[ppl]


        if max(temp.values()) > POP_SIZE/2 :
            pol.sort(key = lambda p : temp[p])
            for p  in pol :
                dico[p] = n
                n-=1

            return dico


        pol.sort(key = lambda p : temp[p])
        if len(pol)>2 :
            dico[pol[0]] = n
            del pol[0]
            n-=1
        else :
            raise Exception("égalité")




"""
Reste à tester :

Retirer l'aspect Tenseur (garder pour affichage) et passer à une database panda avec personnes et positions seulement



Remplir avec les données des politiciens actuels


...
"""




## Affichage
assert N_OPPINIONS < 3


if N_OPPINIONS == 2 :
    X_pop = [pop[0] for pop in POP]
    Y_pop = [pop[1] for pop in POP]

    X_pol = [pop[0] for pop in POLITICIANS]
    Y_pol = [pop[1] for pop in POLITICIANS]

    plt.plot(X_pop,Y_pop, "bo", label = "Votants")
    plt.plot(X_pol,Y_pol, "ro", label = "Politiciens", ms = 10)


    plt.title("Carte des Votants et des Politiciens", fontdico = font_title, loc = "left")
    plt.xlabel(X_LABEL_NAME, fontdico = font_idea1)
    plt.ylabel(Y_LABEL_NAME, fontdico = font_idea2)
    plt.legend(bbox_to_anchor =(1.05, 1.10), ncol = 2,
                fontsize = "small")

    plt.show()


else :
    X_pop = [pop[0] for pop in POP]
    Y_pop = [1 for pop in POP]

    X_pol = [pop[0] for pop in POLITICIANS]
    Y_pol = [1 for pop in POLITICIANS]

    plt.plot(X_pop,Y_pop, "b|", label = "Votants", ms = 50)
    plt.plot(X_pol,Y_pol, "r|", label = "Politiciens", ms = 70)

    lim = [min(min(X_pop),min(X_pol)),max(max(X_pop),max(X_pol))]
    plt.plot(lim,[1,1],"k-")

    plt.ylim([0.5,1.5])

    plt.title("Carte des Votants et des Politiciens", fontdico = font_title, loc = "left")
    plt.xlabel(X_LABEL_NAME, fontdico = font_idea1)
    plt.ylabel(Y_LABEL_NAME, fontdico = font_idea2)
    plt.legend(bbox_to_anchor =(1.05, 1.10), ncol = 2,
                fontsize = "small")

    plt.show()






## Barycentre

# Affiche aussi le barycentre des POLITICIANS 
assert N_OPPINIONS < 3

X_pop = [pop[0] for pop in POP]
Y_pop = [pop[1] for pop in POP]

X_pol = [pop[0] for pop in POLITICIANS]
Y_pol = [pop[1] for pop in POLITICIANS]

plt.plot(X_pop,Y_pop, "bo", label = "Votants")
plt.plot(X_pol,Y_pol, "ro", label = "Politiciens", ms = 10)

B = arround(barycentre(POP))
plt.plot(B[0],B[1], "ko", label = "barycentre", ms = 10)



plt.title("Carte des Votants et des Politiciens", fontdico = font_title, loc = "left")
plt.xlabel(X_LABEL_NAME, fontdico = font_idea1)
plt.ylabel(Y_LABEL_NAME, fontdico = font_idea2)
plt.legend(bbox_to_anchor =(1.10, 1.10), ncol = 2,
            fontsize = "small")



plt.show()



