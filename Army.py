

class Army:
    def __init__(self, mat, matsize, corner, color, parent):

        self.corner = corner
        self.color = color
        self.size = matsize

        self.parent = parent

        if self.corner == 'ul':
            self.king = King(mat, 0, 0, 1, 'ul', self.color, self)

            self.guard1 = Guardian(mat, 1, 0, 1, 'ul', self.color, self)
            self.guard2 = Guardian(mat, 0, 1, 2, 'ul', self.color, self)

            self.knight1 = Knight(mat, 2, 0, 1, 'ul', self.color, self)
            self.knight2 = Knight(mat, 1, 1, 2, 'ul', self.color, self)
            self.knight3 = Knight(mat, 0, 2, 3, 'ul', self.color, self)

        elif self.corner == 'ur':
            self.king = King(mat, self.size - 1, 0, 1, 'ur', self.color, self)

            self.guard1 = Guardian(mat, self.size - 2, 0, 1, 'ur', self.color, self)
            self.guard2 = Guardian(mat, self.size - 1, 1, 2, 'ur', self.color, self)

            self.knight1 = Knight(mat, self.size - 3, 0, 1, 'ur', self.color, self)
            self.knight2 = Knight(mat, self.size - 2, 1, 2, 'ur', self.color, self)
            self.knight3 = Knight(mat, self.size - 1, 2, 3, 'ur', self.color, self)

        elif self.corner == 'dl':
            self.king = King(mat, 0, self.size - 1, 1, 'dl', self.color, self)

            self.guard1 = Guardian(mat, 0, self.size - 2, 1, 'dl', self.color, self)
            self.guard2 = Guardian(mat, 1, self.size - 1, 2, 'dl', self.color, self)

            self.knight1 = Knight(mat, 0, self.size - 3, 1, 'dl', self.color, self)
            self.knight2 = Knight(mat, 1, self.size - 2, 2, 'dl', self.color, self)
            self.knight3 = Knight(mat, 2, self.size - 1, 3, 'dl', self.color, self)

        elif self.corner == 'dr':
            self.king = King(mat, self.size - 1, self.size - 1, 1, 'dr', self.color, self)

            self.guard1 = Guardian(mat, self.size - 1, self.size - 2, 1, 'dr', self.color, self)
            self.guard2 = Guardian(mat, self.size - 2, self.size - 1, 2, 'dr', self.color, self)

            self.knight1 = Knight(mat, self.size - 1, self.size - 3, 1, 'dr', self.color, self)
            self.knight2 = Knight(mat, self.size - 2, self.size - 2, 2, 'dr', self.color, self)
            self.knight3 = Knight(mat, self.size - 3, self.size - 1, 3, 'dr', self.color, self)


