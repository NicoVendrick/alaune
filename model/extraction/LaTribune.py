    # -*- coding:utf-8 -*-
     
import urllib, lxml.html
import time
from model import modele_donnees
     
def unes(targetURL):
	quotidien = {'nom': 'laTribune', 'url':'http://www.latribune.fr'}
	modele_donnees.insert_quotidien(quotidien)
	file = urllib.urlopen(targetURL)
	data = file.read().decode('utf8')
	file.close()
	doc = lxml.html.document_fromstring(data)
	titres= doc.xpath("//div[@class='main-article']//article/h2/a/text()")
	titres+= doc.xpath('//div[@class="title-wrapper"]//a/text()')
	titres+= doc.xpath('//div[@class="title-river"]//a/text()')
	liens = doc.xpath('//div[@class="main-article"]/article/h2/a/@href')
	liens+= doc.xpath('//div[@class="title-wrapper"]//a/@href')
	liens+= doc.xpath('//div[@class="title-river"]//a/@href')
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
		dico['URL']= str(tab[j][1].encode('utf8'))
		dico['date']=tab[j][2]
		quotidien = {'nom': 'laTribune', 'url':'http://www.latribune.fr'}
		modele_donnees.insert_une(dico, quotidien)
		j=j+1

