import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 1024, 640
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Déplacer la balle")

# Chargement de l'image de l'arrière-plan
background_image = pygame.image.load("IMG3.jpg").convert()

# Chargement de l'image de la balle
ball_image = pygame.image.load("basket-ball.png").convert_alpha()

# Classe représentant la balle
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ball_image
        self.rect = self.image.get_rect()

    def update(self):
        pass

    def start_dragging(self):
        pass

    def stop_dragging(self):
        pass

    def launch_from_point(self, x, y):
        # Définit la position de la balle sur le point de départ spécifié
        self.rect.center = (x, y)

# Création de la balle
ball = Ball()

# Groupe de sprites contenant la balle
all_sprites = pygame.sprite.Group()
all_sprites.add(ball)

# Point de départ de la balle
start_x, start_y = WIDTH // 2, HEIGHT // 2

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Si l'utilisateur clique sur la balle, commencez à la déplacer
            if event.button == 1 and ball.rect.collidepoint(event.pos):
                ball.start_dragging()
            # Si l'utilisateur clique n'importe où ailleurs, lancez la balle à partir de ce point
            else:
                ball.launch_from_point(*event.pos)

    # Dessiner l'arrière-plan
    SCREEN.blit(background_image, (0, 0))

    # Dessiner la balle
    all_sprites.draw(SCREEN)

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Limite de vitesse de la boucle
    clock.tick(60)

# Quitter Pygame
pygame.quit()
sys.exit()