import pygame


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32*4, 4*128))
        self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def right(self, speed):
        self.rect.x -= speed

    def left(self, speed):
        self.rect.x += speed

    def up(self, speed):
        self.rect.y += speed

    def down(self, speed):
        self.rect.y -= speed
