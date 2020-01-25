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
                if (o.rect.top in list(range(player.up_cord, player.down_cord - 1))) and (
                        o.rect.left <= player.right_cord):
                    self.collision_list.append('right')
                if (o.rect.center[1] in list(range(player.up_cord, player.down_cord - 1))) and \
                        (((o.rect.right - player.left_cord) < 15) and (0 < (o.rect.right - player.left_cord))):
                    self.collision_list.append('left')
            if (player.down_cord in list(range(o.rect.top, o.rect.top + 2))) \
                    and ((player.left_cord in range(o.rect.left - 1, o.rect.right - 1) or
                          (player.right_cord in range(o.rect.left - 1, o.rect.right - 1)))):
                self.collision_list.append('bottom')
            if (player.up_cord in list(range(o.rect.bottom - 15, o.rect.bottom - 20))) \
                    and ((player.left_cord in range(o.rect.left - 1, o.rect.right - 1) or
                          (player.right_cord in range(o.rect.left - 1, o.rect.right - 1)))):
                self.collision_list.append('top')
        return self.collision_list

    def gravity(self, player, blocks_obj):

        max_height = 99999
        min_height = 0
        self.min_dist = 9999
        self.item = player
        for self.o in blocks_obj:

            if ((self.o.rect.right >= self.item.left_cord) and (self.item.right_cord >= self.o.rect.right)) or \
                    ((self.o.rect.left >= self.item.left_cord) and (self.item.right_cord >= self.o.rect.left)):
                print(self.item.down_cord, self.o.rect.top)
                if (self.o.rect.top - self.item.down_cord) > 0:
                    self.min_dist = min(self.min_dist, self.o.rect.top - self.item.down_cord)
                # max_height = min(max_height, o.rect.top)
                # min_height = max(min_height, o.rect.top)

        # if (0 < (max_height - player.down_cord)) and ((max_height - player.down_cord) < 20):
        #     self.item.down(max_height - player.down_cord)
        #     self.delta = max_height - player.down_cord
        #
        # elif (0 < (min_height - player.down_cord)) and ((min_height - player.down_cord) < 20):
        #     self.item.down(min_height - player.down_cord)
        #     self.delta = min_height - player.down_cord

        if self.min_dist <= 20:
            self.item.down(self.min_dist)
            self.delta = self.min_dist

        else:
            self.item.down(20)
            self.delta = 20

        # elif max_height >= player.down_cord + 20:
        #     self.item.down(20)
        #     self.delta = 20

        return True, self.delta
