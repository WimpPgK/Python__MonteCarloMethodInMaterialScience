import random
import numpy as np

class energy02:


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grainEnergy = np.zeros((x, y), dtype=float)


    def calculateEnergyHomogenous(self, energy):
        for m in range(self.x):
            for n in range(self.y):
                pom = random.random() / 10 - 0.05

                self.grainEnergy[m][n] = energy + energy * pom
                # print(self.grainEnergy[m][n])


    def calculateEnergyHeterogenous(self, matrix, nergyInside, energyOnEdge):
        for m in range(0,self.x):
            for n in range(0,self.y):

                #pom = float(random.random())
                #if(pom > 0.8):
                #    self.grainEnergy[m][n] = 240
                #else:
                #     self.grainEnergy[m][n] = 1

                test = self.neighbourhood(m, n, matrix)
                if (test == 0):
                    pom = random.random() / 10 - 0.05
                    self.grainEnergy[m][n] = nergyInside + nergyInside * pom
                    #self.grainEnergy[m][n] = 250




                else:
                    pom = random.random() / 10 - 0.05
                    self.grainEnergy[m][n] = energyOnEdge + energyOnEdge * pom
                    #self.grainEnergy[m][n] = 0



                    #print("Granica")


    def neighbourhood(self, a,b, matrix):

        energy = 8;
        if(a!=0 and a!= self.x-1 and b!=0 and b!=self.y-1):

                energy = 8
                if matrix[a-1][b+1] == matrix[a][b]:
                    energy -= 1
                if matrix[a][b+1] == matrix[a][b]:
                    energy -= 1
                if matrix[a+1][b+1]== matrix[a][b]:
                    energy -= 1
                if matrix[a - 1][b]== matrix[a][b]:
                    energy -= 1
                if matrix[a + 1][b]== matrix[a][b]:
                    energy -= 1
                if matrix[a - 1][b-1]== matrix[a][b]:
                    energy -= 1
                if matrix[a][b-1] == matrix[a][b]:
                    energy -= 1
                if matrix[a + 1][b-1]== matrix[a][b]:
                    energy -= 1


        return energy