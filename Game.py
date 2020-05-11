from sys import exit
from Mat import Mat
from Player import Playgroup


class ChessLike:
    def __init__(self):
        self.m = Mat(int(input('Taille du plateau (conseillé min 11) : ')))
        self.pg = Playgroup(self.m)

        self.round_by_roun(self.m)

    def round_by_roun(self, m):
        gagnant = False
        while not gagnant:
            self.pg.p1.ask(m) if gagnant is False else None
            gagnant = True if self.winner(m) else False

            self.pg.p3.ask(m) if gagnant is False else None
            gagnant = True if self.winner(m) else False

            self.pg.p2.ask(m) if self.pg.nplayers >= 3 and gagnant is False else None
            gagnant = True if self.winner(m) else False

            self.pg.p4.ask(m) if self.pg.nplayers > 3 and gagnant is False else None
            gagnant = True if self.winner(m) else False

    def winner(self, m):
        size = m.getSize()
        res = False
        kingP1 = self.pg.p1.army.king.isAlive()
        kingP2 = self.pg.p3.army.king.isAlive()
        kingP3 = self.pg.p2.army.king.isAlive() if self.pg.nplayers >= 3 else False
        kingP4 = self.pg.p4.army.king.isAlive() if self.pg.nplayers > 3 else False

        if kingP1 and not kingP2 and not kingP3 and not kingP4:
            print('Joueur rouge Gagnant')
            res = True
            exit()
        elif not kingP1 and kingP2 and not kingP3 and not kingP4:
            print('Joueur bleu Gagnant')
            res = True
            exit()
        elif not kingP1 and not kingP2 and kingP3 and not kingP4:
            print('Joueur vert Gagnant')
            res = True
            exit()
        elif not kingP1 and not kingP2 and not kingP3 and kingP4:
            print('Joueur jaune Gagnant')
            res = True
            exit()

        elif m.mat[size//2][size//2] != 9 :
            if m.mat[size//2][size//2][0] == 3:
                if m.mat[size//2][size//2][1] == 'red':
                    print('Joueur rouge Gagnant')
                    res = True
                    exit()
                elif m.mat[size//2][size//2][1] == 'green':
                    print('Joueur vert Gagnant')
                    res = True
                    exit()
                elif m.mat[size//2][size//2][1] == 'blue':
                    print('Joueur bleu Gagnant')
                    res = True
                    exit()
                elif m.mat[size // 2][size // 2][1] == 'yellow':
                    print('Joueur jaune Gagnant')
                    res = True
                    exit()

        return res


if __name__ == '__main__':
    g = ChessLike()


