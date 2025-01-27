from sprite_object import *

class weapon(AnimatedSprite):
    def __init__(self, game, path= "animated_sprites/shotgun/1pac.png", scale=0.4, animation_time=90):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)