class Knight:

    def __init__(self, mat, init_posx, init_posy, index, corner, color, parent):
        self.color = color
        self.posX = init_posx
        self.posY = init_posy
        self.init_pos = (init_posx, init_posy)
        self.lastpos = ()

        self.corner = corner
        self.index = index
        self.setpos(self.posX, self.posY, mat, self.color)

        self.parent = parent
        self.alive = True

    def MovFw(self, mat):
        self.rempos(self.posX, self.posY, mat)

        if self.corner == 'ul':
            self.posY += 1
        elif self.corner == 'ur':
            self.posY += 1
        elif self.corner == 'dl':
            self.posY -= 1
        elif self.corner == 'dr':
            self.posY -= 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def MovBw(self, mat):
        self.rempos(self.posX, self.posY, mat)

        if self.corner == 'ul':
            self.posY -= 1
        elif self.corner == 'ur':
            self.posY -= 1
        elif self.corner == 'dl':
            self.posY += 1
        elif self.corner == 'dr':
            self.posY += 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def MovLft(self, mat):
        self.rempos(self.posX, self.posY, mat)

        if self.corner == 'ul':
            self.posX += 1
        elif self.corner == 'ur':
            self.posX += 1
        elif self.corner == 'dl':
            self.posX -= 1
        elif self.corner == 'dr':
            self.posX -= 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def MovRgt(self, mat):
        self.rempos(self.posX, self.posY, mat)

        if self.corner == 'ul':
            self.posX -= 1
        elif self.corner == 'ur':
            self.posX -= 1
        elif self.corner == 'dl':
            self.posX += 1
        elif self.corner == 'dr':
            self.posX += 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def rempos(self, xpos, ypos, mat):
        mat.mat[ypos][xpos] = 0
        self.lastpos = (xpos, ypos)

    def setpos(self, xpos, ypos, mat, color):
        self.posX = xpos
        self.posY = ypos
        mat.mat[ypos][xpos] = (1, color, self.index)

    def verify(self, xpos, ypos, mat, color):
        size = mat.getSize()
        res = False
        if 0 <= xpos < size and 0 <= ypos < size:
            if mat.mat[ypos][xpos] == 0:
                res = True
            else:
                res = True
                piece = mat.mat[ypos][xpos][0]
                color = mat.mat[ypos][xpos][1]
                index = mat.mat[ypos][xpos][2]
                self.kill(piece, color, index, mat, xpos, ypos)
        return res

    def kill(self, piece, color, index, mat, xpos, ypos):

        if piece == 1:      # knight
            if color == 'red':
                if index == 1:
                    self.parent.parent.parent.p1.army.knight1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p1.army.knight2.killpiece(mat, xpos, ypos)
                else:
                    self.parent.parent.parent.p1.army.knight3.killpiece(mat, xpos, ypos)
            elif color == 'green':
                if index == 1:
                    self.parent.parent.parent.p2.army.knight1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p2.army.knight2.killpiece(mat, xpos, ypos)
                else:
                    self.parent.parent.parent.p2.army.knight3.killpiece(mat, xpos, ypos)
            elif color == 'blue':
                if index == 1:
                    self.parent.parent.parent.p3.army.knight1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p3.army.knight2.killpiece(mat, xpos, ypos)
                else:
                    self.parent.parent.parent.p3.army.knight3.killpiece(mat, xpos, ypos)
            else:
                if index == 1:
                    self.parent.parent.parent.p4.army.knight1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p4.army.knight2.killpiece(mat, xpos, ypos)
                else:
                    self.parent.parent.parent.p4.army.knight3.killpiece(mat, xpos, ypos)
        elif piece == 2:    # guard
            if color == 'red':
                if index == 1:
                    self.parent.parent.parent.p1.army.guard1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p1.army.guard2.killpiece(mat, xpos, ypos)
            elif color == 'green':
                if index == 1:
                    self.parent.parent.parent.p2.army.guard1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p2.army.guard2.killpiece(mat, xpos, ypos)
            elif color == 'blue':
                if index == 1:
                    self.parent.parent.parent.p3.army.guard1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p3.army.guard2.killpiece(mat, xpos, ypos)
            else:
                if index == 1:
                    self.parent.parent.parent.p4.army.guard1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p4.army.guard2.killpiece(mat, xpos, ypos)
        else:               # king
            if color == 'red':
                self.parent.parent.parent.p1.army.king.killpiece(mat, xpos, ypos)
            elif color == 'green':
                self.parent.parent.parent.p2.army.king.killpiece(mat, xpos, ypos)
            elif color == 'blue':
                self.parent.parent.parent.p3.army.king.killpiece(mat, xpos, ypos)
            else:
                self.parent.parent.parent.p4.army.king.killpiece(mat, xpos, ypos)

    def killpiece(self, mat,  xpos, ypos):
        self.alive = False
        self.posX = xpos
        self.posY = ypos
        mat.mat[ypos][xpos] = 0

    def isAlive(self):
        return self.alive


