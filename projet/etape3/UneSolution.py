"""  module pour la classe UneSolution """
import random

from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape3.Solution import Solution


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
    #    A ECRIRE/COMPLETER
    #    //////////////////////////////////////////////
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
        sommets = self.tg.getSommets()
        sommets.remove(self.dep)
        while len(sommets)>0:
            indice = random.randint(0,len(sommets)-1)
            l.append(sommets[indice])
            sommets.remove(sommets[indice])
        l.append(self.dep)
        return l

    #    methodes de la classe abstraite Solution
    #    //////////////////////////////////////////////
    def lesVoisins(self):
    
        out = []
        temp_out = set()

        n = len(self.ordre_visite)
        for i in range(1, n - 1):  # On exclut le premier et le dernier sommet
            sommet = self.ordre_visite[i]

            for j in range(i+1, n - 1):  # On peut insérer entre les positions 1 et n-2
                if i == j:
                    continue  # Pas besoin de réinsérer à la même position
                # Construire une nouvelle solution
                nouvelle_liste = self.ordre_visite[:i] + self.ordre_visite[i + 1:]
                nouvelle_liste.insert(j, sommet)

                # Vérifier l'unicité et ajouter la solution
                tuple_liste = tuple(nouvelle_liste)  # Les listes ne sont pas hashables, convertir en tuple
                if tuple_liste not in temp_out:
                    temp_out.add(tuple_liste)
                    out.append(UneSolution(self.tg, depart=self.dep, l_ordre_visite=nouvelle_liste))

        return out


    def unVoisin(self):
        """  methode recuperant un voisin de la solution courante

        :return voisin de la solution courante
        """
        voisins = self.lesVoisins()
        indice=0
        min= voisins[0].eval()
        for i in range(1,len(voisins)):
            e = voisins[i].eval()
            if e < min:
                indice = i
        return [voisins[indice]]

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
        return 0

    def __eq__(self, o):
        """  methode de comparaison de la solution courante avec l'objet o

        :param o: l'objet avec lequel on compare

        :return True si la solution courante et o sont egaux, False sinon
        """
        if not isinstance(o, UneSolution):
            return False
        if len(self.ordre_visite) != len(o.ordre_visite):
            return False

        constante = True
        for i in range(len(self.ordre_visite)):
            if self.ordre_visite[i] != o.ordre_visite[i]:
                constante = False

        return constante

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