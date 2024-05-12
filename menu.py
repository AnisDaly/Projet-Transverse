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
        self.current_point_index=28
        self.points_non_utilises=0
        self.L_aff=[]
        self.Panier=False
        self.Compteur=0
        self.mvt_fin=False

    def update(self, event):
        # Gérer les événements de la souris pour déplacer la balle une seule fois
        mouse_pos=pygame.mouse.get_pos()
        if event and not self.has_been_moved:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.is_dragging = True  # Commence à glisser si on clique sur la balle
                    self.mvt_fin=False
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.is_dragging:
                    self.is_dragging = False  # Arrête de glisser quand on relâche le bouton
                    self.has_been_moved = True  # Marque la balle comme déplacée
                    self.x, self.y = mouse_pos
                    distance=math.sqrt((850 - self.x) ** 2 + (398 - self.y)**2)
                    intervalle_points={(1,100):8,(101,200):7,(201,300):6,(301,400):5,(401,500):4,(501,1000):3}
                    for intervalle,nb_points in intervalle_points.items():
                        if intervalle[0]<=distance<=intervalle[1]:
                            self.points_non_utilises=nb_points
            elif event.type == pygame.MOUSEMOTION and self.is_dragging:
                self.rect.move_ip(event.rel)  # Déplace la balle avec le mouvement de la souris
        # Déplacer la balle vers le point actuel
        elif (self.L_points != []) and (not event) and (not self.pressed) and (not self.mvt_fin) and self.has_been_moved:
            if (self.y>398+50 and self.x>890) or (self.y>600):
                self.mvt_fin=True
            elif math.sqrt((850 - self.x) ** 2 + (398 - self.y) ** 2) < 70 and not self.Panier:
                print("PANIER")
                self.Panier = True
            elif self.current_point_index>=self.points_non_utilises:
                target_x, target_y = self.L_points[self.current_point_index]
                dx = target_x - self.x
                dy = target_y - self.y
                distance = math.sqrt(dx ** 2 + dy ** 2)
                speed = 8  # Vitesse de déplacement de la balle
                if distance > speed:
                    self.x += dx * speed / distance
                    self.y += dy * speed / distance
                else:
                    # Si la balle est suffisamment proche du point, passer au point suivant
                    self.current_point_index -= 1
                # Mettre à jour la position de la balle
                self.rect.center = (self.x, self.y)
        elif (not event and self.Panier) or(not event and self.mvt_fin):
            self.Panier=False
            self.mvt_fin=False
            self.Compteur+=1
            print(self.Compteur)
            self.x,self.y = WIDTH//2, HEIGHT//2
            self.has_been_moved=False
            self.rect.center = (self.x, self.y)
            self.L_points.clear()
            self.current_point_index = 28
        else:
            if event and event.type == pygame.MOUSEBUTTONDOWN:
                self.pressed=True
            elif event and event.type == pygame.MOUSEBUTTONUP:
                self.pressed=False
                self.L_aff.clear()
            elif event and self.pressed and event.type == pygame.MOUSEMOTION:
                g = (pygame.mouse.get_pos()[1]-self.y)
                hypothenuse = math.sqrt((mouse_pos[1]-self.y)**2+(mouse_pos[0]-self.x)**2)
                if self.x > mouse_pos[0] or self.x < mouse_pos[0]:
                    cos_a=(mouse_pos[0]-self.x)/hypothenuse
                    self.L_aff.clear()
                    for x_p in range(-700,25,25):
                        y=(-g*x_p**2)/(2*cos_a**2*hypothenuse**2)+((mouse_pos[1]-self.y)/(mouse_pos[0]-self.x))*x_p*2+mouse_pos[1]-self.y
                        self.L_aff.append((self.x-x_p,self.y-y))
                    self.L_points=list(self.L_aff)




# Création de la balle
ball = Ball(WIDTH//2,HEIGHT//2)

# Groupe de sprites contenant la balle
all_sprites = pygame.sprite.Group()
all_sprites.add(ball)

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()
while running:
    # Dessiner l'arrière-plan
    SCREEN.blit(background_image, (0, 0))
    event=pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.NOEVENT:
        ball.update(False)
    else:
        ball.update(event)  # Met à jour la position de la balle en fonction des événements de la souris
    # Dessiner la balle
    all_sprites.draw(SCREEN)
    for i in range(len(ball.L_aff)-1,ball.points_non_utilises+13,-1):
        pygame.draw.circle(SCREEN, (255, 255, 255), ball.L_aff[i], 5)
    pygame.draw.rect(SCREEN, (255,255,255),(850,381,100,10), 5 )
    print(ball.L_aff)
    # Mise à jour de l'affichage
    pygame.display.flip()

    # Limite de vitesse de la boucle
    clock.tick(60)

# Quitter Pygame et fermer la fenêtre
pygame.quit()
sys.exit()
