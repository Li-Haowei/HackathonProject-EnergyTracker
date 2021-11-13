# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 17:13:49 2021

@author: Haowei Li
"""
# importing the modules
import numpy as np
import matplotlib.pyplot as plt
from dataBase import dataBase
from Time import Time
from Course import Course

class Calculation:
     def __init__(self):
          self.database = dataBase()
          self.el = self.database.getEmotion
          self.al = self.database.getAssignment
     
     #def sortByTime(self):
     
     def plotEmotion(self):
          """plot emotion level with time"""
          x = []
          y = []
          for i in range(len(self.el)):
               x.append(self.el[i][0])
               y.append(self.el[i][1])
          #plotting
          plt.title("Emotion Level")
          plt.xlabel("date")
          plt.ylabel("level")
          plt.plot(x, y, color ="red")
          plt.show()
     def plotEnergy(self):
          """plot emotion level with time"""
          x = []
          y = []
          for i in range(len(self.el)):
               x.append(self.el[i][0])
               y.append(self.el[i][2])
          #plotting
          plt.title("Energy Level")
          plt.xlabel("date")
          plt.ylabel("level")
          plt.plot(x, y, color ="green")
          plt.show()
     def plotFocus(self):
          """plot emotion level with time"""
          x = []
          y = []
          for i in range(len(self.el)):
               x.append(self.el[i][0])
               y.append(self.el[i][3])
          #plotting
          plt.title("Focus Level")
          plt.xlabel("date")
          plt.ylabel("level")
          plt.plot(x, y, color ="blue")
          plt.show()
     def plotEmotionHybre(self):
          x = []
          y1 = []
          y2 = []
          y3 = []
          for i in range(len(self.el)):
               x.append(self.el[i][0])
               y1.append(self.el[i][1])
               y2.append(self.el[i][2])
               y3.append(self.el[i][3])
          #plotting
          plt.title("Level")
          plt.xlabel("date")
          plt.ylabel("level")
          plt.plot(x, y1, color ="red")
          plt.plot(x, y2, color ="green")
          plt.plot(x, y3, color ="blue")
          plt.show()