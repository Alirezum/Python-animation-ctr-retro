import pygame
import sys
import random
import math
import time

# Initialize pygame
pygame.init()

# Setup window
WIDTH, HEIGHT = 600, 250
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro CRT Animation")

# Colors
Black = (10, 10, 10)
DARK_GREEN = (20, 40, 20)
RED = (255, 60, 60)
WITHE = (230, 230 ,230)

# Font
font = pygame.font.SysFont("monaspace", 40, bold=True)

clock = pygame.time.Clock()
start_time = time.time()

# Variable for moving horizontal 
line_offset = 0

def draw_scaline(surface, offset=0):
    for y in range(-offset, HEIGHT, 4):
        pygame.draw.line(surface, (0,0,0), (0,y), (WIDTH, y) , 1)

def draw_glow_circle(surface, color ,pos, radius, intensity=5):
    for i in range(intensity, 0, -1):
        alpha = int(50 / 1)
        glow_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.circle(glow_surface, (*color, alpha), pos, radius + i * 3)
        surface.blit(glow_surface, (0, 0))

def draw_glow_text(surface, text, font, color, pos, intensity=5):
    base = font.render(text, True, color)
    for i in range(intensity, 0, -1):
        glow_surface = font.render(text, True, color)
        glow_surface.set_alpha(30)
        surface.blit(glow_surface, (pos[0] - i, pos[1]))
        surface.blit(glow_surface, (pos[0] + i, pos[1]))
        surface.blit(glow_surface, (pos[0], pos[1] - i))
        surface.blit(glow_surface, (pos[0], pos[1] + i))
    surface.blit(base, pos)

def applay_ctr_curve(x, y):
    curve_strength = 0.05
    center_x = WIDTH / 2
    offset = (x - center_x) * curve_strength
    return int(x), int(y + offset)

msg = input("Enter you massage:")
flicking_msg = input("Enter you flicking massage:")



# Main animation loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Background with subtle flicker
    flicker = random.randint(-10, 10)
    bg_color = (
        max(0, DARK_GREEN[0] + flicker),
        max(0, DARK_GREEN[1] + flicker),
        max(0, DARK_GREEN[2] + flicker),
    )
    screen.fill(bg_color)

    # Update moving line offset
    line_offset = (line_offset + 1) % 4
    draw_scaline(screen, line_offset)

    # Pulse effect for sircle 
    elapsed = time.time() - start_time
    radius = 15 + int(5 * math.sin(elapsed * 5))

    # Draw glowing circle with CTR curve
    cx, xy = applay_ctr_curve(80, HEIGHT // 2)
    draw_glow_circle(screen, RED, (cx, xy), radius)

    # Static "msg" with CTR curve
    px, py = applay_ctr_curve(150, HEIGHT // 2 - 20)
    draw_glow_text(screen, msg, font, WITHE, (px, py))

    # Blinking "msg" with CTR curve
    if int(elapsed *2) %2 == 0:
        sx, sy = applay_ctr_curve(350, HEIGHT // 2 - 20)
        draw_glow_text(screen, flicking_msg, font, RED, (sx, sy))

    # Update display
    pygame.display.flip()
    clock.tick(60)



