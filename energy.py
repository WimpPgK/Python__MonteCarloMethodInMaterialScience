import numpy as np

def Energy(x, y):
    energia = np.zeros((x, y), dtype=int)


def findBorders(matrix01, matrix02, c, n):

    energia = matrix01
    #energia = np.zeros((x, y), dtype=int)


    for i in range(1, x - 1):
        for j in range(1, y - 1):
            if checkBorder(energia, i, j, n):
                energia[i][j] = -2
                print("wejscie do petli")


def checkBorder(grain, pom01, pom02):
    pom = -1;

    licznik = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (grain[pom01 + i][pom02 + j] >= 0) and (grain[pom01 + i][pom02 + j] < self.n):
                licznik += 1
                if pom != -1 and pom != grain[pom01 + i][pom02 + j]:
                    print(licznik)
                    return True
                pom = grain[pom01 + i][pom02 + j]

    return False