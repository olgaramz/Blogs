# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 23:00:23 2016

@author: Asus
"""

import lxml.html
import urllib.request
import feedparser

def getLinks(username):
    links = []
    rsslink = 'http://' + username + '.livejournal.com/data/rss'
    d = feedparser.parse(rsslink)
    items = d.entries
    for i in items:
        link = i.link
        links.append(link)
    return(links)

def getTexts(lst):
    texts = []
    for i in lst:
        with urllib.request.urlopen(i) as response:
            html = response.read().decode()
            tree = lxml.html.fromstring(html)
            #article = tree.xpath('.//div[@class="j-e-text"]/text()')
            article = tree.xpath('.//div[@class="entry-content"]/text()')
            #article = tree.xpath('.//article[@class=" b-singlepost-body entry-content e-content "]/text()')
            #article = tree.xpath('.//div[@class="asset-body"]/text()')
            #article = tree.xpath('.//div[@class="entry_text"]/text()')
            articletxt = '\n'.join(article)           
            texts.append(articletxt)
    return texts
  
blog = 'veraneo'
filename = blog + '_blog.txt'

entries = getLinks(blog)

recentArticles = getTexts(entries)
txtstrng = '\n'.join(recentArticles)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(txtstrng)
