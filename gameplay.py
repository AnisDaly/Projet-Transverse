import random
import pygame
import math
def start_game():
    # Initialisation de Pygame
    pygame.init()
    screen = pygame.display.set_mode((1024, 640))  # Grande fenêtre pour plus d'espace

    # Chargement et ajustement de la taille de l'image du ballon de basket
    ball_image = pygame.image.load('assets/image/basket-ball.png')
    ball_image = pygame.transform.scale(ball_image, (60, 60))  # Ajustement de la taille pour s'adapter à l'échelle du jeu
    ball_rect = ball_image.get_rect()

    # Chargement et préparation de l'image d'arrière-plan
    background_image = pygame.image.load("assets/image/IMG3.jpg").convert()
    background_image = pygame.transform.scale(background_image, (1024, 640))  # Ajustement de la taille pour remplir l'écran

    # Chargement de l'image du panier de basketball et ajustement de sa taille
    hoop_image = pygame.image.load('assets/image/panier.png')
    hoop_image = pygame.transform.scale(hoop_image, (120, 100))  # Ajustement de la taille au besoin
    hoop_rect = hoop_image.get_rect()
    hoop_rect.x = 800  # Positionnement du panier sur le côté droit de l'écran
    hoop_rect.y = 180  # Positionnement du panier à une hauteur appropriée

    # Couleurs
    BLACK = (0, 0, 0)

    # Paramètres initiaux du ballon
    initial_x = random.randint(300,600)  # Position de départ centrée
    initial_y = random.randint(300,500)
    pos_x = initial_x
    pos_y = initial_y
    speed = 0
    angle = 0
    gravity = 9.8
    signe=1

    dt = 0.15

    # Liste pour la trajectoire en pointillés
    L_points=[]
    L_aff=[]
    # Nombre de panier
    compteur=0

    # Le rebond
    restitution = 0.8  # Bon effet de rebond

    # État du ballon
    dragging = False
    launched = False
    pressed = False

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
                    pressed = True
                    anchor_x, anchor_y = mouse_x, mouse_y
            elif event.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    dragging = False
                    pressed = False
                    L_aff.clear()
                    launched = True
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    dx = anchor_x - mouse_x
                    dy = anchor_y - mouse_y
                    speed = math.sqrt(dx**2 + dy**2) * 0.4  # Facteur de vitesse augmenté
                    angle = math.degrees(math.atan2(-dy, dx))
                    time = 0
            elif event.type == pygame.MOUSEMOTION and pressed:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = anchor_x - mouse_x
                dy = anchor_y - mouse_y
                point_x = initial_x
                point_y = initial_y
                time = 0
                dt = 0.50
                speed = math.sqrt(dx ** 2 + dy ** 2) * 0.4
                angle = math.degrees(math.atan2(-dy, dx))
                for i in range(15):
                    velocity_x = speed * math.cos(math.radians(angle))
                    velocity_y = speed * math.sin(math.radians(angle)) - gravity * time
                    point_x += velocity_x * dt
                    point_y -= velocity_y * dt
                    time += dt
                    L_points.append((point_x, point_y))
                L_aff = list(L_points)

        # Dessiner l'image de fond
        screen.blit(background_image, (0, 0))

        if launched:
            # Mise à jour de la position du ballon
            velocity_x = speed * math.cos(math.radians(angle))
            velocity_y = speed * math.sin(math.radians(angle)) - gravity * time
            pos_x += signe*velocity_x * dt
            pos_y -= velocity_y * dt
            time += dt

            # Gérer les rebonds
            if pos_y >= screen.get_height() - ball_rect.height / 2:
                pos_y = screen.get_height() - ball_rect.height / 2
                speed *= restitution
                time = 0

            if 190-10 <= pos_y <= 230+10 and 790-10 <= pos_x <= 820+10:
                dt = -0.15

            if 904-10 <= pos_x <= 918+10 and 190-10 <= pos_y <= 223+10:
                signe = (-1)


            # Réinitialiser la position si la vitesse devient très faible
            if speed < 1 or pos_x >= 1024:
                initial_x = random.randint(300, 600)
                initial_y = random.randint(300, 500)
                pos_x = initial_x
                pos_y = initial_y
                speed = 0
                launched = False
                signe = 1

            if math.sqrt((858-pos_x)**2+(210-pos_y)**2) <= 20:
                initial_x = random.randint(300, 600)
                initial_y = random.randint(300, 500)
                pos_x = initial_x
                pos_y = initial_y
                speed = 0
                launched = False
                signe = 1
                compteur += 1
                print(compteur)

        # Dessiner le ballon de basket et le panier par-dessus le fond
        ball_rect.center = (int(pos_x), int(pos_y))
        screen.blit(ball_image, ball_rect)
        screen.blit(hoop_image, hoop_rect)

        for coord in L_aff:
            pygame.draw.circle(screen, (255, 255, 255), coord,5)
        L_points.clear()
        #print(pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()