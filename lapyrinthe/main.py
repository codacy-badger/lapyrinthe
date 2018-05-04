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
import lab
import player
import constants as PC


pg.init()

LABY = lab.Laby()
LABY.make_lab(LABY.cell_list)
LABY.display(LABY.cell_list)
PLAYER = player.Perso(LABY.cell_list)

CONTINUER = 1
while CONTINUER:
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

    PC.FENETRE.blit(PC.BG0, (0, 0))
    PC.FENETRE.blit(PC.HUD, PC.HUD_COORD)
    LABY.display(LABY.cell_list)
    PC.FENETRE.blit(PLAYER.perso, PLAYER.perso_pos)
    pg.display.flip()

    if PLAYER.perso_pos == PC.END_COORD:
        CONTINUER = 0
