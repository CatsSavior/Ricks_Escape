import pygame
import Rick
import Physics
import Shoot
import create_level
import password
import doors
import paper


width = 1280
height = 1024

lever1_x = 192
lever1_y = height + 320 + 128*4
lever1_pressed = 0
lever2_x = 192
lever2_y = height + 320 + 128*11
lever2_pressed = 0
computer_x = 704
computer_y = height + 320 + 128*4
computer_pressed = 0

pygame.init()
phys = Physics.Physics()
# win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Test_game')

mpbg = pygame.image.load('src\\map.png')
mpbg_width = mpbg.get_width()*4
mpbg_height = mpbg.get_height()*4
mpbg = pygame.transform.scale(mpbg, (mpbg_width, mpbg_height))
mpbg_back = mpbg

bg = pygame.image.load('background.png')
bg_width = bg.get_width()*4
bg_height = bg.get_height()*4
bg = pygame.transform.scale(bg, (bg_width, bg_height))

died = pygame.image.load('src\\died.png')
died = pygame.transform.scale(pygame.image.load('src\\died.png'),
                              (died.get_width()*4, died.get_height()*4))

zapiska = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load('src\\env\\1984.png')))
zap_x = 128*22
zap_y = 128*9 + 32

x = width/2
y = height - 64
speed = 20
bull_speed = 35

x_mpbg = 0
y_mpbg = -128*2
x_bg = 0
y_bg = -800

running = True

gg_sprites = pygame.sprite.Group()
block_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
kill_sprites = pygame.sprite.Group()
door_sprites = pygame.sprite.Group()
bdoor_sprites = pygame.sprite.Group()

blocks = []
create_level.create_lvl(height, block_sprites, kill_sprites, door_sprites, bdoor_sprites)
player = Rick.Rick(100, 300)
gg_sprites.add(player)

clock = pygame.time.Clock()

water_array = [pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load('src\\env\\waterfall_01.png'))),
               pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load('src\\env\\waterfall_02.png')))]

ur_array = [pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load('src\\env\\uranWater_01.png'))),
            pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load('src\\env\\uranWater_02.png'))),
            pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load('src\\env\\uranWater_03.png'))),
            pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load('src\\env\\uranWater_04.png')))]

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
wat_anim = 0
wat_x = 128*26
wat_y = 128*7
ur_anim = 0
ur_y = 128*31
ur_x = 0

pygame.mixer.music.load('src\\music.WAV')
pygame.mixer.music.play(-1)

