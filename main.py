#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Lapyrinthe
main.py - Code de base pour lancer l'UI
lab.py - Classes pour la création du Labyrinthe
player.py - Classes pour le joueur
constants.py - Fichier de constantes
img/*.png - cases du Labyrinthe
"""

import pygame as pg
import datetime
import lab
import player
import constants as PC
import sys
import pickle

if getattr(sys, 'frozen', False):
    basedir = sys._MEIPASS
else:
    basedir = "."

pg.init()
pg.display.set_caption("Lapyrinthe")
pg.display.set_icon(PC.ICONE)

CONTINUER = 1
while CONTINUER:
    PC.FENETRE.blit(PC.ACCUEIL, (0, 0))
    pg.display.flip()
    MENU = 1
    GAME = 0
    WIN = 0
    FONT = pg.font.Font("{}/img/NotoMono-Regular.ttf".format(basedir), 20)

    # Menu du jeu
    while MENU:
        pg.time.Clock().tick(30)
        for event in pg.event.get():
            if (
                event.type == pg.QUIT or
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                CONTINUER = 0
                MENU = 0
                GAME = 0
                WIN = 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    MENU = 0
                    GAME = 1
                    WIN = 0

    # Initialisation à chaque nouvelle partie
    if GAME == 1:
        START = datetime.datetime.now()
        TIME = 0
        LABY = lab.Laby()
        LABY.make_lab(LABY.cell_list)
        LABY.display(LABY.cell_list)
        PLAYER = player.Perso(LABY.cell_list)

    # Jeu
    while GAME:
        pg.time.Clock().tick(60)
        TIME = datetime.datetime.now() - START
        CHRONO = FONT.render(str(TIME.seconds), 1, PC.WHITE)
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                CONTINUER = 0
                MENU = 0
                GAME = 0
                WIN = 0
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                MENU = 1
                GAME = 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    PLAYER.move("up")
                if event.key == pg.K_DOWN:
                    PLAYER.move("down")
                if event.key == pg.K_LEFT:
                    PLAYER.move("left")
                if event.key == pg.K_RIGHT:
                    PLAYER.move("right")
        PLAYER.collect()
        PC.FENETRE.blit(PC.BG0, (0, 0))
        PC.FENETRE.blit(PC.HUD, PC.HUD_COORD)
        PC.FENETRE.blit(CHRONO, (10, 575))
        LABY.display(LABY.cell_list)
        LABY.display_hud()
        PC.FENETRE.blit(PLAYER.perso, PLAYER.perso_pos)
        pg.display.flip()

        if (
            PC.CARROT_GOT == 1 and
            PC.RADIS_GOT == 1 and
            PC.SALAD_GOT == 1
        ):
            GAME = 0
            MENU = 0
            WIN = 1

    while WIN:
        for event in pg.event.get():
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                MENU = 1
                GAME = 0
                WIN = 0
                PC.CARROT_GOT = 0
                PC.RADIS_GOT = 0
                PC.SALAD_GOT = 0

        PC.FENETRE.blit(PC.BG0, (0, 0))
        PC.FENETRE.blit(PC.WIN, (0, 0))
        try:
            PC.SCORES[0]
        except IndexError:
            WIN_TXT = FONT.render("First Score:", 1, PC.WHITE)
            PC.SCORES.append(TIME.seconds)
        else:
            if int(TIME.seconds) <= PC.SCORES[0]:
                WIN_TXT = FONT.render("NEW HIGH SCORE:", 1, PC.WHITE)
                PC.FENETRE.blit(WIN_TXT, (250, 300))
                PC.FENETRE.blit(CHRONO, (450, 300))
                PC.SCORES.append(TIME.seconds)
                pickle.dump(PC.SCORES, open('scores.dat', 'wb'))
            else:
                WIN_TXT = FONT.render("Time:", 1, PC.WHITE)
                BEST = "Best : {}".format(str(PC.SCORES[0]))
                BST_TXT = FONT.render(BEST, 1, PC.WHITE)
                PC.FENETRE.blit(WIN_TXT, (300, 250))
                PC.FENETRE.blit(CHRONO, (450, 250))
                PC.FENETRE.blit(BST_TXT, (350, 350))

        pg.display.flip()

pg.quit()
