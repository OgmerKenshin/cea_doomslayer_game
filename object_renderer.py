import pygame as pg
from game_settings import * 


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen