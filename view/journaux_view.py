#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template
from model import modele_donnees

def journaux(journal):
	return render_template('mot.html') + modele_donnees.select_une(journal)
		
def affiche_form () :
	return render_template('Formulaire.html')