import pygame
import sys
import math

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
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = ball_image
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Position initiale au centre
        self.is_dragging = False  # Pour suivre l'état de glissement
        self.has_been_moved = False  # Pour vérifier si la balle a déjà été déplacée
        self.pressed=False
        self.L_points=[]
        self.current_point_index=0
        self.L_aff=[]

    def update(self, event):
        # Gérer les événements de la souris pour déplacer la balle une seule fois
        mouse_pos=pygame.mouse.get_pos()
        if not self.has_been_moved:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.is_dragging = True  # Commence à glisser si on clique sur la balle
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.is_dragging:
                    self.is_dragging = False  # Arrête de glisser quand on relâche le bouton
                    self.has_been_moved = True  # Marque la balle comme déplacée
                    self.x, self.y = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEMOTION and self.is_dragging:
                self.rect.move_ip(event.rel)  # Déplace la balle avec le mouvement de la souris
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.pressed=True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.pressed=False
                self.L_aff.clear()
            elif self.pressed and event.type == pygame.MOUSEMOTION:
                g=(pygame.mouse.get_pos()[1]-self.y)/100
                hypothenus=math.sqrt((pygame.mouse.get_pos()[1]-self.y)**2+(pygame.mouse.get_pos()[0]-self.x)**2)
                if self.x > pygame.mouse.get_pos()[0] or self.x < pygame.mouse.get_pos()[0]:
                    cos_a=(pygame.mouse.get_pos()[0]-self.x)/hypothenus
                    self.L_aff.clear()
                    for x_p in range(0,300,25):
                        y=(-g*x_p**2)/(2*cos_a**2*hypothenus**2)+((mouse_pos[1]-self.y)/(mouse_pos[0]-self.x))*x_p+mouse_pos[1]-self.y
                        self.L_aff.append((self.x+x_p,self.y+y))
                    self.L_points=self.L_aff
        # Déplacer la balle vers le point actuel
        if self.L_points!=[] and not self.pressed:
            target_x, target_y = self.L_points[self.current_point_index]
            dx = target_x - self.x
            dy = target_y - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            speed = 5  # Vitesse de déplacement de la balle
            if distance > speed:
                self.x += dx * speed / distance
                self.y += dy * speed / distance
            else:
                # Si la balle est suffisamment proche du point, passer au point suivant
                self.current_point_index = (self.current_point_index + 1) % len(self.L_points)

        # Mettre à jour la position de la balle
        self.rect.center = (self.x, self.y)



# Création de la balle
ball = Ball(250, 250)

# Groupe de sprites contenant la balle
all_sprites = pygame.sprite.Group()
all_sprites.add(ball)

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()
while running:
    # Dessiner l'arrière-plan
    SCREEN.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            ball.update(event)  # Met à jour la position de la balle en fonction des événements de la souris


    # Dessiner la balle
    all_sprites.draw(SCREEN)

    for pos in ball.L_aff:
        pygame.draw.circle(SCREEN, (255, 255, 255), pos, 5)

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Limite de vitesse de la boucle
    clock.tick(60)

# Quitter Pygame et fermer la fenêtre
pygame.quit()
sys.exit()
