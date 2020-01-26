import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, side=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((8, 4))
        self.image.fill((90, 228, 214))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.side = side

    def move(self, speed):
        self.rect.x += speed*self.side
