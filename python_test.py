##Wie dit leest, is een retard

def main():
    naam = "sequence_pep.gb"
    sequence = leesBestand(naam)
    print(sequence,"\n")
    gcPercentage = bepaalGCpercentage(sequence)
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


def bepaalGCpercentage(sequence):
    x = sequence.upper()
    total = len(x)
    #print (total)
    c = x.count("C")
    #print (c)
    g = x.count("G")
    #print (g)
    gc_total = g+c
    #print (gc_total)
    gc_perc = (gc_total / total)*100
    print ("GC:","{:.2f}".format(gc_perc)+"%")


#def schrijfHTMLrapport (gcPercentage, sequentie, bestandsnaam):

main()
