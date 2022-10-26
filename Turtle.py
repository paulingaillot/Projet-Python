import turtle


class Turtle:
    def __init__(self, tailleCarre):
        self.__tailleCarre = tailleCarre

    # methode dessiner carré afin d'afficher un carré de couleur noir
    def __dessinerCarre(self, debutX, debutY):
        turtle.hideturtle()
        turtle.up()
        turtle.goto(debutX-250, 400-debutY)
        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.down()
        for i in range(0, 4):
            turtle.forward(self.__tailleCarre)
            turtle.right(90)
        turtle.up()
        turtle.end_fill()

    # methode dessiner carré afin d'afficher un carré de couleur bleu
    def __dessinerCarre2(self, debutX, debutY):
        turtle.hideturtle()
        turtle.up()
        turtle.goto(debutX-250, 400-debutY)
        turtle.fillcolor('blue')
        turtle.begin_fill()
        turtle.down()
        for i in range(0, 4):
            turtle.forward(self.__tailleCarre)
            turtle.right(90)
        turtle.up()
        turtle.end_fill()

    # methode dessiner carré afin d'afficher un carré de couleur orange (on aurait pu mettre un parametre couleur et faire le tout en une seule methode)
    def __dessinerCarre3(self, debutX, debutY):
        turtle.hideturtle()
        turtle.up()
        turtle.goto(debutX-250, 400-debutY)
        turtle.fillcolor('orange')
        turtle.begin_fill()
        turtle.down()
        for i in range(0, 4):
            turtle.forward(self.__tailleCarre)
            turtle.right(90)
        turtle.up()
        turtle.end_fill()

    # methode pour le carré de couleur rouge pour la ligne d'arrivé
    def __dessinerarrive(self, debutX, debutY):
        turtle.hideturtle()
        turtle.up()
        turtle.goto(debutX-250, 400-debutY)
        turtle.fillcolor('red')
        turtle.begin_fill()
        turtle.down()
        for i in range(0, 4):
            turtle.forward(self.__tailleCarre)
            turtle.right(90)
        turtle.up()
        turtle.end_fill()

    # methode pour le carré de couleur verte pour la ligne de depart

    def __dessineruser(self, debutX, debutY):
        turtle.hideturtle()
        turtle.up()
        turtle.goto(debutX-250, 400-debutY)
        turtle.fillcolor('green')
        turtle.begin_fill()
        turtle.down()
        for i in range(0, 4):
            turtle.forward(self.__tailleCarre)
            turtle.right(90)
        turtle.up()
        turtle.end_fill()

    # Fonction afin de trouver le chemin pour sortir du labyrinth

    def deplacement(self, maze):

         # On cherche la position de depart
        for x in range(maze.obtenirLargeur()):
            for y in range(maze.obtenirHauteur()):
                if maze.obtenirChiffreCase(x, y) == "1":
                    xp = x
                    yp = y

        # on créé un tableau pour enregistrer l'ordre dnas lequel nous sommes passé sur les cases afin de revenir en arreire si nous sommes coincés
        tab = []

        # on parcourt tant que l'on est pas sur la case d'arrivé
        while maze.obtenirChiffreCase(xp, yp) != "3":
            # on verifie les cases autour si il y a une case sur laquelle nous ne sommes pas passé
            if (xp+1) < maze.obtenirLargeur() and maze.obtenirChiffreCase(xp+1, yp) == "2" or maze.obtenirChiffreCase(xp+1, yp) == "3":
                tab.append([xp, yp])
                maze.placerChiffreCase(xp, yp, "-1")
                xp = xp+1
                self.__dessinerCarre2(xp*self.__tailleCarre, yp*self.__tailleCarre)
            elif (yp+1) < maze.obtenirLargeur() and maze.obtenirChiffreCase(xp, yp+1) == "2" or maze.obtenirChiffreCase(xp, yp+1) == "3":
                tab.append([xp, yp])
                maze.placerChiffreCase(xp, yp, "-1")
                yp = yp+1
                self.__dessinerCarre2(xp*self.__tailleCarre, yp*self.__tailleCarre)
            elif (xp-1) > 0 and maze.obtenirChiffreCase(xp-1, yp) == "2" or maze.obtenirChiffreCase(xp-1, yp) == "3":
                tab.append([xp, yp])
                maze.placerChiffreCase(xp, yp, "-1")
                xp = xp-1
                self.__dessinerCarre2(xp*self.__tailleCarre, yp*self.__tailleCarre)
            elif (yp-1) > 0 and maze.obtenirChiffreCase(xp, yp-1) == "2" or maze.obtenirChiffreCase(xp, yp-1) == "3":
                tab.append([xp, yp]) # on enregistre la case sur laquelle on est au cas ou n,ous soyons sur le mauvais chemin
                maze.placerChiffreCase(xp, yp, "-1") # on met -1 pour dire on est deja passé ici
                yp = yp-1 # on met a jour la posistion du "joueur"
                self.__dessinerCarre2(xp*self.__tailleCarre, yp*self.__tailleCarre) # on dessine le chemin ou les "joueur" est passé
            # si il n'y a aucune solution on reviens en arriere avec notre tableua
            else :
                maze.placerChiffreCase(xp, yp, "-1")
                ta = tab.pop()
                xp = ta[0]
                yp = ta[1]

        # on parcourt le tableau pour en deduire le chemin le plus court

        tab.append([xp, yp])
        for i in tab:
             self.__dessinerCarre3(i[0]*self.__tailleCarre,i[1]*self.__tailleCarre)


    # on affiche le labyrinth
    def dessinerCarte(self, maze):
        for x in range(maze.obtenirHauteur()):
            for y in range(maze.obtenirLargeur()):
                if maze.obtenirChiffreCase(x, y) == "0":
                    self.__dessinerCarre(x*self.__tailleCarre, y*self.__tailleCarre)
                if maze.obtenirChiffreCase(x, y) == "1":
                    self.__dessineruser(x*self.__tailleCarre, y*self.__tailleCarre)
                if maze.obtenirChiffreCase(x, y) == "3":
                    self.__dessinerarrive(x*self.__tailleCarre, y*self.__tailleCarre)

    #def parcourirCarte(self, maze, debutX, debutY):


    def quitterAvecClick(self):
        turtle.exitonclick()

    def saveAsEps(self, pathFile):
        """Save the turtle canvas as Eps."""
        turtle.getscreen().getcanvas().postscript(file=pathFile + '.eps')
