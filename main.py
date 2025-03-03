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

    SIDE_PAD = 100
    TOP_PAD = 150


    def __init__(self, width, height, list):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(list)

    def set_list(self, list):
        self.list = list
        self.max_val = max(list)
        self.min_val = min(list)

        self.pixel_width = round((self.width - self.SIDE_PAD) / len(list))
        self.pixel_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

def generate_starting_list(n, min_val, max_val)
    list = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        list.append(val)

        return list

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)

        pygame.display.update()

        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False
    pygame.quit()

if __name__ == "__main__":
    main()