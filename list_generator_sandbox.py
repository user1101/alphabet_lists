#This will be a list generator that takes user input

#Authors: Jack Kong
#Date edited: 1/13/2017

import random
import sys
import os

filess = str(raw_input("Enter in the filename: "))

namer = filess + '_LIST.list'

lengthx = ["1","2","3","4","5","6","7"]

appendarray = []

i = 0

h = 0

while (i < len(lengthx)): 

    appendarray.append(str(raw_input('Enter a string into the list: ')))
    i = i+1

f = namer
f = open (namer, 'w')
while (h < len(lengthx)):
    print >> f, appendarray[h]
    h = h+1
f.close()

#Trash lines 5below
#words = raw_input('Enter a list of words to create a list: \n')
#string_input = raw_input()
#input_list = string_input.split() #splits the string to spaces
#input_list = [str(a) for a in input_list]





