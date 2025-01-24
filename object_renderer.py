import pygame as pg
from game_settings import * 


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture("txture_packs/sky.png",(WIDTH, HALF_HEIGHT))
        self.sky_offset = 0

    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_floor()

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.0 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))


    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    def draw_floor(self):
        floor_color = (30, 30, 30)
        pg.draw.rect(self.screen, floor_color, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):
        return{
            1: self.get_texture('txture_packs/4.png'),
            2: self.get_texture('txture_packs/2.png'),
            3: self.get_texture('txture_packs/3.png'),
            4: self.get_texture('txture_packs/1.png'),
            5: self.get_texture('txture_packs/5.png'),
        }