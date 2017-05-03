# -*- coding:utf-8 -*-
 
import urllib, lxml.html
import time
from model import modele_donnees
 
def unes(targetURL):
	quotidien = {'nom': 'LePoint', 'url':'http://www.lepoint.fr'}
	modele_donnees.insert_quotidien(quotidien)
	file = urllib.urlopen(targetURL)
	data = file.read().decode('utf8')
	file.close()
 
	doc = lxml.html.document_fromstring(data)
	articles_href = doc.xpath('//article[@class="en-continu-li"]//a/@href')
 
	doc = lxml.html.document_fromstring(data)
	article_titles = doc.xpath('//h2[@class="art-lead"]/text()')
	
	i=0
	date = []
	while i < len(article_titles):
		date.append(time.strftime('%Y/%m/%d',time.localtime()))
		i=i+1
	tab = zip(article_titles, articles_href, date)
	dico = {}
	j=0
	while j<len(tab):
		dico ['titre']=str(tab[j][0].encode('utf8'))
		dico['URL']= targetURL + str(tab[j][1].encode('utf8'))
		dico['date']=tab[j][2]
		quotidien = {'nom': 'LePoint', 'url':'http://www.lepoint.fr'}
		modele_donnees.insert_une(dico, quotidien)
		j=j+1