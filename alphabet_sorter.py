#!/usr/bin/env python
#This will be a sorter for a Alphabetical List

#Authors: Jack Kong
#Date edited: 1/12/2017

import random
import sys
import os

unumber = os.getuid()
pnumber = os.getpid()
where = os.getcwd()
what = os.uname()
used = os.times()

redo = int(input('Press 1 to start the Alphabetical List sorter or press 0 to exit: ')) #int decleration converts string to int input

while redo == 1:

    sortlist = ["time1","time2","time3"]

    afile = raw_input('\nEnter the filename here: ')

    linenum = int(input('\nEnter the number of words you will be entering: '))

    names = afile + '_SORT.sort'

    i = 0 #this counts the word number

    n = 0 #this counts the number of works

    if redo == 1:

            f = names
            f = open (names, 'w')
            f.write('This file was created by' + str(what) + '\n')
            f.write('The file was generated in this directory: ' + str(where) + '\n')
            f.write('This file was generated at this time: ' + str(used) + '\n')
            f.write('Program will now list out your wordset in alphabetical order \n')
            while i < linenum:

                f.write( 'Word # ' + str(i) + 'is:' + sortlist[n] + '\n')

                i = i + 1 #functionality: adds 1 to each iteration of the loop starting at 1
                n = n + 1 #functionality: gets the next element in the wordlist

            f.write('This is the last line of the file. Program has completed the task\n')
            f.close()

            print('\nScript is looping. Please wait .... ')

            redo = int(input('\nPress 1 to start the Alphabetical List sorter or press 0 to exit: '))

            
