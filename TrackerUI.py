from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from dataBase import dataBase
from Time import Time
from Course import Course
from Calculation import Calculation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


window = Tk()
window.title("Energy Tracker")
window.geometry("1000x1000")
d = dataBase() # this is the dataBase


e1 = Entry(window, width=20, borderwidth=10)
e1.grid(row=0,column=1,columnspan=1, padx=0,pady=40)
e1.insert(0,"Day/Month/Year")


e2 = Entry(window, width=20, borderwidth=10)
e2.grid(row=0,column=2,columnspan=1, padx=0,pady=40)
e2.insert(0,"Hours:Minutes")


e3 = Entry(window, width=20, borderwidth=10)
e3.grid(row=0,column=3,columnspan=1, padx=0,pady=40)
e3.insert(0,"Emotion Level")

e4 = Entry(window, width=20, borderwidth=10)
e4.grid(row=0,column=4,columnspan=1, padx=0,pady=40)
e4.insert(0,"Energy Level")

e5 = Entry(window, width=20, borderwidth=10)
e5.grid(row=0,column=5,columnspan=1, padx=0,pady=40)
e5.insert(0,"Focus Level")

     
     
def save1():
     d.addEmotion(e1.get()+" "+e2.get(), e3.get(), e4.get(), e5.get())
     e1.delete(0,END)
     e2.delete(0,END)
     e3.delete(0,END)
     e4.delete(0,END)
     e5.delete(0,END)
     e1.insert(0,"Day/Month/Year")
     e2.insert(0,"Hours:Minutes")
     e3.insert(0,"Emotion Level")
     e4.insert(0,"Energy Level")
     e5.insert(0,"Focus Level")
     return  

e6 = Entry(window, width=20, borderwidth=10)
e6.grid(row=1,column=1,columnspan=1, padx=0,pady=40)
e6.insert(0,"Day/Month/Year")


e7 = Entry(window, width=20, borderwidth=10)
e7.grid(row=1,column=2,columnspan=1, padx=0,pady=40)
e7.insert(0,"Hours:Minutes")


e8 = Entry(window, width=20, borderwidth=10)
e8.grid(row=1,column=3,columnspan=1, padx=0,pady=40)
e8.insert(0,"Course")

e9 = Entry(window, width=20, borderwidth=10)
e9.grid(row=1,column=4,columnspan=1, padx=0,pady=40)
e9.insert(0,"Percentage")

e10 = Entry(window, width=20, borderwidth=10)
e10.grid(row=1,column=5,columnspan=1, padx=0,pady=40)
e10.insert(0,"Finished")

def save2():
     d.addAssignment(e6.get()+" "+e7.get(), e8.get(), e9.get(), e10.get())
     e6.delete(0,END)
     e7.delete(0,END)
     e8.delete(0,END)
     e8.delete(0,END)
     e10.delete(0,END)
     e6.insert(0,"Day/Month/Year")
     e7.insert(0,"Hours:Minutes")
     e8.insert(0,"Course")
     e9.insert(0,"Percentage")
     e10.insert(0,"Finished")
     return  

def plotEmotion():
     c = Calculation()
     x=[]
     y=[]
     fig = Figure(figsize = (5, 3),dpi = 100)
     for i in range(len(c.el)):
          x.append(c.el[i][0])
          y.append(c.el[i][1])
     plot1 = fig.add_subplot(111)
     plot1.plot(x,y)
     canvas = FigureCanvasTkAgg(fig,master = window)  
     canvas.draw()
     canvas.get_tk_widget().grid(row=3,column=1,columnspan=4, rowspan=4) 
     toolbar = NavigationToolbar2Tk(canvas,window)
     toolbar.update() 
def plotEnergy():
     c = Calculation()
     x=[]
     y=[]
     fig = Figure(figsize = (5, 3),dpi = 100)
     for i in range(len(c.el)):
          x.append(c.el[i][0])
          y.append(c.el[i][2])
     plot1 = fig.add_subplot(111)
     plot1.plot(x,y)
     canvas = FigureCanvasTkAgg(fig,master = window)  
     canvas.draw()
     canvas.get_tk_widget().grid(row=3,column=1,columnspan=4, rowspan=4) 
     toolbar = NavigationToolbar2Tk(canvas,window)
     toolbar.update() 
