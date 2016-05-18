
import os
lettre = input
while lettre !=  "Q"  : 
	annee = input ("Q pour quitter.\nSaisissez une année : ")
	annee = int (annee)

	bissextile = False

	if annee % 400 == 0 : 
		bissextile == True
	elif annee % 100 == 0 : 
		bissextile == False 
	elif annee % 4 == 0 :
		bissextile == True
	else : 
		bissextile == False
	if bissextile : 
		print ("L'année est bissextile.")
	else : 
		print ("L'année n'est pas bissextile.\n")
os.system("pause")


	
