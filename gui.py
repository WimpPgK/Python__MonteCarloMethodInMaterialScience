
import tkinter as tk
from tkinter import simpledialog
import matrix
import CA_matrix
import energy
from tkinter import ttk
from tkinter import *
import numpy as np
import energy02


import time

class Gui:

    def guiInit(self):


        window = tk.Tk()
        window.state('zoomed')
        xDimention = IntVar()
        yDimention = IntVar()
        amountOfGrains = IntVar()
        MCS = IntVar()
        numberGrainSelect = IntVar()
        secondGrainGrowth = StringVar()
        energyDistribution = StringVar()
        energyInside = IntVar();
        energyOnEdge = IntVar();


        xDimention.set(130)
        yDimention.set(130)
        amountOfGrains.set(3)
        MCS.set(10)
        numberGrainSelect.set(1)
        energyInside.set(4)
        energyOnEdge.set(7)

        self.size_x_canvas = int(window.winfo_screenwidth()*0.84)
        self.size_y_canvas = int(window.winfo_screenheight()*0.91)

        # generate dwawing space
        canvas = tk.Canvas(window, width=self.size_x_canvas, height=self.size_y_canvas, bg="blue")
        canvas.grid(row=0, column=4, rowspan=70,
                    columnspan=5)  # plansza do rysowania bedzie zajmowac 100 wierszy i 4 kolumny

        ################# GUI of space generation ##########################

        label_xDimention = ttk.Label(window, text="X space dimention").grid(column=0, row=0, sticky=E)
        label_yDimention = ttk.Label(window, text="Y space dimention").grid(column=0, row=1, sticky=E)
        label_amountOfGrain = ttk.Label(window, text="Amount of grain").grid(column=0, row=2, sticky=E)
        label_MCS = ttk.Label(window, text="MCS").grid(column=0, row=9, sticky=E)
        label_numberGrainSelect = ttk.Label(window, text="Number of grain to select").grid(column=0, row=12, sticky=E)
        label_secondGrainGrowth = ttk.Label(window, text="Second grain growth").grid(column=0, row=15, sticky=E)
        label_energyDistribution = ttk.Label(window, text="Energy distribution").grid(column=0, row=17, sticky=E)
        label_energyInside = ttk.Label(window, text="Energy inside").grid(column=0, row=18, sticky=E);
        label_energyOnEdge = ttk.Label(window, text="Energy on edge").grid(column=0, row=19, sticky=E);

        entry_xDimention = ttk.Entry(window, textvariable=xDimention).grid(column=1, row=0)
        entry_yDimention = ttk.Entry(window, textvariable=yDimention).grid(column=1, row=1)
        entry_amountOfGrain = ttk.Entry(window, textvariable=amountOfGrains).grid(column=1, row=2)
        entry_MCS = ttk.Entry(window, textvariable=MCS).grid(column=1, row=9)
        entry_numberGrainSelect = ttk.Entry(window, textvariable=numberGrainSelect).grid(column=1, row=12)
        entry_energyInside= ttk.Entry(window, textvariable=energyInside).grid(column=1, row=18)
        entry_energyOnEdge = ttk.Entry(window, textvariable=energyOnEdge).grid(column=1, row=19)


        entry_amountOfGrain = ttk.Button(window, text="Generate space",
                                         command=lambda: self.generateSpace(xDimention.get(), yDimention.get(), amountOfGrains.get(), canvas)
                                         ).grid(column=0, columnspan=2, row=3)  #uzywamy funkcji lambda do wywolania docelowej funkcji obslugi kilkniecia

        button_startMCS = ttk.Button(window, text="DO IT",
                                         command=lambda: self.MCSiteration(self.m, xDimention.get(), yDimention.get(),
                                                                            amountOfGrains.get(), canvas, MCS.get())
                                         ).grid(column=0, columnspan=2,
                                                row=10)  # uzywamy funkcji lambda do wywolania docelowej funkcji obslugi kilkniecia

        button_grainSelect = ttk.Button(window, text="Clear space",
                                    command=lambda: self.grainSelect(xDimention.get(), yDimention.get(),
                                                                      amountOfGrains.get(), canvas, numberGrainSelect.get())
                                    ).grid(column=0, columnspan=2,
                                           row=13)  # uzywamy funkcji lambda do wywolania docelowej funkcji obslugi kilkniecia

        button_recrystallization = ttk.Button(window, text="Start dual phase",
                                         command=lambda: self.recrystallization(amountOfGrains.get(), canvas, MCS.get(), secondGrainGrowth.get())
                                         ).grid(column=0, columnspan=2,row=16)  # uzywamy funkcji lambda do wywolania docelowej funkcji obslugi kilkniecia

        button_showEnergy = ttk.Button(window, text="Show energy distribution",
                                             command=lambda: self.energyDistribution(canvas, energyDistribution.get(), energyInside.get(), energyOnEdge.get())
                                             ).grid(column=0, columnspan=2,
                                                    row=20)  # uzywamy funkcji lambda do wywolania docelowej funkcji obslugi kilkniecia



        combobox_secondGrainGrowth = ttk.Combobox(window, textvariable=secondGrainGrowth,
                                                    state='readonly')  # nie mozna wpisac wlasnej liczby zamiast tych do wybrania
        combobox_secondGrainGrowth['values'] = ("Monte Carlo", "Cellular Automata")
        combobox_secondGrainGrowth.grid(column=1, row=15)
        combobox_secondGrainGrowth.current(0)


        combobox_energyDistribution = ttk.Combobox(window, textvariable=energyDistribution,
                                                    state='readonly')  # nie mozna wpisac wlasnej liczby zamiast tych do wybrania
        combobox_energyDistribution['values'] = ("Homogenious", "Heterogenous")
        combobox_energyDistribution.grid(column=1, row=17)
        combobox_energyDistribution.current(0)

        ############# end of space generation ##############################



        #####################  FRAGMEMT DO TESTOWANIA  #########################


        self.generateSpace(xDimention.get(), yDimention.get(), amountOfGrains.get(), canvas)




        window.mainloop()




