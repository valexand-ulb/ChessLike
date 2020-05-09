

class Army:
    def __init__(self, mat, matsize, corner, color):

        self.corner = corner
        self.color = color
        self.size = matsize

        if self.corner == 'ul':
            self.king = King(mat, 0, 0, 1, 'ul', self.color)

            self.guard1 = Guardian(mat, 1, 0, 1, 'ul', self.color)
            self.guard2 = Guardian(mat, 0, 1, 2, 'ul', self.color)

            self.knight1 = Knight(mat, 2, 0, 1, 'ul', self.color)
            self.knight2 = Knight(mat, 1, 1, 2, 'ul', self.color)
            self.knight3 = Knight(mat, 0, 2, 3, 'ul', self.color)

        elif self.corner == 'ur':
            self.king = King(mat, self.size - 1, 0, 1, 'ur', self.color)

            self.guard1 = Guardian(mat, self.size - 2, 0, 1, 'ur', self.color)
            self.guard2 = Guardian(mat, self.size - 1, 1, 2, 'ur', self.color)

            self.knight1 = Knight(mat, self.size - 3, 0, 1, 'ur', self.color)
            self.knight2 = Knight(mat, self.size - 2, 1, 2, 'ur', self.color)
            self.knight3 = Knight(mat, self.size - 1, 2, 3, 'ur', self.color)

        elif self.corner == 'dl':
            self.king = King(mat, 0, self.size - 1, 1, 'dl', self.color)

            self.guard1 = Guardian(mat, 0, self.size - 2, 1, 'dl', self.color)
            self.guard2 = Guardian(mat, 1, self.size - 1, 2, 'dl', self.color)

            self.knight1 = Knight(mat, 0, self.size - 3, 1, 'dl', self.color)
            self.knight2 = Knight(mat, 1, self.size - 2, 2, 'dl', self.color)
            self.knight3 = Knight(mat, 2, self.size - 1, 3, 'dl', self.color)

        elif self.corner == 'dr':
            self.king = King(mat, self.size - 1, self.size - 1, 1, 'dr', self.color)

            self.guard1 = Guardian(mat, self.size - 1, self.size - 2, 1, 'dr', self.color)
            self.guard2 = Guardian(mat, self.size - 2, self.size - 1, 2, 'dr', self.color)

            self.knight1 = Knight(mat, self.size - 1, self.size - 3, 1, 'dr', self.color)
            self.knight2 = Knight(mat, self.size - 2, self.size - 2, 2, 'dr', self.color)
            self.knight3 = Knight(mat, self.size - 3, self.size - 1, 3, 'dr', self.color)


class Knight(Army):
    def __init__(self, mat, init_posx, init_posy, index, corner, color):
        self.color = color
        self.posX = init_posx
        self.posY = init_posy
        self.init_pos = (init_posx, init_posy)
        self.lastpos = ()

        self.corner = corner
        self.index = index
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

    def kill(self):
        if self.live > 0:
            self.live -= 1
            self.posX = (self.init_pos[0])
            self.posY = (self.init_pos[1])

    def rempos(self, xpos, ypos, mat):
        mat.mat[ypos][xpos] = 0
        self.lastpos = (xpos, ypos)

    def setpos(self, xpos, ypos, mat, color):
        self.posX = xpos
        self.posY = ypos
        mat.mat[ypos][xpos] = (1, color, self.index)

    def verify(self, xpos, ypos, mat, color):
        if mat.mat[ypos][xpos] == 9:
            res = False
        elif type(mat.mat[ypos][xpos]) == tuple and mat.mat[ypos][xpos][1] == color:
            res = False
        elif mat.mat[ypos][xpos] == 0:
            res = True
        else:
            res = True
            piece = mat.mat[ypos][xpos][0]
            color = mat.mat[ypos][xpos][1]
            index = mat.mat[ypos][xpos][2]

            """
            if piece == 1:
                if color == 'red':
                    if index == 1:
                        pass
                    elif index == 2:
                        pass
                    else:
                        pass
                elif color == 'green':
                    if color == 'red':
                        if index == 1:
                            pass
                        elif index == 2:
                            pass
                        else:
                            pass
                elif color == 'blue':
                    if color == 'red':
                        if index == 1:
                            pass
                        elif index == 2:
                            pass
                        else:
                            pass
                else:
                    if color == 'red':
                        if index == 1:
                            pass
                        elif index == 2:
                            pass
                        else:
                            pass
            elif piece == 2:
                pass
            else:
                pass
            """
        return res

    def killpiece(self, mat, xpos, ypos):
        pass



class Guardian(Army):
    def __init__(self, mat, init_posx, init_posy, index, corner, color):
        self.color = color
        self.posX = init_posx
        self.posY = init_posy
        self.init_pos = (init_posx, init_posy)
        self.lastpos = ()

        self.corner = corner
        self.index = index

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

    def kill(self):
        if self.live > 0:
            self.live -= 1
            self.posX = (self.init_pos[0])
            self.posY = (self.init_pos[1])

    def rempos(self, xpos, ypos, mat):
        mat.mat[ypos][xpos] = 0
        self.lastpos = (xpos, ypos)

    def setpos(self, xpos, ypos, mat, color):
        self.posX = xpos
        self.posY = ypos
        mat.mat[ypos][xpos] = (2, color, self.index)

    def verify(self, xpos, ypos, mat, color):
        if mat.mat[ypos][xpos] == 9:
            res = False
        elif type(mat.mat[ypos][xpos]) == tuple and mat.mat[ypos][xpos][1] == color:
            res = False
        else:
            res = True
        return res


class King(Army):
    def __init__(self, mat, init_posx, init_posy, index, corner, color):
        self.color = color
        self.posX = init_posx
        self.posY = init_posy
        self.init_pos = (init_posx, init_posy)
        self.lastpos = ()

        self.corner = corner
        self.index = index

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
        if mat.mat[ypos][xpos] == 0 or mat.mat[ypos][xpos] == 9 or mat.mat[ypos][xpos] == 8 or mat.mat[ypos][xpos][1] != color:
            res = True
        else:
            res = False
        return res

