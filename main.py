import pygame
import Rick
import Physics
import Shoot
import create_level
from time import sleep

width = 1280
height = 1024

pygame.init()
phys = Physics.Physics()
win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption('Test_game')

mpbg = pygame.image.load('src\\map.png')
mpbg_width = mpbg.get_width()*4
mpbg_height = mpbg.get_height()*4
mpbg = pygame.transform.scale(mpbg, (mpbg_width, mpbg_height))

bg = pygame.image.load('background.png')
bg_width = bg.get_width()*5
bg_height = bg.get_height()*5
bg = pygame.transform.scale(bg, (bg_width, bg_height))

x = width/2
y = height - 64
speed = 20
bull_speed = 35

x_mpbg = 0
y_mpbg = -128*2
x_bg = -500
y_bg = -500

running = True

gg_sprites = pygame.sprite.Group()
block_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
kill_sprites = pygame.sprite.Group()

blocks = []
create_level.create_lvl(height, block_sprites, kill_sprites)
player = Rick.Rick(100, 300)
gg_sprites.add(player)

clock = pygame.time.Clock()

isJump = False
isShoot = False
jumpCount = 14
fall_time = 0
shoot_count = 0
last_pos = 'Stand'
anim_iter = 0
fall = False
pos_x = 'Left'
pos_y = None

while running:
    clock.tick(60)
    delta = 0
    last_pos = 'Stand'
    pos_y = None

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

    if ('bottom' not in collision_list) and not isJump:
        fall, delta = phys.gravity(player, block_sprites)
        if fall:
            pos_y = 'Fall'

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
            pos_x = last_pos
            # player.animation(anim_iter, last_pos)
        elif keys[pygame.K_a]:
            x_bg += speed*1.1
            x_mpbg += speed
            for o in block_sprites:
                o.left(speed)
            for k in kill_sprites:
                k.left(delta)
            last_pos = 'Left'
            pos_x = last_pos
            # player.animation(anim_iter, last_pos)

    if not('right' in collision_list):
        if keys[pygame.K_d] and player.rect.x <= (width - width//3 - player.image.get_width()/2):
            player.right(speed)
            last_pos = 'Right'
            pos_x = last_pos

        elif keys[pygame.K_d]:
            x_bg -= speed*1.1
            x_mpbg -= speed
            for o in block_sprites:
                o.right(speed)
            for k in kill_sprites:
                k.right(delta)
            last_pos = 'Right'
            pos_x = last_pos

    if ('bottom' in collision_list) and not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    elif isJump:
        if (jumpCount >= 0) and not('top' in collision_list):
            player.up(jumpCount*abs(jumpCount)*0.4)
            jumpCount -= 1
            pos_y = 'JumpUp'
        elif (jumpCount < 0) or ('top' in collision_list):
            jumpCount = 14
            isJump = False

    if player.down_cord >= 700:
        delta = player.down_cord - 700
        player.up(delta)
        y_bg -= delta
        y_mpbg -= delta
        for o in block_sprites:
            o.down(delta)
        for k in kill_sprites:
            k.down(delta)

    elif player.up_cord <= 200:

        delta = player.up_cord - 200
        player.up(delta)
        y_bg -= delta
        y_mpbg -= delta
        for o in block_sprites:
            o.down(delta)
        for k in kill_sprites:
            k.down(delta)

    if keys[pygame.K_n] and (not isShoot):
        isShoot = True
        shoot_side = pos_x

    if isShoot:
        if shoot_count == 0:
            if shoot_side == 'Right':
                last_pos = 'RightShoot'
            elif shoot_side == 'Left':
                last_pos = 'LeftShoot'
            shoot_count += 1

        elif shoot_count == 18:
            if shoot_side == 'Right':
                last_pos = 'RightShoot'
                bullet_sprites.add(Shoot.Bullet(player.right_cord, player.up_cord+27*4, 1))
            elif shoot_side == 'Left':
                last_pos = 'LeftShoot'
                bullet_sprites.add(Shoot.Bullet(player.left_cord, player.up_cord+27*4, -1))
            shoot_count += 1

        elif shoot_count < 25:
            if shoot_side == 'Right':
                last_pos = 'RightShoot'
            elif shoot_side == 'Left':
                last_pos = 'LeftShoot'
            shoot_count += 1

        elif shoot_count >= 25:
            isShoot = False
            shoot_count = 0

    if keys[pygame.K_s] and ('bottom' not in collision_list):
        player.down(speed)

    if (keys[pygame.K_w] and not(player.rect.center[1] <= (height//6 - player.image.get_width()/2))) and\
            ('top' not in collision_list):
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

    for b in bullet_sprites:
        hit = pygame.sprite.spritecollide(b, block_sprites, dokill=False)
        if not hit:
            b.move(bull_speed)
        else:
            bullet_sprites.remove(b)

    player.animation(anim_iter, last_pos, pos_y, shoot_count)

    for k in kill_sprites:
        hit = pygame.sprite.spritecollide(k, gg_sprites, dokill=False)
        if hit:
            player.die()
            running = False

    win.fill((100,100,100))
    win.blit(bg, (x_bg,y_bg))
    win.blit(mpbg, (x_mpbg, y_mpbg))
    bullet_sprites.update()
    gg_sprites.update()
    block_sprites.update()
    bullet_sprites.draw(win)
    gg_sprites.draw(win)
    block_sprites.draw(win)
    pygame.display.update()

    if anim_iter < 58:
        anim_iter += 1
    else:
        anim_iter = 0

pygame.quit()
