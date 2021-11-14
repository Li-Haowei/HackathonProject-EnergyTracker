from tkinter import *
import numpy as np

from matplotlib import *
import matplotlib.pyplot as plt
from dataBase import dataBase
from Time import Time
from Course import Course
from Calculation import Calculation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


window = Tk()
window.title("Energy Tracker")
#window.geometry("1000x1000")
#window.attributes('-fullscreen',True)
window.state('zoomed')
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
          if (int(c.el[i][1]) + int(c.el[i][2]) + int(c.el[i][3]))/3 not in dic.keys():
               dic[(int(c.el[i][1]) + int(c.el[i][2]) + int(c.el[i][3])/3)] = [str(c.el[i][0])]
          else:
               dic[(int(c.el[i][1]) + int(c.el[i][2]) + int(c.el[i][3])/3)].append(str(c.el[i][0]))
     return dic

determine = [
          [10,14,"Bear", "Much like its namesake, the bear chronotype follows "+
           "the solar cycle, and usually doesn’t have much trouble waking up in "+
           "the morning or falling asleep at night. This chronotype is most "+
           "productive in the morning, and will typically struggle with an "+
           "afternoon slump after lunch, generally around 2–4 p.m. Eight hours "
           +"of sleep is typical for a bear, and normal sleep hours are "+
           "usually between 11 p.m. and 7 a.m.",
           "7–8 a.m.: Wake up\n"+
          "10 a.m.–2 p.m.: Focus on deep work\n"+
          "2–4 p.m.: Work on lighter tasks\n"+
          "4–10 p.m.: Relax and unwind\n"+
          "10–11 p.m.: Get ready for bed\n"+
          "11 p.m.–7 a.m.: Sleep\n"],
          [17,23,"Wolf",
           "Just like their real life counterparts, wolf \n"+
           "chronotypes are most productive at night. The wolf \n"+
           "needs more time to hit snooze in the morning to get all \n"+
           "the energy they need to sustain their two bursts of creative \n"+
           "energy: the first around noon, and the second coming around 6 p.m. \n"+
           "when most others have finished their work for the day. \n"+
           "Similar to what is considered a night owl, this chronotype \n"+
           "doesn’t get going until the sun sets, and they may have difficulty \n"+
           "waking when it comes back up. Wolves are often happy to go to bed \n"+
           "at midnight, or well past it, to help fuel their creativity.\n",
           "7:30–9 a.m.: Wake up\n"+
          "10 a.m.–12 p.m.: Focus on lighter tasks\n"+
          "12–2 p.m.: Complete deep or creative work\n"+
          "2–5 p.m.: Focus on lighter, less intense tasks\n"+
          "5–9 p.m.: Engage in creative tasks\n"+
          "9–10 p.m.: Unwind from the day\n"+
          "10 p.m.–12 a.m.: Prepare for bed\n"+
          "12–7:30 a.m.: Sleep\n"
          ],
          [8,12,"Lion","The early lion gets the worm. This chronotype feels "+
           "most alive in the morning with energy levels peaking before noon, "+
           "and is typically able to complete massive amounts of work before"+
           "lunch. Waking up early is a breeze for lions and everything tends "+
           "to run smoothly until midday. Just as fast as energy for a lion "+
           "is gained, it’s lost. The afternoon slump hits this group hard, "+
           "often needing a power nap to recharge, and by the evening they "+
           "feel drained. It’s important for lions to have an evening wind-down "+
           "routine to help them decompress from the day, before calling it an "+
           "early night around 10 p.m. Lions generally need around eight hours "+
           "of sleep per night to sustain their high energy levels in the early morning",
           "6–7 a.m.: Wake up\n"+
          "8 a.m.–12 p.m.: Focus on deep work\n"+
          "12–4 p.m.: Focus on lighter tasks\n"+
          "4–9 p.m.: Daily unwind and relax\n"+
          "9–10 p.m.: Get ready for bed\n"+
          "10 p.m. – 6 a.m.: Sleep\n"],
          [15,21,"Dolphin","The insomniac of the water, actual dolphins sleep with "+
           "half of their brain on at a time — this helps them stay alert and aware "+
           "of predators. Dolphins have a hard time waking up in the morning, but "+
           "once they get going, their productivity reaches its peak around mid-morning. "+
           "Similar to their nocturnal counterpart, there is always underlying tiredness "+
           "for dolphins due to their anxious sleeping behaviors — including having "+
           "a hard time falling asleep each night and rarely getting a full night of "+
           "sleep. Dolphin chronotypes will usually fall asleep because their body "+
           "needs to, not because they willingly give in to sleep. Because of their "+
           "sporadic sleeping habits, it’s recommended they sleep from about midnight to 6 a.m."
           ,
           "6:30–7:30 a.m.: Wake up\n"+
           "8–10 a.m.: Engage with easy to-dos\n"+
          "10 a.m.–12 p.m.: Focus on demanding tasks\n"+
          "12–4 p.m.: Complete less demanding tasks\n"+
          "4–10 p.m.: Relax, unwind from the day\n"+
          "10–11:30 p.m.: Prepare for bed\n"+
          "12–6:30 a.m.: Sleep\n"]
          ]
import tkinter.font as tkFont
fontStyle20 = tkFont.Font(family="Lucida Grande", size=20)
fontStyle11 = tkFont.Font(family="Lucida Grande", size=11)
def whatAreU():
     dic = calculation()
     listOfKeys = list(dic.keys())
     listOfKeys.sort()
     peak = dic[listOfKeys[-1]][0]
     peak = peak.split(" ")[1]
     peak = peak.split(":")[0]
     for i in determine:
          if i[0]<int(peak) and int(peak)<i[1]:
               #animal
               myLabel1 = Label(window,text=(i[2]+" "),font=fontStyle20,bg="pink")
               myLabel1.grid(row=0,column=9,columnspan=3)
               #description
               myLabel2 = Label(window,text=i[3],font=fontStyle11,bg="green")
               myLabel2.grid(row=1,column=9,columnspan=3,rowspan=3)
               #schedule
               myLabel3 = Label(window,text=i[4],font=fontStyle11,bg="grey")
               myLabel3.grid(row=4,column=9,columnspan=3,rowspan=3)
               return
     myLabel1 = Label(window,text="No fit ",font=fontStyle20,bg="pink")
     myLabel1.grid(row=0,column=9,columnspan=3)
     return
def clearData():
     d.delEmotionDataBase()
     d.delAssignmentDataBase()
     
button7 = Button(window, text="What are you", borderwidth=10, padx = 20, pady = 10, bg="white", command=lambda: whatAreU())
button7.grid(row=6,column=6) 

button8 = Button(window, text="Wipe All Records", borderwidth=10, padx = 20, pady = 10, bg="white", command=lambda: clearData())
button8.grid(row=7,column=6) 



    
window.mainloop() 
