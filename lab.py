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

import random
import pygame as pg
import constants as pc


class Cell():
    """ Chaque cellule du Labyrinthe """
    def __init__(self, x, y):
        """ x, y are coordinates
            visited is the status while making the Laby
            doors are open(1), close(0), [n, s, e, w]
            tag is the Nth of each cell
        """
        self.x = x
        self.y = y
        self.doors = [0, 0, 0, 0]
        self.tag = int()
        self.num = int()


class Laby():
    """ Creation et affichage du Labyrinthe
        methode de la fusion aleatoire des chemins
    """
    def __init__(self):
        """ Initialise la liste des cellules """
        self.cell_list = list()
        self.celltag = list()
        self.neigh = list()
        self.ctag = int()
        self.ntag = int()
        number = 0
        for i in range(0, pc.COTE_Y):
            for j in range(0, pc.COTE_X):
                cell = Cell(j, i)
                cell.num = number
                cell.tag = number
                self.cell_list.append(cell)
                number += 1

    def make_door(self, celllist, cell, neighbours):
        """ Permet l'ouverture de portes entre cases adjacentes:
        si les cases ont un mur commun, décider aléatoirement quel mur ouvrir,
        tant qu'elles n'ont pas le même tag
        """
        ng = random.choice(neighbours)
        self.ctag = cell.tag
        if ng != "X":
            self.ntag = ng.tag
            if (
                    (cell.tag != ng.tag) and
                    (cell.y == ng.y or cell.x == ng.x)
            ):
                # Ouverture porte Nord
                if cell.y - ng.y > 0:
                    cell.doors[0] = 1
                    ng.doors[1] = 1
                    ng.tag = cell.tag
                # Ouverture porte Sud
                if cell.y - ng.y < 0:
                    cell.doors[1] = 1
                    ng.doors[0] = 1
                    ng.tag = cell.tag
                # Ouverture porte Est
                if cell.x - ng.x < 0:
                    cell.doors[2] = 1
                    ng.doors[3] = 1
                    ng.tag = cell.tag
                # Ouverture porte Ouest
                if cell.x - ng.x > 0:
                    cell.doors[3] = 1
                    ng.doors[2] = 1
                    ng.tag = cell.tag
                for item in celllist:
                    if item.tag == self.ntag:
                        item.tag = self.ctag

    def make_lab(self, celllist):
        """ faire le Labyrinthe """
        self.celltag = [0]
        while self.celltag.count(self.celltag[0]) < pc.COTE_X * pc.COTE_Y:
            c = random.randrange(0, pc.COTE_X * pc.COTE_Y)
            self.celltag.clear()
            N = celllist[c].num
            # les cellules voisines sont stockées dans une liste
            # elle sont sous la forme [N, S, E, W].
            # Si il n'y a pas de voisin dans la direction, il y a un X
            # à la place de l'objet Cell prévu
            self.neigh = list()
            # Cellule Nord
            if celllist[c].y > 0 and celllist[c].y < pc.COTE_Y:
                self.neigh.append(celllist[N - pc.COTE_X])
            else:
                self.neigh.append("X")
            # Cellule Sud
            if celllist[c].y >= 0 and celllist[c].y < pc.COTE_Y - 1:
                self.neigh.append(celllist[N + pc.COTE_X])
            else:
                self.neigh.append("X")
            # Cellule Est
            if celllist[c].x >= 0 and celllist[c].x < pc.COTE_X - 1:
                self.neigh.append(celllist[N + 1])
            else:
                self.neigh.append("X")
            # Cellule Ouest
            if celllist[c].x > 0 and celllist[c].x < pc.COTE_X:
                self.neigh.append(celllist[N - 1])
            else:
                self.neigh.append("X")
            # self.liste.pop()
            self.make_door(celllist, celllist[c], self.neigh)
            for item in celllist:
                self.celltag.append(item.tag)

    def display(self, celllist):
        """ Afficher le Labyrinthe"""
        for item in celllist:
            case = pg.image.load(
                "img/w{}{}{}{}.png".format(
                    item.doors[0], item.doors[1], item.doors[2], item.doors[3])
            ).convert_alpha()
            pc.FENETRE.blit(case, (item.x * pc.CELL_X, item.y * pc.CELL_Y))
            if item.num == 0:
                flag = pg.image.load("img/wstart.png").convert_alpha()
                pc.FENETRE.blit(flag, (0, 0))
            if item.num == (pc.COTE_X * pc.COTE_Y - 1):
                end = pg.image.load("img/wend.png").convert_alpha()
                pc.FENETRE.blit(
                    end, ((pc.COTE_X - 1) * pc.CELL_X, (pc.COTE_Y - 1) * pc.CELL_Y)
                )
