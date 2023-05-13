import pygame

pygame.init()
screen_rect = pygame.Rect(0, 0, 512, 768)
screen = pygame.display.set_mode(screen_rect.size)
bg = pygame.image.load("./bg3.jpg")
screen.blit(bg, (0, 0))

hero = pygame.image.load("./hero.png")
hero_rect = hero.get_rect()
hero_rect.centerx = screen_rect.centerx
hero_rect.bottom = screen_rect.bottom - 100
screen.blit(hero, hero_rect)

clock = pygame.time.Clock()
while True:
    clock.tick(480)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero_rect.x -= 10
            if event.key == pygame.K_RIGHT:
                hero_rect.x += 10
            if event.key == pygame.K_UP:
                hero_rect.y -= 10
            if event.key == pygame.K_DOWN:
                hero_rect.y += 10
    # hero_rect.y -= 3
    if hero_rect.bottom < 0:
        hero_rect.top = screen_rect.bottom
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    pygame.display.update()
pygame.quit()
