import sys
from random import shuffle, randrange


def make_maze(w=20, h=20):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["02"] * w + ['0'] for _ in range(h)] + [[]]
    hor = [["00"] * w + ['0'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "02"
            if yy == y: ver[y][max(x, xx)] = "22"
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s


if __name__ == '__main__':
    sys.setrecursionlimit(2000000000)

    fichier = open("ressources/data.txt", "w")
    fichier.write(make_maze())
    fichier.close()
