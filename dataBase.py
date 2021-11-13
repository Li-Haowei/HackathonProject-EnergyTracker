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
          self.etotalRows = 0
          self.atotalRows = 0
     
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
          self.base.save('dataBase.xlsx')
          self.etotalRows +=1
          
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
          self.atotalRows +=1
           
     def delEmotion(self,date):
          """delete the emotion records on that date"""
          i = 1
          cell_val = self.emotionTracker.cell(row=i,column=1)
          while cell_val.value!=date and i<=self.etotalRows:
               i += 1
               cell_val = self.emotionTracker.cell(row=i,column=1)
          if i>self.etotalRows:
               return False
          self.emotionTracker['A' + str(i)] = None
          self.emotionTracker['B' + str(i)] = None
          self.base.save('dataBase.xlsx')
          
          return True
     def delAssignment(self,date):
          """delete the assignment records on that date"""
          i = 1
          cell_val = self.assignmentTracker.cell(row=i,column=1)
          while cell_val.value!=date and i<=self.atotalRows:
               i += 1
               cell_val = self.assignmentTracker.cell(row=i,column=1)
          if i>self.atotalRows:
               return False
          self.assignmentTracker['A' + str(i)] = None
          self.assignmentTracker['B' + str(i)] = None
          self.assignmentTracker['C' + str(i)] = None
          self.assignmentTracker['D' + str(i)] = None
          self.base.save('dataBase.xlsx')
          
          return True
