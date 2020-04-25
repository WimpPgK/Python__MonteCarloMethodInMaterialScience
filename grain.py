import numpy as np

class Grain:
    def __init__(self, a):
        self.id = -1;
        self.colourR = 1
        self.colourG = 1
        self.colourB = 1
        self.flag = 0

    def __str__(self):
        wynik = "Id:%s     kolor:%s"% (self.id ,self.color)
        return wynik


