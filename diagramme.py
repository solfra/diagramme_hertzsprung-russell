#importation des biblioteque utiles
import numpy as np
import matplotlib.pyplot as plt

#definition des listes utilisé comme des listes vides
HIP = []
Vmag = []
dist = []
color = []
spctr_type = []
mag_abs = []

#partie qui recupère les données et les met en formes
f = open("vizier_votable.tsv", "r")
ligne = True 
while ligne: #parcours tout le fichier
    ligne = f.readline() #lit une ligne
    donne = ligne.split(";") #découpe cette ligne avec ; comme séparateur
    if len(donne) == 6 : #si on est dans le jeux de donnée
        donne_ligne = [d.strip() for d in donne] #supprime les espace et les \n
        try:
            float(donne_ligne[3]) #test si le 3eme element de la liste est un float
            float(donne_ligne[2])
        except ValueError : #si cette element n'est pas float il va poser problème par la suite
            continue #on saute donc cette ligne
        
        if  float(donne_ligne[2]) <=0 : #supprime les lignes avec une valeur de distance negatives ou egales a zeros qui seront un problème dans le logarime par la suite
            continue
        else : #sépare la ligne dans les différentes liste
            HIP.append(int(donne_ligne[0]))
            Vmag.append(float(donne_ligne[1]))
            dist.append(float(donne_ligne[2]))
            color.append(float(donne_ligne[3]))
            spctr_type.append(donne_ligne[4])
f.close()

Vmag = np.array(Vmag)
dist = np.array(dist)

mag_abs = Vmag -5*(-1+np.log10(1/(dist*(10**(-3) )))) #calcul de la magitude absolue M=m-5(log(D)-1) et D = 1/plx avec plx en arcsecond

print("nombre d'étoiles considéré", len(mag_abs))

B_V = np.array(color)

ax = plt.gca()
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(15, -10) #permet de retourner le diagramme
plt.plot(B_V, mag_abs, linestyle = 'none', marker = ',')
plt.title("Diagramme de Hertzsprung-Russell \n d'après le catalogue Hipparcos")
plt.xlabel("Couleur (B-V)")
plt.ylabel("magnitude absolue")
plt.show()
plt.close()
