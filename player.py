from game_settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED
        speed_sin = speed = sin_a
        speed_cos = speed = cos_a
        

    def update(self):
        self.movement()

    #to know the player's coords 
    @property
    def pos(self):
        return self.x, self.y

    # to know what the coordinates of the tile the player is on
    @property
    def map_pos(self):
        return int(self.x), int(self.y)