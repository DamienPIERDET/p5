from AGARIO.creep import Creep
from AGARIO.player import Player
from p5 import core

mon_joueur = Player()
creep = []


def setup():
    print("setup START")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]
    global mon_joueur, creep
    mon_joueur = Player()

    for i in range(0,1000):
        creep.append(Creep())
    print("setup END")


def run():
    for c in creep:
        c.afficher(core)

    print("run")
    mon_joueur.afficher(core)
    if core.getMouseLeftClick() is not None:
        mon_joueur.deplacer(core.getMouseLeftClick())


if __name__ == '__main__':
    core.main(setup, run)
