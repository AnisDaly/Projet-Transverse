import pygame
import math

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((1200, 800))  # Grande fenêtre pour plus d'espace

# Chargement et ajustement de la taille de l'image du ballon de basket
ball_image = pygame.image.load('assets/image/basket-ball.png')
ball_image = pygame.transform.scale(ball_image, (60, 60))  # Ajustement de la taille pour s'adapter à l'échelle du jeu
ball_rect = ball_image.get_rect()

# Chargement et préparation de l'image d'arrière-plan
background_image = pygame.image.load("assets/image/IMG3.jpg").convert()
background_image = pygame.transform.scale(background_image, (1200, 800))  # Ajustement de la taille pour remplir l'écran

# Chargement de l'image du panier de basketball et ajustement de sa taille
hoop_image = pygame.image.load('assets/image/panier.png')
hoop_image = pygame.transform.scale(hoop_image, (120, 100))  # Ajustement de la taille au besoin
hoop_rect = hoop_image.get_rect()
hoop_rect.x = 900  # Positionnement du panier sur le côté droit de l'écran
hoop_rect.y = 300  # Positionnement du panier à une hauteur appropriée

# Couleurs
BLACK = (0, 0, 0)

# Paramètres initiaux du ballon
initial_x = 600  # Position de départ centrée
initial_y = 400
pos_x = initial_x
pos_y = initial_y
speed = 0
angle = 0
gravity = 9.8

dt = 0.15

# Le rebond
restitution = 0.8  # Bon effet de rebond

# État du ballon
dragging = False
launched = False

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if ball_rect.collidepoint(mouse_x, mouse_y):
                dragging = True
                anchor_x, anchor_y = mouse_x, mouse_y
        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                dragging = False
                launched = True
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = anchor_x - mouse_x
                dy = anchor_y - mouse_y
                speed = math.sqrt(dx**2 + dy**2) * 0.4  # Facteur de vitesse augmenté
                angle = math.degrees(math.atan2(-dy, dx))
                time = 0

    # Dessiner l'image de fond
    screen.blit(background_image, (0, 0))

    if launched:
        # Mise à jour de la position du ballon
        velocity_x = speed * math.cos(math.radians(angle))
        velocity_y = speed * math.sin(math.radians(angle)) - gravity * time
        pos_x += velocity_x * dt
        pos_y -= velocity_y * dt
        time += dt

        # Gérer les rebonds
        if pos_y >= screen.get_height() - ball_rect.height / 2:
            pos_y = screen.get_height() - ball_rect.height / 2
            speed *= restitution
            time = 0

        # Réinitialiser la position si la vitesse devient très faible
        if speed < 1:
            pos_x = initial_x
            pos_y = initial_y
            speed = 0
            launched = False

    # Dessiner le ballon de basket et le panier par-dessus le fond
    ball_rect.center = (int(pos_x), int(pos_y))
    screen.blit(ball_image, ball_rect)
    screen.blit(hoop_image, hoop_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
