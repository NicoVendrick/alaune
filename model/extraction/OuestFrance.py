#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, lxml.html
import time
from model import modele_donnees

def unes(targetURL):
	quotidien = {'nom': 'ouestfrance', 'url':'http://www.ouest-france.fr'}
	modele_donnees.insert_quotidien(quotidien)
	file = urllib.urlopen(targetURL)
	data = file.read().decode('utf8')
	file.close()
	doc = lxml.html.document_fromstring(data)
	article_href = doc.xpath('//article[@data-vr-contentbox]/a/@href')
	doc=lxml.html.document_fromstring(data)
	articles_titles = doc.xpath('//article[@data-vr-contentbox]//h2[@class="title "]/text()')
	i=0
	date = []
	while i < len(articles_titles):
		date.append(time.strftime('%Y/%m/%d',time.localtime()))
		i=i+1
	tab = zip(articles_titles, article_href, date)
	dico = {}
	j=0
	while j<len(tab):
		dico ['titre']=str(tab[j][0].encode('utf8'))
		dico['URL']= targetURL + str(tab[j][1].encode('utf8'))
		dico['date']=tab[j][2]
		quotidien = {'nom': 'ouestfrance', 'url':'http://www.ouest-france.fr'}
		modele_donnees.insert_une(dico, quotidien)
		j=j+1