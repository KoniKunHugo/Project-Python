#DEBUT
r = 12000
s = 1250
e = 10
rh = 230
assertionFinale = (( (365*3) / (24 - (16 - 8)) ) * (rh)  > r) == (e * s < r)
partieUnUn = (( (365*3) / (24 - (16 - 8)) ) * (rh)  > r) #True
partieUnDeux = (e * s < r) #False
assertionFinale = partieUnUn == partieUnDeux #False

assertionFinaleDeux = ((365 * 3) / (4 - (12 - 8)) * (rh)  > r) == (e * s  < r)
partieDeuxUn = ((365 * 3) / (4 - (12 - 8)) * (rh)  > r) #False
partieDeuxDeux = (e * s  < r) #False
assertionFinaleDeux = partieDeuxUn == partieDeuxDeux #True

def add(x,y):
    return(x+y)

def sub(x,y):
    return(x-y)

def multiply(x,y):
    return(x*y)

#on défini la fonction divide qui prend en compte de variable x et y et qui divisera x et y
def divide(x,y):
    #si la valeur de y est différente de 0
    if y != 0 :
        #on retourne la valeur de la division de x et y
        return(x/y)
    #sinon ça veut dire que y = 0
    else : 
        #nous retournons une erreur "division par 0"
        return("ERROR division par 0")

def modulo(x,y):
    return(x%y)

def salaireNet(brut, coeff):
    return (brut - brut/coeff)

#def salaireParSec(salaireHoraire, heureParJourOuvre, nombreJoursOuvreParAn):
    #return (nombreJoursOuvreParAn*heureParJourOuvre*salaireHoraire/2592000)

def salaireParSec(salaireHoraire, heureParJourOuvre, nombreJoursOuvreParAn):
    #Calculer mon salaire annuel
    salaireAnnuel = salaireHoraire * heureParJourOuvre * nombreJoursOuvreParAn
    #Calculer le nombre de secondes par année
    nbSecondesParAn = 365*24*60*60
    #Je pose et retourne la division
    return(salaireAnnuel / nbSecondesParAn)

#Definir une fonction withdrawFees qui retire un pourcentage à un total en fonction d'un total et d'un pourcentage
def withdrawFees(total, percent):
        #Definir fees en fonction d'un total et d'un pourcentage
        fees = total*(percent/100)
        #soustraire fees au total
        result = total - fees
        #retourner la valeur obtenue
        return(result)

#Definir une fonction qui retourne le salaire net en fonction du salaire brut (float) et du secteur d'activité  (isPublic > booleen)
def calculBrutEnNet(salaireBrut, isPublic):
    #Si je suis un travailleur du secteur public
    if isPublic :
        #Alors je soustrais 15% de mon salaire Brut à mon salaire Brut et je l'assigne à la variable salaireNet
        salaireNet = salaireBrut - (salaireBrut / (15 / 100))
    #Sinon je suis un travailleur du secteur privé
    else :
        #Alors je soustrais 23% de mon salaire Brut à mon salaire Brut et je l'assigne à la variable salaireNet
        salaireNet = salaireBrut - (salaireBrut / (23 / 100))
    #Retourner salaireNet
    return(salaireNet)

#def input():
    #On attribu à une variable un caractere de type string

input('a')
#"Exercice:
#"Faire un mini jeu qui affiche un message lorsque input renvoie le bon caractère
#"le caractere doit être paramétrable

#definir une variable x qui sera le caractère paramétrable
# x = 'h'"
#definir une variable y vide qui servira de réceptacle à la variable aléatoire
# y = ''"
#definir une fonction qui fera des boucles jusqu'à ce que x et y soient le même caractère à l'aide de la fonction input qui changera constamment avec une variable z qui sera le compteur et qui commencera nécessairement avec la valeur 0
# def miniJeu(x,y, z=0):"
    #tant que x n'est pas égal à y
    # while x!=y :"
        #nous rajoutons un au compteur z puis relançons la fonction input et nous poursuivons la boucle
        # z = z+1"
        # y= input()"
    #retourner le message de la victoire 
    # return("VICTOIRE !!! et le nombre de fois qui fut nécessaire à obtenir la victoire est ", z)

#definir une variable x qui sera le caractère paramétrable
x = 'h'
#definir une variable y vide qui servira de réceptacle à la variable aléatoire
y = ''
#definir une variable z qui sert de compteur
z = 0
#definir une fonction qui fera des boucles jusqu'à ce que x et y soient le même caractère à l'aide de la fonction input qui changera constamment avec une variable z qui sera le compteur
def miniJeu(x,y, z):
    #si x n'est pas égal à y
    if x != y :
        #alors nous rajoutons un compteur à z puis nous éxécutons la fonction input puis l'attribuons à y et nous rappelons la fonction miniJeu
        z = z+1
        input()
        miniJeu(x,y,z)
    #sinon
    else :
        #Retourner le méssage de victoire absolu
        return("VICTOIRE")

# ex1
prenom = "Hugo"
nom = "XIA"
def identite(nom,prenom):
    return(nom + ',' +prenom)

# ex2
liste = [0,0,0,1,1,1]
def 
# ex3
print("bonjour")
#FIN