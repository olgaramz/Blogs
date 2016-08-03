# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:27:06 2016

@author: Asus
"""

import re

def cleanText(file):
    output = 'output.txt'
    with open(file, 'r', encoding = 'utf-8') as f:
        with open(output, 'w', encoding = 'utf-8') as f1:
            for line in f:
                cleanLine = re.split('\s+', line)
                newCleanLine = ' '.join(cleanLine)
                f1.write(newCleanLine)             
    return

cleanText('blogtexts.txt')