def plotFocus():
     c = Calculation()
     x=[]
     y=[]
     fig = Figure(figsize = (5, 3),dpi = 100)
     for i in range(len(c.el)):
          x.append(c.el[i][0])
          y.append(c.el[i][3])
     plot1 = fig.add_subplot(111)
     plot1.plot(x,y)
     canvas = FigureCanvasTkAgg(fig,master = window)  
     canvas.draw()
     canvas.get_tk_widget().grid(row=3,column=1,columnspan=4, rowspan=4) 
     toolbar = NavigationToolbar2Tk(canvas,window)
     toolbar.update() 
     
def plotHybre():
     c = Calculation()
     x=[]
     y1=[]
     y2=[]
     y3=[]
     fig = Figure(figsize = (5, 3),dpi = 100)
     for i in range(len(c.el)):
          x.append(c.el[i][0])
          y1.append(c.el[i][1])
          y2.append(c.el[i][2])
          y3.append(c.el[i][3])
     plot1 = fig.add_subplot(111)
     plot1.plot(x,y1, color ="red",label="Emotion")
     plot2 = fig.add_subplot(111)
     plot2.plot(x,y2, color ="green",label="Energy")
     plot3 = fig.add_subplot(111)
     plot3.plot(x,y3, color ="blue",label="Focus")
     canvas = FigureCanvasTkAgg(fig,master = window)  
     canvas.draw()
     canvas.get_tk_widget().grid(row=3,column=1,columnspan=4, rowspan=4) 
     toolbar = NavigationToolbar2Tk(canvas,window)
     toolbar.update() 
     
button1 = Button(window, text="Store Your Mental Status", borderwidth=10, padx = 20, pady = 10, bg="white", command=lambda: save1())
button1.grid(row=0,column=6) 
button2 = Button(window, text="Store Assignment Information", borderwidth=10, padx = 20, pady = 10, bg="white", command=lambda: save2())
button2.grid(row=1,column=6) 
button3 = Button(window, text="Plot Emotion Graph", borderwidth=10, padx = 20, pady = 10, bg="white", command=lambda: plotEmotion())
button3.grid(row=2,column=6) 
button4 = Button(window, text="Plot Energy Graph", borderwidth=10, padx = 20, pady = 10, bg="white", command=lambda: plotEnergy())
button4.grid(row=3,column=6) 
button5 = Button(window, text="Plot Focus Graph", borderwidth=10, padx = 20, pady = 10, bg="white", command=lambda: plotFocus())
button5.grid(row=4,column=6) 
button6 = Button(window, text="Plot Hybre Graph", borderwidth=10, padx = 20, pady = 10, bg="white", command=lambda: plotHybre())
button6.grid(row=5,column=6) 
    
def calculation():
     c = Calculation()
     dic = {}
     for i in range(len(c.el)):
          if (c.el[i][1] + c.el[i][2] + c.el[i][3])/3 not in dic.keys():
               dic[(int(c.el[i][1]) + int(c.el[i][2]) + int(c.el[i][3])/3)] = [str(c.el[i][0])]
          else:
               dic[(int(c.el[i][1]) + int(c.el[i][2]) + int(c.el[i][3])/3)].append(str(c.el[i][0]))
     return dic

determine = [[10,14,"Bear"],[17,23,"Wolf"],[8,12,"Lion"],[15,21,"Dolphin"]]
def whatAreU():
     dic = calculation()
     listOfKeys = list(dic.keys())
     listOfKeys.sort()
     peak = dic[listOfKeys[-1]][0]
     peak = peak.split(" ")[1]
     peak = peak.split(":")[0]
     
     for i in determine:
          if i[0]<peak and peak>i[1]:
               myLabel1 = Label(window,text=i[2])
               myLabel1.grid(8,1)
     myLabel1 = Label(window,text="No fit")
     
def clearData():
     d.delEmotionDataBase()
     d.delAssignmentDataBase()
     
button7 = Button(window, text="What are you", borderwidth=10, padx = 20, pady = 10, bg="white", command=lambda: whatAreU())
button7.grid(row=6,column=6) 

button8 = Button(window, text="Wipe All Records", borderwidth=10, padx = 20, pady = 10, bg="white", command=lambda: clearData())
button8.grid(row=7,column=6) 
    
window.mainloop() 
