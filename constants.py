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
import sys
import pickle


if getattr(sys, 'frozen', False):
    basedir = sys._MEIPASS
else:
    basedir = "."

# Mixer Pre-Init
# pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pg.mixer.pre_init(44100, -16, 2, 512)
pg.mixer.init()

# Taille de la fenêtre
FENETRE = pg.display.set_mode((800, 600), pg.HWSURFACE | pg.DOUBLEBUF)
ACCUEIL = pg.image.load("{}/img/splash.png".format(basedir)).convert_alpha()
ICONE = pg.image.load("{}/img/player/p_up.png".format(basedir)).convert_alpha()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Scores
try:
    open('scores.dat', 'rb')
except FileNotFoundError:
    l_scores = list()
    pickle.dump(l_scores, open('scores.dat', 'wb'))
    SCORES = pickle.load(open('scores.dat', 'rb'))
else:
    SCORES = pickle.load(open('scores.dat', 'rb'))

# Background image
BG0 = pg.image.load("{}/img/bg0.png".format(basedir))
WIN = pg.image.load("{}/img/win.png".format(basedir)).convert_alpha()

# Music
pg.mixer.music.load("{}/sfx/Nicolai_Heidlas-Take_The_Chance.ogg".format(basedir))

# HUD
HUD = pg.image.load("{}/img/hud0.png".format(basedir))
HUD_COORD = (0, 570)

# Nombre et taille des cellules
CELL_X = 40  # taille X des cellules
CELL_Y = 30  # taille Y des cellules
COTE_X = 20  # nombre de cellules en X
COTE_Y = 19  # nombre de cellules en Y

# Items images
FLAG = pg.image.load("{}/img/items/flag.png".format(basedir)).convert_alpha()

CARROT = pg.image.load("{}/img/items/carrot.png".format(basedir)).convert_alpha()
CARROT_GOT = 0
CARROT_COORD = (CELL_X * (COTE_X - 1), CELL_Y * (COTE_Y - 1))
CARROT_HUD = (CELL_X * COTE_X / 2, CELL_Y * COTE_Y)

RADIS = pg.image.load("{}/img/items/radis.png".format(basedir)).convert_alpha()
RADIS_GOT = 0
RADIS_COORD = (CELL_X * (COTE_X - 1), 0)
RADIS_HUD = (CELL_X * ((COTE_X / 2) + 1), CELL_Y * COTE_Y)

SALAD = pg.image.load("{}/img/items/salad.png".format(basedir)).convert_alpha()
SALAD_GOT = 0
SALAD_COORD = (0, CELL_Y * (COTE_Y - 1))
SALAD_HUD = (CELL_X * ((COTE_X / 2) + 2), CELL_Y * COTE_Y)

# Items sounds
ITEM = pg.mixer.Sound("{}/sfx/item.ogg".format(basedir))

# Player images
P_UP = pg.image.load("{}/img/player/p_up.png".format(basedir)).convert_alpha()
P_DOWN = pg.image.load("{}/img/player/p_down.png".format(basedir)).convert_alpha()
P_LEFT = pg.image.load("{}/img/player/p_left.png".format(basedir)).convert_alpha()
P_RIGHT = pg.image.load("{}/img/player/p_right.png".format(basedir)).convert_alpha()

# Player sounds
JUMP = pg.mixer.Sound("{}/sfx/jump.ogg".format(basedir))
