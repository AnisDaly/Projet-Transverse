import pygame
#simple prototype
wScreen = 1200
hScreen = 500

# Initialize Pygame
pygame.init()

# Initialize Pygame's display module
win = pygame.display.set_mode((wScreen, hScreen))
pygame.display.set_caption('Projectile Motion')

ball_image = pygame.image.load("assets/image/basket-ball.png").convert_alpha()
gravity = 0.1
bounce_stop = 0.2
retention = 1

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ball_image
        self.rect = self.image.get_rect()
        self.radius = self.image.get_width() // 2
        self.x = wScreen // 2
        self.y = hScreen // 2
        self.vel_x =0
        # Initial velocity in the x-direction
        self.vel_y = 0  # Initial velocity in the y-direction
        self.gravity = 0.5
        self.is_dragging = False  # Pour suivre l'état de glissement
        self.has_been_moved = False  # Pour vérifier si la balle a déjà été déplacée
        self.pressed = False

    def update(self):
        # Update velocity due to gravity
        self.vel_y += self.gravity

        # Update position
        self.x += self.vel_x
        self.y += self.vel_y

        # Update rect position for drawing
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def check_gravity(self):
        if self.y < hScreen - self.radius:
            self.vel_y += gravity
        else:
            if self.vel_y > bounce_stop:
                self.vel_y = self.vel_y * -1 * retention
            else:
                if abs(self.vel_y) <= bounce_stop:
                    self.y_speed = 0





ball = Ball()
all_sprites = pygame.sprite.Group()
all_sprites.add(ball)

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if z
    if ball.has_been_moved == True:
        ball.check_gravity()
    # Update
        all_sprites.update()

    # Draw
    win.fill((0, 0, 0))  # Clear the screen
    all_sprites.draw(win)  # Draw all sprites
    pygame.display.flip()  # Update the display

    clock.tick(60)  # Cap the frame rate at 60 FPS

pygame.quit()
quit()
