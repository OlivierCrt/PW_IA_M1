"""  module pour la classe UneSolution """
import random

from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape3.Solution import Solution
from projet.solvers.SolverTabou import SolverTabou  #a enlever juste pour montrer a la prof



class UneSolution(Solution):
    """
    Classe pour definir une solution pour le cas 3 de la tache 2 (hérite de Solution)
    """

    #    attributs
    #    A COMPLETER
    #    //////////////////////////////////////////////
    tg: GrapheDeLieux
    """  le graphe representant le monde """

    ordre_visite: list[int]

    dep : int

    #    constructeurs
    
    def __init__(self, tg: GrapheDeLieux,depart : int = 0, l_ordre_visite=[]):
        """  constructeur d'une solution a partir du graphe representant le monde

        :param tg: graphe representant le monde
        """
        self.tg = tg
        self.dep = depart
        if l_ordre_visite:
            self.ordre_visite = l_ordre_visite.copy()
        else:
            self.ordre_visite = self.randomListe()

    def randomListe(self):
        l = [self.dep]
        sommets = self.tg.getSommets().copy()
        sommets.remove(self.dep)
        while len(sommets)>0:
            indice = random.randint(0,len(sommets)-1)
            l.append(sommets[indice])
            sommets.remove(sommets[indice])
        l.append(self.dep)
        return l

    #    methodes de la classe abstraite Solution
    #    //////////////////////////////////////////////


    def unVoisinListe(self):
        """  
            sous fonction d 'olivier

        :return voisin de la solution courante sous forme de liste
        """
        first_random = random.randint(1, len(self.ordre_visite)-2)
    
        while True:
            second_random = random.randint(1,len(self.ordre_visite) -2)
            if second_random != first_random:
                break


        if (first_random > second_random) :
            temp = first_random
            first_random = second_random
            second_random = temp

        gogo = self.ordre_visite.copy()

        gogo[first_random:second_random] = gogo[first_random:second_random][::-1]

        return gogo
    



    def unVoisin(self) :
        voisin_liste = self.unVoisinListe() 
        return [UneSolution(self.tg, self.dep, voisin_liste)]
        




    def lesVoisins(self):
        nbvoisins = self.tg.getNbSommets() //2

        liste_ordre =[]
        actuel =self.unVoisinListe()
        k=UneSolution(self.tg, self.dep,actuel)
        visite=[]
        visite.append(actuel)

        for i in range (nbvoisins):
            if k not in liste_ordre :
                liste_ordre.append(k)
            
            
            actuel = self.unVoisinListe()
               
            k =UneSolution(self.tg, self.dep,actuel)
        return liste_ordre


        


        
    
        


    
        

    def eval(self):
        """  methode recuperant la valeur de la solution courante

        :return valeur de la solution courante
        """
        eval = 0
        e = self.ordre_visite[0]
        for i in self.ordre_visite[1:]:
            eval += GrapheDeLieux.dist(e,i,self.tg)
            e = i
        return eval

    def nelleSolution(self):
        """  methode generant aleatoirement une nouvelle solution
        a partir de la solution courante

        :return nouvelle solution generee aleatoirement a partir de la solution courante
        """
        return UneSolution(self.tg)

    def displayPath(self):
        """  methode affichant la solution courante comme un chemin dans le graphe
        """
        #    A ECRIRE
        print("la meilleure solution est : ",self.eval())
        for e in self.ordre_visite:
            print(e)








    #    methodes pour pouvoir utiliser cet objet dans des listes et des map
    #    //////////////////////////////////////////////
    def __hash__(self):
        """  methode permettant de recuperer le code de hachage de la solution courante
        pour une utilisation dans des tables de hachage

        :return code de hachage
        """
        #    A ECRIRE et MODIFIER le return en consequence
        return hash(tuple(self.ordre_visite))

    def __eq__(self, o):
        """  methode de comparaison de la solution courante avec l'objet o

        :param o: l'objet avec lequel on compare

        :return True si la solution courante et o sont egaux, False sinon
        """
        if not isinstance(o, UneSolution):
            return False
        if len(self.ordre_visite) != len(o.ordre_visite):
            return False

        m = True
        for i in range(len(self.ordre_visite)):
            if self.ordre_visite[i] != o.ordre_visite[i]:
                m = False  #MCL: ICI je rajouterais un break car 
                #MCL: des qu il y a un indice pour lequel les valeurs 
                #MCL: ne correspondent pas on sait que c est faux et 
                #MCL: c est inutile de continuer a verifier

        return m

        #    methode pour affichage futur (heritee d'Object)

    #    //////////////////////////////////////////////
    def __str__(self):
        """  methode mettant la solution courante sous la forme d'une
        chaine de caracteres en prevision d'un futur affichage

        :return representation de la solution courante sour la forme d'une chaine de caracteres
        """
        s=""
        for e in self.ordre_visite:
            s += str(e) + "-"
        s += " avec un score de :" + str(self.eval()) + "\n"
        return s




"""
tg = GrapheDeLieux.loadGraph("Data/town150.txt",True)
tsp = UneSolution(tg)
l = tsp.lesVoisins()
print("Initial:",tsp.ordre_visite)
for i in l :
    print(i.ordre_visite)


SolverTabou.tabou(tsp,10)

"""