##############################################################################################
    def energyDistribution(self, canvas, energyDistribution, energyInside, energyOnEdge):

        #for i in range(self.x):
           #for j in range(self.y):
                #print(self.grain[i][j])


        self.e1 = energy02.energy02(self.x, self.y)

        if energyDistribution == "Homogenious":

            self.e1.calculateEnergyHomogenous(energyInside)
            self.showImageEnergy(self.x, self.y, 1, canvas, "homogenous",energyInside, energyOnEdge )
            print()


        elif energyDistribution == "Heterogenous":
            self.e1.calculateEnergyHeterogenous(self.grain, energyInside,energyOnEdge)
            self.showImageEnergy( self.x, self.y, 1, canvas, "heterogenous", energyInside, energyOnEdge)


    def recrystallization(self, amountOfGrains, canvas, MCS, secondGrainGrowth):


        if secondGrainGrowth == "Monte Carlo":
            self.m02 = matrix.Matrix(self.x, self.y, amountOfGrains)  # wymiary planszys, liczba ziarn
            self.m02.createGrains()  # utworzenie ziarn o zadanej ilosci ronych id
            self.RecIteration(self.m02, self.x, self.y, amountOfGrains, canvas, MCS)
            for i in range(self.x):
                for j in range(self.y):
                    self.grain[i][j] = self.m02.grain[i][j]
            self.showImage(self.m, self.x, self.y, amountOfGrains, canvas, "recrystallization")






        elif secondGrainGrowth == "Cellular Automata":

            #print("CELLULAR AUTPMATA")
            s = simpledialog.askinteger("", "Amount of grains")
            self.m02 = CA_matrix.Matrix(self.x, self.y, s)
            self.m02.createGrains(self.m.grain)
            self.m02.randomizeGrainPosition()
            self.showImage(self.m02, self.x, self.y, amountOfGrains, canvas, "recrystallization")

            self.m02.algorithmCA("ToDo")
            while True:
                pom = self.m02.numberOfFalse
                flaga = self.m02.algorithmCA("ToDo")
                self.showImage(self.m02, self.x, self.y, amountOfGrains, canvas, "recrystallization")
                if flaga:
                    break
                if(pom == self.m02.numberOfFalse):
                    break

            self.showImage(self.m02, self.x, self.y, amountOfGrains, canvas, "recrystallization")

            for i in range (self.x):
                for j in range (self.y):
                    #print(self.m02.grain[i][j])
                    if(self.m02.grain[i][j] == -1):
                        self.grain[i][j] = 99991
                    else:
                        self.grain[i][j] = 7000 + self.m02.grain[i][j]



    def grainSelect(self,  x,y,n, canvas, Ngrains):
        self.m.selectGrains(Ngrains)
        self.showImage(self.m, x, y, n, canvas, "white")






    def MCSiteration(self,matrix, x,y,n, canvas, MCS):

        for i in range (MCS):
            matrix.monteCarloIteratio()
            #time.sleep(.5)
            #self.showImage(matrix, x, y, n, canvas, "") wyswietlanie po kazdej iteracji
        self.showImage(matrix, x, y, n, canvas, "")
        for k in range(self.x):
            for j in range(self.y):
                self.grain[k][j] = matrix.grain[k][j]





    def RecIteration(self,matrix, x,y,n, canvas, MCS):

        for i in range (MCS):
            matrix.monteCarloIteratio()
            self.showImage(self.m, self.x, self.y, n, canvas, "recrystallization")

    def generateSpace(self, x,y,n, canvas):


        self.m = matrix.Matrix(x, y, n)  # wymiary planszys, liczba ziarn
        self.m.createGrains()  # utworzenie ziarn o zadanej ilosci ronych id
        self.showImage(self.m ,x, y, n, canvas, "")
        self.grain = np.zeros((x, y), dtype=int)


    def showImage(self, matrix, x, y, n, canvas, flag):

        canvas.delete("all")
        self.x = x
        self.y = y
        x_size = self.size_x_canvas / (x -2)
        y_size = self.size_y_canvas / (y-2)
        x_pointer = 1
        y_pointer = 1

        if flag =="":
            for i in range(1, self.size_x_canvas, int(x_size+1)):
                for j in range(1, self.size_y_canvas, int(y_size+1)):
                    kolor = matrix.getColour(matrix.grain[x_pointer][y_pointer])
                    canvas.create_rectangle(i, j, i + x_size+1, j + y_size+1, fill=kolor, outline="")
                    y_pointer += 1
                x_pointer += 1
                y_pointer = 1


        elif flag =="white":
            for i in range(1, self.size_x_canvas, int(x_size+1)):
                for j in range(1, self.size_y_canvas, int(y_size+1)):
                    if(matrix.grain[x_pointer][y_pointer] == -1):
                        kolor = "#ffffff"
                        canvas.create_rectangle(i, j, i + x_size + 1, j + y_size + 1, fill=kolor, outline="")
                    else:
                        #kolor = matrix.getColour(matrix.grain[x_pointer][y_pointer])
                        kolor = 'black'
                        canvas.create_rectangle(i, j, i + x_size+1, j + y_size+1, fill=kolor, outline="")
                    y_pointer += 1
                x_pointer += 1
                y_pointer = 1

        elif flag == "recrystallization":
            for i in range(0, self.size_x_canvas, int(x_size+1)):
                for j in range(0, self.size_y_canvas, int(y_size+1)):
                    if self.m.grain[x_pointer][y_pointer] == -1:
                        kolor = self.m02.getColour(self.m02.grain[x_pointer][y_pointer])

                        canvas.create_rectangle(i, j, i + x_size + 1, j + y_size + 1, fill=kolor, outline="")

                    else:
                        #kolor = self.m.getColour(self.m.grain[x_pointer][y_pointer])
                        self.grain[x_pointer][y_pointer] = 99991
                        kolor = 'black'
                        canvas.create_rectangle(i, j, i + x_size+1, j + y_size+1, fill=kolor, outline="")
                    y_pointer += 1
                x_pointer += 1
                y_pointer = 1


        canvas.update()

    def showImageEnergy(self, x, y, n, canvas, flag, energyInside, energyOnEdge):
        canvas.delete("all")
        self.x = x
        self.y = y
        x_size = self.size_x_canvas / (x -1)
        y_size = self.size_y_canvas / (y-1)
        x_pointer = 1
        y_pointer = 1
        #print("KOKOWA01")
        if flag=="homogenous":
            #print("GOWNO")
            for i in range(0, self.size_x_canvas, int(x_size+1)):
                for j in range(0, self.size_y_canvas, int(y_size+1)):

                    min = energyInside - energyInside*0.1;
                    max = energyInside + energyInside*0.1;
                    mappedEnergy = 100+(self.e1.grainEnergy[x_pointer][y_pointer] - min)/(max-min)*50

                    kolor = '#%02X%02X%02X' % (int(mappedEnergy) , int(mappedEnergy) ,int(mappedEnergy) )

                    canvas.create_rectangle(i, j, i + x_size + 1, j + y_size + 1, fill=kolor, outline="")


                    y_pointer += 1
                x_pointer += 1
                y_pointer = 1
        else:
            x_pointer = 1
            y_pointer = 1
            #("KOKOWA02")
            for i in range(0, self.size_x_canvas, int(x_size + 1)):
                for j in range(0, self.size_y_canvas, int(y_size + 1)):
                    min = energyInside - energyInside * 0.1;
                    max = energyOnEdge + energyOnEdge * 0.1;
                    mappedEnergy = 150 - (self.e1.grainEnergy[x_pointer][y_pointer] - min) / (max - min) * 100

                    #mappedEnergy = self.e1.grainEnergy[x_pointer][y_pointer]
                    #print(self.e1.grainEnergy[x_pointer][y_pointer])
                    kolor = '#%02X%02X%02X' % (int(mappedEnergy), int(mappedEnergy), int(mappedEnergy))
                    #print(kolor)
                    canvas.create_rectangle(i, j, i + x_size + 1, j + y_size + 1, fill=kolor, outline="")

                    y_pointer += 1
                    print(y_pointer)
                x_pointer += 1
                y_pointer = 1