while running:
    delta = 0
    last_pos = 'Stand'
    pos_y = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    collision_list = phys.collision(player, block_sprites)
    for d in door_sprites:
        print(phys.collision(player, door_sprites))
        print(abs(player.rect.center[0] - d.rect.center[0]))
        print(abs(player.rect.center[1] - d.rect.center[1]))
    if (abs(player.rect.center[0] - d.rect.center[0]) < 160) and (abs(player.rect.center[1] - d.rect.center[1]) < 200):
        collision_list.append('right')

    if ('bottom' not in collision_list) and not isJump:
        fall, delta = phys.gravity(player, block_sprites)
        if fall:
            pos_y = 'Fall'

    if not('left' in collision_list):
        if keys[pygame.K_a] and player.rect.x >= (width//3 - player.image.get_width()/2):
            player.left(speed)
            last_pos = 'Left'
            pos_x = last_pos

        elif keys[pygame.K_a]:
            x_bg += speed*1.1
            x_mpbg += speed
            lever1_x += speed
            lever2_x += speed
            computer_x += speed
            wat_x += speed
            ur_x += speed
            zap_x += speed
            for o in block_sprites:
                o.left(speed)
            for k in kill_sprites:
                k.left(speed)
            for d in door_sprites:
                d.left(speed)
            for b in bdoor_sprites:
                b.left(speed)
            last_pos = 'Left'
            pos_x = last_pos

    if not('right' in collision_list):
        if keys[pygame.K_d] and player.rect.x <= (width - width//3 - player.image.get_width()/2):
            player.right(speed)
            last_pos = 'Right'
            pos_x = last_pos

        elif keys[pygame.K_d]:
            x_bg -= speed*1.1
            x_mpbg -= speed
            lever1_x -= speed
            lever2_x -= speed
            computer_x -= speed
            wat_x -= speed
            ur_x -= speed
            zap_x -= speed
            for o in block_sprites:
                o.right(speed)
            for k in kill_sprites:
                k.right(speed)
            for d in door_sprites:
                d.right(speed)
            for b in bdoor_sprites:
                b.right(speed)
            last_pos = 'Right'
            pos_x = last_pos

    if ('bottom' in collision_list) and not isJump:
        if keys[pygame.K_u]:
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
        lever1_y -= delta
        lever2_y -= delta
        computer_y -= delta
        wat_y -= delta
        ur_y -= delta
        zap_y -= delta
        for o in block_sprites:
            o.down(delta)
        for k in kill_sprites:
            k.down(delta)
        for d in door_sprites:
            d.down(delta)
        for b in bdoor_sprites:
            b.down(delta)

    elif player.up_cord <= 200:

        delta = player.up_cord - 200
        player.up(delta)
        y_bg -= delta
        y_mpbg -= delta
        lever1_y -= delta
        lever2_y -= delta
        computer_y -= delta
        wat_y -= delta
        ur_y -= delta
        zap_y -= delta
        for o in block_sprites:
            o.down(delta)
        for k in kill_sprites:
            k.down(delta)
        for d in door_sprites:
            d.down(delta)
        for b in bdoor_sprites:
            b.down(delta)

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

    if keys[pygame.K_m] and (abs(player.rect.x - computer_x) < 150) and (abs(player.rect.y - computer_y) < 150):
        if computer_pressed == 0:
            password.passw(1984)
            lever1_pressed = 1
            lever2_pressed = 1
    if keys[pygame.K_m] and (abs(player.rect.x - zap_x) < 150) and (abs(player.rect.y - zap_y) < 150):
        paper.zap()
    if keys[pygame.K_m] and (abs(player.rect.x - lever1_x) < 150) and (abs(player.rect.y - lever1_y) < 150):
        if lever1_pressed == 0:
            lever1_pressed = 1
    if keys[pygame.K_m] and (abs(player.rect.x - lever2_x) < 150) and (abs(player.rect.y - lever2_y) < 150):
        if lever2_pressed == 0:
            lever2_pressed = 1

    if lever1_pressed == 1:
        for d in door_sprites:
            x_d, _ = d.rect.center
            y_d = d.rect.top
        door_sprites.empty()
        door_sprites.add(doors.Door(x_d, y_d + 128))
        lever1_pressed = 2

    if lever2_pressed == 1:
        for d in door_sprites:
            x_d, _ = d.rect.center
            y_d = d.rect.top
        door_sprites.empty()
        door_sprites.add(doors.Door(x_d, y_d))
        lever2_pressed = 2

    for b in bullet_sprites:
        hit = pygame.sprite.spritecollide(b, block_sprites, dokill=False)
        if not hit:
            b.move(bull_speed)
        else:
            bullet_sprites.remove(b)

    player.animation(anim_iter, last_pos, pos_y, shoot_count)

    if anim_iter % 3 == 0:
        wat_anim = anim_iter % 2
    if anim_iter % 5 == 0:
        ur_anim = anim_iter % 4

    if mpbg != died:

        win.fill((0, 0, 0))
        win.blit(bg, (x_bg,y_bg))
        door_sprites.update()
        # bdoor_sprites.update()
        win.blit(mpbg, (x_mpbg, y_mpbg))
        door_sprites.draw(win)
        # bdoor_sprites.draw(win)
        win.blit(water_array[wat_anim], (wat_x, wat_y))
        win.blit(ur_array[ur_anim], (ur_x, ur_y))
        bullet_sprites.update()
        gg_sprites.update()
        block_sprites.update()
        bullet_sprites.draw(win)
        gg_sprites.draw(win)
        # block_sprites.draw(win)
        pygame.display.update()

    elif mpbg == died:
        win.blit(died, (0, 0))
        pygame.display.update()

    for k in kill_sprites:
        hit = pygame.sprite.spritecollide(k, gg_sprites, dokill=False)
        if hit:
            mpbg = died

    if keys[pygame.K_ESCAPE]:
        running = False

    if anim_iter < 58:
        anim_iter += 1
    else:
        anim_iter = 0

pygame.quit()
