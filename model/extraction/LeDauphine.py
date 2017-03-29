# -*- coding:utf-8 -*-
     
import urllib, lxml.html
import time
from model import modele_donnees
     
def unes(targetURL):
	quotidien = {'nom': 'leDauphine', 'url':'http://www.ledauphine.com'}
	modele_donnees.insert_quotidien(quotidien)
	file = urllib.urlopen(targetURL)
	data = file.read().decode('utf8')
	file.close()
	doc = lxml.html.document_fromstring(data)
	titres=doc.xpath("//a[@class='titre']/text()")
	liens=doc.xpath("//a[@class='titre']/@href")
	i=0
	date = []
	while i < len(titres):
		date.append(time.strftime('%Y/%m/%d',time.localtime()))
		i=i+1
	tab = zip(titres, liens, date)
	dico = {}
	j=0
	while j<len(tab):
		dico ['titre']=str(tab[j][0].encode('utf8'))
		dico['URL']= targetURL + str(tab[j][1].encode('utf8'))
		dico['date']=tab[j][2]
		quotidien = {'nom': 'leDauphine', 'url':'http://www.ledauphine.com'}
		modele_donnees.insert_une(dico, quotidien)
		j=j+1