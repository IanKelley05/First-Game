import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

font = pygame.font.Font(None, 74)  # Use default font, size 74
text_surface = font.render("Minali", True, "red")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("pink")
    
    text_rect = text_surface.get_rect(center=(player_pos.x, player_pos.y))
    screen.blit(text_surface, text_rect)
    
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()