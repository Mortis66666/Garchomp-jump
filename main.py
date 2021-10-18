import pygame
import os
from utils import *
import time







pygame.font.init()
pygame.mixer.init()

width, height = 1000,600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Garchomp jump")
garwidth, garheight = 103,107


score_font = pygame.font.SysFont("comicsans",40)

cacnea_rate = [False for _ in range(120)] + [True]

white = (233,233,233)
black = (0,0,0)
fps = 60



hitted = pygame.USEREVENT +1

garchomp = pygame.image.load(
    os.path.join("Assets", "garchomp.png")
)

garchomp = pygame.transform.flip(pygame.transform.scale(garchomp,(garwidth,garheight)),True,False)

cacnea = enlarge(pygame.image.load(
    os.path.join("Assets","cacnea.png")
),0.5)

jump_sound = pygame.mixer.Sound(os.path.join("Assets","jump.wav"))

jump = cacnea.get_height() + 70
print(jump)

land = pygame.Rect(0,height//2-5,width,10)

#fire_bg = pygame.Rect(200,height-100,500,80)


def draw_window(gar,cacneas,score,record):
    win.fill(white)
    pygame.draw.rect(win,black,land)
    #pygame.draw.rect(win,black,fire_bg)

    score_img = score_font.render(f"Score: {score}",1,black)
    record_img = score_font.render(f"Record: {record}",1,black)
    #fire_img = score_font.render("Fire Blast: ",1,black)

    win.blit(score_img,(10,10))
    win.blit(record_img,(width-record_img.get_width()-10,10))
    #win.blit(fire_img,(0,height-100))

    win.blit(garchomp,(gar.x,gar.y))

    for cac in cacneas:
        win.blit(cacnea,(cac.x,cac.y))


    pygame.display.update()

def handle_movement(key_pressed,garchomp):

    if (key_pressed[pygame.K_UP] or key_pressed[pygame.K_SPACE]) and not is_jump(garchomp):
        garchomp.y -= jump
        jump_sound.play()



def handle_cactus(cactuses,garchomp,move) -> None:

    for cactus in cactuses:
        cactus.x -= move
        if cactus.colliderect(garchomp):
            pygame.event.post(pygame.event.Event(hitted))


def main():

    run = True
    clock = pygame.time.Clock()
    gar = pygame.Rect(width//2-garwidth//2-300,height//2-garheight//2-50,garwidth,garheight)

    cacneas = []
    move = 6
    score = 0

    jumpcooldown = 20

    record = get_record()


    while run:

        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == hitted:
                run = False


        if score % 100 == 0:
            move += 2

        if break_record(score):
            record = score

        key_pressed = pygame.key.get_pressed()
        handle_movement(key_pressed,gar)

        if is_cacnea(cacnea_rate):
            cac = pygame.Rect(width-cacnea.get_width(),height//2-cacnea.get_height(),cacnea.get_width(),cacnea.get_height())
            cacneas.append(cac)

        if is_jump(gar) and jumpcooldown == 0:
            gar.y += jump
            jumpcooldown = 10

        elif is_jump(gar) and jumpcooldown != 0:
            jumpcooldown -= 1
            

        handle_cactus(cacneas,gar,move)

        draw_window(gar,cacneas,score,record)

        score += 1






    break_record(score)
    time.sleep(2)
    main()





if __name__ == "__main__":
    main()
