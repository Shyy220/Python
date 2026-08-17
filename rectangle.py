import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("My First Rectangle")
running = True

while running:
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(0,0,255), (100,50,200,150))

pygame.display.update()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
pygame.quit()