class Guardian:
    def __init__(self, mat, init_posx, init_posy, index, corner, color, parent):
        self.color = color
        self.posX = init_posx
        self.posY = init_posy
        self.init_pos = (init_posx, init_posy)
        self.lastpos = ()

        self.corner = corner
        self.index = index

        self.parent = parent
        self.alive = True

        self.setpos(self.posX, self.posY, mat, self.color)

    def MovFw(self, mat):
        self.rempos(self.posX, self.posY, mat)
        if self.corner == 'ul':
            self.posX += 1
            self.posY += 1
        elif self.corner == 'ur':
            self.posX -= 1
            self.posY += 1
        elif self.corner == 'dl':
            self.posX += 1
            self.posY -= 1
        elif self.corner == 'dr':
            self.posX -= 1
            self.posY -= 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def MovBw(self, mat):
        self.rempos(self.posX, self.posY, mat)
        if self.corner == 'ul':
            self.posX -= 1
            self.posY -= 1
        elif self.corner == 'ur':
            self.posX += 1
            self.posY -= 1
        elif self.corner == 'dl':
            self.posX -= 1
            self.posY += 1
        elif self.corner == 'dr':
            self.posX += 1
            self.posY += 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def MovLft(self, mat):
        self.rempos(self.posX, self.posY, mat)
        if self.corner == 'ul':
            self.posX += 1
            self.posY -= 1
        elif self.corner == 'ur':
            self.posX += 1
            self.posY += 1
        elif self.corner == 'dl':
            self.posX -= 1
            self.posY -= 1
        elif self.corner == 'dr':
            self.posX += 1
            self.posY -= 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def MovRgt(self, mat):
        self.rempos(self.posX, self.posY, mat)
        if self.corner == 'ul':
            self.posX -= 1
            self.posY += 1
        elif self.corner == 'ur':
            self.posX -= 1
            self.posY -= 1
        elif self.corner == 'dl':
            self.posX += 1
            self.posY += 1
        elif self.corner == 'dr':
            self.posX -= 1
            self.posY += 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def rempos(self, xpos, ypos, mat):
        mat.mat[ypos][xpos] = 0
        self.lastpos = (xpos, ypos)

    def setpos(self, xpos, ypos, mat, color):
        self.posX = xpos
        self.posY = ypos
        mat.mat[ypos][xpos] = (2, color, self.index)

    def verify(self, xpos, ypos, mat, color):
        size = mat.getSize()
        res = False
        if 0 <= xpos < size and 0 <= ypos < size:
            if mat.mat[ypos][xpos] == 0:
                res = True
            else:
                res = True
                piece = mat.mat[ypos][xpos][0]
                color = mat.mat[ypos][xpos][1]
                index = mat.mat[ypos][xpos][2]
                self.kill(piece, color, index, mat, xpos, ypos)
        return res

    def kill(self, piece, color, index, mat, xpos, ypos):

        if piece == 1:      # knight
            if color == 'red':
                if index == 1:
                    self.parent.parent.parent.p1.army.knight1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p1.army.knight2.killpiece(mat, xpos, ypos)
                else:
                    self.parent.parent.parent.p1.army.knight3.killpiece(mat, xpos, ypos)
            elif color == 'green':
                if index == 1:
                    self.parent.parent.parent.p2.army.knight1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p2.army.knight2.killpiece(mat, xpos, ypos)
                else:
                    self.parent.parent.parent.p2.army.knight3.killpiece(mat, xpos, ypos)
            elif color == 'blue':
                if index == 1:
                    self.parent.parent.parent.p3.army.knight1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p3.army.knight2.killpiece(mat, xpos, ypos)
                else:
                    self.parent.parent.parent.p3.army.knight3.killpiece(mat, xpos, ypos)
            else:
                if index == 1:
                    self.parent.parent.parent.p4.army.knight1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p4.army.knight2.killpiece(mat, xpos, ypos)
                else:
                    self.parent.parent.parent.p4.army.knight3.killpiece(mat, xpos, ypos)
        elif piece == 2:    # guard
            if color == 'red':
                if index == 1:
                    self.parent.parent.parent.p1.army.guard1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p1.army.guard2.killpiece(mat, xpos, ypos)
            elif color == 'green':
                if index == 1:
                    self.parent.parent.parent.p2.army.guard1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p2.army.guard2.killpiece(mat, xpos, ypos)
            elif color == 'blue':
                if index == 1:
                    self.parent.parent.parent.p3.army.guard1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p3.army.guard2.killpiece(mat, xpos, ypos)
            else:
                if index == 1:
                    self.parent.parent.parent.p4.army.guard1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p4.army.guard2.killpiece(mat, xpos, ypos)
        else:               # king
            if color == 'red':
                self.parent.parent.parent.p1.army.king.killpiece(mat, xpos, ypos)
            elif color == 'green':
                self.parent.parent.parent.p2.army.king.killpiece(mat, xpos, ypos)
            elif color == 'blue':
                self.parent.parent.parent.p3.army.king.killpiece(mat, xpos, ypos)
            else:
                self.parent.parent.parent.p4.army.king.killpiece(mat, xpos, ypos)

    def killpiece(self, mat,  xpos, ypos):
        self.alive = False
        self.posX = xpos
        self.posY = ypos
        mat.mat[ypos][xpos] = 0

    def isAlive(self):
        return self.alive


