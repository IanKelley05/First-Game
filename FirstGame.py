import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0
player_1_pos = pygame.Vector2(screen.get_width() / 2 - 100, screen.get_height() / 2)
player_2_pos = pygame.Vector2(screen.get_width() / 2 + 100, screen.get_height() / 2)

font = pygame.font.Font(None, 74)  # Use default font, size 74
text_1_surface = font.render("Minali", True, "red")
text_2_surface = font.render("Ian", True, "blue")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("pink")
    
    pygame.draw.circle(screen, "red", player_1_pos, 30)
    pygame.draw.circle(screen, "blue", player_2_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_2_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_2_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_2_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_2_pos.x += 300 * dt

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_1_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_1_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_1_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_1_pos.x += 300 * dt

    text_rect = text_1_surface.get_rect(center=(player_1_pos.x, player_1_pos.y - 100))
    screen.blit(text_1_surface, text_rect)

    text_rect = text_2_surface.get_rect(center=(player_2_pos.x, player_2_pos.y - 100))
    screen.blit(text_2_surface, text_rect)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000 

pygame.quit()