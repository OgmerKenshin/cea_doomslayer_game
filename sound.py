import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = "animated_sprites/sounds"
        self.shotgun = pg.mixer.Sound(self.path + '/gunshot.wav')
        self.npc_pain = pg.mixer.Sound(self.path + '/npc_pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + '/npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + '/npc_attack.wav')
        self.player_pain = pg.mixer.Sound(self.path + '/player_pain.wav')
        
