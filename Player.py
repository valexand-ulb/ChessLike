from Army import Army
from os import name, system
from sys import exit


class Playgroup:
    def __init__(self, mat):
        self.nplayers = int(input('Number of players (2-4) : '))

        if self.nplayers == 2:
            self.p1 = Player(mat, 1, 'ul', 'red', self)
            self.p3 = Player(mat, 2, 'dr', 'blue', self)
            mat.printM()
        elif self.nplayers == 3:
            self.p1 = Player(mat, 1, 'ul', 'red', self)
            self.p2 = Player(mat, 2, 'ur', 'green', self)
            self.p3 = Player(mat, 3, 'dr', 'blue', self)
            mat.printM()

        elif self.nplayers == 4:
            self.p1 = Player(mat, 1, 'ul', 'red', self)
            self.p2 = Player(mat, 2, 'ur', 'green', self)
            self.p3 = Player(mat, 3, 'dr', 'blue', self)
            self.p4 = Player(mat, 4, 'dl', 'yellow', self)
            mat.printM()


class Player:
    def __init__(self, mat, index, corner, color, parent):
        self.index = index
        self.corner = corner
        self.color = color

        self.parent = parent

        matsize = mat.getSize()

        if self.corner == 'ul':
            self.army = Army(mat, matsize, 'ul', self.color, self)
        elif self.corner == 'ur':
            self.army = Army(mat, matsize, 'ur', self.color, self)
        elif self.corner == 'dl':
            self.army = Army(mat, matsize, 'dl', self.color, self)
        elif self.corner == 'dr':
            self.army = Army(mat, matsize, 'dr', self.color, self)

    def ask(self, mat):
        fini = False
        det = 'HELP : \n------- \n1) Pieces: \n King : K \n Guardian (1-2) : G \n Knight (1-3) : Kn \n'
        det2 = '2) Moves: \n Forward : F \n Backward : B \n Left : L ' + \
               '\n Right : R \n Diag up/down/left/right : D + U/D + L/R\n'
        det3 = 'e.g: Kn3 F = third knight forward\n     K DUR = king diagonal up right\n     G1 L = first guardian left'

        while not fini:
            ask = input(('J' + str(self.index) + ': Quel pion jouer ? (for help input H) :'))

            if ask == 'H':

                if name == 'posix':
                    system('clear')
                elif name == 'nt':
                    system('cls')

                print(det)
                print(det2)
                print(det3)
                print('')
                ask2 = input('Press any Key to continue : ')


                if name == 'posix':
                    system('clear')
                elif name == 'nt':
                    system('cls')

                mat.printM()

            elif ask == 'pass':
                fini = True

            elif ask == 'exit':
                exit()
                fini = True
            else:
                if 2 < len(ask) < 6:
                    lres = ask.split(' ')
                    piece = lres[0]
                    mov = lres[1]

                    if len(piece) == 1 and piece == 'K':  # king
                        if mov == 'F':
                            if self.army.king.isAlive() and self.army.king.MovFw(mat):
                                fini = True

                        elif mov == 'B':
                            if self.army.king.isAlive() and self.army.king.MovBw(mat):
                                fini = True

                        elif mov == 'L':
                            if self.army.king.isAlive() and self.army.king.MovLft(mat):
                                fini = True

                        elif mov == 'R':
                            if self.army.king.isAlive() and self.army.king.MovRgt(mat):
                                fini = True

                        elif mov == 'DUL':
                            if self.army.king.isAlive() and self.army.king.MovDUL(mat):
                                fini = True

                        elif mov == 'DUR':
                            if self.army.king.isAlive() and self.army.king.MovDUR(mat):
                                fini = True

                        elif mov == 'DDL':
                            if self.army.king.isAlive() and self.army.king.MovDDL(mat):
                                fini = True

                        elif mov == 'DDR':
                            if self.army.king.isAlive() and self.army.king.MovDDR(mat):
                                fini = True

                        else:
                            print('Movement ' + mov + ' non reconnu...')

                    elif len(piece) == 2 and piece[0] == 'G':  # guard
                        if mov == 'F':
                            if piece[-1] == '1':
                                if self.army.guard1.isAlive() and self.army.guard1.MovFw(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            elif piece[-1] == '2':
                                if self.army.guard2.isAlive() and self.army.guard2.MovFw(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            else:
                                print('Guardian ' + piece[-1] + " n'existe pas ...")

                        elif mov == 'B':
                            if piece[-1] == '1':
                                if self.army.guard1.isAlive() and self.army.guard1.MovBw(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            elif piece[-1] == '2':
                                if self.army.guard2.isAlive() and self.army.guard2.MovBw(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            else:
                                print('Guardian ' + piece[-1] + " n'existe pas ...")

                        elif mov == 'L':
                            if piece[-1] == '1':
                                if self.army.guard1.isAlive() and self.army.guard1.MovLft(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            elif piece[-1] == '2':
                                if self.army.guard2.isAlive() and self.army.guard2.MovLft(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            else:
                                print('Guardian ' + piece[-1] + " n'existe pas ...")

                        elif mov == 'R':
                            if piece[-1] == '1':
                                if self.army.guard1.isAlive() and self.army.guard1.MovRgt(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            elif piece[-1] == '2':
                                if self.army.guard2.isAlive() and self.army.guard2.MovRgt(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            else:
                                print('Guardian ' + piece[-1] + " n'existe pas ...")
                        else:
                            print('Movement ' + mov + ' non reconnu...')

                    elif len(piece) == 3 and piece[0:2] == 'Kn':  # knight
                        if mov == 'F':
                            if piece[-1] == '1':
                                if self.army.knight1.isAlive() and self.army.knight1.MovFw(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            elif piece[-1] == '2':
                                if self.army.knight2.isAlive() and self.army.knight2.MovFw(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            elif piece[-1] == '3':
                                if self.army.knight3.isAlive() and self.army.knight3.MovFw(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            else:
                                print('Knight ' + piece[-1] + " n'existe pas ...")

                        elif mov == 'B':
                            if piece[-1] == '1':
                                if self.army.knight1.isAlive() and self.army.knight1.MovBw(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            elif piece[-1] == '2':
                                if self.army.knight2.isAlive() and self.army.knight2.MovBw(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            elif piece[-1] == '3':
                                if self.army.knight3.isAlive() and self.army.knight3.MovBw(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            else:
                                print('Knight ' + piece[-1] + " n'existe pas ...")

                        elif mov == 'L':
                            if piece[-1] == '1':
                                if self.army.knight1.isAlive() and self.army.knight1.MovLft(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            elif piece[-1] == '2':
                                if self.army.knight2.isAlive() and self.army.knight2.MovLft(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            elif piece[-1] == '3':
                                if self.army.knight3.isAlive() and self.army.knight3.MovLft(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            else:
                                print('Knight ' + piece[-1] + " n'existe pas ...")

                        elif mov == 'R':
                            if piece[-1] == '1':
                                if self.army.knight1.isAlive() and self.army.knight1.MovRgt(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            elif piece[-1] == '2':
                                if self.army.knight2.isAlive() and self.army.knight2.MovRgt(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            elif piece[-1] == '3':
                                if self.army.knight3.isAlive() and self.army.knight3.MovRgt(mat):
                                    fini = True
                                else:
                                    print('Pièce morte')
                            else:
                                print('Knight ' + piece[-1] + " n'existe pas ...")

                        else:
                            print('Movement ' + mov + ' non reconnu...')

                    else:
                        print('Piece ' + piece + ' non reconnue...')
                else:
                    print('Formme non valide')

        mat.printM()
