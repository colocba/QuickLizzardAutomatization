#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automatization script for opening tabs in quicklizard
@author: Amir Baum
"""

from bs4 import BeautifulSoup
import webbrowser
import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta

productsCheck = 0
numberOfPages = 0
start = datetime.now()

def diff(t_a, t_b):
    t_diff = relativedelta(t_b, t_a)  # later/end time comes first!
    return '{h}h {m}m {s}s'.format(h=t_diff.hours, m=t_diff.minutes, s=t_diff.seconds)

def openTabs(data) :
    soup = BeautifulSoup(data, 'html.parser')
    for a in soup.find_all('a',href=True):
        if isinstance(a.get('class'), type(None)):
            if 'http' in a['href']:
                global productsCheck
                productsCheck += 1
                webbrowser.open(a['href'])
    global numberOfPages
    numberOfPages += 1

def printStats() :
    print('______________________________________')
    print('Products check: ' + str(productsCheck))
    print('Number of pages checked: ' + str(numberOfPages))
    print('Start working at: ' + str(start.time().strftime('%H:%M')))
    print('You have been working for: ' + str(diff(start,datetime.now())))
    print('______________________________________')

def displayMenu() :
    print('<file_name>: Opening tabs of this file.')
    print('1: Show status.')
    print('2: Make a daily report when quiting the script')
    print('quit: Quit script.')
    print('\n*******************************************************\n')

def makeDailyReport() :
    report_file = open(str(start.date().strftime('%d_%m_%y')) + '.txt', 'w')
    report_file.write('---------------- Daily report ---------------- \n')
    report_file.write('Date: ' + str(start.date().strftime('%d/%m/%y')) + '\n')
    report_file.write('Products check: ' + str(productsCheck) + '\n')
    report_file.write('Number of pages checked: ' + str(numberOfPages) + '\n')
    report_file.write('Start working at: ' + str(start.time().strftime('%H:%M')) + '\n')
    report_file.write('Time worked: ' + str(diff(start,datetime.now())))

if __name__ == "__main__" :
    
    import os
    dirpath = os.getcwd()
    printReport = False

    print('\n********** Quicklizard Automatization script **********\n')
    displayMenu()
    
    while True :
        print('\nEnter the file name')
        filename = input('>> ')
        
        if filename == 'quit' :
            if printReport == True :
                makeDailyReport()
            break
        elif filename == '1' :
            printStats()
            continue
        elif filename == '2' :
            printReport = True
            print('Changes saved.')
            continue
        
        path = dirpath + '/' + filename
        
        try:
            with open(path, 'r') as myfile:
                data = myfile.read()
            openTabs(data)
        except OSError as e:
            print(e.strerror)
            continue