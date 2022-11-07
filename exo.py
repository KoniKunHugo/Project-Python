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
#FIN