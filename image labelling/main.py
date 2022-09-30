# req stands for requirements
import pygame
from pygame.locals import *
import pandas as pd
from random import randint,choice
import time
pygame.font.init()
FPS = 60
WIDTH,HEIGHT = 850,500
GEN_COLOR = lambda : (randint(0,255),randint(0,255),randint(0,255))
BLACK = (0,0,0)
WHITE = (255,255,255)
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
CLOCK = pygame.time.Clock()
FONT_WEIGHT = ['bold','italic']
ALL_FONTS = [(font,randint(80,90)) for font in pygame.font.get_fonts() if 'wingdings' not in font]
READ_FILE = lambda : pd.read_csv('caption_dataset.csv')
FILE_INFO = READ_FILE()
# the raw column is thesame as the labels column
ALL_SENTENCES,IMAGE_FILENAME = iter(FILE_INFO['raw']),iter(FILE_INFO['imagesId'])

def draw():
    # choose font
    BG_COLOR = BLACK
    WINDOW.fill(BG_COLOR)
    randomFont = choice(ALL_FONTS)
    fontName,size = 'arialblack', 80
    font = pygame.font.SysFont(fontName,size)
    # render font

    fontColor = WHITE
    sentence = next(ALL_SENTENCES)
    font = font.render(sentence,True,fontColor)
    WINDOW.blit(font,(WIDTH // 2 - 400,HEIGHT // 2 - 100))
    filename = next(IMAGE_FILENAME)
    pygame.image.save(WINDOW, filename)
    pygame.display.update()


def main(): 
    running = True 
    while running :
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                running  = False

        draw() 

if __name__ == '__main__':
    main()



