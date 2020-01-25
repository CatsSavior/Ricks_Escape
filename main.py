import pygame
import Rick
# import Block
import Physics
import create_level

width = 1280
height = 1024

pygame.init()
phys = Physics.Physics()
win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption('Test_game')

mpbg = pygame.image.load('mapAll.png')
mpbg_width = mpbg.get_width()*4
mpbg_height = mpbg.get_height()*4
mpbg = pygame.transform.scale(mpbg, (mpbg_width, mpbg_height))

bg = pygame.image.load('background.png')
bg_width = bg.get_width()*5
bg_height = bg.get_height()*5
bg = pygame.transform.scale(bg, (bg_width, bg_height))

x = width/2
y = height - 64
speed = 15

x_mpbg = 0
y_mpbg = 0
x_bg = -500
y_bg = -500

running = True

gg_sprites = pygame.sprite.Group()
block_sprites = pygame.sprite.Group()

blocks = []
create_level.create_lvl(height, block_sprites)
# for i in range(8):
#     block_sprites.add(Block.Block(64+128*i, height-64-16))
# block_sprites.add(Block.Block(64+128*6, height-64-128))
# block_sprites.add(Block.Block(64+128*6, height-64-128*2))
# block_sprites.add(Block.Block(64+128*6, height-64-128*3))
# pygame.Rect.unionall(block_sprites.sprites())
player = Rick.Rick(100, 300)
gg_sprites.add(player)

clock = pygame.time.Clock()

isJump = False
jumpCount = 14

fall_time = 0

last_pos = 'Stand'

anim_iter = 0

fall = False

while running:
    clock.tick(60)
    delta = 0
    last_pos = 'Stand'

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
    # collision_list = []
    # print(collision_list)

    # if ('bottom' not in collision_list) and not isJump:
    #     fall, delta = phys.gravity(player, block_sprites)
    #     if fall:
    #         last_pos = 'Fall'

    #     print(delta_y)

    # if keys[pygame.K_LSHIFT] and speed == 10:
    #     speed = speed * 2
    # elif not (keys[pygame.K_LSHIFT] or speed == 10):
    #     speed = 10

    # if len(hits) < 3 or last_pos != 'right':
    if not('left' in collision_list):
        if keys[pygame.K_a] and player.rect.x >= (width//3 - player.image.get_width()/2):
            player.left(speed)
            last_pos = 'Left'
            # player.animation(anim_iter, last_pos)
        elif keys[pygame.K_a]:
            x_bg += speed*1.1
            x_mpbg += speed
            for o in block_sprites:
                o.left(speed)
            last_pos = 'Left'
            # player.animation(anim_iter, last_pos)

    if not('right' in collision_list):
        if keys[pygame.K_d] and player.rect.x <= (width - width//3 - player.image.get_width()/2):
            player.right(speed)
            last_pos = 'Right'

        elif keys[pygame.K_d]:
            x_bg -= speed*1.1
            x_mpbg -= speed
            for o in block_sprites:
                o.right(speed)
            last_pos = 'Right'

    if ('bottom' in collision_list) and not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    elif isJump and not('up' in collision_list):
        if jumpCount >= 0:
            player.up(jumpCount*abs(jumpCount)*0.4)
            jumpCount -= 1
        else:
            jumpCount = 14
            isJump = False

    if player.down_cord >= 700:
        delta = player.down_cord - 700
        player.up(delta)
        y_bg -= delta
        # y_mpbg += delta
        for o in block_sprites:
            o.down(delta)

    elif player.up_cord <= 200:

        delta = player.up_cord - 200
        player.up(delta)
        y_bg -= delta
        # y_mpbg += delta
        for o in block_sprites:
            o.down(delta)

    if keys[pygame.K_s] and ('bottom' not in collision_list):
        player.down(speed)

    if keys[pygame.K_w] and not(player.rect.center[1] <= (height//6 - player.image.get_width()/2)):
        player.up(speed)



    # print(player.rect.center)
    # if player.rect.center[1] >= (height - height//6 - player.image.get_width()/2):
    #     delta_y = abs((height - height//6 - player.image.get_width()/2) - player.rect.center[1])
    #     y_bg -= delta_y*1.1
    #     y_mpbg -= delta_y
    #     for o in block_sprites:
    #         o.down(delta_y)
    # if player.rect.center[1] <= (height//6 - player.image.get_width()/2):
    #     delta_y = abs((height//6 - player.image.get_width()/2) - player.rect.center[1])
    #     y_bg += delta_y*1.1
    #     y_mpbg += delta_y
    #     for o in block_sprites:
    #         o.up(delta_y)
    player.animation(anim_iter, last_pos)
    win.fill((100,100,100))
    win.blit(bg, (x_bg,y_bg))
    # win.blit(mpbg, (x_mpbg,wwwwwwy_mpbg))
    gg_sprites.update()
    block_sprites.update()
    gg_sprites.draw(win)
    block_sprites.draw(win)
    # pygame.draw.circle(win, (255, 0, 0), (player.left_cord, player.up_cord), 10)
    # pygame.draw.circle(win, (255, 0, 0), (player.right_cord, player.down_cord), 10)
    pygame.display.update()

    if anim_iter < 58:
        anim_iter += 1
    else:
        anim_iter = 0

pygame.quit()
