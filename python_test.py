##Wie dit leest, is een retard

def main():
    naam = "sequence_pep.gb"
    sequentie = leesBestand(naam)
    print (sequentie)
   # gcPercentage = bepaalGCpercentage(sequentie)
    #schrijfHTMLrapport(gcPercentage, sequentie, bestandsnaam)
    

def leesBestand(bestandsnaam):
    bestand = open(bestandsnaam)
    raw_data = ""
    lees = False
    for regel in bestand:
        if "ORIGIN" in regel:
            lees = True
        if lees == True:
            raw_data += regel[10:]
    sequence = raw_data.replace(" ", "").replace("\n", "").replace("\r", "")
    return sequence


#def bepaalGCpercentage(sequentie):


#def schrijfHTMLrapport (gcPercentage, sequentie, bestandsnaam):

main()
