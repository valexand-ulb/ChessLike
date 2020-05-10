from os import name, system

class Mat:
    def __init__(self, n, v=True):
        if n >= 7 and n%2 == 1:
            self.size = n
        elif n >=7 and n%2 == 0:
            self.size = n+1
        elif n < 7 and n%2 == 1:
            self.size = n+6
        elif n < 7 and n%2 == 0:
            self.size = n+7
        else:
            raise ValueError
        self.veg = v
        self.mat = [[0 for i in range(self.size)] for j in range(self.size)]
        self.mat[self.size//2][self.size//2] = 9

    def getSize(self):
        return self.size

    def printM(self):
        s = ''
        # l = [' ', '⚔', '🛡', '👑', '🌲', 0, 0, 0, 0, '⛫']
        l = ['   ', ' ⚔ ', ' G ', ' K ', ' 🌲 ', 0, 0, 0, 0, ' ⛫ ']
        for elem in self.mat:
            for p in elem:
                if type(p) == tuple:
                    s += ' ' + str(l[p[0]]) + ' '
                else:
                    s += ' ' + str(l[p]) + ' '
            s += '\n\n\n'
        # """
        if name == 'posix':
            system('clear')
        elif name == 'nt':
            system('cls')
        # """
        print(s)