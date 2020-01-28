import pygame


class Doorb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.break_array = [pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load('src\\env\\doorCracked_01.png'))),
                            pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load('src\\env\\doorCracked_02.png'))),
                            pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load('src\\env\\doorCracked_03.png'))),
                            pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load('src\\env\\doorCracked_04.png')))]
        self.image = self.break_array[0]

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.broken = False
        self.braking = False

    def right(self, speed):
        self.rect.x -= speed

    def left(self, speed):
        self.rect.x += speed

    def up(self, speed):
        self.rect.y += speed

    def down(self, speed):
        self.rect.y -= speed