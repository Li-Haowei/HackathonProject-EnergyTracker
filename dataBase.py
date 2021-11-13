# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 12:26:34 2021

@author: Haowei Li
"""
import openpyxl
path = "./dataBase.xlsx"

class dataBase():
     def __init__(self):
          self.base = openpyxl.load_workbook(path)
          self.emotionTracker = self.base['emotionTracker']
          self.assignmentTracker = self.base['assignmentTracker']
     def addEmotion(self,date,level):
          """add the date and emotion level into dataBase"""
          i = 0
          cell_val = ''
          # Finds which row is blank first
          while cell_val != None:
               i += 1
               cell_val = self.emotionTracker['A' + str(i)].value         
          #x = input('Prompt: ')
          
          self.emotionTracker['A' + str(i)] = date
          self.emotionTracker['B' + str(i)] = level
          # Modify Sheet, Starting With Row i
          self.base.save('dataBase.xlsx')
      def addAssignment(self,deadline,course,percentage,finished):
          """add the deadline, course, percentage of assignment, and finish status into dataBase"""
          i = 0
          cell_val = ''
          # Finds which row is blank first
          while cell_val != None:
               i += 1
               cell_val = self.assignmentTracker['A' + str(i)].value         
               
          self.assignmentTracker['A' + str(i)] = deadline
          self.assignmentTracker['B' + str(i)] = course
          self.assignmentTracker['C' + str(i)] = percentage
          self.assignmentTracker['D' + str(i)] = finished
          self.base.save('dataBase.xlsx')
     
