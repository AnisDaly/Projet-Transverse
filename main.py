import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 1024, 640
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Déplacer la balle")

# Chargement de l'image de l'arrière-plan
background_image = pygame.image.load("assets/image/IMG3.jpg").convert()

# Chargement de l'image de la balle
ball_image = pygame.image.load("assets/image/basket-ball.png").convert_alpha()

# Classe représentant la balle
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ball_image
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Position initiale au centre
        self.is_dragging = False  # Pour suivre l'état de glissement
        self.has_been_moved = False  # Pour vérifier si la balle a déjà été déplacée

    def update(self, event):
        # Gérer les événements de la souris pour déplacer la balle une seule fois
        if not self.has_been_moved:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.is_dragging = True  # Commence à glisser si on clique sur la balle
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.is_dragging:
                    self.is_dragging = False  # Arrête de glisser quand on relâche le bouton
                    self.has_been_moved = True  # Marque la balle comme déplacée
            elif event.type == pygame.MOUSEMOTION and self.is_dragging:
                self.rect.move_ip(event.rel)  # Déplace la balle avec le mouvement de la souris

# Création de la balle
ball = Ball()

# Groupe de sprites contenant la balle
all_sprites = pygame.sprite.Group()
all_sprites.add(ball)

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            ball.update(event)  # Met à jour la position de la balle en fonction des événements de la souris

    # Dessiner l'arrière-plan
    SCREEN.blit(background_image, (0, 0))

    # Dessiner la balle
    all_sprites.draw(SCREEN)

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Limite de vitesse de la boucle
    clock.tick(60)

# Quitter Pygame et fermer la fenêtre
pygame.quit()
sys.exit()