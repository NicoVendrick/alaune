#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template
from model import modele_donnees

def wordcloud ():
	return render_template ('wordcloud.html')+ modele_donnees.select_texte()


def wordcloud_key (name) :
	tabGraph=modele_donnees.select_ocurrence_date(name)
	html = "<script>\n"
	html += "var dataset = freqData=[{State:'J-7',freq:"+str(tabGraph[0])+"},{State:'J-6',freq:"+str(tabGraph[1])+"},{State:'J-5',freq:"+str(tabGraph[2])+"},{State:'J-4',freq:"+str(tabGraph[3])+"},{State:'J-3',freq:"+str(tabGraph[4])+"},{State:'J-2',freq:"+str(tabGraph[5])+"},{State:'J-1',freq:"+str(tabGraph[6])+"},{State:'Jour J',freq:"+str(tabGraph[7])+"}];;\n"
	html += "dashboard('#dashboard',freqData);\n"
	html += "</script>\n"
	html += htmlize(modele_donnees.MotWithLink (name))
	return render_template('onclick.html') + html
	
def htmlize(titles_and_href):
	html = ''
	html += '<ul>'
	for item in titles_and_href:
		html += '<li><a href="' + item[1] + '">' + item[0].strip() + ' ' + str(item[2]) + '</a></li>\n'
	html += '</ul>'
	return html
	
def contact ():
	return render_template('contact.html')