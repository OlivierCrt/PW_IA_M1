"""
module pour l'état de l'etape 2 ds le cas 1
"""
from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape2.Etat import Etat


class EtatCas1(Etat) :
    """ Classe pour definir un etat pour le cas 1 de la tache 2 (hérite de Etat)
    """

    # attributs
    tg : GrapheDeLieux
    courant :int
    final :int
    """ le graphe representant le monde """

    # constructeurs
    # A ECRIRE/MODIFIER/COMPLETER
    # //////////////////////////////////////////////
    def __init__(self, tg : GrapheDeLieux, param1 = None, param2 = None) :
        """ constructeur d'un etat a partir du graphe representant le monde

        :param tg: graphe representant le monde

        :param param1: ville de depart

        :param param2: ville d arrive
        """
        self.tg = tg
        if param1 is None:
          self.courant = 0
        else:
          self.courant=param1



        if param2 is None:
          self.final = self.tg.getNbSommets()-1
        else:
          self.final = param2

    def estSolution(self) :
        """ methode detectant si l'etat est une solution

        :return true si l'etat courant est une solution, false sinon
        """
        if self.courant == self.final :
          return True
        else :

          return False


    def successeurs(self) :
        """ methode permettant de recuperer la liste des etats successeurs de l'etat courant

        :return liste des etats successeurs de l'etat courant
        """
        successeurs=[]
        voisins = self.tg.getAdjacents(self.courant)
        for voisin in voisins:
            successeurs.append(EtatCas1(self.tg, voisin, self.final))
        return successeurs


    def h(self) :
        """ methode permettant de recuperer l'heuristique de l'etat courant

        :return heuristique de l'etat courant
        """

        return GrapheDeLieux.dist(self.courant, self.final, self.tg)


    def k(self, e) :
        """ methode permettant de recuperer le cout du passage de l'etat courant à l'etat e

        :param e: un etat

        :return cout du passage de l'etat courant à l'etat e
        """
        return self.tg.getCoutArete(self.courant, e.courant)


    def displayPath(self, pere) :
        """ methode pour afficher le chemin qui a mene a l'etat courant en utilisant la map des peres

        :param pere: map donnant pour chaque etat, son pere
        """
        chemin = []
        etat = self
        longueur_totale = 0

        if etat not in pere:
            print("Erreur : etat pas dans pere")
            return

        while etat in pere and pere[etat] is not None:
            chemin.append(etat.courant)

            parent = pere[etat]
            cout_arete = self.tg.getCoutArete(etat.courant, parent.courant)
            longueur_totale += cout_arete

            etat = parent

        if etat is not None:
            chemin.append(etat.courant)

        chemin.reverse()

        print(f"Chemin trouvé : {' -> '.join(map(str, chemin))}")
        print(f"Longueur totale du chemin : {longueur_totale}")




    def __hash__(self) :
        """ methode permettant de recuperer le code de hachage de l'etat courant
        pour une utilisation dans des tables de hachage

        :return code de hachage
        """
        return hash((self.courant,self.final))


    def __eq__(self, o) :
        """ methode de comparaison de l'etat courant avec l'objet o

        :param o: l'objet avec lequel on compare

        :return true si l'etat courant et o sont egaux, false sinon
        """
        if isinstance(o, EtatCas1):#on check quand meme si ils sont du mm type, return bool
          return self.courant == o.courant
        return False



    def __str__(self) :
        """ methode mettant l'etat courant sous la forme d'une
        chaine de caracteres en prevision d'un futur affichage

        :return representation de l'etat courant sour la forme d'une
        chaine de caracteres
        """

        return f"EtatCas1(position={self.courant}, target={self.final})"



