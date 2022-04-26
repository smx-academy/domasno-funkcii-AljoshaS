#Da se napravi programa koja bi bila za potrebite na nekoja biblioteka, 
# vo programata da ima moznosti da se vnesuvaat novi knigi, da se zaclenuvaat novi clenovi, 
# da se pozajmuvaat knigi, da se vrakjaat knigi.
#Podatoci za knigite koi ke treba da se cuvaat: Naslov, avtor, zanr, kolicina
#Podatoci za sekoj clen koi ke treba da se cuvaat: Ime i prezime, email, telefonski broj, 
# broj na clenska kniska, dali ima zemeno kniga.
#Clen koj ima zemeno kniga ne moze da zeme druga kniga
#*probajte vo razlicni fajlovi "knigi.json", "clenovi.json" da gi cuvate podatocite
import json
from turtle import clear

def novichlenovi():
    novichlenovi={}
    prodolzhi="da"
    with open('chlenovi.json') as f:
        novichlenovi = json.load(f) 

    while prodolzhi.lower()=="da":
        chlenovi=input("Vnesete ime i prezime na noviot chlen: ")
        novichlenovi[chlenovi]={}

        email=input("Vnesete email kontakt na chlenot: ")
        novichlenovi[chlenovi]["email kontakt"]=email

        telbroj=input("Vnesete tel. broj kontakt na chlenot: ")
        novichlenovi[chlenovi]["tel. broj"]=telbroj

        chlenskabroj=input("Vnesete broj od chlenska knishka: ")
        novichlenovi[chlenovi]["broj od chlenska knishka: "]=chlenskabroj

        brojPozajmeniKnigi=int(input("Broj na pozajmeni knigi? Vnesete 0 bidejki e nov chlen "))
        novichlenovi[chlenovi]["kolichina na pozajmeni knigi"]=brojPozajmeniKnigi

        prodolzhi=input("Dali sakate da prodolzhite da vnesuvate novi chlenovi? ")
        if prodolzhi!="da":

            with open('chlenovi.json', 'w') as f:
                json.dump(novichlenovi, f, indent=2)

            print("Listata chlenovi na bibliotekata e: {}".format(novichlenovi))
    return novichlenovi
#a=novichlenovi(novichlenovi)

def vnesknigi():
    noviknigi={}
    prodolzhi="da"
    with open("knigi.json") as f:
        noviknigi = json.load(f)

    while prodolzhi.lower()=="da":
        knigi=input("Vnesete naslov na kniga: ")
        noviknigi[knigi]={}

        avtor=input("Vnesete avtor na knigata: ")
        noviknigi[knigi]["Avtor"]=avtor

        zhanr=input("Vnesete go zhanrot na knigata: ")
        noviknigi[knigi]["Zhanr"]=zhanr

        kolichina=int(input("Vnesete kolichina na knigi: "))
        noviknigi[knigi]["kolichina na knigi"]=kolichina
        prodolzhi=input("Dali sakate da prodolzhite? ")

        if prodolzhi.lower()!="da":

            with open('knigi.json', 'w') as f:
                json.dump(noviknigi, f, indent=2)

            print("Vashiot spisok na knigi e: {}".format(noviknigi))
    return vnesknigi
#b=vnesknigi(vnesknigi)

def zemanjekniga():
    zemanjekniga={}
    prodolzhi="da"

    with open('chlenovi.json') as f:
        novichlenovi = json.load(f)

    with open('knigi.json') as f:
        noviknigi =json.load(f)

    while prodolzhi.lower()=="da":
        chlen=input("Koj chlen pozajmuva kniga? ")
        zemanjekniga[chlen]={}

        if novichlenovi[chlen]['kolichina na pozajmeni knigi']>0:
            print("Chlenot {} ne mozhe da pozajmuva novi knigi bidejki ne ja vratil prethodno pozajmenata kniga.".format(chlen))
        if novichlenovi[chlen]['kolichina na pozajmeni knigi']==0:
            kniga=input("Koja kniga ja pozajmuva? ")
            zemanjekniga[chlen]["kniga pozajmena"]=kniga
            novichlenovi[chlen]['kniga koja ja ima pozajmeno']=kniga
            
        kolichinaZemeno=int(input("Kolku knigi pozajmuva? "))
        if noviknigi[kniga]["kolichina na knigi"]==0:
            print("Nema kniga na zaliha za ponatamoshno pozajmuvanje")
        elif kolichinaZemeno >1:
            print("Ne mozhe da se pozajmi povekje od edna kniga")
        elif kolichinaZemeno ==1:
            zemanjekniga[chlen]['kolichina na pozajmeni knigi']=kolichinaZemeno
            novichlenovi[chlen]["kolichina na pozajmeni knigi"]=novichlenovi[chlen]["kolichina na pozajmeni knigi"]+kolichinaZemeno
            print(noviknigi[kniga])
            noviknigi[kniga]["kolichina na knigi"]=noviknigi[kniga]["kolichina na knigi"]-kolichinaZemeno

        prodolzhi=input("Dali sakate da prodolzhite? ")
        if prodolzhi.lower()!="da":

            with open('chlenovi.json', 'w') as f:
                json.dump(novichlenovi, f, indent=2)

            with open('knigi.json', 'w') as f:
                json.dump(noviknigi, f, indent=2)

            print("Vashiot spisok so pozajmeni knigi e: {}".format(zemanjekniga))
    return zemanjekniga
#c=zemanjekniga(zemanjekniga)

def vrakjanjekniga():
    vrakjanjekniga={}
    prodolzhi="da"

    with open('chlenovi.json') as f:
        novichlenovi = json.load(f)

    with open('knigi.json') as f:
        noviknigi =json.load(f)

    while prodolzhi.lower()=="da":
        kniga=input("Koja kniga se vrakja? ")
        vrakjanjekniga[kniga]={}

        chlen=input("Koj chlen ja vrakja? ")
        vrakjanjekniga[kniga]["Chlen"]=chlen

        kolichinaVrateni=int(input("Kolku knigi vrakja chlenot? "))
        if kolichinaVrateni>1:
            print("Klient mozhe da ima samo edna pozajmena kniga i mozhe da vrati samo edna!")
        else:
            if novichlenovi[chlen]["kolichina na pozajmeni knigi"]==0:
                print("Klientot ja nema pozajmeno taa kniga")
            if novichlenovi[chlen]["kolichina na pozajmeni knigi"]==1:
                novichlenovi[chlen]["kolichina na pozajmeni knigi"]=novichlenovi[chlen]["kolichina na pozajmeni knigi"]-kolichinaVrateni
                noviknigi[kniga]["kolichina na knigi"]=noviknigi[kniga]["kolichina na knigi"]+kolichinaVrateni
        
        prodolzhi=input("Dali sakate da prodolzhite? ")
        if prodolzhi.lower()!="da":

            with open('chlenovi.json', 'w') as f:
                json.dump(novichlenovi, f, indent=2)

            with open('knigi.json', 'w') as f:
                json.dump(noviknigi, f, indent=2)

            print("Vashata vratena kniga i chlenot koj ja vratil: {}".format(vrakjanjekniga))
    return vrakjanjekniga
#d=vrakjanjekniga(vrakjanjekniga)


        
