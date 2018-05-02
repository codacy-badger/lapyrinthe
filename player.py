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
import constants as pc


class Perso():
    """ Cree le personnage """
    def __init__(self, celllist):
        self.celllist = celllist
        self.cell = self.celllist[0]
        self.perso = pg.image.load("img/wp1_down.png").convert_alpha()
        self.perso_pos = (self.cell.x, self.cell.y)

    def move(self, move):
        """ pour bouger le personnage en fonction
        de la case où il se trouve
        """
        if (
                move == "up" and
                self.cell.num - pc.COTE_X >= 0 and
                self.cell.doors[0] == 1
        ):
            self.cell = self.celllist[self.cell.num - pc.COTE_X]
            self.perso_pos = (self.cell.x * pc.CELL_X, self.cell.y * pc.CELL_Y)
            self.perso = pg.image.load("img/wp1_up.png").convert_alpha()
        elif (
                move == "down" and
                self.cell.num + pc.COTE_X <= (pc.COTE_X * pc.COTE_Y) - 1 and
                self.cell.doors[1] == 1
        ):
            self.cell = self.celllist[self.cell.num + pc.COTE_X]
            self.perso_pos = (self.cell.x * pc.CELL_X, self.cell.y * pc.CELL_Y)
            self.perso = pg.image.load("img/wp1_down.png").convert_alpha()
        elif (
                move == "left" and
                self.cell.num - 1 >= 0 and
                self.cell.doors[3] == 1
        ):
            self.cell = self.celllist[self.cell.num - 1]
            self.perso_pos = (self.cell.x * pc.CELL_X, self.cell.y * pc.CELL_Y)
            self.perso = pg.image.load("img/wp1_left.png").convert_alpha()
        elif (
                move == "right" and
                self.cell.num + 1 <= (pc.COTE_X * pc.COTE_Y) - 1 and
                self.cell.doors[2] == 1
        ):
            self.cell = self.celllist[self.cell.num + 1]
            self.perso_pos = (self.cell.x * pc.CELL_X, self.cell.y * pc.CELL_Y)
            self.perso = pg.image.load("img/wp1_right.png").convert_alpha()
