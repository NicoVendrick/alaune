#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import modele_donnees
from extraction import CourrierInternational, LePoint, JournalduNet, _20minutes, LaTribune, LeDauphine, LeParisien, LePoint, sudouest

def extraction():
	date_J=time.strftime('%Y-%m-%d',time.localtime())
	date_article = modele_donnees.select_date('leDauphine')
	if date_article == None or date_J != date_article :
		CourrierInternational.unes('http://www.courrierinternational.com')
		LeParisien.unes('http://www.leparisien.fr')
		LePoint.unes('http://www.lepoint.fr')
		JournalduNet.unes('http://www.lejournaldunet.fr')
		LaTribune.unes('http://www.latribune.fr')
		_20minutes.unes('http://www.20minutes.fr')
		LeDauphine.unes('http://www.ledauphine.com')
		sudouest.unes('http://www.sudouest.fr')