import pygame
import Rick
import Block
import Physics

width = 1280
height = 1024

pygame.init()
phys = Physics.Physics()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Test_game')

bg = pygame.image.load('bg.jpg')

x = width/2
y = height - 64
speed = 15

x_bg = -500
y_bg = -500

running = True

gg_sprites = pygame.sprite.Group()
block_sprites = pygame.sprite.Group()

blocks = []
for i in range(6):
    block_sprites.add(Block.Block(64+128*i, height-64))
block_sprites.add(Block.Block(64+128*6, height-64-128))
player = Rick.Rick(width/2, height-260)
gg_sprites.add(player)

clock = pygame.time.Clock()

isJump = False
jumpCount = 20

fall_time = 0

last_pos = 'None'


def collision(player, blocks_obj):
    collision_list = []
    for o in blocks_obj:
        if (o.rect.bottom in range(player.up_cord, player.down_cord)) and (o.rect.left <= player.right_cord):
            collision_list.append('right')
        if (o.rect.bottom in range(player.up_cord, player.down_cord)) and (o.rect.right >= player.left_cord):
            collision_list.append('left')
        if (o.rect.top <= player.down_cord) and ((player.left_cord in range(o.rect.left, o.rect.right) or
                                                     (player.right_cord in range(o.rect.left, o.rect.right)))):
            collision_list.append('bottom')
    return collision_list


while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # for i in range(1*fall_time//4):
    #     hits = pygame.sprite.spritecollide(player, block_sprites, dokill=False)
    #     if not hits:
    #         player.down(1)
    #         fall_time += 1
    #     else:
    #         print(hits)
    #         fall_time = 4

    keys = pygame.key.get_pressed()
    collision_list = phys.collision(player, block_sprites)
    print(collision_list)

    if 'bottom' not in collision_list:
        phys.gravity(player)

    # if keys[pygame.K_LSHIFT] and speed == 10:
    #     speed = speed * 2
    # elif not (keys[pygame.K_LSHIFT] or speed == 10):
    #     speed = 10

    # if len(hits) < 3 or last_pos != 'right':
    if keys[pygame.K_LEFT] and player.rect.x >= (width//6 - player.image.get_width()/2):
        player.left(speed)
        # last_pos = 'right'
    elif keys[pygame.K_LEFT]:
        x_bg += speed
            # last_pos = 'right'
    print('bottom' not in collision_list)
    if not('right' in collision_list):
        if keys[pygame.K_RIGHT] and player.rect.x <= (width - width//6 - player.image.get_width()/2):
            player.right(speed)
            # last_pos = 'left'
        elif keys[pygame.K_RIGHT]:
            x_bg -= speed
        # last_pos = 'left'
    if not isJump:
        # if keys[pygame.K_UP] and player.rect.y >= 200:
        #     player.up(speed)
        # elif keys[pygame.K_UP]:
        #     y_bg += speed
        # if keys[pygame.K_DOWN] and player.rect.y <= 700:
        #     player.down(speed)
        # elif keys[pygame.K_DOWN]:
        #     y_bg -= speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= 0:
            player.up(jumpCount*abs(jumpCount)*0.5)
            jumpCount -= 1
        else:
            jumpCount = 13
            isJump = False

    win.blit(bg, (x_bg,y_bg))
    gg_sprites.update()
    block_sprites.update()
    gg_sprites.draw(win)
    block_sprites.draw(win)
    pygame.draw.circle(win, (255, 0, 0), (player.left_cord, player.up_cord), 10)
    pygame.draw.circle(win, (255, 0, 0), (player.right_cord, player.down_cord), 10)
    pygame.display.update()

pygame.quit()
