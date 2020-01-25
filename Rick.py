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

        self.stand_array = [pygame.transform.scale(pygame.image.load('src\\Rick\\RickStay_01_01.png'),
                                                   (self.width, self.height)),
                            pygame.transform.scale(pygame.image.load('src\\Rick\\RickStay_01_02.png'),
                                                   (self.width, self.height))]
        self.right_array = [pygame.transform.scale(pygame.image.load('src\\Rick\\RickRun_03_01.png'),
                                                   (self.width, self.height)),
                            pygame.transform.scale(pygame.image.load('src\\Rick\\RickRun_03_02.png'),
                                                   (self.width, self.height)),
                            pygame.transform.scale(pygame.image.load('src\\Rick\\RickRun_03_03.png'),
                                                   (self.width, self.height)),
                            pygame.transform.scale(pygame.image.load('src\\Rick\\RickRun_03_04.png'),
                                                   (self.width, self.height))]

        self.jump_up_array = []

        self.fall = []

        self.shoot_array = [pygame.transform.scale(pygame.image.load('src\\Rick\\RickShoot_02_01.png'),
                                                   (self.width, self.height)),
                            pygame.transform.scale(pygame.image.load('src\\Rick\\RickShoot_02_02.png'),
                                                   (self.width, self.height)),
                            pygame.transform.scale(pygame.image.load('src\\Rick\\RickShoot_02_03.png'),
                                                   (self.width, self.height)),
                            pygame.transform.scale(pygame.image.load('src\\Rick\\RickShoot_02_02.png'),
                                                   (self.width, self.height)),
                            pygame.transform.scale(pygame.image.load('src\\Rick\\RickShoot_02_01.png'),
                                                   (self.width, self.height))]

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
            if i % 5 == 0:
                self.image = self.right_array[i % 4]
        if state == 'Left':
            if i % 5 == 0:
                self.image = pygame.transform.flip(self.right_array[i % 4], True, False)
        if state == 'Stand':
            if i % 5 == 0:
                self.image = self.stand_array[i % 2]
        if state == 'RightShoot':
            pass
        if state == 'LeftShoot':
            pass
        if state == 'JumpUp':
            pass
        if state == 'Fall':
            pass

