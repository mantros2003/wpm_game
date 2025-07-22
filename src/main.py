import pygame
import Key
import utils

# Display constants
DISP_SIZE_X, DISP_SIZE_Y = 1200, 800

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((DISP_SIZE_X, DISP_SIZE_Y))
pygame.display.set_caption("Kdyboard")
clock = pygame.time.Clock()
FPS = 60

# Create keys
keys = pygame.sprite.Group()
row_1 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
row_2 = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
row_3 = ["z", "x", "c", "v", "b", "n", "m"]
pos_1 = utils.get_pos_list(row_1, DISP_SIZE_X//2, 280, 10, 80)
pos_2 = utils.get_pos_list(row_2, DISP_SIZE_X//2, 380, 10, 80)
pos_3 = utils.get_pos_list(row_3, DISP_SIZE_X//2, 480, 10, 80)
for i in range(len(row_1)):
    keys.add(Key.Key(pos_1[i][0], pos_1[i][1], 80, row_1[i].upper()))
for i in range(len(row_2)):
    keys.add(Key.Key(pos_2[i][0], pos_2[i][1], 80, row_2[i].upper()))
for i in range(len(row_3)):
    keys.add(Key.Key(pos_3[i][0], pos_3[i][1], 80, row_3[i].upper()))
pos_space = utils.get_pos_list(["sapce"], DISP_SIZE_X//2, 580, 10, 800)
for i in range(len(pos_space)):
    keys.add(Key.Key(pos_space[i][0], pos_space[i][1], 80, "Space", isSpace=True))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        for key in keys.sprites():
            key.handle_event(event)

    keys.update()

    screen.fill((255, 153, 204))

    keys.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)
