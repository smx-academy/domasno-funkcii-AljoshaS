#Da se napravi programa koja bi bila za potrebite na nekoja biblioteka, 
# vo programata da ima moznosti da se vnesuvaat novi knigi, da se zaclenuvaat novi clenovi, 
# da se pozajmuvaat knigi, da se vrakjaat knigi.
#Podatoci za knigite koi ke treba da se cuvaat: Naslov, avtor, zanr, kolicina
#Podatoci za sekoj clen koi ke treba da se cuvaat: Ime i prezime, email, telefonski broj, 
# broj na clenska kniska, dali ima zemeno kniga.
#Clen koj ima zemeno kniga ne moze da zeme druga kniga
#*probajte vo razlicni fajlovi "knigi.json", "clenovi.json" da gi cuvate podatocite

odgovor=input("Nov chlen: novchlen ; \n Nova kniga: novakniga ; \n Zemanje kniga: zemanjekniga ; \n Vrakjanje kniga: vrakjanjekniga ; :")
if odgovor=="novchlen":
    from funkciibiblioteka import novichlenovi
    novichlenovi()
if odgovor=="novakniga":
    from funkciibiblioteka import vnesknigi
    vnesknigi()
if odgovor=="zemanjekniga":
    from funkciibiblioteka import zemanjekniga
    zemanjekniga()
if odgovor=="vrakjanjekniga":
    from funkciibiblioteka import vrakjanjekniga
    vrakjanjekniga()
