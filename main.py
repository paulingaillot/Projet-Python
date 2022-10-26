import turtle
from maze import Maze
from Turtle import Turtle
# Pour tester Maze 4 on doit
# baisser la taille de chaque carré a 8
# mettre le tracer a 20-30

# On créé notre fenetre avec turtle
t = turtle
# On defini la taille de notre fenetre
t.setup(1000, 1000)
# On definit le nom de notre fenetre
t.title("Labyrinthe TP3")
#tracer  afin d'accelerer l'affichage sur notre fenetre
t.tracer(10000)
# On créé notre classe Labyrinth
maze = Maze('ressources/data.txt')
# On definit desormais notre classe d'affichage dans la turtle
tt = Turtle(2)
# On dessine le labyrinth
tt.dessinerCarte(maze)
t.tracer(100)
# On appelle la fonction qui cherche a sortir du labyrinth (IA)
tt.deplacement(maze)
# On enregistre le resultats
tt.saveAsEps("labyrinthe")
t.exitonclick()
