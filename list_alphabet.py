#This will be a list generator that takes user input

#Authors: Jack Kong
#Date edited: 1/13/2017

import random
import sys
import os
import datetime

filess = str(raw_input("Enter in the filename: "))

namer = filess + '_LIST.list' #append the file nextension _LIST.list

lengthinput = int(raw_input("\nEnter the # of words you want to sort: "))

tablex = [] #information to store in variable tablex'

timex = tablex #new varible to store table for file generation

i = 0

n = 0

h = 1

while (i < lengthinput):
     tablex.append(str(raw_input("\nEnter a word or letter: ")))
     i = i+1

tablex.sort()

     #Start the file generation
f = namer
f = open (namer, 'w')
print >> f, '\nThe filename is: ' + str(namer) 
print >> f, '\nThe file was generated at: ' + str(datetime.datetime.now())
print >> f, '\nListed below is your list in alphabetical order: ' 
while (n < lengthinput):
     print >> f, '\n' + str(h) + '. ' + timex[n]
     n = n+1
     h = h+1
f.close()

#Lessons learned
#-------#
#while loops executes definitely based on condition
#variable arrays should be reassigned in order to not have indexing conflicts
#variable array can have elements appended using list.append
#.sort() function will take list and sort alphabetically







