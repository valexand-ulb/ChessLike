from time import sleep
from Mat import Mat
from Player import Playgroup


def round_by_roun(m):
    gagnant = False
    while not gagnant:
        pg.p1.ask(m)
        pg.p2.ask(m)
        pg.p3.ask(m) if pg.nplayers >= 3 else None
        pg.p4.ask(m) if pg.nplayers == 4 else None


m = Mat(int(input('Taille du plateau (conseillé min 11) : ')))
pg = Playgroup(m)
round_by_roun(m)


