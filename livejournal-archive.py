# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:39:02 2016

@author: Asus
"""
import re
import lxml.html
import urllib.request

startlink = 'http://ammo1.livejournal.com/2015/'

def getDayLinks(url):
    queue = []
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()
        tree = lxml.html.fromstring(html)
        linksOnPage = tree.xpath('.//@href')
        for n in linksOnPage:
            m = re.search(r'http://ammo1.livejournal.com/2015/\d{2}/\d{2}', n)
            if m != None:
                queue.append(n)
    return queue

def getTextLinks(lst):
    textLinks = []
    for i in lst:
        with urllib.request.urlopen(i) as response:
            html = response.read().decode()
        tree = lxml.html.fromstring(html)
        linksOnPage = tree.xpath('.//@href')
        for n in linksOnPage:
            m = re.search(r'http://ammo1.livejournal.com/\d+.html$', n)
            if m != None:
                textLinks.append(n)
    return textLinks

def getTexts(lst):
    visited = []    
    count = 0
    for i in lst:
        if i not in visited:
            count += 1
            with urllib.request.urlopen(i) as response:
                html = response.read().decode()
            tree = lxml.html.fromstring(html)
            article = tree.xpath('.//div[@class="j-e-text"]/text()')
            #article = tree.xpath('.//div[@class="entry-content"]/text()')
            #article = tree.xpath('.//article[@class=" b-singlepost-body entry-content e-content "]/text()')
            #article = tree.xpath('.//div[@class="asset-body"]/text()')
            #article = tree.xpath('.//div[@class="entry_text"]/text()')
            articletxt = '\n'.join(article)
            visited.append(i)
            filename = 'C:\\Users\\Asus\\Desktop\\ammo12015\\' + str(count) + '.txt'
            with open(filename, 'w', encoding = 'utf-8') as f:
                f.write(articletxt)
    return

links = getDayLinks(startlink)
entries = getTextLinks(links)
getTexts(entries)
