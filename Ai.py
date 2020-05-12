from copy import deepcopy
from random import shuffle

class Ai:
    def __init__(self):
        pass


    """
    def minimax(self,coup,plateau,profondeur=2,joueur):
        if profondeur == 0 or coup est gagnant:
            return (None, score)
        
        if joueur maximise:
            meilleurcoup -= 1000
            meilleurcoup = []
            for coup in coup possible:
                copie plateau
                joue sur copie
                score = minimax(coup, nouveau plateau, profondeur-1, False)
                if meilleurscore < score:
                    meilleurscore = score
                    meilleurcoup = [(coup,score)]
                elif meilleurscore == score:
                    meilleurcoup.append([coup,score])
        
        else:
            meilleurscore = 1000
            meilleurcoup = []
            for coup in couppossible:
            copie le plateau
            joue sur copie
            score = minimax(coup, nouveau plateau, profondeur-1, True)
             if meilleurscore > score:
              meilleurscore = score
              meilleurcoup = [(coup,score)]
            elif meilleurscore == score:
                meilleurcoup.append([coup,score])
                
        shuffle(meilleurcoup)
        return meilleurcoup[0]
             
            
                    
        
    """

