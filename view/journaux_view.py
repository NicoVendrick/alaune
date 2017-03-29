#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template
from model import modele_donnees

def journaux(journal):
	if journal == 'courrier':
			return render_template('mot.html') + modele_donnees.select_une(journal)
	elif journal == 'leParisien':
		return render_template('mot.html') + modele_donnees.select_une(journal)
	elif journal == 'LePoint':
		return render_template('mot.html') + modele_donnees.select_une(journal)
	elif journal == 'JournalduNet':
		return render_template('mot.html') + modele_donnees.select_une(journal)
	elif journal == 'laTribune':
		return render_template('mot.html') + modele_donnees.select_une(journal)
	elif journal == '20minutes':
		return render_template('mot.html') + modele_donnees.select_une(journal)
	elif journal == 'leDauphine':
		return render_template('mot.html') + modele_donnees.select_une(journal)
	elif journal == 'sudouest':
		return render_template('mot.html') + modele_donnees.select_une(journal)
		
def affiche_form () :
	return render_template('Formulaire.html')