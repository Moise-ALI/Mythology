#coding:utf-8
import pygame

pygame.init()

size = (500, 300)
pygame.display.set_caption("Mythology")
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
background = 0x90B0E0
white = (255, 255, 255)

screen.fill(background)
menu = pygame.Rect(100, 50, 300, 200)
pygame.draw.rect(screen, white, menu, 2)

pygame.display.flip()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Fermeture du jeu")
