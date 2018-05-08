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
import constants as PC
import sys

if getattr(sys, 'frozen', False):
    basedir = sys._MEIPASS
else:
    basedir = "."

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
        for i in range(0, PC.COTE_Y):
            for j in range(0, PC.COTE_X):
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
        while self.celltag.count(self.celltag[0]) < PC.COTE_X * PC.COTE_Y:
            c = random.randrange(0, PC.COTE_X * PC.COTE_Y)
            self.celltag.clear()
            N = celllist[c].num
            # les cellules voisines sont stockées dans une liste
            # elle sont sous la forme [N, S, E, W].
            # Si il n'y a pas de voisin dans la direction, il y a un X
            # à la place de l'objet Cell prévu
            self.neigh = list()
            # Cellule Nord
            if celllist[c].y > 0 and celllist[c].y < PC.COTE_Y:
                self.neigh.append(celllist[N - PC.COTE_X])
            else:
                self.neigh.append("X")
            # Cellule Sud
            if celllist[c].y >= 0 and celllist[c].y < PC.COTE_Y - 1:
                self.neigh.append(celllist[N + PC.COTE_X])
            else:
                self.neigh.append("X")
            # Cellule Est
            if celllist[c].x >= 0 and celllist[c].x < PC.COTE_X - 1:
                self.neigh.append(celllist[N + 1])
            else:
                self.neigh.append("X")
            # Cellule Ouest
            if celllist[c].x > 0 and celllist[c].x < PC.COTE_X:
                self.neigh.append(celllist[N - 1])
            else:
                self.neigh.append("X")
            # self.liste.pop()
            self.make_door(celllist, celllist[c], self.neigh)
            for item in celllist:
                self.celltag.append(item.tag)

    def display(self, celllist):
        """ Afficher le Labyrinthe """
        for item in celllist:
            case = pg.image.load(
                "{}/img/path/{}{}{}{}.png".format(
                    basedir,
                    item.doors[0],
                    item.doors[1],
                    item.doors[2],
                    item.doors[3])
            ).convert_alpha()
            PC.FENETRE.blit(case, (item.x * PC.CELL_X, item.y * PC.CELL_Y))
            if item.num == 0:
                flag = PC.FLAG.convert_alpha()
                PC.FENETRE.blit(flag, (0, 0))
            if item.num == (PC.COTE_X * PC.COTE_Y - 1) and PC.CARROT_GOT == 0:
                carrot = PC.CARROT
                PC.FENETRE.blit(carrot, PC.CARROT_COORD)
            if item.num == (PC.COTE_X - 1) and PC.RADIS_GOT == 0:
                radis = PC.RADIS
                PC.FENETRE.blit(radis, PC.RADIS_COORD)
            if item.num == ((PC.COTE_X - 1) * PC.COTE_Y) and PC.SALAD_GOT == 0:
                salad = PC.SALAD
                PC.FENETRE.blit(salad, PC.SALAD_COORD)

    def display_hud(self):
        """ affichage du HUD """
        if PC.CARROT_GOT == 1:
            carrot = PC.CARROT
            PC.FENETRE.blit(carrot, PC.CARROT_HUD)
        if PC.RADIS_GOT == 1:
            radis = PC.RADIS
            PC.FENETRE.blit(radis, PC.RADIS_HUD)
        if PC.SALAD_GOT == 1:
            salad = PC.SALAD
            PC.FENETRE.blit(salad, PC.SALAD_HUD)
