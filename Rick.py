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
        self.left_cord = int(self.rect.x) + 96
        self.right_cord = int(self.rect.x + self.width) + 96
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

        self.jump_up_array = [pygame.transform.scale(pygame.image.load('src\\Rick\\RickJump_04_01.png'),
                                                     (self.width, self.height))]

        self.fall = [pygame.transform.scale(pygame.image.load('src\\Rick\\RickJump_04_02.png'),
                                                     (self.width, self.height))]

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

        self.died_sprite = pygame.transform.scale(pygame.image.load('src\\Rick\\rickDead_05.png'),
                                                  (self.width, self.height))

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

    def animation(self, i, state_x='Stand', state_y=None, shoot_count=0):
        if state_y == 'JumpUp':
            self.image = self.jump_up_array[0]
            return 0
        if state_y == 'Fall':
            self.image = self.fall[0]
            return 0
        if state_x == 'Right':
            if i % 5 == 0:
                self.image = self.right_array[i % 4]
        if state_x == 'Left':
            if i % 5 == 0:
                self.image = pygame.transform.flip(self.right_array[i % 4], True, False)
        if state_x == 'Stand':
            if i % 5 == 0:
                self.image = self.stand_array[i % 2]
        if state_x == 'RightShoot':
            if shoot_count % 6 == 0:
                self.image = self.shoot_array[i % 5]
        if state_x == 'LeftShoot':
            if shoot_count % 6 == 0:
                self.image = pygame.transform.flip(self.shoot_array[shoot_count % 5], True, False)

    def die(self):
        self.image = self.died_sprite
