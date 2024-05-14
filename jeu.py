import pygame
import sys
import math
import random

class Button():
    def __init__(self, image, text_input, pos, font, base_color, hovering_color):
        self.font = font
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        return self.rect.collidepoint(position)

    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

# Initialiser pygame
pygame.init()
pygame.mixer.init()  # Initialiser le module de mixage

# Définir les couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

# Charger les effets sonores
map_select_sound = pygame.mixer.Sound("sons/science-documentary-169621.mp3")
map_select_sound.set_volume(0.01)  # Régler le volume à 50%

# Charger la musique de fond (à jouer pendant le jeu)
game_music = pygame.mixer.Sound("sons/science-documentary-169621.mp3")
game_music.set_volume(0.01)  # Régler le volume à 50%

# Dimensions de l'écran
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 640

def JOUER():
    global indice

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if JOUER_RETOUR.checkForInput(mouse_pos):
                    main_menu()

                elif RECT_FLECHE_GAUCHE.collidepoint(mouse_pos):
                    if indice != 0:
                        indice -= 1

                elif RECT_FLECHE_DROITE.collidepoint(mouse_pos):
                    if indice != 3:
                        indice += 1

                elif JOUER_MAP.checkForInput(mouse_pos):
                    map_select_sound.play()  # Jouer le son de sélection de carte
                    if indice == 0:
                        PLAY_GAME(0, LISTE_GRAVITES[0])
                    elif indice == 1:
                        PLAY_GAME(1, LISTE_GRAVITES[1])
                    elif indice == 2:
                        PLAY_GAME(2, LISTE_GRAVITES[2])
                    else:
                        PLAY_GAME(3, LISTE_GRAVITES[3])

        BG = pygame.image.load("assets/image/bckgimg2.jpg")
        SCREEN.blit(BG, (0, 0))

        dimension = 60
        hauteur_ecran = 640
        largeur_ecran = 1024

        JOUER_text = get_font(50).render("Choisissez un terrain !", True, "White")
        JOUER_rect = JOUER_text.get_rect(center=(512, 65))
        SCREEN.blit(JOUER_text, JOUER_rect)

        JOUER_RETOUR.changeColor(mouse_pos)
        JOUER_RETOUR.update(SCREEN)
        JOUER_MAP.changeColor(mouse_pos)
        JOUER_MAP.update(SCREEN)

        if indice == 0:
            SCREEN.blit(pygame.image.load(LISTE_MAPS_RESIZED[0]), (largeur_ecran // 2 - 307, hauteur_ecran // 2 - 192))
            pygame.draw.rect(SCREEN, "White",
                             pygame.Rect(largeur_ecran // 2 - 307, hauteur_ecran // 2 - 192, largeur_ecran - 410,
                                         hauteur_ecran - 255), 5)
            SCREEN.blit(FLECHE_DROITE, RECT_FLECHE_DROITE)

        elif indice == 1:
            SCREEN.blit(pygame.image.load(LISTE_MAPS_RESIZED[1]), (largeur_ecran // 2 - 307, hauteur_ecran // 2 - 192))
            pygame.draw.rect(SCREEN, "White",
                             pygame.Rect(largeur_ecran // 2 - 307, hauteur_ecran // 2 - 192, largeur_ecran - 410,
                                         hauteur_ecran - 255), 5)
            SCREEN.blit(FLECHE_GAUCHE, RECT_FLECHE_GAUCHE)
            SCREEN.blit(FLECHE_DROITE, RECT_FLECHE_DROITE)

        elif indice == 2:
            SCREEN.blit(pygame.image.load(LISTE_MAPS_RESIZED[2]), (largeur_ecran // 2 - 307, hauteur_ecran // 2 - 192))
            pygame.draw.rect(SCREEN, "White",
                             pygame.Rect(largeur_ecran // 2 - 307, hauteur_ecran // 2 - 192, largeur_ecran - 410,
                                         hauteur_ecran - 255), 5)
            SCREEN.blit(FLECHE_GAUCHE, RECT_FLECHE_GAUCHE)
            SCREEN.blit(FLECHE_DROITE, RECT_FLECHE_DROITE)

        else:
            SCREEN.blit(pygame.image.load(LISTE_MAPS_RESIZED[3]), (largeur_ecran // 2 - 307, hauteur_ecran // 2 - 192))
            pygame.draw.rect(SCREEN, "White",
                             pygame.Rect(largeur_ecran // 2 - 307, hauteur_ecran // 2 - 192, largeur_ecran - 410,
                                         hauteur_ecran - 255), 5)
            SCREEN.blit(FLECHE_GAUCHE, RECT_FLECHE_GAUCHE)

        pygame.display.update()

def PLAY_GAME(indice, gravite):
    global en_jeu
    global score_p1, score_p2
    global current_player

    # Déclarer les scores comme globales
    score_p1, score_p2 = 0, 0
    current_player = 1  # Initialiser le joueur 1

    background_image = pygame.image.load(LISTE_MAPS[indice])
    BLACK = (0, 0, 0)
    dimension = 60
    hauteur_ecran = 640
    largeur_ecran = 1024

    initial_x = random.randint(300, 600)
    initial_y = random.randint(300, 500)
    pos_x, pos_y = initial_x, initial_y
    speed, angle, gravity = 0, 0, LISTE_GRAVITES[indice]
    dt = 0.15
    time = 0

    L_points, L_aff = [], []
    compteur = 0

    restitution = 0.8
    dragging, launched, pressed = False, False, False

    clock = pygame.time.Clock()

    # Jouer la musique de jeu lorsque le jeu commence
    game_music.play(-1)

    while en_jeu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not launched:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if RECT_BALL_IMAGE.collidepoint(mouse_x, mouse_y):
                        dragging, pressed = True, True
                        anchor_x, anchor_y = mouse_x, mouse_y
                    elif RECT_PAUSE.collidepoint(mouse_x, mouse_y):
                        PAUSE_GAME()
            elif event.type == pygame.MOUSEBUTTONUP and dragging:
                dragging, pressed, launched = False, False, True
                L_aff.clear()
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx, dy = anchor_x - mouse_x, anchor_y - mouse_y
                speed = math.sqrt(dx**2 + dy**2) * 0.4
                angle = math.degrees(math.atan2(-dy, dx))
                time = 0
            elif event.type == pygame.MOUSEMOTION and pressed:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx, dy = anchor_x - mouse_x, anchor_y - mouse_y
                point_x, point_y = initial_x, initial_y
                dt = 0.50
                speed = math.sqrt(dx ** 2 + dy ** 2) * 0.4
                angle = math.degrees(math.atan2(-dy, dx))
                time = 0
                L_points.clear()
                for i in range(15):
                    velocity_x = speed * math.cos(math.radians(angle))
                    velocity_y = speed * math.sin(math.radians(angle)) - gravity * time
                    point_x += velocity_x * dt
                    point_y -= velocity_y * dt
                    time += dt
                    L_points.append((point_x, point_y))
                L_aff = list(L_points)

        SCREEN.blit(background_image, (0, 0))

        if launched:
            velocity_x = speed * math.cos(math.radians(angle))
            velocity_y = speed * math.sin(math.radians(angle)) - gravity * time
            pos_x += velocity_x * dt
            pos_y -= velocity_y * dt
            time += dt

            if pos_y >= SCREEN.get_height() - RECT_BALL_IMAGE.height / 2:
                pos_y = SCREEN.get_height() - RECT_BALL_IMAGE.height / 2
                speed *= restitution
                time = 0

            if 180 <= pos_y <= 230 and 780 <= pos_x <= 830:
                dt = -0.15

            if 894 <= pos_x <= 938 and 180 <= pos_y <= 233:
                signe = -1

            if speed < 1 or pos_x >= SCREEN_WIDTH:
                initial_x = random.randint(300, 600)
                initial_y = random.randint(300, 500)
                pos_x, pos_y = initial_x, initial_y
                speed, launched = 0, False
                signe = 1
                # Changer de joueur après chaque tir
                current_player = 2 if current_player == 1 else 1

            if math.sqrt((848 - pos_x)**2 + (200 - pos_y)**2) <= 20:
                initial_x = random.randint(300, 600)
                initial_y = random.randint(300, 500)
                pos_x, pos_y = initial_x, initial_y
                speed, launched = 0, False
                signe, compteur = 1, compteur + 1
                if current_player == 1:
                    score_p1 += 2  # Incrémenter le score du joueur 1
                else:
                    score_p2 += 2  # Incrémenter le score du joueur 2
                # Changer de joueur après chaque tir
                current_player = 2 if current_player == 1 else 1

        RECT_BALL_IMAGE.center = (int(pos_x), int(pos_y))
        SCREEN.blit(BALL_IMAGE, RECT_BALL_IMAGE)
        SCREEN.blit(HOOP_IMAGE, RECT_HOOP)
        SCREEN.blit(PAUSE, RECT_PAUSE)

        for coord in L_aff:
            pygame.draw.circle(SCREEN, (255, 255, 255), coord, 5)

        # Afficher les scores
        score_p1_text = get_font(30).render(f"Joueur 1: {score_p1}", True, (255, 255, 255))
        score_p2_text = get_font(30).render(f"Joueur 2: {score_p2}", True, (255, 255, 255))
        SCREEN.blit(score_p1_text, (10, 10))
        SCREEN.blit(score_p2_text, (SCREEN_WIDTH - score_p2_text.get_width() - 10, 10))

        # Afficher le joueur actuel
        current_player_text = get_font(30).render(f"Tour du joueur {current_player}", True, (255, 255, 255))
        current_player_rect = current_player_text.get_rect(center=(SCREEN_WIDTH // 2, 30))
        SCREEN.blit(current_player_text, current_player_rect)

        pygame.display.flip()
        clock.tick(60)

def PAUSE_GAME():
    global en_jeu
    en_jeu = False

    text_input = "     Appuyez sur Echap pour quitter.\n Appuyez sur Entree pour reprendre."
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    en_jeu = True
                    main_menu()
                elif event.key == pygame.K_RETURN:
                    en_jeu = True
                    return

        SCREEN.blit(pygame.image.load(LISTE_MAPS[indice]), (0, 0))
        pygame.draw.rect(SCREEN, WHITE, pygame.Rect(300, 200, 420, 200))
        pygame.draw.rect(SCREEN, BLACK, pygame.Rect(300, 200, 420, 200), 5)

        PAUSE_TEXT = get_font(30).render("Pause", True, ORANGE)
        PAUSE_RECT = PAUSE_TEXT.get_rect(center=(SCREEN_WIDTH // 2, 250))
        SCREEN.blit(PAUSE_TEXT, PAUSE_RECT)

        lines = text_input.split('\n')
        y_offset = 300
        for line in lines:
            text_render = get_font(15).render(line, True, BLACK)
            text_rect = text_render.get_rect(x=340, y=y_offset)
            SCREEN.blit(text_render, text_rect)
            y_offset += 20

        pygame.display.update()

def AIDE():
    global jeu_quittable

    text_input = "Le principe du jeu est tres simple : \nchoisis une carte et deviens un vrai \ntireur d'elite ! Saisis la balle par \nun clic gauche, ajuste ta trajectoire \net la force en fonction des pointilles \net vise le panier pour marquer des points ! \nChaque panier marque augmentera\nton score de +2 ou +3 en fonction de s'il a \ntouche ou non l'arceau. \n\nLance toi et deviens un vrai pro du shoot !"

    jeu_quittable = False

    while True:
        AIDE_MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP and AIDE_RETOUR.checkForInput(AIDE_MOUSE_POS):
                jeu_quittable = True
                main_menu()

        pygame.draw.rect(SCREEN, WHITE, pygame.Rect(60, 60, SCREEN_WIDTH - 120, SCREEN_HEIGHT - 120))
        pygame.draw.rect(SCREEN, BLACK, pygame.Rect(60, 60, SCREEN_WIDTH - 120, SCREEN_HEIGHT - 120), 5)

        AIDE_TEXT = get_font(60).render("Aide", True, ORANGE)
        AIDE_RECT = AIDE_TEXT.get_rect(center=(SCREEN_WIDTH // 2, 120))
        SCREEN.blit(AIDE_TEXT, AIDE_RECT)

        lines = text_input.split('\n')
        y_offset = 220
        for line in lines:
            text_render = get_font(15).render(line, True, BLACK)
            text_rect = text_render.get_rect(x=90, y=y_offset)
            SCREEN.blit(text_render, text_rect)
            y_offset += 20

        AIDE_RETOUR.changeColor(AIDE_MOUSE_POS)
        AIDE_RETOUR.update(SCREEN)

        pygame.display.update()

def main_menu():
    global jeu_quittable

    # Arrêter la musique de jeu si elle est en cours
    game_music.stop()
    map_select_sound.stop()  # Arrêter également le son de sélection de carte

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT and jeu_quittable:
                pygame.quit()
                sys.exit()

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(75).render("Basket Sniper", True, "Orange")
        MENU_RECT = MENU_TEXT.get_rect(center=(512, 100))

        JOUER_BUTTON.changeColor(MENU_MOUSE_POS)
        AIDE_BUTTON.changeColor(MENU_MOUSE_POS)
        QUIT_BUTTON.changeColor(MENU_MOUSE_POS)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [JOUER_BUTTON, AIDE_BUTTON, QUIT_BUTTON]:
            button.update(SCREEN)

        if pygame.mouse.get_pressed()[0]:
            if JOUER_BUTTON.checkForInput(MENU_MOUSE_POS):
                JOUER()
            if AIDE_BUTTON.checkForInput(MENU_MOUSE_POS):
                AIDE()
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS) and jeu_quittable:
                pygame.quit()
                sys.exit()

        jeu_quittable = True
        pygame.display.update()

pygame.init()

SCREEN = pygame.display.set_mode((1024, 640))
pygame.display.set_caption("Menu")
BG = pygame.image.load("assets/image/bckgimg2.jpg")

def get_font(size):
    return pygame.font.Font("assets/image/boohong.otf", size)

JOUER_RETOUR = Button(image=pygame.image.load("assets/image/Quit Rect.png"), pos=(902, 590),
                      text_input="Retour", font=get_font(45), base_color="White", hovering_color="Orange")

FLECHE_DROITE = pygame.image.load("assets/image/fleche_droite.png")
FLECHE_GAUCHE = pygame.image.load("assets/image/fleche_gauche.png")
BALL_IMAGE = pygame.image.load("assets/image/basket-ball.png")
HOOP_IMAGE = pygame.image.load("assets/image/panier.png")
PAUSE = pygame.image.load("assets/image/pause_button.png")

RECT_PAUSE = PAUSE.get_rect()
RECT_FLECHE_DROITE = FLECHE_DROITE.get_rect()
RECT_FLECHE_GAUCHE = FLECHE_GAUCHE.get_rect()
RECT_BALL_IMAGE = BALL_IMAGE.get_rect()
RECT_HOOP = HOOP_IMAGE.get_rect()

RECT_PAUSE.x = 15
RECT_PAUSE.y = 15
hauteur_fleche = 310
RECT_FLECHE_DROITE.center = 0, hauteur_fleche
RECT_FLECHE_GAUCHE.center = 0, hauteur_fleche
RECT_FLECHE_DROITE.x = 940
RECT_FLECHE_GAUCHE.x = 10
RECT_HOOP.x = 800
RECT_HOOP.y = 180

indice = 0
score = 0
LISTE_GRAVITES = [10, 10, 1.62, 20]

jeu_quittable = True
en_jeu = True

LISTE_MAPS_RESIZED = ["assets/image/IMG_resized.jpg", "assets/image/terrain_basket_public_resized.png", "assets/image/IMG2_resized.jpg", "assets/image/IMG3_resized.jpg"]
LISTE_MAPS = ["assets/image/IMG.jpg", "assets/image/terrain_basket_public.png", "assets/image/IMG2.jpg", "assets/image/IMG3.jpg"]
LISTE_FLECHES = ["fleche_droite.png", "fleche_droite.png"]

AIDE_RETOUR = Button(image=None, pos=(512, 520),
                     text_input="RETOUR", font=get_font(50), base_color="Black", hovering_color="Orange")

JOUER_BUTTON = Button(image=pygame.image.load("assets/image/Play Rect.png"), pos=(512, 250),
                     text_input="JOUER", font=get_font(40), base_color="White", hovering_color="Orange")

JOUER_MAP = Button(image=pygame.image.load("assets/image/Play Rect.png"), pos=(512, 590),
                     text_input="JOUER", font=get_font(40), base_color="White", hovering_color="Orange")

AIDE_BUTTON = Button(image=pygame.image.load("assets/image/Options Rect.png"), pos=(512, 400),
                     text_input="AIDE", font=get_font(40), base_color="White", hovering_color="Orange")

QUIT_BUTTON_POS = (512, 550)

QUIT_BUTTON = Button(image=pygame.image.load("assets/image/Quit Rect.png"), pos=QUIT_BUTTON_POS,
                     text_input="QUIT", font=get_font(40), base_color="White", hovering_color="Orange")

main_menu()
