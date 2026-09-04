import random
import pygame
import array
import math

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BLUE = (5, 5, 25)

clock = pygame.time.Clock()

try:
    collision_sound = pygame.mixer.Sound("collision.wav")
except FileNotFoundError:
    sample_rate = 22050
    n_samples = int(sample_rate * 0.1)
    buf = array.array('h', [0] * n_samples)
    for i in range(n_samples):
        t = float(i) / sample_rate
        buf[i] = int(32767 * math.sin(2.0 * math.pi * 523.25 * t))
    collision_sound = pygame.mixer.Sound(buffer=buf)

music_playing = False
try:
    pygame.mixer.music.load("space_ambient.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    music_playing = True
except FileNotFoundError:
    pass

try:
    background_img = pygame.image.load("space_background.png").convert()
    background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
except FileNotFoundError:
    background_img = None

stars = []
for _ in range(50):
    stars.append({
        "x": random.randint(0, SCREEN_WIDTH),
        "y": random.randint(0, SCREEN_HEIGHT),
        "speed": random.uniform(0.5, 2.0),
        "size": random.randint(1, 3)
    })

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            self.image = pygame.image.load("galactic_hero.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))
        except FileNotFoundError:
            self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (0, 102, 204), (20, 20), 20)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            self.image = pygame.image.load("cosmic_alien.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (30, 30))
        except FileNotFoundError:
            self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (204, 0, 0), (15, 15), 15)
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

score = 0
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_group.add(enemy)

font = pygame.font.SysFont(None, 36)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    for star in stars:
        star["y"] += star["speed"]
        if star["y"] > SCREEN_HEIGHT:
            star["y"] = 0
            star["x"] = random.randint(0, SCREEN_WIDTH)

    collided_enemies = pygame.sprite.spritecollide(player, enemy_group, False)
    for enemy in collided_enemies:
        score += 1
        collision_sound.play()
        enemy.reset_position()

    if background_img:
        screen.blit(background_img, (0, 0))
    else:
        screen.fill(DARK_BLUE)
        for star in stars:
            pygame.draw.circle(screen, WHITE, (int(star["x"]), int(star["y"])), star["size"])

    all_sprites.draw(screen)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
