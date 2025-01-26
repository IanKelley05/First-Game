import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Load the background
background = pygame.image.load('PurrpleBricks.png')
screen.blit(background, (0, 0))
pygame.display.update()

# Load character images
player_1_image = pygame.image.load('Boy.png')  
player_2_image = pygame.image.load('Ghost.png')

# Scale the images if needed
player_1_image = pygame.transform.scale(player_1_image, (60, 60))
player_2_image = pygame.transform.scale(player_2_image, (100, 100))

# Initialize player positions
player_1_pos = pygame.Vector2(screen.get_width() / 2 - 100, screen.get_height() / 2)
player_2_pos = pygame.Vector2(screen.get_width() / 2 + 100, screen.get_height() / 2)

# Load font for names
font = pygame.font.Font(None, 74)
text_1_surface = font.render("Me", True, "blue")
text_2_surface = font.render("Scary Ghost", True, "red")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Redraw the background to clear the screen
    screen.blit(background, (0, 0))

    # Draw the players
    screen.blit(player_1_image, player_1_pos)
    screen.blit(player_2_image, player_2_pos)

    # Handle player 1 movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_1_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_1_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_1_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_1_pos.x += 300 * dt

    # Handle player 2 automatic movement towards player 1
    if player_1_pos.y > player_2_pos.y:
        player_2_pos.y += 200 * dt
    if player_1_pos.y < player_2_pos.y:
        player_2_pos.y -= 200 * dt
    if player_1_pos.x > player_2_pos.x:
        player_2_pos.x += 200 * dt
    if player_1_pos.x < player_2_pos.x:
        player_2_pos.x -= 200 * dt

    # Draw player names above their positions
    text_rect = text_1_surface.get_rect(center=(player_1_pos.x + 30, player_1_pos.y - 40))
    screen.blit(text_1_surface, text_rect)

    text_rect = text_2_surface.get_rect(center=(player_2_pos.x + 35, player_2_pos.y - 40))
    screen.blit(text_2_surface, text_rect)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
