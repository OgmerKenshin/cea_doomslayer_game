from sprite_object import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = "static_sprites"
        self.anim_sprite_path = "animated_sprites"
        add_sprite = self.add_sprite

        

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)