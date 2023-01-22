import pygame as pg
import pygame.font
import button
import meteo
from player import Player

WIDTH, HEIGHT = 900, 900
TITLE = 'Dodge simulator'


def main():
    pg.init()
    win = pg.display.set_mode((WIDTH, HEIGHT))
    backG = pg.image.load('image/background.jpg')
    pg.display.set_caption(TITLE)
    icon = pg.image.load('image/dodge.png')
    pg.display.set_icon(icon)

    key = False
    body = 0
    time = 0
    timespeed = 1.5

    meteor_shower = []
    num_drops = 60

    for i in range(0, num_drops):
        meteor_shower.append(meteo.Meteor(win))

    game_paused = False

    font = pygame.font.SysFont("arialblack", 40)
    TEXT_COL = (127, 255, 212)

    resume_img = pg.image.load('image/button_resume.png').convert_alpha()
    quit_img = pg.image.load('image/button_quit.png').convert_alpha()
    resume_button = button.Button(360, 125, resume_img, 1)
    quit_button = button.Button(390, 250, quit_img, 1)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        win.blit(img, (x, y))

    clock = pg.time.Clock()

    game = True
    dan = Player(WIDTH / 2, HEIGHT / 2, win)
    running = True
    while running == True:
        time += timespeed
        timespeed += 0.002
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    game_paused = True
                if event.key == pg.K_RETURN:
                    game_paused = False
                if event.key == pg.K_LEFT:
                    dan.left_pressed = True
                if event.key == pg.K_RIGHT:
                    dan.right_pressed = True
                if event.key == pg.K_UP:
                    dan.up_pressed = True
                if event.key == pg.K_DOWN:
                    dan.down_pressed = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    dan.left_pressed = False
                if event.key == pg.K_RIGHT:
                    dan.right_pressed = False
                if event.key == pg.K_UP:
                    dan.up_pressed = False
                if event.key == pg.K_DOWN:
                    dan.down_pressed = False
            if event.type == pg.QUIT:
                running = False

        if game == True:
            win.blit(backG, (0, 0))
            dan.draw(win)
            dan.update()
            text = font.render('Skóre: ' + str(body), True, (127, 255, 212))

            for k in meteor_shower:
                k.draw()

            for k in meteor_shower:
                k.pohyb()
            win.blit(text, (10, 50, 1, 10))
            for meteo.Meteor in meteor_shower:
                if meteo.Meteor.y > 860:
                    if game_paused == True:
                        pass
                    else:
                        body += 1
            if game_paused == True:
                if resume_button.draw(win):
                    game_paused = False
                if quit_button.draw(win):
                    running = False
            else:
                draw_text("Press Space to pause", font, TEXT_COL, 220, 10)

            for meteo.Meteor in meteor_shower:
                if game_paused == True:
                    pass
                elif dan.x <= meteo.Meteor.x + 50 and dan.x + 25 >= meteo.Meteor.x and dan.y <= meteo.Meteor.y + 50 and dan.y + 25 >= meteo.Meteor.y:
                    game = False

        else:
            win.fill((47, 79, 79))
            text = font.render('Konec hry', True, (218, 165, 32))
            text2 = font.render('Skóre: ' + str(body), True, (218, 165, 32))
            text3 = font.render('Chceš pokračovat ve hře?', True, (218, 165, 32))
            text4 = font.render('Zmačkni F a hraj znovu', True, (218, 165, 32))
            textRect = text.get_rect()
            textRect.center = (450, 300)
            text2Rect = text.get_rect()
            text2Rect.center = (450, 350)
            text3Rect = text.get_rect()
            text3Rect.center = (300, 400)
            text4Rect = text.get_rect()
            text4Rect.center = (330, 450)
            win.blit(text, textRect)
            win.blit(text2, text2Rect)
            win.blit(text3, text3Rect)
            win.blit(text4, text4Rect)

            if pg.key.get_pressed()[pg.K_f]:
                game_paused = False
                game = True
                body = 0
                time = 0
                timespeed = 1.5
                dan.x = 430
                dan.y = 450
                # dan je prostě borec
                for meteo.Meteor in meteor_shower:
                    meteo.Meteor.reset()

        pg.display.flip()
        clock.tick(60)


main()
