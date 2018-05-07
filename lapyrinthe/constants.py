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

# Taille de la fenêtre
FENETRE = pg.display.set_mode((800, 600))
ACCUEIL = pg.image.load("img/splash.png").convert_alpha()
ICONE = pg.image.load("img/player/p_up.png").convert_alpha()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Background image
BG0 = pg.image.load("img/bg0.png")
WIN = pg.image.load("img/win.png").convert_alpha()

# HUD
HUD = pg.image.load("img/hud0.png")
HUD_COORD = (0, 570)

# Nombre et taille des cellules
CELL_X = 40  # taille X des cellules
CELL_Y = 30  # taille Y des cellules
COTE_X = 20  # nombre de cellules en X
COTE_Y = 19  # nombre de cellules en Y

FLAG = pg.image.load("img/items/flag.png").convert_alpha()

CARROT = pg.image.load("img/items/carrot.png").convert_alpha()
CARROT_GOT = 0
CARROT_COORD = (CELL_X * (COTE_X - 1), CELL_Y * (COTE_Y - 1))
CARROT_HUD = (CELL_X * COTE_X / 2, CELL_Y * COTE_Y)

RADIS = pg.image.load("img/items/radis.png").convert_alpha()
RADIS_GOT = 0
RADIS_COORD = (CELL_X * (COTE_X - 1), 0)
RADIS_HUD = (CELL_X * ((COTE_X / 2) + 1), CELL_Y * COTE_Y)

SALAD = pg.image.load("img/items/salad.png").convert_alpha()
SALAD_GOT = 0
SALAD_COORD = (0, CELL_Y * (COTE_Y - 1))
SALAD_HUD = (CELL_X * ((COTE_X / 2) + 2), CELL_Y * COTE_Y)

# Player images
P_UP = pg.image.load("img/player/p_up.png").convert_alpha()
P_DOWN = pg.image.load("img/player/p_down.png").convert_alpha()
P_LEFT = pg.image.load("img/player/p_left.png").convert_alpha()
P_RIGHT = pg.image.load("img/player/p_right.png").convert_alpha()