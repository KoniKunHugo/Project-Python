from random import *


#On admet une fonction random qui retourne une valeur aléatoire parmi la liste donnée
def aleatoire(x):
  return (choice(x))


#On admet une fonction input qui demande à l'utilisateur une valeur et qui la retourne
def mehInput():
  return (input("Que faîtes vous ? (pierre, ciseaux ou feuille) :"))


#Definir une fonction Shifumi
def shifumi():
  #Definir une variable scoreJoueur et l'initialiser à 0 qui sera le compteur de victoire du joueur
  scoreJoueur = 0
  #Definir une variable scoreCPU et l'initialiser à 0 qui sera le compteur de victoire du CPU
  scoreCPU = 0
  #Definir un tableau qui contiendra les choix du CPU : pierre, ciseaux, feuille
  choixCPU = ["pierre", "ciseaux", "feuille"]
  #Tant que ScoreCPU < 3 ou ScoreJoueur < 3
  while scoreCPU < 3 or scoreJoueur < 3:
    #Alors Definir une variable x qui récupèrera le retour de ll'éxécution input qui aura comme valeur soit papier soit pierre soit ciseaux
    x = mehInput()
    #Éxécuter la fonction aléatoire et assigner à y le retour de la fonction aléatoire qui tirera le choix du CPU parmi ciseaux, pierre et feuille
    y = aleatoire(choixCPU)
    print(y)
    #Si x est égal à y
    if x == y:
      #Alors afficher "égalité"
      print("Draw")
    #Sinon si x est égal à "pierre" et y est égal à "feuille"
    elif x == "pierre" and y == "feuille":
      #Alors afficher "défaite"
      print("Lost")
      #Imcrémenter à ScoreCPU 1
      scoreCPU = scoreCPU + 1
    #Sinon si x est égal à "feuille" et y est égal à "pierre"
    elif x == "feuille" and y == "pierre":
      #Alors afficher "victoire"
      print("Victory")
      #Imcrémenter à ScoreJoueur 1
      scoreJoueur = scoreJoueur + 1
    #Sinon si x est égal à "ciseaux" et y est égal à "pierre"
    elif x == "ciseaux" and y == "pierre":
      #Alors afficher "defaite"
      print("Lost")
      #Imcrémenter à ScoreCPU 1
      scoreCPU = scoreCPU + 1
    #Sinon si x est égal à "pierre" et y est égal à "ciseaux"
    elif x == "pierre" and y == "ciseaux":
      #Alors afficher "victoire"
      print("Victory")
      #Imcrémenter à ScoreJoueur 1
      scoreJoueur = scoreJoueur + 1
    #Sinon si x est égal à "ciseaux" et y est égal à "feuille"
    elif x == "ciseaux" and y == "feuille":
      #Alors afficher "victoire"
      print("Victory")
      #Imcrémenter à ScoreJoueur 1
      scoreJoueur = scoreJoueur + 1
    #Sinon si x est égal à "feuille" et y est égal à "ciseaux"
    elif x == "feuille" and y == "ciseaux":
      #Alors afficher "défaite"
      print("Lost")
      #Imcrémenter à ScoreCPU 1
      scoreCPU = scoreCPU + 1
    #Sinon afficher "erreur"
    else:
      print("Erreur")
  #Si ScoreCPU est égal à 3
  if scoreCPU == 3:
    #Alors retourner "You lost, so bad bad"
    return ("You lost, so bad bad")
  #Sinon
  else:
    #Alors retourner "You won, Conglaraturatation"
    return ("You won, Conglaraturatation")
