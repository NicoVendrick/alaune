#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
from flask import Flask, request, render_template
from model import modele_donnees, modele_extraction
from view import wordcloud_view, journaux_view
import jinja2
 
app = Flask(__name__)
app.jinja_loader = jinja2.FileSystemLoader('./view/templates')

@app.route('/')
def accueil():
	modele_extraction.extraction() # à enlever dès que l'extraction tournera toute seul !
	return wordcloud_view.wordcloud()


@app.route('/onclick/<name>')
def wordcloud(name) :
	return wordcloud_view.wordcloud_key(name)

@app.route('/contact.html')
def contact() :
	return wordcloud_view.contact()

	
@app.route('/quel_journal', methods = ['POST'])
def quel_journal():
	journal = request.form['journal']
	return journaux_view.journaux(journal)
		
@app.route('/Formulaire.html')
def afficheForm () :
	return journaux_view.affiche_form()


if __name__ == '__main__':

	app.run(debug=True)
