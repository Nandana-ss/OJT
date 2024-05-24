import pygame
import sys
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Elastic Ball Animation")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (254, 0, 0)
ball_radius = 30
ball_color = RED
gravity = 0.5
bounce_factor = 0.8
ball_x = width // 2
ball_y = 0
ball_velocity_y = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball_y += ball_velocity_y
    ball_velocity_y += gravity  
    if ball_y >= height - ball_radius:
        ball_y = height - ball_radius
        ball_velocity_y = -ball_velocity_y * bounce_factor
    screen.fill(WHITE)
    pygame.draw.circle(screen, ball_color, (ball_x, int(ball_y)), ball_radius)
    pygame.display.flip() 
    pygame.time.Clock().tick(60)
pygame.quit()
sys.exit()