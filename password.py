import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((900,1200),0,32)
pygame.display.set_caption("Rick&Morty")


def passw(true_pass):
    FPS = 10
    clock = pygame.time.Clock()
    first, second, third, fourth = "0", "0", "0", "0"
    all_num = [first, second, third, fourth]
    active = 0
    active_x = 190
    active_y = 190

    (x,y,fontSize) = (200,200,100)
    myFont = pygame.font.SysFont("None", fontSize)
    fontColor = (255,255,0)
    bgColor = (255,255,255)



    mainLoop = True
    while mainLoop:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                mainLoop = False

        numb1 = myFont.render(all_num[0], 0, (fontColor))
        numb2 = myFont.render(all_num[1], 0, (fontColor))
        numb3 = myFont.render(all_num[2], 0, (fontColor))
        numb4 = myFont.render(all_num[3], 0, (fontColor))


        screen.fill(bgColor)
        pygame.draw.rect(screen, (200, 200, 200), (active_x, active_y, 65, 75))
        screen.blit(numb1,(x,y))
        screen.blit(numb2,(x+70,y))
        screen.blit(numb3,(x+140,y))
        screen.blit(numb4,(x+210,y))



    # for i in pygame.event.get():
        keys = pygame.key.get_pressed()
    # if keys[pygame.KEYDOWN]:
        if keys[pygame.K_LEFT]:
            if active != 0:
                active -= 1
                active_x -= 70
        if keys[pygame.K_RIGHT]:
            if active != 3:
                active += 1
                active_x += 70
        if keys[pygame.K_UP]:
            if all_num[active] != '9':
                all_num[active] = str(int(all_num[active])+1)
            else:
                all_num[active] = '0'
        if keys[pygame.K_DOWN]:
            if all_num[active] != '0':
                all_num[active] = str(int(all_num[active])-1)
            else:
                all_num[active] = '9'
        if int(all_num[0]+all_num[1]+all_num[2]+all_num[3]) == true_pass:
            print('win')
            mainLoop = False
        pygame.display.update()


if __name__ == '__main__':
    passw(1984)
