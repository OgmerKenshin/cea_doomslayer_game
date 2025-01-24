import pygame as pg
from game_settings import *

class SpriteObjects:
    def __init__(self, game, path="static_sprites/chair.png", pos=(10.5, 3.5)):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIGTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2