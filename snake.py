import pygame, random

pygame.init()
W, H, S = 600, 400, 20
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

snake = [(300, 200)]
dx, dy = S, 0
food = (random.randrange(0, W, S), random.randrange(0, H, S))
score = 0
running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and dy == 0: dx, dy = 0, -S
            elif e.key == pygame.K_DOWN and dy == 0: dx, dy = 0, S
            elif e.key == pygame.K_LEFT and dx == 0: dx, dy = -S, 0
            elif e.key == pygame.K_RIGHT and dx == 0: dx, dy = S, 0

    head = (snake[0][0] + dx, snake[0][1] + dy)
    if head in snake or not (0 <= head[0] < W and 0 <= head[1] < H):
        running = False
    snake.insert(0, head)
    if head == food:
        score += 1
        food = (random.randrange(0, W, S), random.randrange(0, H, S))
    else:
        snake.pop()

    screen.fill((20, 20, 30))
    for x, y in snake:
        pygame.draw.rect(screen, (0, 220, 100), (x, y, S - 2, S - 2))
    pygame.draw.rect(screen, (255, 60, 60), (*food, S, S))
    screen.blit(font.render(f"Ball: {score}", True, (255, 255, 255)), (10, 10))
    pygame.display.flip()
    clock.tick(10)

pygame.quit()