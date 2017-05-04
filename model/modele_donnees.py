#!/usr/bin/env python
# coding: utf8
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from collections import Counter
import mysql.connector
import time, json

config = json.loads(open('config.json', 'r').read())
cnx = mysql.connector.connect(** config)
cursor = cnx.cursor()


def insert_quotidien(quotidien):
	add_quotidien = ("INSERT INTO quotidiens(id, nom, URL) VALUES (NULL,%(nom)s, %(url)s)")
	data_quotidien = quotidien
	cursor.execute (("SELECT id FROM quotidiens WHERE nom LIKE (%(nom)s)"), data_quotidien)
	id_exist = ()
	for (id) in cursor:
		id_exist = id_exist + id
	if id_exist == () :
		cursor.execute (add_quotidien, data_quotidien)
	cnx.commit()
	
	
def insert_une(une, quotidien):
	add_une = ("INSERT INTO unes (id, titre, URL, date, quotidien_id) VALUES (NULL, %(titre)s, %(URL)s, %(date)s, %(quotidien_id)s)")
	id_quotidien = cursor.execute (("SELECT id FROM quotidiens WHERE nom LIKE (%(nom)s)"), quotidien)
	id_exist = ()
	data_une = une
	for (id) in cursor:
		id_quotidien = id
	une ['quotidien_id'] = id_quotidien[0]
	cursor.execute (("SELECT id FROM unes WHERE titre LIKE (%(titre)s)"), data_une)
	for (id) in cursor:
		id_exist = id
	if id_exist == () :
		cursor.execute (add_une, data_une)
	cnx.commit()
	   
def select_une(journal):
	quotidien_id = cursor.execute ("SELECT id FROM quotidiens WHERE nom LIKE '%s'" %journal)
	for (id) in cursor:
		id_quotidien = id
	cursor.execute ("SELECT titre, URL, date FROM unes WHERE quotidien_id LIKE '%s' AND date LIKE CURDATE()" %int(id_quotidien[0]))
	rows = cursor.fetchall()
	html = ''
	html += '<h1>'
	html += 'Votre Journal : ' + journal + '</h1>'
	html += '<h2 id=titre> Unes principales de votre Journal : </h2>'
	html += '<a href="Formulaire.html"> Retour </a>'
	html += '<ul>'
	for (titre, URL, date) in rows:
		html += '<li>'
		html += '<a href="' + URL + '">' + titre.strip() + '</a></li>'
	html += '</ul>'
	return html
		
def select_date(journal):
	id_quotidien = cursor.execute ("SELECT id FROM quotidiens WHERE nom LIKE '%s'" %journal)
	for (id) in cursor:
		id_quotidien = id
	if id_quotidien == None :
		return None
	UneExist = cursor.execute ("SELECT date FROM unes WHERE quotidien_id LIKE '%s'" %id_quotidien[0])
	for (date) in cursor:
		UneExist = date
	if UneExist == None :
		return None
	date = cursor.execute ("SELECT date FROM unes WHERE quotidien_id LIKE '%s'" %id_quotidien[0])
	for (i) in cursor:
		date = i
	return str(date[0])
	
def select_texte () :
	cursor.execute ("SELECT titre FROM unes WHERE date >= DATE_ADD(CURDATE(), INTERVAL -7 DAY)")
	titre=()
	titles=[]
	i=0
	for une in cursor:
		titre = titre + une
	text = ""
	i=0
	while i < len(titre) :
		text = text + " " + titre[i]
		i=i+1
	word_string = text.encode('utf8')
	word_string = word_string.replace('"'," ")
	word_string = word_string.replace('\n'," ")
	word_string = word_string.replace('#'," ")
	replace = [":", ",", ".", "?", "!", " à ", " Les ", " après ", " les ", " a ", " entre ", " été ", "(", ")", "«", "»", " encore ", " ans ", " avant ", " va ", " un ", " Deux ", " deux " ," trois ", " quatre ", " cinq ", " six ", " sept ", " huit ", " neuf ", " dix ", " d’un ", " plus ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " fait ", " A ", " vue ", " devant ", " derrière ", " -", " bon ", " contre ", " toujours ", " Pourquoi ", " TF ", " veut ", " depuis ", " sans ", " moins ", " garde ", " d'", " l'", " c'", " n'", "l’", " s'", "%", " e ", " chez ", "Après", "Avant", " face ", " doit ", " lors ", " sous ", " avoir ", " être ", " heure ", " Pen ","morts", " faire ", " tout ", "bien ", " Quand ", " peut ", "–", " comment ", " a-t-il "," mis ", " vont ", " met ", " où ", " nouveau ", " nouvelle ", " qu'", " faut ", " vers ", " VIDEO ", " grand ", " retour ", " si ", " L'", "Comment ", " selon ", " passe ", " ils ", " tous ", "'", " près ", " pourquoi ", " er ", " demande ", " dernier ", " personnes ", " coup ", " très ", " euros ", " Macron-Le " ]
	for word in replace :
		word_string=word_string.replace(word," ")
	word_string = unicode(word_string, ('utf8'))
	word_string = stopWords(word_string)
	html = '' + '\n'
	html += "<script>" + '\n'
	html += 'var words = ['
	for i in range(len(word_string)-1):
		html += "{text : '" + word_string[i]['text'] + "', size: " + str(word_string[i]['size']) + ", href: '" + word_string[i]['href'] + "'},"
	i = len(word_string)-1
	html += "{text : '" + word_string[i]['text'] + "', size: " + str(word_string[i]['size']) + ", href: '" + word_string[i]['href'] + "'}"
	html += ']; \n'
	html += "wordcloud(words);" + '\n'
	html += "</script>"	+ '\n'
	html += "</html>" 
	return html
	
def select_ocurrence_date (word) :
	tab=[]
	for i in range (0,8):
		cursor.execute ("SELECT count(titre) FROM unes WHERE titre LIKE '%"+word+"%' AND date = DATE_ADD(CURDATE(), INTERVAL -"+str(i)+" DAY)")
		for j in cursor:
			if j[0]==0 :
				tab.append (0)
			else : tab.append(j[0])
	tab.reverse()
	return tab
	
def stopWords (chaine) :
	tokenizer = TreebankWordTokenizer()
	tokens = tokenizer.tokenize(chaine)
	# chargement des stopwords français
	french_stopwords = set(stopwords.words('french'))
	# un petit filtre
	tokens = [token for token in tokens if token.lower() not in french_stopwords]
	counts = Counter(tokens)
	counts=counts.most_common(50)
	dico={}
	tabDico=[]
	for i in range(0,len(counts)):
		dico['text'] = counts[i][0]
		dico['size'] = counts[i][1]
		dico['href'] = "onclick/"+counts[i][0]
		tabDico.append(dico)
		dico={}
	return tabDico

		
def MotWithLink (word):
	requeteSQL = "SELECT titre, URL, date FROM unes WHERE titre LIKE '%"+word+"%' AND date >= DATE_ADD(CURDATE(), INTERVAL -7 DAY)"
	cursor.execute (requeteSQL)
	tabLink=[]
	tabTitre=[]
	tabDate=[]
	for titre,URL, date in cursor :
		tabLink.append(URL)
		tabTitre.append(titre)
		tabDate.append(date)
	return zip(tabTitre, tabLink, tabDate)	
	