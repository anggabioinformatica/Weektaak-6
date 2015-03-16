##Wie dit leest, is een retard

def main():
    naam = "sequence_pep.gb"
    leesBestand(naam)
   # gcPercentage = bepaalGCpercentage(sequentie)
    #schrijfHTMLrapport(gcPercentage, sequentie, bestandsnaam)
    

def leesBestand(bestandsnaam):
    bestand = open(bestandsnaam)
    lees = False
    for regel in bestand:
        if "ORIGIN" in regel:
            lees = True
        if lees == True:
            print (regel)


#def bepaalGCpercentage(sequentie):


#def schrijfHTMLrapport (gcPercentage, sequentie, bestandsnaam):

main()
