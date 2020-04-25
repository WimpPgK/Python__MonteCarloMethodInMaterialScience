import numpy as np
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import *
import grain
import time
import random
import math

class Matrix:



    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n
        self.grain = np.full((x, y),-1, dtype=int)
        self.grainPre = np.zeros((x, y), dtype=int)
        self.grainPrev = np.zeros((x, y), dtype=int)

        self.grainList = np.empty(n, dtype=grain.Grain)
        #self.idList = np.random.choice (0, 21478347, n)
        # wektoryzacja _init_ w klasie Grain w celu utworzenia macierzy obiektow
        vSite = np.vectorize(grain.Grain)
        init_vector = np.arange(n).reshape((n))





        self.grainList[:] = vSite(init_vector)


    def createGrains(self, firstPhrase):

        self.firstPhase = firstPhrase

        for i in range (self.n):
            self.grainList[i].id = i;
            self.grainList[i].colourG = np.random.randint(0, 255);
            self.grainList[i].colourB = np.random.randint(0, 200);
            self.grainList[i].colourR = np.random.randint(0, 255);

    def randomizeGrainPosition(self):




        pom01 = random.randint(1, self.x-2)
        pom02 = random.randint(1, self.y-2)
        licznik = None
        for i in range(self.n):
            licznik = 0
            while self.grain[pom01][pom02] != -1 or self.grain[pom01][pom02] == -2 or self.firstPhase[pom01][pom02] != -1 and licznik < 1000:
                pom01 = random.randint(1, self.x-2)
                pom02 = random.randint(1, self.y-2)
                #print("Powtorzenie numer %s" % (licznik))
                licznik += 1
            if self.grain[pom01][pom02] == -2:
                print ("NALOZENIEQ!!!")
            self.grain[pom01][pom02] = i


    def algorithmCA(self, neighbourhoodType):

        flaga = True


        for i in range(self.x):
            for j in range(self.y):
                self.grainPre[i][j] = self.grain[i][j]

        for i in range (self.x):
            for j in range(self.y):
                if self.grainPre[i][j] == -1 and self.grainPre[i][j] != -2 and self.firstPhase[i][j] == -1:
                    self.grain[i][j] = self.checkNeighbours(i,j)

        self.numberOfFalse = 0
        for i in range (1, self.x-1):
            for j in range(1, self.y-1):
                if self.grain[i][j] == -1:
                    flaga = False
                    self.numberOfFalse += 1


        return flaga


    def checkNeighbours(self, a, b):

        lista = np.zeros(self.n)


        if (a != 0 and a != self.x - 1 and b != 0 and b != self.y - 1):
            if self.grainPre[a - 1][b + 1] != -1 and self.grainPre[a - 1][b + 1] != -2:
                lista[self.grainPre[a - 1][b + 1]] += 1
            if self.grainPre[a][b + 1] != -1 and self.grainPre[a][b + 1] != -2:
                lista[self.grainPre[a][b + 1]] += 1
            if self.grainPre[a + 1][b + 1] != -1 and self.grainPre[a + 1][b + 1] != -2:
                lista[self.grainPre[a + 1][b + 1]] += 1
            if self.grainPre[a - 1][b] != -1 and self.grainPre[a - 1][b] != -2:
                lista[self.grainPre[a - 1][b]] += 1
            if self.grainPre[a+1][b] != -1 and self.grainPre[a+1][b] != -2:
                lista[self.grainPre[a+1][b]] += 1
            if self.grainPre[a - 1][b - 1] != -1 and self.grainPre[a - 1][b - 1] != -2:
                lista[self.grainPre[a - 1][b - 1]] += 1
            if self.grainPre[a][b - 1] != -1 and self.grainPre[a][b - 1] != -2:
                lista[self.grainPre[a][b - 1]] += 1
            if self.grainPre[a + 1][b - 1] != -1 and self.grainPre[a + 1][b - 1] != -2:
                lista[self.grainPre[a + 1][b - 1]] += 1

        max = 0
        wsk = 0
        for i in range (self.n):
            if lista[i] > max:
                max = lista[i]
                wsk = i

        if max != 0:
            return wsk
        else:
            return -1




    def getColour(self, id):

        if id != -1:
            colour = '#%02X%02X%02X' % (self.grainList[id].colourR, self.grainList[id].colourG, self.grainList[id].colourG)
        else:
            colour = "#ffffff"

        return colour



    def selectGrains(self, Ngrains):
        print (Ngrains)

        for i in range(self.n-Ngrains):
            self.grainList[i].flag = -1;
            for m in range(self.x):
                for n in range(self.y):
                    if self.grain[m][n] == i:
                        self.grain[m][n] = -1





    def printMatrix(self, matrix):
        for i in range(self.x):
            for j in range(self.y):
                sys.stdout.write(str(matrix[i, j]) +" ")
            print()







        for i in range(self.x):
            for j in range (self.y):
                pom = np.random.randint(0, self.n)
                self.grain[i][j] = self.grainList[pom].id


    def addInclusion(self, n, type, size):

        pom01 = random.randint(1, self.x - 2)
        pom02 = random.randint(1, self.y - 2)
        licznik = None

        for i in range(n):
            licznik = 0
            while self.grain[pom01][pom02] == -2 and licznik < 100:
                pom01 = random.randint(1, self.x - 2)
                pom02 = random.randint(1, self.y - 2)
                print("Powtorzenie numer %s" % (licznik))
                licznik += 1

            if type == "circual":
                self.grain[pom01][pom02] = -2
                self.grainPre[pom01][pom02] = -2
                for i in range (-size-1, size+1):
                    for j in range (-size-1, size+1):
                        if (pom01+i) > 0 and (pom01+i) < (self.x -1) and (pom02+j) > 0 and (pom02+j) < (self.y-1) \
                                and math.sqrt(i*i + j*j) < size:
                            self.grain[pom01+i][pom02+j] = -2


            elif type == "square":

                self.grain[pom01][pom02] = -2
                self.grainPre[pom01][pom02] = -2
                for i in range (int(-size/2), int(size-(size/2))):
                    for j in range (int(-size/2), int(size-(size/2))):
                        if (pom01+i) > 0 and (pom01+i) < (self.x -1) and (pom02+j) > 0 and (pom02+j) < (self.y-1):
                            self.grain[pom01+i][pom02+j] = -2



        def addInclusion(self, n, type, size):

            pom01 = random.randint(1, self.x - 2)
            pom02 = random.randint(1, self.y - 2)
            licznik = None

            for i in range(n):
                licznik = 0
                while self.grain[pom01][pom02] == -2 and self.checkBorder(pom01, pom02) and licznik < 1000:
                    pom01 = random.randint(1, self.x - 2)
                    pom02 = random.randint(1, self.y - 2)
                    print("Powtorzenie numer %s" % (licznik))
                    licznik += 1

                if type == "circual":
                    self.grain[pom01][pom02] = -2
                    self.grainPre[pom01][pom02] = -2
                    for i in range(-size - 1, size + 1):
                        for j in range(-size - 1, size + 1):
                            if (pom01 + i) > 0 and (pom01 + i) < (self.x - 1) and (pom02 + j) > 0 and (pom02 + j) < (self.y - 1) \
                                    and math.sqrt(i * i + j * j) < size:
                                self.grain[pom01 + i][pom02 + j] = -2


                elif type == "square":

                    self.grain[pom01][pom02] = -2
                    self.grainPre[pom01][pom02] = -2
                    for i in range(int(-size / 2), int(size - (size / 2))):
                        for j in range(int(-size / 2), int(size - (size / 2))):
                            if (pom01 + i) > 0 and (pom01 + i) < (self.x - 1) and (pom02 + j) > 0 and (pom02 + j) < (self.y - 1):
                                self.grain[pom01 + i][pom02 + j] = -2


    def findBorders(self):
        for i in range (1, self.x -1):
            for j in range(1, self.y -1):
                if self.checkBorder(i,j):
                    self.grain[i][j] = -2
                    print("wejscie do petli")


    def checkBorder(self, pom01, pom02):

        pom = -1;

        licznik =0
        for i in range (-1,2):
            for j in range (-1,2):
                if (self.grain[pom01+i][pom02+j] >= 0) and (self.grain[pom01+i][pom02+j] < self.n):
                    licznik += 1
                    if pom != -1 and pom != self.grain[pom01+i][pom02+j]:
                        print(licznik)
                        return True
                    pom = self.grain[pom01+i][pom02+j]


        return False