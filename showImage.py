import pygame
import keyboard

pygame.init()
image = pygame.image.load("images/ship.png")
screen = pygame.display.set_mode((1024,768))

# rect = pygame.Rect(0,0, 50,50)
rect = image.get_rect()
rect.center = (400,300)

screen.blit(image, rect)
pygame.display.flip()
a = keyboard.read_key()