class King:
    def __init__(self, mat, init_posx, init_posy, index, corner, color, parent):
        self.color = color
        self.posX = init_posx
        self.posY = init_posy
        self.init_pos = (init_posx, init_posy)
        self.lastpos = ()

        self.corner = corner
        self.index = index

        self.alive = True
        self.parent = parent

        self.setpos(self.posX, self.posY, mat, self.color)

    def MovFw(self, mat):
        self.rempos(self.posX, self.posY, mat)

        if self.corner == 'ul':
            self.posY += 1
        elif self.corner == 'ur':
            self.posY += 1
        elif self.corner == 'dl':
            self.posY -= 1
        elif self.corner == 'dr':
            self.posY -= 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def MovBw(self, mat):
        self.rempos(self.posX, self.posY, mat)

        if self.corner == 'ul':
            self.posY -= 1
        elif self.corner == 'ur':
            self.posY -= 1
        elif self.corner == 'dl':
            self.posY += 1
        elif self.corner == 'dr':
            self.posY += 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def MovLft(self, mat):
        self.rempos(self.posX, self.posY, mat)

        if self.corner == 'ul':
            self.posX += 1
        elif self.corner == 'ur':
            self.posX += 1
        elif self.corner == 'dl':
            self.posX -= 1
        elif self.corner == 'dr':
            self.posX -= 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def MovRgt(self, mat):
        self.rempos(self.posX, self.posY, mat)

        if self.corner == 'ul':
            self.posX -= 1
        elif self.corner == 'ur':
            self.posX -= 1
        elif self.corner == 'dl':
            self.posX += 1
        elif self.corner == 'dr':
            self.posX += 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def MovDUL(self, mat):
        self.rempos(self.posX, self.posY, mat)

        if self.corner == 'ul':
            self.posX += 1
            self.posY += 1
        elif self.corner == 'ur':
            self.posX -= 1
            self.posY += 1
        elif self.corner == 'dl':
            self.posX += 1
            self.posY -= 1
        elif self.corner == 'dr':
            self.posX -= 1
            self.posY -= 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def MovDDR(self, mat):
        self.rempos(self.posX, self.posY, mat)

        if self.corner == 'ul':
            self.posX -= 1
            self.posY -= 1
        elif self.corner == 'ur':
            self.posX += 1
            self.posY -= 1
        elif self.corner == 'dl':
            self.posX -= 1
            self.posY += 1
        elif self.corner == 'dr':
            self.posX += 1
            self.posY += 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def MovDDL(self, mat):
        self.rempos(self.posX, self.posY, mat)

        if self.corner == 'ul':
            self.posX += 1
            self.posY -= 1
        elif self.corner == 'ur':
            self.posX += 1
            self.posY += 1
        elif self.corner == 'dl':
            self.posX -= 1
            self.posY -= 1
        elif self.corner == 'dr':
            self.posX += 1
            self.posY -= 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def MovDUR(self, mat):
        self.rempos(self.posX, self.posY, mat)

        if self.corner == 'ul':
            self.posX -= 1
            self.posY += 1
        elif self.corner == 'ur':
            self.posX -= 1
            self.posY -= 1
        elif self.corner == 'dl':
            self.posX += 1
            self.posY += 1
        elif self.corner == 'dr':
            self.posX -= 1
            self.posY += 1

        if self.verify(self.posX, self.posY, mat, self.color):
            self.setpos(self.posX, self.posY, mat, self.color)
            return True
        else:
            self.setpos(self.lastpos[0], self.lastpos[1], mat, self.color)
            return False

    def rempos(self, xpos, ypos, mat):
        mat.mat[ypos][xpos] = 0
        self.lastpos = (xpos, ypos)

    def setpos(self, xpos, ypos, mat, color):
        self.posX = xpos
        self.posY = ypos
        mat.mat[ypos][xpos] = (3, color, self.index)

    def verify(self, xpos, ypos, mat, color):
        size = mat.getSize()
        res = False
        if 0 <= xpos < size and 0 <= ypos < size:
            if mat.mat[ypos][xpos] == 0:
                res = True
            elif mat.mat[ypos][xpos] == 9:
                res = True
            else:
                res = True
                piece = mat.mat[ypos][xpos][0]
                color = mat.mat[ypos][xpos][1]
                index = mat.mat[ypos][xpos][2]
                self.kill(piece, color, index, mat, xpos, ypos)
        return res

    def kill(self, piece, color, index, mat, xpos, ypos):

        if piece == 1:      # knight
            if color == 'red':
                if index == 1:
                    self.parent.parent.parent.p1.army.knight1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p1.army.knight2.killpiece(mat, xpos, ypos)
                else:
                    self.parent.parent.parent.p1.army.knight3.killpiece(mat, xpos, ypos)
            elif color == 'green':
                if index == 1:
                    self.parent.parent.parent.p2.army.knight1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p2.army.knight2.killpiece(mat, xpos, ypos)
                else:
                    self.parent.parent.parent.p2.army.knight3.killpiece(mat, xpos, ypos)
            elif color == 'blue':
                if index == 1:
                    self.parent.parent.parent.p3.army.knight1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p3.army.knight2.killpiece(mat, xpos, ypos)
                else:
                    self.parent.parent.parent.p3.army.knight3.killpiece(mat, xpos, ypos)
            else:
                if index == 1:
                    self.parent.parent.parent.p4.army.knight1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p4.army.knight2.killpiece(mat, xpos, ypos)
                else:
                    self.parent.parent.parent.p4.army.knight3.killpiece(mat, xpos, ypos)
        elif piece == 2:    # guard
            if color == 'red':
                if index == 1:
                    self.parent.parent.parent.p1.army.guard1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p1.army.guard2.killpiece(mat, xpos, ypos)
            elif color == 'green':
                if index == 1:
                    self.parent.parent.parent.p2.army.guard1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p2.army.guard2.killpiece(mat, xpos, ypos)
            elif color == 'blue':
                if index == 1:
                    self.parent.parent.parent.p3.army.guard1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p3.army.guard2.killpiece(mat, xpos, ypos)
            else:
                if index == 1:
                    self.parent.parent.parent.p4.army.guard1.killpiece(mat, xpos, ypos)
                elif index == 2:
                    self.parent.parent.parent.p4.army.guard2.killpiece(mat, xpos, ypos)
        else:               # king
            if color == 'red':
                self.parent.parent.parent.p1.army.king.killpiece(mat, xpos, ypos)
            elif color == 'green':
                self.parent.parent.parent.p2.army.king.killpiece(mat, xpos, ypos)
            elif color == 'blue':
                self.parent.parent.parent.p3.army.king.killpiece(mat, xpos, ypos)
            else:
                self.parent.parent.parent.p4.army.king.killpiece(mat, xpos, ypos)

    def killpiece(self, mat,  xpos, ypos):
        self.alive = False
        self.posX = xpos
        self.posY = ypos
        mat.mat[ypos][xpos] = 0

    def isAlive(self):
        return self.alive
