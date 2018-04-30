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

BG0 = pg.image.load("img/bg0w.png")
# cote_fenetre = fond.get_rect().size
CELL_X = 80  # taille X des cellules
CELL_Y = 60  # taille Y des cellules
COTE_X = 10  # nombre de cellules en X
COTE_Y = 10  # nombre de cellules en Y

FENETRE = pg.display.set_mode((CELL_X * COTE_X, CELL_Y * COTE_Y))

END = (CELL_X * (COTE_X - 1), CELL_Y * (COTE_Y - 1))
