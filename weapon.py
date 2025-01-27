from sprite_object import *

class weapon(AnimatedSprite):
    def __init__(self, game, path= "animated_sprites/shotgun/1pac.png", scale=0.4, animation_time=90):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_with() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())

    def draw(self):
        self.game.screen.blit(self..images[0], self.weapon_pos)
