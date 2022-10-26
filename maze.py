class Maze:

    def __init__(self, fichier):
        fileRead = open(fichier, 'r')
        lines = fileRead.readlines()
        fileRead.close()
        self.__tab = []
        for line in lines:
            self.__tab.append([char for char in line.rstrip("\n")])
        self.__largeur = len(self.__tab[0])
        self.__hauteur = len(self.__tab)

    def obtenirChiffreCase(self, x, y):
        try:
            return self.__tab[y][x]
        except IndexError:
            return "0"

    def obtenirLargeur(self):
        return self.__largeur

    def obtenirHauteur(self):
        return self.__hauteur

    def placerChiffreCase(self, x, y, valeur):
        self.__tab[y][x] = valeur
