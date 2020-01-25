import pygame


class Physics:
    def __init__(self):
        self.collision_list = []
        self.item = None

    def collision(self, player, blocks_obj):
        self.collision_list = []

        for o in blocks_obj:
            if (o.rect.top in list(range(player.up_cord, player.down_cord-1))) and (o.rect.left <= player.right_cord):
                self.collision_list.append('right')
            # print(o.rect.top, list(range(player.up_cord, player.down_cord)))
            # print(o.rect.left, player.right_cord)
            if (o.rect.top in range(player.up_cord, player.down_cord)) and (o.rect.right >= player.left_cord):
                self.collision_list.append('left')
            if (player.down_cord in list(range(o.rect.top-3, o.rect.top+10))) \
                    and ((player.left_cord in range(o.rect.left-1, o.rect.right-1) or
                          (player.right_cord in range(o.rect.left-1, o.rect.right-1)))):
                self.collision_list.append('bottom')
        return self.collision_list

    def gravity(self,item):
        self.item = item
        self.item.down(10)
