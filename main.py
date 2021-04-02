
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = (0,255,0)
RED = (200,10,10)
YELLOW = (200, 200, 10)
BLUE = (0,32,255)
WINDOW_HEIGHT = 300
WINDOW_WIDTH = 300


def drawGrid(matrix):
    blockSize = 10 #Set the size of the grid block
    i = 0
    j= 0
    for y in range(3, WINDOW_WIDTH, blockSize + 3):

        for x in range(3, WINDOW_HEIGHT, blockSize + 3):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            try:
                if (matrix[i][j] == 0):
                    pygame.draw.rect(SCREEN, BLUE, rect)
                elif (matrix[i][j] == 1):
                    pygame.draw.rect(SCREEN, RED, rect)
                elif (matrix[i][j] == 2):
                    pygame.draw.rect(SCREEN, GREEN, rect)
                elif (matrix[i][j] == 3):
                    pygame.draw.rect(SCREEN, WHITE, rect)

            except:
                pygame.draw.rect(SCREEN, WHITE, rect)

            j = j + 1
        j = 0
        i = i + 1

if __name__ == '__main__':
    matrix = []  # define empty matrix

    for i in range(20):
        row = []
        for j in range(20):
            row.append(3)
        matrix.append(row)


    x = [*range(0, 10, 1)]
    y = [*range(0, 10, 1)]
    all_cells = []
    for i in (x):
        for j in (y):
            all_cells.append([i, j])

    num_of_healthy = 10
    for i in range (num_of_healthy):
        choice = random.choice(all_cells)
        all_cells.remove(choice)
        matrix[choice[0]][choice[1]] = 0

    num_of_sick = 10
    for i in range(num_of_healthy):
        choice = random.choice(all_cells)
        all_cells.remove(choice)
        matrix[choice[0]][choice[1]] = 1



    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()

    finish = False
    #matrix = [[0, 1,2], [3, 2, 1]]
    # 0 healthy BLUE
    # 1 sick RED
    # 2 immuned/recovred GREEN
    # 3 empty WHITE

    while not finish:
        drawGrid(matrix)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

        pygame.display.update()