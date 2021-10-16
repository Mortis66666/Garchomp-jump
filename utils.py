import pygame
import random
import mysql.connector
from constants import *

db = mysql.connector.connect(**kwargs)

mycursor = db.cursor()


def enlarge(object,factor):
    size = object.get_width() * factor , object.get_height() * factor
    return pygame.transform.scale(object,size)

def is_cacnea(pos):
    return random.choice(pos)

def is_jump(garchomp):

    return garchomp.y != 197



def break_record(score) -> bool:
    mycursor.execute("SELECT record FROM Record")

    record = 0

    for x in mycursor:
        record += x[0]

    if record > score:
        return False

    mycursor.execute("UPDATE Record SET record = %s WHERE record = %s",(score,record))
    db.commit()

    return True

def get_record() -> int:

    mycursor.execute("SELECT record FROM Record")

    rec = 0

    for x in mycursor:
        rec = x[0]

    return rec

def testing():
    pass


