import pygame

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        """ El siguiente codigo fue reemplazado para hacerlo mas legible """
        #if event.type == pygame.QUIT\
        #or event.type == pygame.MOUSEBUTTONUP\
        #or event.type == pygame.KEYUP: 
        if event.type in [pygame.QUIT, pygame.MOUSEBUTTONUP, pygame.KEYUP]:
            run = False