import pygame


class Physics:
    def __init__(self):
        self.collision_list = []
        self.item = None
        self.delta = 0
        self.min_dist = 99999

    def collision(self, player, blocks_obj):
        self.collision_list = []

        for o in blocks_obj:
            if (o.rect.left in list(range(player.rect.x, player.rect.x + player.width))) \
                    or (o.rect.right in list(range(player.rect.x, player.rect.x + player.width))):
                if (o.rect.center[1] in list(range(player.up_cord - 8, player.down_cord - 1))) and \
                        (((player.right_cord + 4 - o.rect.left) < 29) and (9 <= (player.right_cord + 4 - o.rect.left))):
                    self.collision_list.append('right')
                if (o.rect.center[1] in list(range(player.up_cord - 8, player.down_cord - 1))) and \
                        (((o.rect.right - player.left_cord) < 29) and (9 <= (o.rect.right - player.left_cord))):
                    self.collision_list.append('left')
            if (player.down_cord in list(range(o.rect.top, o.rect.top + 2))) \
                    and ((player.left_cord in range(o.rect.left - 1, o.rect.right + 1) or
                          (player.right_cord in range(o.rect.left - 1, o.rect.right + 1)))):
                self.collision_list.append('bottom')
            if (player.up_cord + 13*4 in list(range(o.rect.bottom, o.rect.bottom + 53))) \
                    and ((player.left_cord in range(o.rect.left - 1, o.rect.right + 1) or
                          (player.right_cord in range(o.rect.left - 1, o.rect.right + 1)))):
                self.collision_list.append('top')
        return self.collision_list

    def gravity(self, player, blocks_obj):

        self.min_dist = 9999
        self.item = player
        for self.o in blocks_obj:

            if ((self.o.rect.right >= self.item.left_cord) and (self.item.right_cord >= self.o.rect.right)) or \
                    ((self.o.rect.left >= self.item.left_cord) and (self.item.right_cord >= self.o.rect.left)):
                if (self.o.rect.top - self.item.down_cord) > 0:
                    self.min_dist = min(self.min_dist, self.o.rect.top - self.item.down_cord)

        if self.min_dist <= 30:
            self.item.down(self.min_dist)
            self.delta = self.min_dist

        else:
            self.item.down(30)
            self.delta = 30

        return True, self.delta
