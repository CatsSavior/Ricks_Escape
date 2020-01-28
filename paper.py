import pygame


pygame.init()
display = pygame.display.set_mode((1280, 1024), pygame.FULLSCREEN)
clock = pygame.time.Clock()


def zap():
    running = True
    image = pygame.image.load('src\\env\\1984.png')
    image = pygame.transform.scale(image, (image.get_width()*4, image.get_height()*4))
    display.blit(image, (0, 0))
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                running = False
        pygame.display.update()
