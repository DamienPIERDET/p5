import random
import pygame
from pygame.math import Vector2
import core

drops = []


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800,800]

def run():
    print("run")
    for d in drops:
        d.tomber(400)
        d.afficher(core)


core.main(setup, run)
