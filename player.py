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

import constants as PC


class Perso():
    """ Cree le personnage """
    def __init__(self, celllist):
        self.celllist = celllist
        self.cell = self.celllist[0]
        self.perso = PC.P_RIGHT
        self.perso_pos = (self.cell.x, self.cell.y)

    def collect(self):
        """Get item"""
        if self.perso_pos == PC.CARROT_COORD:
            PC.CARROT_GOT = 1
            PC.ITEM.play()
        if self.perso_pos == PC.RADIS_COORD:
            PC.RADIS_GOT = 1
            PC.ITEM.play()
        if self.perso_pos == PC.SALAD_COORD:
            PC.SALAD_GOT = 1
            PC.ITEM.play()

    def move(self, move):
        """ pour bouger le personnage en fonction
        de la case où il se trouve
        """
        if (
                move == "up" and
                self.cell.num - PC.COTE_X >= 0 and
                self.cell.doors[0] == 1
        ):
            PC.JUMP.play()
            self.cell = self.celllist[self.cell.num - PC.COTE_X]
            self.perso_pos = (self.cell.x * PC.CELL_X, self.cell.y * PC.CELL_Y)
            self.perso = PC.P_UP
        elif (
                move == "down" and
                self.cell.num + PC.COTE_X <= (PC.COTE_X * PC.COTE_Y) - 1 and
                self.cell.doors[1] == 1
        ):
            PC.JUMP.play()
            self.cell = self.celllist[self.cell.num + PC.COTE_X]
            self.perso_pos = (self.cell.x * PC.CELL_X, self.cell.y * PC.CELL_Y)
            self.perso = PC.P_DOWN
        elif (
                move == "left" and
                self.cell.num - 1 >= 0 and
                self.cell.doors[3] == 1
        ):
            PC.JUMP.play()
            self.cell = self.celllist[self.cell.num - 1]
            self.perso_pos = (self.cell.x * PC.CELL_X, self.cell.y * PC.CELL_Y)
            self.perso = PC.P_LEFT
        elif (
                move == "right" and
                self.cell.num + 1 <= (PC.COTE_X * PC.COTE_Y) - 1 and
                self.cell.doors[2] == 1
        ):
            PC.JUMP.play()
            self.cell = self.celllist[self.cell.num + 1]
            self.perso_pos = (self.cell.x * PC.CELL_X, self.cell.y * PC.CELL_Y)
            self.perso = PC.P_RIGHT
