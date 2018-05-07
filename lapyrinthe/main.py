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


pg.init()

FONT = pg.font.Font('./NotoMono-Regular.ttf', 20)
START = datetime.datetime.now()
TIME = 0

LABY = lab.Laby()
LABY.make_lab(LABY.cell_list)
LABY.display(LABY.cell_list)
PLAYER = player.Perso(LABY.cell_list)

CONTINUER = 1
while CONTINUER:
    pg.time.Clock().tick(60)
    TIME = datetime.datetime.now() - START
    CHRONO = FONT.render(str(TIME), 1, PC.WHITE)
    for event in pg.event.get():
        if (event.type == pg.QUIT or
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            CONTINUER = 0
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
        CONTINUER = 0
