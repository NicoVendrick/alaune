#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template
from model import modele_donnees

def wordcloud ():
	return render_template ('wordcloud.html')+ modele_donnees.select_texte()


def wordcloud_key (name) :
	tabGraph=modele_donnees.select_ocurrence_date(name)
	html = "<script>\n"
	html += "var dataset =" + str(tabGraph)+";\n"
	html += "graph (dataset);\n"
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