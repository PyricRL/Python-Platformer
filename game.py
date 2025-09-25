import sys

import pygame

from scripts.entities import PhysicsEntity
from scripts.utils import load_image
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds

class Game:                 # Use classes because its oop and just better
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Hi")
        self.screen = pygame.display.set_mode((800, 600))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'decor': load_image('tiles/decor'),
            'grass': load_image('tiles/grass'),
            'large_decor': load_image('tiles/large_decor'),
            'stone': load_image('tiles/stone'),
            'player': load_image('entities/player.png'),
            'background': load_image('background.png'),
            'clouds': load_image('clouds'),
        }
        
        self.clouds = Clouds(self.assets['clouds'], count=16)

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size=16)

        self.scroll = [0, 0]    # Camera pos, will need to also add offset to all rendered items
        # Basically we subtract scroll from the position of all rendered items so that they move opposite of the way we want the camera to move
        # so it gets a camera moving feel but is actually everything else moving. Another reason to use positions instead of velocity for the player
        # in certain cases
        # line 37/41 in tilemap.py and line 54 in entities.py
    
    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0, 0))

            # find where camera is and move it to where it should be
            # currently keeps player in center
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))  # helps with pixel glitches due to floats

            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll)

            self.tilemap.render(self.display, offset=render_scroll)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_SPACE:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            pygame.time.Clock().tick(60)

Game().run()