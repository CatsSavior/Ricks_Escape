import pygame


class Rick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('src\\Rick\\rick.png')
        self.width = self.image.get_width()*4
        self.height = self.image.get_height()*4
        self.image = pygame.transform.scale(self.image, (self.width,
                                                         self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.left_cord = int(self.rect.x)
        self.right_cord = int(self.rect.x + self.width)
        self.up_cord = int(self.rect.y)
        self.down_cord = int(self.rect.y + self.height)

        self.stand_array = [pygame.image.load('src\\Rick\\RickStay_01_01.png'),
                            pygame.image.load('src\\Rick\\RickStay_01_02.png')]

    def right(self, speed):
        self.rect.x += speed
        self.left_cord = int(self.rect.x)
        self.right_cord = int(self.rect.x + self.width)

    def left(self, speed):
        self.rect.x -= speed
        self.left_cord = int(self.rect.x)
        self.right_cord = int(self.rect.x + self.width)

    def up(self, speed):
        self.rect.y -= speed
        self.up_cord = int(self.rect.y)
        self.down_cord = int(self.rect.y + self.height)

    def down(self, speed):
        self.rect.y += speed
        self.up_cord = int(self.rect.y)
        self.down_cord = int(self.rect.y + self.height)

    def animation(self, i, state='Stand'):
        if state == 'Right':
            pass
        if state == 'Left':
            pass
        if state == 'Stand':
            pass
        if state == 'RightBul':
            pass
        if state == 'LeftBul':
            pass
        if state == 'Jump':
            pass
