import random
import string
import sys

depth=3 # par exemple. Avec 2 les noms sont moins réalistes

markov={}
entrees=[]
prenoms=set()
langues=set()

f=open("Prenoms.csv")


for ligne in f:
    ligne=ligne.split(";")
    langs=ligne[2].split(',')
    langs=[lang.strip() for lang in langs]
    nom=ligne[0].strip()
    [langues.add(l) for l in langs]
    if "french" in langs:# langues possibles dans le fichier : voir la liste langues
        # On pourrait aussi rajouter le filtre de genre (ligne[1]=="f" ou "m")
        prenoms.add(nom)
        entrees.append(nom[0:0+depth])
        for i in range(len(nom)-depth):
            if nom[i:i+depth] not in markov.keys():
                markov[nom[i:i+depth]]=[]
            markov[nom[i:i+depth]].append(nom[i+1:i+1+depth])
        if nom[-depth:] not in markov.keys():
            markov[nom[-depth:]]=[]
        markov[nom[-depth:]].append('\x07') # on sonne la fin de la récré hihi hoho haha
        
f.close()


def prenom():
    m=""
    lettre2=random.choice(list(entrees))
    while lettre2!='\x07':
        lettre=lettre2
        m+=lettre[0]
        lettre2=random.choice(markov[lettre])
    m+=lettre[1:]
    return m

if __name__=="__main__":
    try:
        n=int(sys.argv[1])
    except:
        n=5
    
    for i in range(n):
        print(prenom())
