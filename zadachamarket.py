#Da se napravi programa koja bi bila za potrebite vo nekoja prodavnica, 
#vo programata da ima moznosti da se dodavaat novi produkti, i da moze da se prodavaat. 
#Koga korisnikot ke plati da se presmeta dali i kolku kusur ke treba da mu se vrati i da se odzeme od zalihite vo prodavnicata.
#moja preporaka "magacinot" neka vi bide vo json fajl
odgovor=input("Dali kje vnesuvate produkti ili kje prodavate? Odgovori: vnesuvam ili prodavam; \n")
if odgovor.lower()=="vnesuvam":
    print("Pochnete so vnesuvanje na produkti vo magacin")
    from funkciimarket import vnesmagacin
    vnesmagacin()
if odgovor.lower()=="prodavam":
    print("Pochnete da prodavate produkti od magacin")
    from funkciimarket import prodazhba 
    prodazhba()
    

    
    
    

