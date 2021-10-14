import pygame
import random


def enlarge(object,factor):
    size = object.get_width() * factor , object.get_height() * factor
    return pygame.transform.scale(object,size)

def is_cacnea(pos):
    return random.choice(pos)

def is_jump(garchomp):

    return garchomp.y != 197