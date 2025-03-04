import pygame
import random
pygame.init()

# Game information / Global Values
class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    SIDE = 100
    TOP = 150


    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.max_val = max(lst)
        self.min_val = min(lst)

        self.pixel_width = round((self.width - self.SIDE) / len(lst))
        self.pixel_height = round((self.height - self.TOP) / (self.max_val - self.min_val))
        self.start_x = self.SIDE // 2

def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst
def draw(info):
    info.window.fill(info.BACKGROUND_COLOR) #override color (reset)
    draw_list(info)
    pygame.display.update()

def draw_list(info):
    lst = info.lst

    for i, val in enumerate(lst):
        x = info.start_x + 1 * info.block_width
        y = info.height - (val - info.min_val)* info.block_height

        color = info.GRADIENTS[i % 3]
        
        pygame.draw.rect(info.window, color, (x ,y , info.block_width, info.height))


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(600, 400, lst)
    while run:
        clock.tick(60)
        draw(draw_info) #resets background
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

if __name__ == "__main__":
    main()