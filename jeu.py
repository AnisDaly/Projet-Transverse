import pygame
import sys


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

                    if indice == 0:

                        PLAY_GAME(0, LISTE_GRAVITES[0])

                    elif indice == 1:

                        PLAY_GAME(1, LISTE_GRAVITES[1])

                    elif indice == 2:

                        PLAY_GAME(2, LISTE_GRAVITES[2])

                    else:

                        PLAY_GAME(3, LISTE_GRAVITES[3])

        BG = pygame.image.load("bckgimg2.jpg")
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
    global score
    global LISTE_GRAVITES
    global LISTE_MAPS
    global LISTE_MAPS_RESIZED
    global LISTE_FLECHES

    while True:

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        SCREEN.blit(pygame.image.load(LISTE_MAPS[indice]), (0, 0))

        pygame.display.update()


def AIDE():

    global QUIT_BUTTON
    global jeu_quittable

    text_input = "Le principe du jeu est tres simple : \nchoisis une carte et deviens un vrai \ntireur d'elite ! Saisis la balle par \nun clic gauche, ajuste ta trajectoire \net la force en fonction des pointilles \net vise le panier pour marquer des points ! \nChaque panier marque augmentera\nton score de +2 ou +3 en fonction de s'il a \ntouche ou non l'arceau. \n\nLance toi et deviens un vrai pro du shoot !"

    jeu_quittable = False

    while True:

        AIDE_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if AIDE_RETOUR.checkForInput(AIDE_MOUSE_POS):
                    jeu_quittable = True
                    main_menu()


        dimension = 60
        hauteur_ecran = 640
        largeur_ecran = 1024

        pygame.draw.rect(SCREEN, "White", pygame.Rect(dimension, dimension, largeur_ecran - 2 * dimension,
                                                      hauteur_ecran - 2 * dimension))
        pygame.draw.rect(SCREEN, "Black", pygame.Rect(dimension, dimension, largeur_ecran - 2 * dimension,
                                                      hauteur_ecran - 2 * dimension), 5)

        AIDE_TEXT = get_font(60).render("Aide", True, "Orange")
        AIDE_RECT = AIDE_TEXT.get_rect(center=(512, 120))
        SCREEN.blit(AIDE_TEXT, AIDE_RECT)

        lines = text_input.split('\n')
        y_offset = 220

        for line in lines:
            text_render = get_font(15).render(line, True, "Black")
            text_rect = text_render.get_rect(x=dimension + 30, y=y_offset)
            SCREEN.blit(text_render, text_rect)
            y_offset += 20

        AIDE_RETOUR.changeColor(AIDE_MOUSE_POS)
        AIDE_RETOUR.update(SCREEN)




        pygame.display.update()


def main_menu():
    global jeu_quittable

    global AIDE_ON
    global QUIT_BUTTON

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

# PAUSE = pygame.image.load("")


RECT_FLECHE_DROITE = FLECHE_DROITE.get_rect()
RECT_FLECHE_GAUCHE = FLECHE_GAUCHE.get_rect()

hauteur_fleche = 310
RECT_FLECHE_DROITE.center = 0, hauteur_fleche
RECT_FLECHE_GAUCHE.center = 0, hauteur_fleche
RECT_FLECHE_DROITE.x = 940
RECT_FLECHE_GAUCHE.x = 10

indice = 0
score = 0
LISTE_GRAVITES = [10, 10, 1.62, 20]

jeu_quittable = True

LISTE_MAPS_RESIZED = ["assets/image/IMG_resized.jpg", "assets/image/terrain_basket_public_resized.png", "assets/image/IMG2_resized.jpg", "assets/image/IMG3_resized.jpg", ]
LISTE_MAPS = ["assets/image/IMG.jpg", "assets/image/terrain_basket_public.png", "assets/image/IMG2.jpg", "assets/image/IMG3.jpg"]
LISTE_FLECHES = ["assets/image/fleche_droite.png", "assets/image/fleche_droite.png"]

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


