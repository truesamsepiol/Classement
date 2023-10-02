#!/bin/python3
# -*- coding: utf-8 -*-
import datetime
import sys


def usage():
    print("USAGE:")
    print("     " + str(sys.argv[0]) + " jour mois annee decalage listeDesMembres")


mois = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"]
jours = {"Monday" : "Lundi", "Tuesday" : "Mardi", "Wednesday" : "Mercredi", "Thursday" : "Jeudi", "Friday" : "Vendredi", "Saturday" : "Samedi", "Sunday" : "Dimanche"}

if __name__ == "__main__":
    if len(sys.argv) != 6:
        usage()
        exit(1)

    jour = int(sys.argv[1])
    nomMois = int(sys.argv[2])
    annee = int(sys.argv[3])
    decalage = int(sys.argv[4])

    date = datetime.datetime(annee, nomMois, jour) # date de depart

    fichier = open(sys.argv[5], "r")
    nom = fichier.readline()
    while nom != '':
        numeroMois = date.month
        nomJour = date.strftime("%A") 
        print(nom[:len(nom) - 1], end='') # afficher sans le \n de la ligne
        print(" ==> " + jours[nomJour] + " " +str(date.day) + " " + mois[numeroMois - 1] + " " + str(date.year))
        nom = fichier.readline()
        duree = datetime.timedelta(days=decalage) # decaler les jours
        date = date + duree
    fichier.close()
