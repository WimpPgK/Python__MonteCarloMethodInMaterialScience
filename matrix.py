import numpy as np
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import *
import grain
import time
import random

class Matrix:



    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n
        self.grain = np.zeros((x, y), dtype=int)
        self.grainList = np.empty(n, dtype=grain.Grain)
        self.grainEnergy = np.zeros((x, y), dtype=float)
        #self.idList = np.random.choice (0, 21478347, n)



        # wektoryzacja _init_ w klasie Grain w celu utworzenia macierzy obiektow
        vSite = np.vectorize(grain.Grain)
        init_vector = np.arange(n).reshape((n))

        self.grainList[:] = vSite(init_vector)


    def printIdList(self):
        for m in range(self.x):
            for n in range(self.y):
                print(self.grain[m][n])






    def selectGrains(self, Ngrains):
        print (Ngrains)

        for i in range(self.n-Ngrains):
            self.grainList[i].flag = -1;
            for m in range(self.x):
                for n in range(self.y):
                    if self.grain[m][n] == i:
                        self.grain[m][n] = -1





    def printMatrix(self):
        for i in range(self.x):
            for j in range(self.y):
                sys.stdout.write(str(self.grain[i, j]) +" ")
            print()



    def createGrains(self):
        for i in range (self.n):
            randomNB = np.random.randint(20, 220);
            self.grainList[i].id = i;
            self.grainList[i].colourG = np.random.randint(0, 256);
            time.sleep(.001)
            self.grainList[i].colourB = np.random.randint(0, 256);
            time.sleep(.001)
            self.grainList[i].colourR = np.random.randint(0, 256);




        for i in range(self.x):
            for j in range (self.y):
                pom = np.random.randint(0, self.n)
                self.grain[i][j] = self.grainList[pom].id


    #####################################################################

    def monteCarloIteratio(self):
        for i in range (self.x*self.y):
            pom_x = np.random.randint(0, self.x)
            pom_y = np.random.randint(0, self.y)

            if self.grainList[self.grain[pom_x][pom_y]].flag != -1: #jezeli ziarno uczestniczy w procesie
                pomId01 = self.grain[pom_x][pom_y]
                energy01 = self.neighbourhood(1, pom_x, pom_y)
                pomN = np.random.randint(0,self.n)
                self.grain[pom_x][pom_y] = self.grainList[pomN].id
                energy02 = self.neighbourhood(1, pom_x, pom_y)


                if energy02>=energy01:
                    self.grain[pom_x][pom_y] = pomId01


    def neighbourhood(self, param, a,b):

        energy = 8;
        if(a!=0 and a!= self.x-1 and b!=0 and b!=self.y-1):

            if param==1:
                energy = 8
                if self.grain[a-1][b+1] == self.grain[a][b]:
                    energy -= 1
                if self.grain[a][b+1] == self.grain[a][b]:
                    energy -= 1
                if self.grain[a+1][b+1]== self.grain[a][b]:
                    energy -= 1
                if self.grain[a - 1][b]== self.grain[a][b]:
                    energy -= 1
                if self.grain[a + 1][b]== self.grain[a][b]:
                    energy -= 1
                if self.grain[a - 1][b-1]== self.grain[a][b]:
                    energy -= 1
                if self.grain[a][b-1] == self.grain[a][b]:
                    energy -= 1
                if self.grain[a + 1][b-1]== self.grain[a][b]:
                    energy -= 1

        return energy


    def getColour(self, id):
        colour = '#%02X%02X%02X' % (self.grainList[id].colourR, self.grainList[id].colourG, self.grainList[id].colourG)
        return colour
